

rule humann2_normalize_genes_read_depth:
    input:
        genes = config['humann2_functional_profiling']['genes'],
        readstats = config['read_stats']['json']
    output:
        ngenes = config['humann2_normalize_genes']['read_depth_norm_genes']
    params:
        script = config['humann2_normalize_genes']['read_depth_script']
    run:
        cmd = ('{params.script} '
               '{input.genes} '
               '{input.readstats} '
               ' > {output.ngenes}')
        shell(cmd)


rule humann2_normalize_genes_ags:
    input:
        genes = config['humann2_normalize_genes']['read_depth_norm_genes'],
        ags = config['microbe_census']['stats']
    output:
        ngenes = config['humann2_normalize_genes']['ags_norm_genes']
    params:
        script = config['humann2_normalize_genes']['ags_script']
    run:
        cmd = ('{params.script} '
               '{input.genes} '
               '{input.ags} '
               ' > {output.ngenes}')
        shell(cmd)