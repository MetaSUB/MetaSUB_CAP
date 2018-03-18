

rule gottcha_taxonomy_profiling:
    input:
        reads1 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read1'),
    output:
        summary = config['gottcha_taxonomy_profiling']['summary_table']
        full = config['gottcha_taxonomy_profiling']['full_table']
    params:
        exc = config['gottcha_taxonomy_profiling']['exc']['filepath']
        index = config['gottcha_taxonomy_profiling']['index']['filepath']
        dirname = 'temp_gottcha_{sample_name}'
    threads: int(config['gottcha_taxonomy_profiling']['threads'])
    resources:
        time = int(config['gottcha_taxonomy_profiling']['time']),
        n_gb_ram = int(config['gottcha_taxonomy_profiling']['ram'])
    run:
        cmd = ('{params.exc} '
               '-t {threads} '
               '--input {input.reads1} '
               '--database {params.index} '
               '--mode full '
               '--outdir {params.dirname} '
               '; '
               'mv {params.dirname}/*.gottcha.tsv {output.summary}; '
               'mv {params.dirname}/*.gottcha_full.tsv {output.summary}; '
        )
        shell(cmd)
