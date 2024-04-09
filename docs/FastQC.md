# FastQC Pipeline

Perform FastQC on an individual or directory of fastq files

## Requirements

[FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)

## Inputs

Either a single fastq file or a directory of fastq files to be processed

## Outputs

A directory of FastQC output files for each input fastq file

## Manual Usage

`python3 qc.py -f Sample1_R1.fastq,Sample1_R2.fastq`  
or  
`python3 qc.py -d /path/to/fastq/directory`

### Options

`-f`/`--fastq` - Input fastq file to filter, R1 and R2 files should be comma separated   
`-d`/`--directory` - Input directory of fastq files to filter  
`-t`/`--threads` - Number of threads to allocate to the FastQC algorithm  
`-m`/`--merge` `</output/path/>`- Merge the lanes of a sample into a single file for FastQC  
`-v`/`--verbose` - Debug output  
