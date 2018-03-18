

rule centrifuge_read_assignments:
    input:
        reads1 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read1'),
        reads2 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read2'),
    output:
        report = config['centrifuge_taxonomy_profiling']['report']
        classification = config['centrifuge_taxonomy_profiling']['classification']
    threads: int(config['centrifuge_taxonomy_profiling']['threads'])
    params:
        index = config['centrifuge_taxonomy_profiling']['index']['filepath']
        exc = config['centrifuge_taxonomy_profiling']['centrifuge']['filepath']
    resources:
        time = int(config['centrifuge_taxonomy_profiling']['time']),
        n_gb_ram = int(config['centrifuge_taxonomy_profiling']['ram'])
    run:
        cmd = ('{params.exc} '
               '-p {threads} '
               '-x {params.index} '
               '-1 {input.reads1} '
               '-2 {input.reads2} '
               '--report-file {output.report} '
               '-S {output.classification} '
        )
        shell(cmd)


rule centrifuge_make_mpa:
    input:
        classification = config['centrifuge_taxonomy_profiling']['classification']
    output:
        kreport = config['centrifuge_taxonomy_profiling']['mpa']
    params:
        index = config['centrifuge_taxonomy_profiling']['index']['filepath'],
        kreport = config['centrifuge_taxonomy_profiling']['kreport']['filepath']
    run:
        cmd = ('{params.kreport} '
               '-x {params.index} '
               '{input.classification} '
               '> '
               '{output.mpa} '
        )
        shell(cmd)