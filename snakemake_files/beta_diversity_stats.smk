
rule measure_beta_diversity:
    input:
        krakens = expandGroup(config['kraken_taxonomy_profiling']['mpa']),
        mphlan2s = expandGroup(config['metaphlan2_taxonomy_profiling']['mpa'])
    output:
        json = config['alpha_dicersity_stats']['json']
    params:
        script = config['pipeline_dir'] + config['beta_diversity_stats']['script']
    run:
        cmd = '{params.script} '
        cmd += '-t metaphlan2 '
        for mphlan2 in mphlan2s:
            cmd += getSample(mphlan2) + ' ' + mphlan2 + ' '
        cmd += '-t kraken '
        for kraken in krakens:
            cmd += getSample(kraken) + ' ' + krakens + ' '
        cmd += ' > {output.json}'
        shell(cmd)
