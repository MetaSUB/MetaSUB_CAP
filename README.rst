MetaSUB Core Analysis Pipeline
=========

This is the core analysis pipeline which will be run on every sample collected by the MetaSUB consortium. This pipeline uses ModuleUlta, DataSuper and SnakeMake.

This pipeline is under heavy development. Most of the documentation for this pipeline is currently internal to MetaSUB.

Collaboration by MetaSUB consortium members is welcome and encouraged.

Please contact David C. Danko (dcd3001@med.cornell.edu) if you have questions about this pipeline.


Installation
------------

To install the Core Analysis Pipeline in developer mode you will need to install PackageMega, DataSuper, ModuleUltra and the CAP itself. This process will be streamlined in the future.

.. code-block:: bash
   
    git clone git@github.com:dcdanko/DataSuper.git 
    cd DataSuper
    python setup.py develop
    cd ..
    
    git clone git@github.com:dcdanko/PackageMega.git 
    cd DataSuper
    python setup.py develop
    cd ..
    
    git clone git@github.com:dcdanko/ModuleUltra.git 
    cd ModuleUltra
    python setup.py develop
    cd ..
    
    git clone git@github.com:MetaSUB/MetaSUB_CAP
    
    cd /analysis/dir
    moduleultra init
    moduleultra install --dev /path/to/MetaSUB_CAP
    moduleultra add pipeline metasub_cap

Running
-------

To run the CAP use the following commands

.. code-block:: bash

   cd /analysis/dir
   python /path/to/MetaSUB_CAP/add_fastq_data_to_datasuper.py <sample_type> [<fastq files>...]
   moduleultra run -p metasub_cap -j <njobs> [--dryrun]
   
To see more options just use the help commands

.. code-block:: bash

   moduleultra run --help
   moduleultra --help
   datasuper --help
   
Most cluster systems will need a custom submit script. You can set a default script using the following command
   
.. code-block:: bash
   
   moduleultra config cluster_submit /path/to/submit_script

Adding Modules
--------------

Roughly, a module is meant to encapsulate a single program (e.g. kraken or metaphlan). Each module should consist of 1-3 snakemake rules and a bit of metadata.

In order to add a module to the CAP you need to write a snakemake rule and a bit of metadata describing the rule. You can check out snakemake_files/kraken_taxonomy_profiling.snkmk and snakemake_files/mash_intersample_dists.snkmk as examples. In particular you need to write a definition of the type of _result_ you expect your module to produce. 

This definition is a small JSON object that defines:
 - The name of the module
 - The names of the files in the modules
 - The types of files in the module (you may also define your own file types)
 - Any modules that your module depends on
 - A flag if the module is run on _groups_ of samples as opposed to individual samples
 
Many examples are visible in pipeline_definitions.json (this is where you should add your definition)

ModuleUltra generates filename patterns for modules automatically. You may reference these filenames (or filenames from modules your module depends on) as `config['<module_name>']['<file_type_name>']`. Many tools will need all microbial reads, these come from the 'filter_macrobial_reads' module and can be referenced as `config['filter_macrobial_dna']['microbial_read1']` and `config['filter_macrobial_dna']['microbial_read2']`.

Most modules will need extra parameters at runtime. These may be stored in pipeline_config.json. There is no limit to what you can store here so long as it is valid JSON. You may even include the results of shell commands in this config by enclosing the commands in backticks. These backticks are evaluated just before the pipeline is run. This is useful to get the absolute path and version of the program being run.

If your module needs custom scripts you may add them to the scripts directory here. You can reference this directory in your modules as config['pipeline_dir']['script_dir']. We are working on a protocol to download and store large databases but this is not yet complete.

**You should add your module on a seperate branch named** `module.<module_name>`

How to make a branch

.. code-block:: bash
   
   cd /path/to/MetaSUB_CAP
   git checkout -b module.<module_name>

Planned Modules
----------------

Feel free to add to this list

- CLARK for taxonomy profiling
- Taxonomy Normalisation using genome counts
- CRASS (CRISPRs)
- StrainPhlAn
- Repeat Masker

Finished Modules
----------------

See docs.modules.rst for more detail.

- Humann2
- Microbe Census (Avergae Genome Size, Genome Counts) 
- Kraken
- Metaphlan2
- Mash
- microbial/macrobial filtering
- Comparisons to HMP  
- Map to AMRs
- Map to Methyltransferases
- Resistome MEGARes
- Intrasample (beta) Diversity
- Intersample (alpha) diversity
- Microbe DB Annotations
- Read Statistics
- Proportions Classified
- Adapter Removal


Module Dependencies
-------------------

We are building a system so that every pipeline can be run in its own conda environement. In principle modules can use any software on Conda or PyPi. Projects on github or bitbucket are also fine so long as they can be installed by script.

Licence
-------

MIT License

