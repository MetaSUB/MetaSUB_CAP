

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
               '--fast '
               ' -x {params.db} '
               ' -1 {input.reads1} '
               ' -2 {input.reads2} '
               '| samtools view -F 4 -b '
               '> {output.bam} ')
        shell(cmd)

rule align_to_macrobial_fragments_single:
    input:
        reads1 = getOriginResultFiles(config, 'filter_human_dna_single', 'nonhuman_reads'),
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
               '--fast '
               ' -x {params.db} '
               ' -U {input.reads1} '
               '| samtools view -F 4 -b '
               '> {output.bam} ')
        shell(cmd)

rule quantify_macrobial:
    input:
        bam = config['quantify_macrobial']['bam'],
        readstats = config['read_stats']['json'],
        biases = config['quantify_macrobial']['biases'],
    output:
        tbl = config['quantify_macrobial']['tbl'],
    params:
        script = config['quantify_macrobial']['script']
    run:
        cmd = (
            '{params.script} '
            '-s {input.readstats} '
            '{input.biases} '
            '{input.bam} '
            '> {output.tbl} '
        )
        shell(cmd)

