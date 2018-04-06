
# TODO

rule find_read_stats:
    input:
        reads1 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read1'),
        reads2 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read2'),
    output:
        json = config['read_stats']['json']
    params:
        script = config['read_stats']['script'],
        nseqs = 10 * 1000
    run:
        cmd = ('{params.script} '
               '-n {params.nseqs} '
               '{input.microbial_reads1} '
               ' > {output.json}')

        shell(cmd)
