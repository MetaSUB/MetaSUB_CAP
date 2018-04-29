
=======
Modules
=======

Quality Control
===============

Filter Human DNA
----------------

Nearly every metagenomic sample contains human DNA. This may be normal (i.e. a human saliva sample) or lab contamination.

Either way the human DNA needs to be removed. The CAP aligns reads to hg38 (with alt contigs) using ``bowtie2 --very-fast`` and proceeds with that did not align. 

Filter Macrobial DNA
--------------------

The CAP looks for DNA from common macrobial species in a sample. This DNA can help us to understand the environment that a sample was sourced from. Most of the species represented in this database are human associated species like dogs, cats, wheat, and rice.

See :ref:`databases` for the full list of species.

Adapter Removal
---------------

The CAP removes reads that contain 'N', reads with low quality bases and trims adapters. This is done via `AdapterRemoval ver 2.1.7`.

`AdapterRemoval GitHub <https://github.com/MikkelSchubert/adapterremoval>`_

`AdapterRemoval Paper <https://doi.org/10.1186/s13104-016-1900-2>`_

Diversity
=========

Alpha Diversity Stats
---------------------

Calculates the richness and shannon index at the species and genus level for both kraken and metaphlan2 output. Output is a json file.

These outputs are produced by a script ``alpha_diversity_stats.py``

`Diversity Indices <https://en.wikipedia.org/wiki/Diversity_index>`_

Beta Diversity Stats
--------------------

Calculates the rho proportionality and Jensen Shannon Distance at the species and genus level for both kraken and metaphlan2 outputs. Output is a json file. These are pairwise functions and are computed between every pair of samples in a given group.

These outputs are produced by a script ``beta_diversity_stats.py``

`Rho Proportionality <https://cran.r-project.org/web/packages/propr/index.html>`_

`Jensen Shannon Distances <https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence>`_

N.B. This is J.S. Distance, the squareroot of J.S. Divergence. This is a metric.

HMP Site Distances
------------------


Mash Sketch
-----------

Produces a Mash Sketch with 10,000,000 representative kmers.

`Mash Paper <https://doi.org/10.1186/s13059-016-0997-x>`_

`Mash GitHub <https://github.com/marbl/Mash>`_

`Mash Docs <http://mash.readthedocs.io/en/latest/>`_

Mash Intersample Distances
^^^^^^^^^^^^^^^^^^^^^^^^^^

Finds the jaccard distance between pairs of kmer profiles in a group of samples.

Runs only on reads that did not align to the human genome or macrobial genomes.

Functional Profiling
====================

HUMAnN2 Functional Profiling
----------------------------

Finds how many reads map to particular genes in particular pathways. The catalog of genes is uniref90 and diamond is used as an aligner. HUMAnN2 is used to quantify values.

Runs only on reads that did not align to the human genome or macrobial genomes.

`HUMAnN2 Paper <https://doi.org/10.1371/journal.pcbi.1002358>`_

`HUMAnN2 BitBucket <https://bitbucket.org/biobakery/humann2/wiki/Home>`_

`DIAMOND GitHub <https://github.com/bbuchfink/diamond>`_

`DIAMOND Paper <https://www.nature.com/articles/nmeth.3176?message-global=remove>`_

HUMAaN2 Gene Normalization
^^^^^^^^^^^^^^^^^^^^^^^^^^

Normalizes RPKM values based on the estimate of average genome size produced by MicrobeCensus. This technique is described in the paper introducing Microbe Census.

This ouput is produced by a script ``normalize_genes.py``

`MicrobeCensus Paper <https://doi.org/10.1186/s13059-015-0611-7>`_

Taxonomy
========

Kraken Taxonomy Profiling
-------------------------

Uses kraken to pseudo-map reads to a database of species. See :ref:`databases` for the details of the database being used.

Runs only on reads that did not align to the human genome or macrobial genomes.

`Kraken Paper <https://doi.org/10.1186/gb-2014-15-3-r46>`_
`Kraken Home Page <https://ccb.jhu.edu/software/kraken/>`_

Kraken Summary
^^^^^^^^^^^^^^

Combines the kraken outputs from a group of samples into a single table.

Produced by a script ``summarize_kraken.py``

Normalized Kraken Taxonomy
^^^^^^^^^^^^^^^^^^^^^^^^^^

Not yet implemented.

MetaPhlAn2 Taxonomy Profiling
-----------------------------

Uses MetaPhlAn2 to estimate the abundance of various species.

Runs only on reads that did not align to the human genome or macrobial genomes.

`MetaPhlAn2 BitBucket <https://bitbucket.org/biobakery/metaphlan2>`_

`MetaPhlAn2 Paper <http://www.nature.com/doifinder/10.1038/nbt.3589>`_

Statistics
==========

Microbe Census 
--------------

Estimates the average genome size for a sample by counting reads that map to Universal Single Copy Genes.

Runs only on reads that did not align to the human genome or macrobial genomes.

`MicrobeCensus GitHub <https://github.com/snayfach/MicrobeCensus>`_
`MicrobeCensus Paper <https://doi.org/10.1186/s13059-015-0611-7>`_

Microbe Census Group Summary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Summarizes the AGS for a groups of samples into a single file.

Produced by a script ``summarize_microbe_census.py``


Read Classification Proportions
-------------------------------

Counts the proportion of reads that mapped to human, bacteria, archaea, virus, and macrobes.

Produced by a script ``count_classified_reads.py``

Read Statistics
---------------

Counts some statistics like codon usage frequency and GC content on a subset of sequences.

Runs seperately on filtered and raw reads.

Produced by a script ``read_stats.py``

AMR Detection
=============

Resistome AMR Profiling
-----------------------

Shortbred AMR Profiling
-----------------------

Miscellaneous
=============

Align To Staph Aureus
---------------------

Maps reads to the Staph. Aureus genome using bowtie2. See :ref:`databases` for the details of the genome being used.




