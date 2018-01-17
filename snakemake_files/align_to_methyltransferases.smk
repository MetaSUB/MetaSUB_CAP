
rule align_to_methyls:
    input:
        reads1 = config['filter_macrobial_dna']['microbial_read1'],
        reads2 = config['filter_macrobial_dna']['microbial_read2'],
    output:
        m8 = config['align_to_methyltransferases']['m8']
    params:
        diamond=config['diamond']['exc']['filepath'],
        db = config['align_to_methyltransferases']['db']['diamond']
    threads: int(config['align_to_methyltransferases']['threads'])
    resources:
        time=int(config['align_to_methyltransferases']['time']),
        n_gb_ram=int(config['align_to_methyltransferases']['ram'])
    run:
        cmd = (' {params.bt2} '
           '-p {threads} '
           '--very-sensitive '
           ' -x {params.db} '
           ' -1 {input.reads1} '
           ' -2 {input.reads2} '
           '| samtools view -F 4 -b '
           '> {output.bam} ')
        shell(cmd)
