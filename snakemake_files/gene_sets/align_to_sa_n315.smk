
rule align_to_sa_n315:
    input:
        reads1 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read1'),
        reads2 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read2'),
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
                ' -x {params.db} '
                ' -1 {input.reads1} '
                ' -2 {input.reads2} '
                '| samtools view -F 4 -b '
                '> {output.bam} ')
        shell(cmd)


rule align_to_sa_n315_single:
    input:
        reads1 = getOriginResultFiles(config, 'filter_human_dna_single', 'nonhuman_reads'),
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
                ' -x {params.db} '
                ' -U {input.reads1} '
                '| samtools view -F 4 -b '
                '> {output.bam} ')
        shell(cmd)
