

rule count_class_proportions:
    input:
        kraken = config['kraken_taxonomy_profiling']['mpa'],
        human_reads1 = config['filter_human_dna']['human_read1'],
        nonhuman_reads1 = config['filter_human_dna']['nonhuman_read1'],
        microbial_reads1 = config['filter_macrobial_dna']['microbial_read1'],
    output:
        json = config['read_classification_proportions']['json']
    params:
        script = config['pipeline_dir'] + config['read_classification_proportions']['script']
    run:
        cmd = ('{params.script} '
               '{input.human_reads1} '
               '{input.nonhuman_reads1} '
               '{input.microbial_reads1} '
               '{input.kraken} '
               ' > {output.json}')

        shell(cmd)
