
rule summarize_microbe_census:
    input:
        stats = expandGroup(config['microbe_census']['stats'])
    output:
        vector = config['microbe_census_group_summary']['vector']
    threads: 1
    params:
        script = config['pipeline_dir'] + config['microbe_census_group_summary']['script'],
        statNames = expandGroup(config['microbe_census']['stats'], names=True)
    run:
        cmd = '{params.script} '
        for sname, mcf in zip(params.statNames, input.stats):
            cmd += ' -s {} {}'.format(sname, mcf)
        cmd += ' > {output.vector}'
        shell(cmd)
