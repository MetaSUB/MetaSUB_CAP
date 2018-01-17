


rule midas_merge_taxa_profile:
    input:
        profiles = expandGroup(config['midas_single_samples']['species_out'])
    output:
        rel_abund = config['midas_merge_groups']['rel_abund'],
        count_reads = config['midas_merge_groups']['count_reads'],
        coverage = config['midas_merge_groups']['coverage'],
        species_prevalence = config['midas_merge_groups']['species_prevalence'],
    params:
        group_name='{group_name}'
        midas = config['midas_merge_groups']['exc']['filepath'],
        ref = config['midas_single_samples']['db']['filepath']
    resources:
        time = 1,
        n_gb_ram = 1
    run:
        cmd = ('{params.midas} '
               'species '
               '{params.group_name}_midas_merge '
               '-t list '
               '-db {params.ref} '
               '-i ')
        cmd += ','.join(input.profiles)
        cmd += ('mv {params.group_name}_midas_merge/relative_abundance.txt {output.rel_abund} ; '
                'mv {params.group_name}_midas_merge/count_reads.txt {output.count_reads} ; '
                'mv {params.group_name}_midas_merge/coverage.txt {output.coverage} ; '
                'mv {params.group_name}_midas_merge/species_prevalence.txt {output.species_prevalence} ; ')
        shell(cmd)
