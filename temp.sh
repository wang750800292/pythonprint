#!/bin/bash

if [[ '1' == '1' ]]; then
    echo 'equal'
else
    echo 'not equal'
fi


if [[ $1 == '' ]]; then
    echo 'need one parameter, ex> {$0 someword}'
elif [[ $1 == 'hello' ]]; then
    echo 'hello'
else
    echo 'i do not konw,  ex> {$0 hello}'
fi

case $1 in
    'hello' )
    echo 'hello';;
    '')
    echo 'need one parameter, ex> {$0 someword}';;
    *)
    echo 'i do not konw,  ex> {$0 hello}';;
esac

a=0
i=0
while [[ $i != 100 ]]; do
    i=$(($i+1))
    a=$(($a+i))
done
echo "the total is $a"

until [[ $i == 101 ]]; do
    i=$(($i+1))
    a=$(($a+i))
done
echo "the total is $a"

for i in $(seq 1 100); do
    if [[ "$i" == "2" ]]; then
        echo $i
    fi
done

for (( i = 0; i < 10; i++ )); do
    a=$(($a+$i))
done
echo "a is $a"


echo $(whoami)
echo $(pwd)
echo $(date +"%s")
# read -p "input a num: " number
# a=0
# for (( i = 0; i < $number; i++ )); do
#     a=$(($a+$i))
# done
# echo "total is $a"

# test -e ~/test/pythonprint/test
# if [[ $? == 1 ]]; then
#     echo 'test is not exist, create it'
#     touch ~/test/pythonprint/test
# else
#     test -f ~/test/pythonprint/test
#     if [[ $? == 0 ]]; then
#         echo 'test is file and remove it and mkdir test'
#         rm ~/test/pythonprint/test
#         mkdir -p ~/test/pythonprint/test
#     else
#         echo 'test is directory and remove it'
#         rm -rf ~/test/pythonprint/test
#     fi

# fi
i=1
for line in `cut -d':' -f1 /etc/passwd`; do
    i=$(($i+1))
    echo 'the' $i 'account is '$line
done    


