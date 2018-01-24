
rule normalize_kraken_taxonomy:
    input:
        ags = config['microbe_census_group_summary']['vector'],
        kraken = config['kraken_group_summary']['json']
    output:
        json = config['normalized_kraken_taxonomy']['json']
    threads: 1
    params:
        script = config['pipeline_dir'] + config['normalized_kraken_taxonomy']['script']
    run:
        cmd = '{params.script} {input.ags} {input.kraken} > {output.json}'
        shell(cmd)
