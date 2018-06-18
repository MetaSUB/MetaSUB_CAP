

rule unzip_methyl_blastm8:
    input:
        gzm8 = config['align_to_methyltransferases']['m8']
    output:
        m8 = temp(config['align_to_methyltransferases']['m8'][:-3])
    run:
        cmd = 'zcat {input.gzm8} > {output.m8}'
        shell(cmd)

rule methyl_make_blastm8:
    input:
        reads1 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read1'),
        reads2 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read2'),
        dmnd_db = config['align_to_methyltransferases']['dmnd']['filepath']
    output:
        m8 = temp(config['align_to_methyltransferases']['m8'][:-3])
    threads: int(config['align_to_methyltransferases']['dmnd']['threads'])
    params:
        dmnd = config['diamond']['exc']['filepath'],
        bsize=int(config['align_to_methyltransferases']['dmnd']['block_size']),
    resources:
        time=int(config['align_to_methyltransferases']['dmnd']['time']),
        n_gb_ram=int(config['align_to_methyltransferases']['dmnd']['ram'])
    run:
        cmd = ('{params.dmnd} blastx '
               '--threads {threads} '
               '-d {input.dmnd_db} '
               '-q {input.reads1} '
               '--block-size {params.bsize} '
               '> {output.m8} ') 
        shell(cmd)


rule methyl_make_blastm8_single:
    input:
        reads1 = getOriginResultFiles(config, 'filter_human_dna_single', 'nonhuman_reads'),
        dmnd_db = config['align_to_methyltransferases']['dmnd']['filepath']
    output:
        m8 = temp(config['align_to_methyltransferases']['m8'][:-3])
    threads: int(config['align_to_methyltransferases']['dmnd']['threads'])
    params:
        dmnd = config['diamond']['exc']['filepath'],
        bsize=int(config['align_to_methyltransferases']['dmnd']['block_size']),
    resources:
        time=int(config['align_to_methyltransferases']['dmnd']['time']),
        n_gb_ram=int(config['align_to_methyltransferases']['dmnd']['ram'])
    run:
        cmd = ('{params.dmnd} blastx '
               '--threads {threads} '
               '-d {input.dmnd_db} '
               '-q {input.reads1} '
               '--block-size {params.bsize} '
               '> {output.m8} ') 
        shell(cmd)


ruleorder: unzip_methyl_blastm8 > methyl_make_blastm8

ruleorder: unzip_methyl_blastm8 > methyl_make_blastm8_single

rule methyl_quantify:
    input:
        m8 = config['align_to_methyltransferases']['m8'][:-3],
        readstats = config['read_stats']['json'],
        ags = config['microbe_census']['stats'],
        fasta = config['align_to_methyltransferases']['fasta_db']['filepath']
    output:
        tbl = config['align_to_methyltransferases']['table']
    params:
        script = config['align_to_methyltransferases']['script'],
    run:
        cmd = ('{params.script} '
               '-s {input.readstats} '
               '-a {input.ags} '
               '-f {input.fasta} '
               '{input.m8} '
               '> {output.tbl} ') 
        shell(cmd)


rule gzip_m8_methyls:
    input:
        m8 = config['align_to_methyltransferases']['m8'][:-3]
    output:
        gzm8 = config['align_to_methyltransferases']['m8']
    run:
        cmd = 'cat {input.m8} | gzip > {output.gzm8}'
        shell(cmd)