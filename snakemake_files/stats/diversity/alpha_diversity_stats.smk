

rule measure_alpha_diversity:
    input:
        metaphlan2 = config['metaphlan2_taxonomy_profiling']['mpa'],
        kraken = config['kraken_taxonomy_profiling']['mpa']
    output:
        json = config['alpha_diversity_stats']['json']
    params:
        script = config['alpha_diversity_stats']['script']
    run:
        cmd = '{params.script} '
        cmd += 'metaphlan2,{input.metaphlan2} '
        cmd += 'kraken,{input.kraken} '
        cmd += ' > {output.json}'

        shell(cmd)