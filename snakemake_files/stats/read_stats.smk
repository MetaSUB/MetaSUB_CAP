
# TODO

rule find_read_stats:
    input:
        reads1 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read1'),
        reads2 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read2'),
        raw_reads1 = config['adapter_removal']['clean_read1'],
        microbial_reads1 = config['filter_human_dna']['nonhuman_read2'],
    output:
        json = config['read_stats']['json']
    params:
        script = config['read_stats']['script'],
        nseqs = 10 * 1000
    run:
        cmd = ('{params.script} '
               '-n {params.nseqs} '
               '{input.raw_reads1} '
               '{input.microbial_reads1} '
               ' > {output.json}')

        shell(cmd)
