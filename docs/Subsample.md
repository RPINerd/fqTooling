# Subsampling Sequences

User friendly wrapper around the SeqTK subsample command to subsample a FASTA or FASTQ file to a specified number of sequences or a specified fraction of the total sequences.

## Requirements

[SeqTK](www.seqtk.com)

## Inputs

A single FastQ or paired FastQ files to subsample.

If the reads are paired, the program will infer the second file from the first file based on everything before the `_R1`/`_R2` in the file name.

## Outputs

FastQ files with the subsampled quantity appended just before the file extension.

For example:
`Sample1_R1.fastq` -> `Sample1_R1.1000.fastq` for 1000 sequences
`Sample1_R1.fastq` -> `Sample1_R1.0_1.fastq` for 10% of the sequences

## Manual Usage

`python3 sample.py -f Sample1_R1.fastq -n 1000`

### Options

`-f`/`--file` - Input FastQ file to subsample
`-n`/`--number` - Desired final sequence count or fraction of the total sequences
`-v`/`--verbose` - Debug output
