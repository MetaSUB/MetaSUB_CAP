
rule measure_beta_diversity:
    input:
        krakens = expandGroup(config['krakenhll_taxonomy_profiling']['report_strict']),
        mphlan2s = expandGroup(config['metaphlan2_taxonomy_profiling']['mpa'])
    output:
        json = config['beta_diversity_stats']['json']
    params:
        script = config['beta_diversity_stats']['script']
    run:
        print(input)
        cmd = '{params.script} '
        for mphlan2 in input.mphlan2s:
            cmd += '-t metaphlan2 ' + getSample(mphlan2) + ' ' + mphlan2 + ' '
        for kraken in input.krakens:
            cmd += '-t kraken ' + getSample(kraken) + ' ' + kraken + ' '
        cmd += ' > {output.json}'
        shell(cmd)
