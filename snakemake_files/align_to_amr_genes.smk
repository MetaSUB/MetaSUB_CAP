
rule align_to_amr_genes:
    input:
        reads1 = config['filter_macrobial_dna']['microbial_read1'],
        reads2 = config['filter_macrobial_dna']['microbial_read2'],
        db = config['align_to_amr_genes']['card_amrs']['bt2']
    output:
        bam = config['align_to_amr_genes']['bam']
    params:
        bt2=config['bt2']['exc']['filepath'],
    threads: int(config['align_to_amr_genes']['threads'])
    resources:
        time=int(config['align_to_amr_genes']['time']),
        n_gb_ram=int(config['align_to_amr_genes']['ram'])
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
