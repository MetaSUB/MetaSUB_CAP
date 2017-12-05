
rule align_to_methyls:
    input:
        reads1 = config['filter_macrobial_dna']['microbial_read1']
        reads2 = config['filter_macrobial_dna']['microbial_read2']
        db = config['databases']['methyltransferases']['bt2']
    output:
        bam = config['align_to_methyltransferases']['bam']
    params:
        bt2=config['bt2']['exc']['filepath'],
    threads: int(config['align_to_methyltransferases']['threads'])
    resources:
        time=int(config['align_to_methyltransferases']['time']),
        n_gb_ram=int(config['align_to_methyltransferases']['ram'])
    run:
        cmd = (' {params.bt2} '
           '-p {threads} '
           '--very-sensitive '
           ' -x {input.db} '
           ' -1 {input.reads1} '
           ' -2 {input.reads2} '
           '| samtools view -F 4 -b '
           '> {output.bam} ')
        shell(cmd)
