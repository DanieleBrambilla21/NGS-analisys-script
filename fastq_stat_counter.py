#!/usr/bin/env python3

# SCRIPT: fastq_stat_counter.py
# Objective: Calculate basic statistics from a compressed FASTQ file

import gzip

# Define the input file (Ensure this matches your filename)
input_file = "test.fastq.gz"

count = 0
total_length = 0

print(f"Opening file: {input_file}...")

# Open the gzipped file in text-read mode ("rt")
with gzip.open(input_file, "rt") as f:
    for line in f:
        count += 1
        # FASTQ format: Sequence is always on lines 2, 6, 10...
        # Logic: If line number modulo 4 equals 2, it's a DNA sequence
        if count % 4 == 2:
            clean_sequence = line.strip()
            total_length += len(clean_sequence)

# Final Calculations
num_sequences = count / 4
avg_length = total_length / num_sequences

print("--- RESULTS ---")
print(f"Total sequences analyzed: {num_sequences}")
print(f"Average DNA length: {avg_length} bp")
