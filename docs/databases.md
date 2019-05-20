# Databases


The MetaSUB CAP uses several databases. This page documents thedifferent databases

## Genes

### Uniref90

The CAP uses Uniref90 to identify functional pathways as a part of
humann2.

The CAP uses Uniref90 as a diamond index. There are separate downloads
for the diamond index and fasta file.

[AWS Download for diamond index](https://s3.amazonaws.com/metasub-cap-databases/uniref90_annotated.1.1.dmnd)
[AWS Download for fasta](https://s3.amazonaws.com/metasub-cap-databases/uniref90.tar.gz)

### MethylTransferases

Database of known methyltransferases including diamond index.

[AWS Download Link](https://s3.amazonaws.com/metasub-cap-databases/methyls_90.tar.gz)

### Virulence Factor DB

Database of known virulence factors including diamond index.

[AWS Download Link](https://s3.amazonaws.com/metasub-cap-databases/vfdb_setB_pro.tar.gz)

## AMRs

### CARD

Comprehensive Antibiotic Resistance Database

[Sequences](https://s3.amazonaws.com/metasub-cap-databases/card_oct_2017_prot_seqs.faa)
[Diamond Index](https://s3.amazonaws.com/metasub-cap-databases/card_oct_2017_prot_seqs.dmnd)

### MegaRes

The CAP uses MegaRes to identify antibiotic resistance genes.

[AWS Download
Link](https://s3.amazonaws.com/metasub-cap-databases/megares_v1.0.1.tar.gz)

## Human Genome - Hg38


The MetaSUB CAP uses Hg38 to filter reads of human origin.

The version of Hg38 we use includes alternate contigs and has human
readable contig names.

The CAP uses Hg38 as a bowtie2 index. The download files contain a
bowtie2 index as well as a fasta file.

[AWS Download Link](https://s3.amazonaws.com/metasub-cap-databases/hg38_alt_contigs.tar.gz)

## Taxa Databases

### MiniKraken

The CAP uses the 8GB version of minikraken produced on October 19, 2017

[AWS Download Link](https://s3.amazonaws.com/metasub-cap-databases/minikraken_20171019_8GB.tgz)

### Microbial Genomes

The CAP aligns reads to Staph Aureus n315 genome using bowtie2

This database includes the SAn315 genome as a fasta and a bowtie2 index.

[AWS Download Link](https://s3.amazonaws.com/metasub-cap-databases/staph_aureus_n315.tar.gz)

## Other

### Macrobial Genomes

See [Macrobial Quantification](https://github.com/MetaSUB/macrobial-genomes)
