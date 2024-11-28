#!/bin/bash


run_paths=$1          
merged_output=$2      
frequency_output=$3   

IFS=',' read -r -a run_files <<< "$run_paths"


cat "${run_files[@]}" > "$merged_output"


awk '{len=$3-$2; count[len]++} END {for (l in count) print l, count[l]}' "$merged_output" | sort -n > "$frequency_output"

