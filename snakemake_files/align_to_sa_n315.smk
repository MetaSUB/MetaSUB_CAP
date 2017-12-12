
rule align_to_sa_n315:
    input:
        reads1 = config['filter_macrobial_dna']['microbial_read1'],
        reads2 = config['filter_macrobial_dna']['microbial_read2']
    output:
        bam = config['align_to_sa_n315']['bam']
    params:
        bt2=config['bt2']['exc']['filepath'],
        db = config['align_to_sa_n315']['db']['bt2']
    threads: int(config['align_to_sa_n315']['threads'])
    resources:
        time=int(config['align_to_sa_n315']['time']),
        n_gb_ram=int(config['align_to_sa_n315']['ram'])
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

