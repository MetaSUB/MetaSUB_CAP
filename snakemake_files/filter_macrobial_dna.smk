


rule filter_macrobial_dna:
    input:
        reads1 = config['filter_human_dna']['nonhuman_read1'],
        reads2 = config['filter_human_dna']['nonhuman_read2']
    output:
        bam = config['filter_macrobial_dna']['bam']
    params:
        bt2 = config['bt2']['exc']['filepath'],
        db = config['filter_macrobial_dna']['db']['filepath']
    threads: int(config['filter_macrobial_dna']['threads'])
    resources:
        time = int(config['filter_macrobial_dna']['time']),
        n_gb_ram = int(config['filter_macrobial_dna']['ram'])
    run:
        cmd = (' {params.bt2} '
           '-p {threads} '
           '--very-fast '
           ' -x {params.db} '
           ' -1 {input.reads1} '
           ' -2 {input.reads2} '
           '| samtools view -F 4 -b '
           '> {output.bam} ')
        cmd = ''.join(cmd)
        shell(cmd)
