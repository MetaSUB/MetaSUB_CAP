

rule align_to_macrobial_fragments:
    input:
        reads1 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read1'),
        reads2 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read2'),
    output:
        bam = config['quantify_macrobial']['bam']
    params:
        bt2 = config['bt2']['exc']['filepath'],
        db = config['quantify_macrobial']['db']['filepath']
    threads: int(config['quantify_macrobial']['threads'])
    resources:
        time = int(config['quantify_macrobial']['time']),
        n_gb_ram = int(config['quantify_macrobial']['ram'])
    run:
        cmd = (' {params.bt2} '
               '-p {threads} '
               '--very-fast '
               ' -x {params.db} '
               ' -1 {input.reads1} '
               ' -2 {input.reads2} '
               '| samtools view -F 4 -b '
               '> {output.bam} ')
        shell(cmd)
