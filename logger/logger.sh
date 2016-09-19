#!/usr/bin/env bash

PROGRAM_NAME=$0
SCORE=-1
LABEL=""
TIMESTAMP="$(date +"%Y-%m-%d-%H-%M-%S")"
OUTPUTSRC="./output/"

#User when iterating through the KVP pairs passed in. This number should ONLY
# be incremented while the models are being read in from CLI

declare -i MODELCOUNT=0
declare -i CURMODEL=0
declare -a MODELARRAYKEYS
declare -a MODELARRAYVALUES
declare -i QUITEMODE=1 #Set to 1 for quiet mode

# Make sure they have git installed and set git to the user.name
command -v git >/dev/null 2>&1 || { echo >&2 "git is required but is not installed.  Aborting."; exit 1; }
AUTHOR=$(git config user.name)


# Since there are several situatoins where usage instructions will be needed to
# be shown to the user, it makes sense to pull that out into it's own function
function help () {
  echo "usage: $PROGRAM_NAME -s score [-h] [-m model] [-l label] [-o location]"
  echo "  -s score      Score from results, must be an integer in [0,100]"
  echo "  -h            Displays these usage instructions"
  echo "  -c            Auto commit file (Make sure your git global config is setup properly)"
  echo "  -m model      Pass in a key value pair for the model, must be in format key1:value1:key2:value2:"
  echo "  -l label      Label that can be used to identify this test later"
  echo "  -o location   Location for output files (defaults to ./output/)"
  exit 1
}

# Used to validate and change the output source directoy
# If the given directory is invalid (such as not being a directoy) the program
# exits with status code 1
# Parameters
# - 1: New Directoy
function changeOutputSrcDir () {
  src=$1
  lastChar="${src: -1}"
  if [ "$lastChar" != "/" ]; then
    src=$src"/"
  fi

  if [ ! -d "$src" ]; then
    echo "Error: Output directory \"$src\" does not exist. Aborting." >&2
    exit 1
  fi
  OUTPUTSRC=$src
}

# Parameters
# - $1 : All the key value pairs for a particular model in the format
# key1:value1:key2:value2...
function addKeyValuePair () {
  IFS=':' read -ra kvpArr <<< "$1"
  kvpCount="${#kvpArr[*]}"
  kvpKeys=""
  kvpValues=""

  for ((index=0; index<"$kvpCount"; index=index+2)); do
      kvpKey=${kvpArr[index]}
      kvpValue=${kvpArr[(index+1)]}

      kvpKeys="$kvpKeys:$kvpKey"
      kvpValues="$kvpValues:$kvpValue"

  done
  MODELARRAYKEYS[$MODELCOUNT]=$kvpKeys
  MODELARRAYVALUES[$MODELCOUNT]=$kvpValues
  MODELCOUNT=$MODELCOUNT+1
}

while getopts ":hcs:m:l:o:" opt; do
  case $opt in
    h)
      help
      exit 0
      ;;
    c)
      QUITEMODE=0
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
    o)
      changeOutputSrcDir $OPTARG
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
OUTPUTJSON="{\"label\" : \"$LABEL\",\"score\" : \"$SCORE\""

if [ "$MODELCOUNT" -ne "0" ]; then
  OUTPUTJSON=$OUTPUTJSON,
fi

let LASTMODELINDEX=MODELCOUNT-1
#Add the models to the output
for ((modelindex=0; modelindex<"$MODELCOUNT";++modelindex));
do


  OUTPUTJSON=$OUTPUTJSON"\"model$modelindex\":{"
  IFS=':' read -ra KEYARR <<< "${MODELARRAYKEYS[modelindex]}"
  IFS=':' read -ra VALARR <<< "${MODELARRAYVALUES[modelindex]}"
  ARRSIZE="${#KEYARR[*]}"
  let LASTPAIRINDEX=ARRSIZE-1

  #Added each pair from the model to the output
  #index starts at 1 because the first one is always going to be empty
  for ((index=1; index<"$ARRSIZE"; ++index));
  do
    JSONLINE="\"${KEYARR[index]}\" : \"${VALARR[index]}\""
    if [ "$index" -eq "$LASTPAIRINDEX" ]
      then
        OUTPUTJSON=$OUTPUTJSON$JSONLINE
      else
        OUTPUTJSON=$OUTPUTJSON$JSONLINE,
    fi
  done

  if [ "$modelindex" -eq "$LASTMODELINDEX" ]; then
    OUTPUTJSON=$OUTPUTJSON"}"
  else
    OUTPUTJSON=$OUTPUTJSON"},"
  fi

done

OUTPUTJSON=$OUTPUTJSON"}"
TESTNAME=$OUTPUTSRC$TIMESTAMP"-"$AUTHOR
FILENAME=$TESTNAME
if [ -n "$LABEL" ]; then
  FILENAME=$FILENAME"-"$LABEL
fi
FILENAME=$FILENAME".log"
echo $FILENAME
echo $OUTPUTJSON > $FILENAME

#If not quiet mode, commit file
if [ "$QUITEMODE" -eq 0 ]; then
  git commit -m "Auto commit from logger for test:$TESTNAME" $FILENAME
fi



exit 0
