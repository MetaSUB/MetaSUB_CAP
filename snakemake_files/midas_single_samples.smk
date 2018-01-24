


rule midas_profile_taxa:
    input:
        reads1 = config['filter_macrobial_dna']['microbial_read1'],
        reads2 = config['filter_macrobial_dna']['microbial_read2']
    output:
        profile = config['midas_single_samples']['profile'],
    threads: int(config['midas_single_samples']['threads'])
    params:
        sample_name='{sample_name}',
        midas = config['midas_single_samples']['exc']['filepath'],
        ref = config['midas_single_samples']['db']['filepath']
    resources:
        time = int(config['midas_single_samples']['time']),
        n_gb_ram = int(config['midas_single_samples']['ram'])
    run:
        cmd = ('{params.midas} '
               'species '
               '{params.sample_name}_midas '
               '-d {params.ref} '
               '-1 {input.reads1} '
               '-2 {input.reads2} '
               '-t {threads} '
               '--remove_temp ; '
               'mv {params.sample_name}_midas/' + 'species_profile.txt {output.profile}')
        shell(cmd)

'''
rule midas_profile_genes:
    input:
        reads1 = config['filter_macrobial_dna']['microbial_read1'],
        reads2 = config['filter_macrobial_dna']['microbial_read2']
    output:
        profile = config['midas_single_samples']['genes_out'],
    threads: int(config['midas_single_samples']['threads'])
    params:
        sample_name = '{sample_name}',
        midas = config['midas_single_samples']['exc']['filepath'],
        ref = config['midas_single_samples']['db']['filepath']
    resources:
        time = int(config['midas_single_samples']['time']),
        n_gb_ram = int(config['midas_single_samples']['ram'])
    run:
        cmd = ('{params.midas} '
               'genes '
               '{params.sample_name}_midas '
               '-d {params.ref} '
               '-1 {input.reads1} '
               '-2 {input.reads2} '
               '-t {threads} '
               '--remove_temp ; '
               'mv {params.sample_name}_midas/' + 'species_profile.txt {output.profile}')
        shell(cmd)
'''