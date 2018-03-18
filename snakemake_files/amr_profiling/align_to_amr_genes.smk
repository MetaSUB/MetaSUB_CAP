
rule align_to_amr_genes:
    input:
        reads1 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read1'),
        reads2 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read2'),
    output:
        bam = config['align_to_amr_genes']['bam']
    params:
        bt2=config['bt2']['exc']['filepath'],
        samtools = config['samtools']['filepath'],
        db = config['align_to_amr_genes']['card_amrs']['bt2']
    threads: int(config['align_to_amr_genes']['threads'])
    resources:
        time=int(config['align_to_amr_genes']['time']),
        n_gb_ram=int(config['align_to_amr_genes']['ram'])
    run:
        cmd = (' {params.bt2} '
           '-p {threads} '
           '--very-sensitive '
           ' -x {params.db} '
           ' -1 {input.reads1} '
           ' -2 {input.reads2} '
           '| {params.samtools} view -F 4 -b '
           '> {output.bam} ')
        shell(cmd)
