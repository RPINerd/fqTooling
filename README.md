# fqTooling

A command line FASTQ file toolbox


# primerFind

Find and summarize the presence of given primers (or any subseq) within a fastq file

## Usage

`python3 primerFind.py -s <sequenceFile> -p <primerFile>`

`-v`/`--verbose` - gives debug output
`-r`/`--reporting` - creates report files based on hits found


# FastQC Pipeline

A straightforward program which can take a file list of fastq's, concatenate them, and perform FastQC on them in serial or scalable parallel

## Requirements

[Python](https://www.python.org/) - built on 3.10x but should be fine for the forseeable future  
[FastQC](https://github.com/s-andrews/FastQC) - the underlying tool to perform QC on your read files  
Bash Environment - current mechanics rely on system calls to the bash command line  

## Input File

File structure should follow the convention `SampleID_Lane#_Read#.fastq`. For example:
Exp001_S1_L002_R1_001.fastq

FastQC Pipe expects a tab-delimited text file with the following structure (lines led with '#' are ignored):

`Path/of/directory | Sample_Name | R1/2/Both`

Example:

```csv
/home/RPINerd/M01234/Fastq_Generation Exp001_S1   2
/home/RPINerd/M01234/Fastq_Generation Exp001_S2   1
/home/RPINerd/M01234/Fastq_Generation Exp001_S3   Both
```

## Running Pipeline

General format for run is `python3 fastqc_pipe.py -f file_list.tsv`

The input file is the only required argument however there are some additional options:  
`--threads` or `-t #` specifies how many threads to allocate to the fastqc algorithm, currently capped at 12  
`--merge` or `-m <desired/path/to/>` allows for a preferred location to be specified for the merged lanes to be written to  
`--verbose` or `-v` pumps out a ton of extra info and saves it to the file fastqc_pipe.log  


# fastq_filtering

Provided a single, or list of, regular expressions, filter out all reads from a given fastq file which match said expression(s).

One use case could be dropping reads with a large amount of poly-A sequences:

`python fqfilter.py -f Sample01.fastq -d "[A]{25}"`

Or perhaps you have a specific adapter at the start of the read that you'd like to isolate

`python fqfilter.py -f Sample01.fastq -k "^ATCGGCTA"`

And you can also do both at once!

`python fqfilter.py -f Sample01.fastq -k "^ATCGGCTA" -d "[A]{25}"`

## Options

|||
|-|-|
| `-f`/`--fastq`        |   Input fastq file to filter                              |
| `-p`/`--pair`         |   Input pair of fastqs. R1 then R2. Files will be syncronized in the ouput for safety of downstream processing!    |
| `-k`/`--keep`         |   Regex expression(s) to keep                             |
| `-d`/`--drop`         |   Regex expression(s) to drop                             |
| ~~`-s`/`--sync`~~         |   ~~Synchronize R1/R2 fastq's for downstream~~ processing     |
| `-v`/`--verbose`      |   Debug output                                            |

## Requirements

Built on Python 3.11, but may be fine back as far as 3.7  
Needs the [BioPython](https://biopython.org/) package


