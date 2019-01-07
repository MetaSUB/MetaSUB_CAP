

rule krakenhll_read_assignment:
    input:
        reads1 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read1'),
        reads2 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read2'),
    output:
        readAssignments = config['krakenhll_taxonomy_profiling']['read_assignments']
    threads: int(config['krakenhll_taxonomy_profiling']['threads'])
    version: ' '.join(config['krakenhll_taxonomy_profiling']['exc']['version'].split('\n'))

    params:
        krakenhll = config['krakenhll_taxonomy_profiling']['exc']['filepath'],
        db = config['krakenhll_taxonomy_profiling']['db']['filepath'],
    resources:
        time = int(config['krakenhll_taxonomy_profiling']['time']),
        n_gb_ram = int(config['krakenhll_taxonomy_profiling']['ram'])
    run:
        cmd = (
            '{params.krakenhll} '
            '--report-file {output.readAssignments} '
            '--gzip-compressed '
            '--fastq-input '
            '--threads {threads} '
            '--paired '
            '--preload '
            '--db {params.db} '
            '{input.reads1} '
            '{input.reads2} '
        )
        shell(cmd)


rule krakenhll_read_assignment_single:
    input:
        reads1 = getOriginResultFiles(config, 'filter_human_dna_single', 'nonhuman_reads'),
    output:
        readAssignments = config['krakenhll_taxonomy_profiling']['read_assignments']
    threads: int(config['krakenhll_taxonomy_profiling']['threads'])
    version: ' '.join(config['krakenhll_taxonomy_profiling']['exc']['version'].split('\n'))

    params:
        krakenhll = config['krakenhll_taxonomy_profiling']['exc']['filepath'],
        db = config['krakenhll_taxonomy_profiling']['db']['filepath'],
    resources:
        time = int(config['krakenhll_taxonomy_profiling']['time']),
        n_gb_ram = int(config['krakenhll_taxonomy_profiling']['ram'])
    run:
        cmd = (
            '{params.krakenhll} '
            '--report-file {output.readAssignments} '
            '--gzip-compressed '
            '--fastq-input '
            '--threads {threads} '
            '--preload '
            '--db {params.db} '
            '{input.reads1} '
        )
        shell(cmd)


rule krakenhll_filter_assignments:
    input:
        readAssignments = config['krakenhll_taxonomy_profiling']['read_assignments']
    output:
        filtered = config['krakenhll_taxonomy_profiling']['report']
    params:
        minkmer = config['krakenhll_taxonomy_profiling']['min_kmer'],
        mincov = config['krakenhll_taxonomy_profiling']['min_cov'],
        script = config['krakenhll_taxonomy_profiling']['script'],
    run:
        cmd = (
            '{params.script} '
            '--min-kmer {params.minkmer} '
            '--min-cov {params.mincov} '
            '{input.readAssignments} '
            '> {output.filtered}'
        )
        shell(cmd)


rule krakenhll_filter_assignments_medium:
    input:
        readAssignments = config['krakenhll_taxonomy_profiling']['read_assignments']
    output:
        filtered = config['krakenhll_taxonomy_profiling']['report_medium']
    params:
        num_kmer = config['krakenhll_taxonomy_profiling']['med_kmer'],
        required_cov = config['krakenhll_taxonomy_profiling']['med_cov'],
        script = config['krakenhll_taxonomy_profiling']['script'],
    run:
        cmd = (
            '{params.script} '
            '--min-kmer {params.num_kmer} '
            '--min-cov {params.required_cov} '
            '{input.readAssignments} '
            '> {output.filtered}'
        )
        shell(cmd)


rule krakenhll_filter_assignments_strict:
    input:
        readAssignments = config['krakenhll_taxonomy_profiling']['read_assignments']
    output:
        filtered = config['krakenhll_taxonomy_profiling']['report_strict']
    params:
        num_kmer = config['krakenhll_taxonomy_profiling']['max_kmer'],
        required_cov = config['krakenhll_taxonomy_profiling']['max_cov'],
        script = config['krakenhll_taxonomy_profiling']['script'],
    run:
        cmd = (
            '{params.script} '
            '--min-kmer {params.num_kmer} '
            '--min-cov {params.required_cov} '
            '{input.readAssignments} '
            '> {output.filtered}'
        )
        shell(cmd)
