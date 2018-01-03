
rule summarize_microbe_census:
    input:
        stats = expandGroup(config['microbe_census']['stats'], names=True)
    output:
        vector = config['microbe_census_summary']['vector']
    threads: 1
    params:
        script = config['pipeline_dir'] + config['microbe_census_summary']['script']
    run:
        cmd = '{params.script} '
        for sname, mcf in input.stats:
            cmd += '-s {} {}'.format(sname, mcf)
        cmd += ' > {output.vector}'
        shell(cmd)
