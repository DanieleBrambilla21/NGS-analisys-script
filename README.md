# NGS Analysis Tools

A collection of lightweight scripts designed for Next-Generation Sequencing (NGS) data processing.

## Contents
- **fastq_stat_counter.py**: A memory-efficient Python script to extract total reads and average sequence length from gzipped FASTQ files.
- **run_qc_pipeline.sh**: A Bash wrapper to automate quality control workflows across multiple datasets.

## Key Features
- **Efficiency**: Handles compressed data (`.gz`) without full decompression.
- **Scalability**: Designed for batch processing in Linux environments (WSL/Ubuntu).
- **Professional Standards**: Uses Shebangs and proper permission handling for pipeline integration.
