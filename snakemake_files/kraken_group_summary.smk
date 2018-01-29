

rule summarize_kraken:
    input:
        kraken = expandGroup(config['kraken_taxonomy_profiling']['mpa'])
    output:
        vector = config['kraken_group_summary']['json']
    threads: 1
    params:
        script = config['kraken_group_summary']['script'],
        statNames = expandGroup(config['kraken_taxonomy_profiling']['mpa'], names=True)
    run:
        cmd = '{params.script} '
        for sname, mcf in zip(params.statNames, input.kraken):
            cmd += ' -s {} {}'.format(sname, mcf)
        cmd += ' > {output.vector}'
        shell(cmd)
