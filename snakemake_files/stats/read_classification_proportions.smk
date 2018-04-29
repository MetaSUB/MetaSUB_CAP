
# TODO

rule count_class_proportions:
    input:
        all_reads = getOriginResultFiles(config, 'adapter_removal', 'clean_read1'),
        readstats = config['read_stats']['json'],
        tbl = config['quantify_macrobial']['tbl'],
        kraken = config['krakenhll_taxonomy_profiling']['report'],
    output:
        json = config['read_classification_proportions']['json']
    params:
        script = config['read_classification_proportions']['script']
    run:
        cmd = ('{params.script} '
               '{input.all_reads} '
               '{input.readstats} '
               '{input.tbl} '
               '{input.kraken} '
               ' > {output.json}')

        shell(cmd)
