from glob import glob


rule humann2_make_blastm8:
    input:
        reads1 = config['filter_macrobial_dna']['microbial_read1'],
        reads2 = config['filter_macrobial_dna']['microbial_read2'],
        dmnd_db = config['humann2_functional_profiling']['db']['filepath']
    output:
        m8 = config['humann2_functional_profiling']['m8']
    threads: int(config['humann2_functional_profiling']['dmnd']['threads'])
    params:
        dmnd = config['diamond']['exc']['filepath'],
        bsize=int(config['humann2_functional_profiling']['dmnd']['block_size']),
    resources:
        time=int(config['humann2_functional_profiling']['dmnd']['time']),
        n_gb_ram=int(config['humann2_functional_profiling']['dmnd']['ram'])
    run:
        cmd = ('{params.dmnd} blastx '
               '--threads {threads} '
               '-d {input.dmnd_db} '
               '-q {input.reads1} '
               '--block-size {params.bsize} '
               '> {output.m8} ') 
    	shell(cmd)


rule humann2_make_summaries:
    input:
        m8 = config['humann2_functional_profiling']['m8']
    output:
        genes = config['humann2_functional_profiling']['genes'],
        path_abunds = config['humann2_functional_profiling']['path_abunds'],
        path_cov  = config['humann2_functional_profiling']['path_cov']
    threads: int(config['humann2_functional_profiling']['threads'])
    params:
        exc=config['humann2_functional_profiling']['exc']['filepath'],
        sample_name='{sample_name}'
    resources:
        time=int(config['humann2_functional_profiling']['time']),
        n_gb_ram=int(config['humann2_functional_profiling']['ram'])
    run:
        odir = params.sample_name + '_humann2'
        genes = odir + '/*genefamilies.tsv'
        abunds = odir + '/*pathabundance.tsv'
        covs = odir + '/*pathcoverage.tsv'
               
        cmd = ('{params.exc} '
               '--input {input.m8} '
               '--output {params.sample_name}_humann2 ; '
               'mv ' + genes + ' {output.genes} ; '
               'mv ' + abunds + ' {output.path_abunds} ; '
               'mv ' + covs + ' {output.path_cov} ; ')
    	shell(cmd)
