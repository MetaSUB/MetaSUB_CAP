

rule krakenhll_read_assignment:
    input:
        reads1 = config['filter_human_dna']['nonhuman_read1'],
        reads2 = config['filter_human_dna']['nonhuman_read2']
    output:
        readAssignments = config['krakenhll_taxonomy_profiling']['read_assignments']
    threads: int(config['krakenhll_taxonomy_profiling']['threads'])
    version: ' '.join(config['krakenhll_taxonomy_profiling']['exc']['version'].split('\n'))

    params:
        krakenhll = config['krakenhll_taxonomy_profiling']['exc']['filepath'],
        db = config['kraken_taxonomy_profiling']['db']['filepath'],
    resources:
        time = int(config['kraken_taxonomy_profiling']['time']),
        n_gb_ram = int(config['kraken_taxonomy_profiling']['ram'])
    run:
        cmd = (
            '{params.krakenhll} --gzip-compressed --fastq-input --threads {threads} '
        '--paired --preload --db {params.db} {input.reads1} {input.reads2} '
            '> {output.readAssignments}')
        shell(cmd)


rule krakenhll_filter_assignments:
    input:
        readAssignments = config['krakenhll_taxonomy_profiling']['read_assignments']

