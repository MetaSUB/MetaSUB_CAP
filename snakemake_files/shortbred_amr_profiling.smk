

rule shortbred_make_amr_table:
    input:
        reads1 = config['filter_macrobial_dna']['microbial_read1'],
        reads2 = config['filter_macrobial_dna']['microbial_read2'] 
    output:
        table = config['shortbred_amr_profiling']['table']
    params:
        ref=config['shortbred_amr_profiling']['ref']['filepath'],
        shortbred=config['shortbred']['exc']['filepath']
    threads: int(config['shortbred_amr_profiling']['threads'])
    version: config['shortbred_amr_profiling']['exc']['version']
    resources:
        time=int(config['shortbred_amr_profiling']['time']),
        n_gb_ram=int(config['shortbred_amr_profiling']['ram'])
    run:
        cmd = ('python2 {params.shortbred} '
               '--markers {params.ref} '
               '--wgs {input.reads1} {input.reads2} '
           '--results {output.table} '
               '--threads {threads} ')
        shell(cmd)

