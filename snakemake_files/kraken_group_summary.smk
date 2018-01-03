

rule summarize_kraken:
    input:
        stats = expandGroup(config['kraken_taxonomy_profilimg']['mpa'], names=True)
    output:
        vector = config['kraken_summary']['json']
    threads: 1
    params:
        script = config['pipeline_dir'] + config['kraken_summary']['script']
    run:
        cmd = '{params.script} '
        for sname, mcf in input.stats:
            cmd += '-s {} {}'.format(sname, mcf)
        cmd += ' > {output.vector}'
        shell(cmd)
