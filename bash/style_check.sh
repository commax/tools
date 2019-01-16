#!/bin/bash

function remove_spaces () {
    file=$1
    
    echo "Removing sapces in file $1"
    
    # remove one or more spaces at end of the line
    sed -i 's/\s\+$//g' $file
}

if [[ -f $1 ]]; then
    remove_spaces $1
elif [[ -d $1 ]]; then
    dir=$1
    
    for name in $(ls $dir)
    do
        if [[ -f $name ]]; then
        remove_spaces $name
        fi
    done
fi
