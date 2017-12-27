

rule find_read_stats:
    input:
        raw_reads1 = getOriginResultFiles(config, "raw_short_read_dna", "read1"),
        microbial_reads1 = config['filter_macrobial_dna']['microbial_read1'],
    output:
        json = config['read_stats']['json']
    params:
        script = config['read_classification_proportions']['script']
        nseqs = 100 * 1000
    run:
        cmd = ('{params.script} '
               '-n {params.nseqs} '
               '{input.raw_reads1} '
               '{input.microbial_reads1} '
               ' > {output.json}')

        shell(cmd)
