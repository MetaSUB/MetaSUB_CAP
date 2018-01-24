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

MegaRes
-------

The CAP uses MegaRes to identify antibiotic resistance genes.

`AWS Download Link <https://s3.amazonaws.com/metasub-cap-databases/megares_v1.0.1.tar.gz>`_

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

MetaPhlAn2
----------

Microbial Genomes
-----------------

The CAP aligns reads to Staph Aureus n315 genome using bowtie2

This database includes the SAn315 genome as a fasta and a bowtie2 index.

`AWS Download Link <https://s3.amazonaws.com/metasub-cap-databases/staph_aureus_n315.tar.gz>`_


Macrobial Genomes
-----------------

.. csv-table:: Macrobial Genomes
    :header: "common name", "scientific name", "accension", "date created", "ftp link"

    "house cat", "felis catus", "GCA_000003115.1", "14-jan-2009", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/003/115/GCA_000003115.1_catChrV17e/GCA_000003115.1_catChrV17e_genomic.fna.gz>`_
    "cow", "bos taurus", "GCA_000003055.5", "24-apr-2009", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/003/055/GCA_000003055.5_Bos_taurus_UMD_3.1.1/GCA_000003055.5_Bos_taurus_UMD_3.1.1_genomic.fna.gz>`_
    "pig", "sus scrofa", "GCA_002844635.1", "18-Dec-2017", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/002/844/635/GCA_002844635.1_USMARCv1.0/GCA_002844635.1_USMARCv1.0_genomic.fna.gz>`_
    "chicken", "gallus gallus", "GCA_002798355.1", "28-Nov-2017", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/002/798/355/GCA_002798355.1_Ogye1.0/GCA_002798355.1_Ogye1.0_genomic.fna.gz>`_
    "rat", "rattus norvegicus", "GCA_000001895.4", "27-Nov-2002", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/001/895/GCA_000001895.4_Rnor_6.0/GCA_000001895.4_Rnor_6.0_cds_from_genomic.fna.gz>`_
    "rabbit", "oryctolagus cuniculus", "GCA_000003625.1", "13-May-2005", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/003/625/GCA_000003625.1_OryCun2.0/GCA_000003625.1_OryCun2.0_genomic.fna.gz>`_
    "zebrafish", "danio rerio", "GCA_000002035.4", "05-Jul-2005", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/002/035/GCA_000002035.4_GRCz11/GCA_000002035.4_GRCz11_genomic.fna.gz>`_
    "housefly", "drosophila melanogaster", "GCA_000001215.4", "30-Apr-2002", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/001/215/GCA_000001215.4_Release_6_plus_ISO1_MT/GCA_000001215.4_Release_6_plus_ISO1_MT_genomic.fna.gz>`_
    "mouse", "mus musculus", "GCA_000002165.1", "07-Jul-2005", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/001/635/GCA_000001635.8_GRCm38.p6/GCA_000001635.8_GRCm38.p6_genomic.fna.gz>`_
    "dog", "canis lupus familiaris", "GCA_000002285.2", "10-Jul-2004", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/002/285/GCA_000002285.2_CanFam3.1/GCA_000002285.2_CanFam3.1_genomic.fna.gz>`_
    "maize", "zea mays", "GCA_000005005.6", "29-Jan-2010", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/005/005/GCA_000005005.6_B73_RefGen_v4/GCA_000005005.6_B73_RefGen_v4_genomic.fna.gz>`_
    "apple", "malus domestica", "GCA_000148765.2", "03-sep-2010", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/148/765/GCA_000148765.2_MalDomGD1.0/GCA_000148765.2_MalDomGD1.0_genomic.fna.gz>`_
    "orange", "citrus sinensis", "GCA_000317415.1", "18-sep-2012", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/317/415/GCA_000317415.1_Csi_valencia_1.0/GCA_000317415.1_Csi_valencia_1.0_genomic.fna.gz>`_
    "honeybee", "apis mellifera", "GCA_000002195.1", "19-dec-2003", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/002/195/GCA_000002195.1_Amel_4.5/GCA_000002195.1_Amel_4.5_genomic.fna.gz>`_
    "pigeon", "columba livia", "GCA_001887795.1", "29-nov-2016", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/001/887/795/GCA_001887795.1_colLiv2/GCA_001887795.1_colLiv2_genomic.fna.gz>`_
    "horse", "equus caballus", "GCA_000002305.1", "24-jan-2007", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/002/305/GCA_000002305.1_EquCab2.0/GCA_000002305.1_EquCab2.0_genomic.fna.gz>`_
    "lettuce", "lactuca sativa", "GCA_002870075.1", "09-jan-2018", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/002/870/075/GCA_002870075.1_Lsat_Salinas_v7/GCA_002870075.1_Lsat_Salinas_v7_genomic.fna.gz>`_
    "potato", "solanum tuberosum", " GCA_000226075.1", "24-may-2011", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/226/075/GCA_000226075.1_SolTub_3.0/GCA_000226075.1_SolTub_3.0_genomic.fna.gz>`_
    "tomato", "solanum lycpersicum", "GCA_000188115.2", "10-dec-2010", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/188/115/GCA_000188115.2_SL2.50/GCA_000188115.2_SL2.50_genomic.fna.gz>`_
    "strawberry", "Fragaria x ananassa", "GCA_000511835.1", "27-nov-2013", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/511/835/GCA_000511835.1_FAN_r1.1/GCA_000511835.1_FAN_r1.1_genomic.fna.gz>`_
    "bannana", "Musa acuminata subsp. malaccensis", "GCA_000313855.2", "09-aug-2012", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/313/855/GCA_000313855.2_ASM31385v2/GCA_000313855.2_ASM31385v2_genomic.fna.gz>`_
    "grape", " Vitis vinifera", "GCA_000003745.2", "13-feb-2007", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/003/745/GCA_000003745.2_12X/GCA_000003745.2_12X_genomic.fna.gz>`_
    "mosquito", "aedes aegypti", "GCA_002204515.1", "15-jun-2017", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/002/204/515/GCA_002204515.1_AaegL5.0/GCA_002204515.1_AaegL5.0_genomic.fna.gz>`_
    "octopus", "Octopus bimaculoides", "GCA_001194135.1", "31-jul-2015", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/001/194/135/GCA_001194135.1_Octopus_bimaculoides_v2_0/GCA_001194135.1_Octopus_bimaculoides_v2_0_genomic.fna.gz>`_
    "salmon", "salmo salar", "GCA_000233375.4", "25-oct-2011", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/233/375/GCA_000233375.4_ICSASG_v2/GCA_000233375.4_ICSASG_v2_genomic.fna.gz>`_
    "cod", "gadus morhua", "GCA_000231765.1", "25-aug-2011", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/231/765/GCA_000231765.1_GadMor_May2010/GCA_000231765.1_GadMor_May2010_genomic.fna.gz>`_
    "wheat", "Triticum aestivum", "GCA_002220415.2", "13-jul-2017", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/002/220/415/GCA_002220415.2_Triticum_3.1/GCA_002220415.2_Triticum_3.1_genomic.fna.gz>`_
    "hops", "  Humulus lupulus var. lupulus", "  GCA_000831365.1", "11-dec-2014", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/831/365/GCA_000831365.1_hl_SW_version_1.0.fasta/GCA_000831365.1_hl_SW_version_1.0.fasta_genomic.fna.gz>`_
    "rice", "Oryza sativa Japonica Group", "GCA_000005425.2", "02-feb-2005", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/005/425/GCA_000005425.2_Build_4.0/GCA_000005425.2_Build_4.0_genomic.fna.gz>`_
    "yam", "Dioscorea rotundata", "GCA_002240015.2", "28-jul-2017", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/002/240/015/GCA_002240015.2_TDr96_F1_Pseudo_Chromosome_v1.0/GCA_002240015.2_TDr96_F1_Pseudo_Chromosome_v1.0_genomic.fna.gz>`_
    "wallaby", "Notamacropus eugenii", "GCA_000004035.1", "26-nov-2008", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/004/035/GCA_000004035.1_Meug_1.1/GCA_000004035.1_Meug_1.1_genomic.fna.gz>`_
    "alligator", "Alligator mississippiensis", "GCA_000281125.4", "24-jul-2012", `NCBI <ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/281/125/GCA_000281125.4_ASM28112v4/GCA_000281125.4_ASM28112v4_genomic.fna.gz>`_
    





