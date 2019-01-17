# MetaSUB Core Analysis Pipeline

[![Build Status](https://api.cirrus-ci.com/github/MetaSUB/MetaSUB_CAP.svg)](https://cirrus-ci.com/github/MetaSUB/MetaSUB_CAP)
![Version](https://img.shields.io/badge/Version-1.1.0-green.svg)


This is the core analysis pipeline which is run on every sample
collected by the MetaSUB consortium. It is designed to provide a
comprehensive set of analyses for metagenomic data.

Collaboration is welcome and encouraged.

Please start an issue or contact [David C. Danko](mailto:dcd3001@med.cornell.edu) if you have questions about this pipeline.

Utilities are available to parse the output of the CAP. Please see the
[CAPalyzer](https://github.com/dcdanko/capalyzer). for details.

## Current Modules

### Taxonomy Profiling
-   KrakenHLL, searching RefSeq Microbial
-   Kraken, searching the minikraken database
-   MetaPhlAn2

### Antibiotic Resistance Profiling
-   Resistome + MegaRES
-   CARD

### Assorted Gene Sets
-   HUMANn2 Pathway Profiling
-   HUMANn2 Functional Gene Profiling
-   Staph. Aureus n315
-   [Common Macrobial
    Genomes](https://github.com/MetaSUB/macrobial-genomes)
-   Methyltransferases Genes (Deprecated)
-   Virulence Factor Genes (Deprecated)

### Statistic
-   Kmer Profiles
-   GC content
-   Similarity to human body site microbiomes
-   [Microbe Directory](https://microbe.directory/) Annotation
-   Average Genome Size Estimation
-   Alpha Diversity (Deprecated)
-   Beta Diversity (Deprecated)

See docs/modules.md for more detail.


## Installation

Normal use of the Core Analysis Pipeline also requires the [MetaSUB QC
Pipeline](https://github.com/MetaSUB/MetaSUB_QC_Pipeline). This is
included in the installation directions below.


``` {.sourceCode .bash}
pip install moduleultra
cd /analysis/dir
moduleultra init
moduleultra install  git@github.com:MetaSUB/MetaSUB_QC_CAP
moduleultra install  git@github.com:MetaSUB/MetaSUB_CAP
moduleultra add pipeline metasub_cap
moduleultra add pipeline metasub_qc_cap
```

## Running

To run the CAP use the following commands

``` {.sourceCode .bash}
cd /analysis/dir
datasuper bio add-fastqs -1 <forward file ext> -2 <reverse file ext> <sample_type> [<fastq files>...]
moduleultra run -p metasub_qc_cap -j <njobs> [--dryrun]
moduleultra run -p metasub_cap -j <njobs> [--dryrun]
```

To see more options just use the help commands

``` {.sourceCode .bash}
moduleultra run --help
moduleultra --help
datasuper --help
```

Most cluster systems will need a custom submit script. You can set a
default script using the following command

``` {.sourceCode .bash}
moduleultra config cluster_submit /path/to/submit_script
```

### Running with Docker

Docker images for the MetaSUB CAP may be found [on docker hub](https://cloud.docker.com/u/metasub/repository/docker/metasub/metasub_cap)

You will still need to download the databases outside of docker. You can use the `download_databases.py` script for this purpose.

To start a shell in the docker machine use the following command:
``` {.sourceCode .bash}
docker run --rm -it -v /path/to/local/dbs:/home/metasub/dbs -v $PWD:/home/metasub/repo metasub_cap:latest /bin/bash -c "source activate cap"
```

From within the shell in the docker machine you can run moduleultra as normal, but be sure to use the flag `-c /home/metasub/docker_pipeline_config.py` in order to correctly find the databases.

## Adding Modules

Roughly, a module is meant to encapsulate a single program (e.g. kraken
or metaphlan). Each module should consist of 1-3 snakemake rules and a
bit of metadata.

In order to add a module to the CAP you need to write a snakemake rule
and a small amount of metadata describing the rule. 

You can use snakemake\_files/kraken\_taxonomy\_profiling.snkmk and
snakemake\_files/mash\_intersample\_dists.snkmk as examples for the snakemake rules.

You will also you need to add a `result_type` to `pipeline_definition.yml` describing the expected files output by your module.

This definition is a small Yaml dictionary that defines:
-   The name of the module
-   The names of the files in the modules
-   The types of files in the module (you may also define your own file types)
-   Any modules that your module depends on
-   A flag if the module is run on groups of samples


ModuleUltra generates filename patterns for modules automatically. You may reference these filenames (or filenames from modules your module depends on) as `config['<module_name>']['<file_type_name>']` for both Snakemake input and output fields.

Most modules will need extra parameters at runtime. These may be stored in `pipeline_config.py`. There is no limit to what you can store though this should be lightweight.

If your module needs custom scripts you may add them to the scripts directory. You can reference this directory in your modules as `config['pipeline_dir']['script_dir']`.

**You should add your module on a separate branch** named `module/<module_name>`

How to make a branch
``` {.sourceCode .bash}
cd /path/to/MetaSUB_CAP
git checkout -b module/<module_name>
```


License
=======

MIT License
