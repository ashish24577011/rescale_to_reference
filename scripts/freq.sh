#!/bin/bash

# Arguments passed from Snakemake
run_paths=$1          # Paths to all run files (comma-separated)
merged_output=$2      # Output file for merged data
frequency_output=$3   # Output file for frequency data

# Convert comma-separated paths into an array
IFS=',' read -r -a run_files <<< "$run_paths"

# Concatenate all run files into one merged file
cat "${run_files[@]}" > "$merged_output"

# Calculate frequency of DNA fragment lengths
awk '{len=$3-$2; count[len]++} END {for (l in count) print l, count[l]}' "$merged_output" | sort -n > "$frequency_output"

