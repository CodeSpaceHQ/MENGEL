#!/usr/bin/env bash

PROGRAM_NAME=$0
SCORE=-1
LABEL=""
MODELCOUNT=1
CURMODEL=0

KEYS=""
VALUES=""


# Since there are several situatoins where usage instructions will be needed to
# be shown to the user, it makes sense to pull that out into it's own function
function help {
  echo "usage: $PROGRAM_NAME -s score [-h] [-n modelcount] [-m model] [-l label]"
  echo "  -s score      Score from results, must be an integer in [0,100]"
  echo "  -n modelcount Number of models being submitted. (Defaults to 1)"
  echo "  -h            Displays these usage instructions"
  echo "  -m model      Pass in a key value pair for the model, must be in format key1:value1:key2:value2:"
  echo "  -l label      Label that can be used to identify this test later"
  exit 1
}

# Parameters
# - $1 : All the key value pairs for a particular model in the format
# key1:value1:key2:value2...
function addKeyValuePair {
  IFS=':' read -ra kvpArr <<< "$1"
  kvpCount="${#kvpArr[*]}"
  for ((index=0; index<"$kvpCount"; index=index+2));
    do
      kvpKey=${kvpArr[index]}
      kvpValue=${kvpArr[(index+1)]}

      KEYS="$KEYS:$kvpKey"
      VALUES="$VALUES:$kvpValue"
    done



  echo "Keys read in"
  echo "Keys = $KEYS"
  echo "Values = $VALUES"
}


while getopts ":hs:m:l:" opt; do
  case $opt in
    h)
      help
      ;;
    n)
      MODELCOUNT=$OPTARG
      ;;
    s)
      SCORE=$OPTARG
      re='^[0-9]+$'
      if ! [[ $SCORE =~ $re ]] ; then
         echo "Error: Score was not a positive integer." >&2;
         help
         exit 1
      elif [[ $SCORE -lt 0 ]]; then
          echo "Error: Score was less than 0" >&2
          help
          exit 1
      elif [[ $SCORE -gt 100 ]]; then
        echo "Error Score was greater than 100" >&2
        help
        exit 1
      fi
      ;;
    m)
      addKeyValuePair $OPTARG
      ;;
    l)
      LABEL=$OPTARG
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      help
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      help
      ;;
  esac
done

if [ $SCORE -lt 0 ]
  then
    echo "Invalid score"
    echo ""
    help
    exit 1
fi

cat <<EOF
{
  "label" : "$LABEL",
  "score" : "$SCORE",
  "model" : {
EOF

IFS=':' read -ra KEYARR <<< "$KEYS"
IFS=':' read -ra VALARR <<< "$VALUES"
ARRSIZE="${#KEYARR[*]}"
let LASTINDEX=ARRSIZE-2

#index starts at 1 because the first one is always going to be empty
for ((index=1; index<"$ARRSIZE"; ++index));
do
  JSONLINE="\"${KEYARR[index]}\" : \"${VALARR[index]}\""
  if [ "$index" -eq "$LASTINDEX" ]
    then
      echo -e "    $JSONLINE,"
    else
      echo -e "    $JSONLINE"
  fi
done

cat <<EOF
  }
}
EOF

exit 0
