'''
This is an example of a basic one-to-one result. It takes
a previously computed result (in this case paired end reads with 
macroscopic DNA removed) and computes another result.

The only thing that needs to be specified here are the snakemake rules
that produce the necessary output files. Each module (this is a module)
needs to correspond to a result-definition given in 
pipeline_definitions.json. This definition tells ModuleUltra what outputs
it should expect.
'''


rule kraken_read_assignment:
    input:
        # these file patterns are automatically generated when
        # the snakemake is preprocessed. The definitions used
        # to generate can be found in pipeline_definition.json.
        reads1 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read1'),
        reads2 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read2'),
    output:
        readAssignments = temp(config['kraken_taxonomy_profiling']['read_assignments'][:-3])
    threads: int( config['kraken_taxonomy_profiling']['threads'])
    # User specified parameters like this can be stored in pipeline_config.json
    # The parameters can be user supplied parameters or constants as necessary
    version: ' '.join(config['kraken_taxonomy_profiling']['exc']['version'].split('\n'))
    # version isn't required but helps with provenance
    params:
        kraken = config['kraken_taxonomy_profiling']['exc']['filepath'],
        db = config['kraken_taxonomy_profiling']['db']['filepath'],
    resources:
        time=int(config['kraken_taxonomy_profiling']['time']),
        n_gb_ram=int(config['kraken_taxonomy_profiling']['ram'])
    run:
        cmd = (
            '{params.kraken} --gzip-compressed --fastq-input --threads {threads} '
        '--paired --preload --db {params.db} {input.reads1} {input.reads2} '
            '> {output.readAssignments}')
        shell(cmd)


rule kraken_make_mpa:
    input:
        raw = config['kraken_taxonomy_profiling']['read_assignments']
    output:
        mpa = config['kraken_taxonomy_profiling']['mpa']
    threads: 1
    version: config['kraken_taxonomy_profiling']['mpa_exc']['version']
    params:
        kraken_mpa = config['kraken_taxonomy_profiling']['mpa_exc']['filepath'],
        db = config['kraken_taxonomy_profiling']['db']['filepath'],
    resources:
        time=1,
        n_gb_ram=5
    shell:
        '{params.kraken_mpa} {input.raw} --db {params.db} > {output.mpa}'


rule kraken_make_report:
    input:
        raw = config['kraken_taxonomy_profiling']['read_assignments']
    output:
        report = config['kraken_taxonomy_profiling']['report']
    threads: 1
    version: config['kraken_taxonomy_profiling']['report_exc']['version']
    params:
        kraken_report = config['kraken_taxonomy_profiling']['report_exc']['filepath'],
        db = config['kraken_taxonomy_profiling']['db']['filepath'],
    resources:
        time=1,
        n_gb_ram=5
    shell:
        '{params.kraken_report} {input.raw} --db {params.db} > {output.report}'


rule compress_read_assignments_kraken:
    input:
        raw = config['kraken_taxonomy_profiling']['read_assignments'][:-3]
    output:
        compressed = config['kraken_taxonomy_profiling']['read_assignments']
    run:
        cmd = 'gzip {input.raw}'
        shell(cmd)


