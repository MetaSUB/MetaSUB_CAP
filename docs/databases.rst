=========
Databases
=========

The MetaSUB CAP uses several databases. This page documents the different databases

Uniref90
--------

The CAP uses Uniref90 to identify functional pathways as a part of humann2.

The CAP uses Uniref90 as a diamond index. There are separate downloads for the diamond index and fasta file.

`AWS Download for diamond index <https://s3.amazonaws.com/metasub-cap-databases/uniref90_annotated.1.1.dmnd>`_
`AWS Download for fasta <https://s3.amazonaws.com/metasub-cap-databases/uniref90.tar.gz>`_

CARD
----

Comprehensive Antibiotic Resistance Database

`Sequences <https://s3.amazonaws.com/metasub-cap-databases/card_oct_2017_prot_seqs.faa>`_
`Diamond Index <https://s3.amazonaws.com/metasub-cap-databases/card_oct_2017_prot_seqs.dmnd>`_

MegaRes
-------

The CAP uses MegaRes to identify antibiotic resistance genes.

`AWS Download Link <https://s3.amazonaws.com/metasub-cap-databases/megares_v1.0.1.tar.gz>`_

MethylTransferases
------------------

Database of known methyltransferases including diamond index.

`AWS Download Link <https://s3.amazonaws.com/metasub-cap-databases/methyls_90.tar.gz>`_

Virulence Factor DB
-------------------

Database of known virulence factors including diamond index.

`AWS Download Link <https://s3.amazonaws.com/metasub-cap-databases/vfdb_setB_pro.tar.gz>`_

Hg38
----

The MetaSUB_CAP uses Hg38 to filter reads of human origin.

The version of Hg38 we use includes alternate contigs and has human readable contig names.

The CAP uses Hg38 as a bowtie2 index. The download files contain a bowtie2 index as well as a fasta file.

`AWS Download Link <https://s3.amazonaws.com/metasub-cap-databases/hg38_alt_contigs.tar.gz>`_

MiniKraken
----------

The CAP uses the 8GB version of minikraken produced on October 19, 2017

`AWS Download Link <https://s3.amazonaws.com/metasub-cap-databases/minikraken_20171019_8GB.tgz>`_

Microbial Genomes
-----------------

The CAP aligns reads to Staph Aureus n315 genome using bowtie2

This database includes the SAn315 genome as a fasta and a bowtie2 index.

`AWS Download Link <https://s3.amazonaws.com/metasub-cap-databases/staph_aureus_n315.tar.gz>`_


Macrobial Genomes
-----------------

See `Macrobial Quantification <https://github.com/MetaSUB/macrobial-genomes>`_








