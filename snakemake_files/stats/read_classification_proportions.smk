
# TODO

rule count_class_proportions:
    input:
        human_reads = getOriginResultFiles(config, 'filter_human_dna', 'human_read1'),
        readstats = config['read_stats']['json'],
        tbl = config['quantify_macrobial']['tbl'],
        kraken = config['kraken_taxonomy_profiling']['mpa'],
    output:
        json = config['read_classification_proportions']['json']
    params:
        script = config['read_classification_proportions']['script']
    run:
        cmd = ('{params.script} '
               '{input.human_reads} '
               '{input.readstats} '
               '{input.tbl} '
               '{input.kraken} '
               ' > {output.json}')

        shell(cmd)
