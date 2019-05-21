
rule unzip_amr_blastm8:
    input:
        gzm8 = config['align_to_amr_genes']['m8']
    output:
        m8 = temp(config['align_to_amr_genes']['m8'][:-3])
    run:
        cmd = 'zcat {input.gzm8} > {output.m8}'
        shell(cmd)

rule amr_make_blastm8:
    input:
        reads1 = config['filter_human_dna']['nonhuman_read1'],
        reads2 = config['filter_human_dna']['nonhuman_read2'],
        dmnd_db = config['align_to_amr_genes']['dmnd']['filepath']
    output:
        m8 = temp(config['align_to_amr_genes']['m8'][:-3])
    threads: int(config['align_to_amr_genes']['dmnd']['threads'])
    params:
        dmnd = config['diamond']['exc']['filepath'],
        bsize = int(config['align_to_amr_genes']['dmnd']['block_size']),
    resources:
        time = int(config['align_to_amr_genes']['dmnd']['time']),
        n_gb_ram = int(config['align_to_amr_genes']['dmnd']['ram'])
    run:
        cmd = ('{params.dmnd} blastx '
               '--sensitive '
               '--threads {threads} '
               '-d {input.dmnd_db} '
               '-q {input.reads1} '
               '--block-size {params.bsize} '
               '> {output.m8} ')
        shell(cmd)


ruleorder: unzip_amr_blastm8 > amr_make_blastm8

rule amr_quantify:
    input:
        m8 = config['align_to_amr_genes']['m8'][:-3],
        readstats = config['read_stats']['json'],
        ags = config['microbe_census']['stats'],
        fasta = config['align_to_amr_genes']['fasta_db']['filepath']
    output:
        tbl = config['align_to_amr_genes']['table']
    params:
        script = config['align_to_amr_genes']['script'],
    resources:
        time = int(config['align_to_amr_genes']['time'])
    run:
        cmd = ('{params.script} '
               '-s {input.readstats} '
               '-a {input.ags} '
               '-f {input.fasta} '
               '{input.m8} '
               '> {output.tbl} ')
        shell(cmd)


rule gzip_m8_amr:
    input:
        m8 = config['align_to_amr_genes']['m8'][:-3]
    output:
        gzm8 = config['align_to_amr_genes']['m8']
    run:
        cmd = 'gzip {input.m8}'
        shell(cmd)
