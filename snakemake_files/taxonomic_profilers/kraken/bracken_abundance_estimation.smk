

rule bracken_estimate_abundance_species:
    input:
        report = config['kraken_taxonomy_profiling']['report']
    output:
        report = config['bracken_abundance_estimation']['species_report']
    params:
        exc = config['bracken_abundance_estimation']['exc'],
        kmers = config['bracken_abundance_estimation']['kmer_distributions']
    run:
        cmd = ('{params.exc} '
               '-i {input.report} '
               '-k {params.kmers} '
               '-l S '
               '-o {output.report} '
        )
        shell(cmd)

rule bracken_estimate_abundance_genus:
    input:
        report = config['kraken_taxonomy_profiling']['report']
    output:
        report = config['bracken_abundance_estimation']['genus_report']
    params:
        exc = config['bracken_abundance_estimation']['exc'],
        kmers = config['bracken_abundance_estimation']['kmer_distributions']
    run:
        cmd = ('{params.exc} '
               '-i {input.report} '
               '-k {params.kmers} '
               '-l G '
               '-o {output.report} '
        )
        shell(cmd)

rule bracken_estimate_abundance_phylum:
    input:
        report = config['kraken_taxonomy_profiling']['report']
    output:
        report = config['bracken_abundance_estimation']['phylum_report']
    params:
        exc = config['bracken_abundance_estimation']['exc'],
        kmers = config['bracken_abundance_estimation']['kmer_distributions']
    run:
        cmd = ('{params.exc} '
               '-i {input.report} '
               '-k {params.kmers} '
               '-l P '
               '-o {output.report} '
        )
        shell(cmd)
