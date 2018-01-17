

rule humann2_normalize_genes:
    input:
        genes = config['humann2_functional_profiling']['genes'],
        ags = config['microbe_census']['stats']
    output:
        ngenes = config['humann2_normalize_genes']['norm_genes']
    params:
        script = config['pipeline_dir'] + config['humann2_normalize_genes']['script'] 
    run:
        cmd = ('{params.script} '
                '{input.genes} '
                '{input.ags} '
                ' > {output.ngenes}')
        shell(cmd)