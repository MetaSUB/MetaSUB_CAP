

rule metaphlan2_make_mpa:
    input:
        reads1 = config['filter_macrobial_dna']['microbial_read1'],
        reads2 = config['filter_macrobial_dna']['microbial_read2'] 
    output:
        mpa = config['metaphlan2_taxonomy_profiling']['mpa'],
        sam = config['metaphlan2_taxonomy_profiling']['sam'],
        bt2 = temp(config['metaphlan2_taxonomy_profiling']['mpa'] + '.bt2_temp')
    threads: int(config['metaphlan2_taxonomy_profiling']['threads'])
    params:
        metaphlan2=config['metaphlan2_taxonomy_profiling']['exc']['filepath'],
    resources:
        time=int(config['metaphlan2_taxonomy_profiling']['time']),
        n_gb_ram=int(config['metaphlan2_taxonomy_profiling']['ram'])
    run:
        cmd = ('{params.metaphlan2} '
               '--input_type fastq '
               '-s {output.sam} '
               '--bowtie2out {output.bt2} '
               '{input.reads1},{input.reads2} '
               '--nproc {threads} '
               '> {output.mpa}')
        shell(cmd)

