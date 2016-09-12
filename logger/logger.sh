#!/usr/bin/env bash

PROGRAM_NAME=$0
KEYS=""
VALUES=""
SCORE=-1
LABEL=""

# Since there are several situatoins where usage instructions will be needed to
# be shown to the user, it makes sense to pull that out into it's own function
function help {
  echo "usage: $PROGRAM_NAME -s score [-h] [-m model] [-l label]"
  echo "  -s score  Score from results, must be greater than 0"
  echo "  -h        Displays these usage instructions"
  echo "  -m model  Pass in a key value pair for the model, must be in format key:value"
  echo "  -l label  Label that can be used to identify this test later"
  exit 1
}

# Parameters
# - $1 : A key value pair in the fomat KEY:VALUE
function addKeyValuePair {
  IFS=':' read -ra kvpArr <<< "$1"
  kvpKey=${kvpArr[0]}
  kvpValue=${kvpArr[1]}
  KEYS="$KEYS:$kvpKey"
  VALUES="$VALUES:$kvpValue"
}


while getopts ":hs:m:l:" opt; do
  case $opt in
    h)
      help
      ;;
    s)
      SCORE=$OPTARG
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
