#!/bin/bash

# NGS Quality Control Automation Pipeline
# Author: [Tuo Nome]
# Objective: Batch process all compressed FASTQ files in the directory

echo "Starting Quality Control analysis..."

# Loop through all gzipped FASTQ files
for file in *.fastq.gz
do
    echo "Processing file: $file"
    # Placeholder for QC command (e.g., fastqc $file)
    # The script ensures all samples are handled consistently
done

echo "Analysis completed successfully!"
