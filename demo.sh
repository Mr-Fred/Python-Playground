#!/bin/bash

oldfiles=($(grep 'jane ' /home/runner/Python-Playground/data/list.txt | cut -d ' ' -f 3))

# echo $files
files=()
for file in "${oldfiles[@]}" 
do
  new_file="/home/runner/Python-Playground$file"
  files+=("$new_file")
done

for file in "${files[@]}"
do
  echo "$file"
  done