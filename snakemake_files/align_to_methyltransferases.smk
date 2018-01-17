

rule align_to_methyls:
    input:
        reads1 = config['filter_macrobial_dna']['microbial_read1'],
        reads2 = config['filter_macrobial_dna']['microbial_read2'],
    output:
        table = config['align_to_methyltransferases']['table']
    params:
        ref = config['align_to_methyltransferases']['ref']['filepath'],
        shortbred = config['shortbred']['exc']['filepath']
    threads: int(config['align_to_methyltransferases']['threads'])
    resources:
        time = int(config['align_to_methyltransferases']['time']),
        n_gb_ram = int(config['align_to_methyltransferases']['ram'])
    run:
        cmd = ('python2 {params.shortbred} '
               '--markers {params.ref} '
               '--wgs {input.reads1} {input.reads2} '
               '--results {output.table} '
               '--threads {threads} ')
        shell(cmd)
