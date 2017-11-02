MetaSUB Core Analysis Pipeline
=========

This is the core analysis pipeline which will be run on every sample collected by the MetaSUB consortium. This pipeline uses ModuleUlta, DataSuper and SnakeMake.

This pipeline is under heavy development. Most of the documentation for this pipeline is currently internal to MetaSUB.

Collaboration by MetaSUB consortium members is welcome and encouraged.

Please contact David C. Danko (dcd3001@med.cornell.edu) if you have questions about this pipeline.


Installation
------------

To install the Core Analysis Pipeline in developer mode you will need to install DataSuper, ModuleUltra and the CAP itself. This process will be streamlined in the future.

.. code-block:: bash
   
    git clone git@github.com:MetaSUB/DataSuper.git 
    cd DataSuper
    python setup.py develop
    cd..
    
    git clone git@github.com:MetaSUB/ModuleUltra.git 
    cd ModuleUltra
    python setup.py develop
    cd..
    
    git clone git@github.com:MetaSUB/MetaSUB_CAP
    
    cd /analysis/dir
    moduleultra init
    moduleultra install --dev /path/to/MetaSUB_CAP
    moduleultra add pipeline metasub_cap

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

Planned Modules
----------------

- Humann2
- CRASS

Finished Modules
----------------

- Kraken
- Metaphlan2
- MASH
- microbial/macrobial filtering

Module Dependencies
-------------------

We are building a system so that every pipeline can be run in its own conda environement. In principle modules can use any software on Conda or PyPi. Projects on github or bitbucket are also fine so long as they can be installed by script.

Licence
-------

MIT License

