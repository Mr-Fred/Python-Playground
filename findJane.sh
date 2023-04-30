#!/bin/bash

oldfiles=($(grep 'jane ' /home/runner/Python-Playground/data/list.txt | cut -d ' ' -f 3))

files=()
for file in "${oldfiles[@]}" 
do
  new_file="/home/runner/Python-Playground$file"
  files+=("$new_file")
done

# one liner version of the above for loop files=($(grep 'jane ' /home/runner/Python-Playground/data/list.txt | cut -d ' ' -f 3 | sed 's|^|/home/runner/Python-Playground|'))


> /home/runner/Python-Playground/data/oldFiles.txt

for file in "${files[@]}"; do 
  if test -e "$file"; then
    echo $file >> /home/runner/Python-Playground/data/oldFiles.txt
  else 
    echo "$file does not exist"
  fi
done