

rule unzip_vfdb_blastm8:
    input:
        gzm8 = config['vfdb_quantify']['m8']
    output:
        m8 = temp(config['vfdb_quantify']['m8'][:-3])
    run:
        cmd = 'zcat {input.gzm8} > {output.m8}'
        shell(cmd)


rule vfdb_make_blastm8:
    input:
        reads1 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read1'),
        reads2 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read2'),
        dmnd_db = config['vfdb_quantify']['dmnd']['filepath']
    output:
        m8 = temp(config['vfdb_quantify']['m8'][:-3])
    threads: int(config['vfdb_quantify']['dmnd']['threads'])
    params:
        dmnd = config['diamond']['exc']['filepath'],
        bsize=int(config['vfdb_quantify']['dmnd']['block_size']),
    resources:
        time=int(config['vfdb_quantify']['dmnd']['time']),
        n_gb_ram=int(config['vfdb_quantify']['dmnd']['ram'])
    run:
        cmd = ('{params.dmnd} blastx '
               '--threads {threads} '
               '-d {input.dmnd_db} '
               '-q {input.reads1} '
               '--block-size {params.bsize} '
               '> {output.m8} ') 
        shell(cmd)


rule vfdb_make_blastm8_single:
    input:
        reads1 = getOriginResultFiles(config, 'filter_human_dna_single', 'nonhuman_reads'),
        dmnd_db = config['vfdb_quantify']['dmnd']['filepath']
    output:
        m8 = temp(config['vfdb_quantify']['m8'][:-3])
    threads: int(config['vfdb_quantify']['dmnd']['threads'])
    params:
        dmnd = config['diamond']['exc']['filepath'],
        bsize=int(config['vfdb_quantify']['dmnd']['block_size']),
    resources:
        time=int(config['vfdb_quantify']['dmnd']['time']),
        n_gb_ram=int(config['vfdb_quantify']['dmnd']['ram'])
    run:
        cmd = ('{params.dmnd} blastx '
               '--threads {threads} '
               '-d {input.dmnd_db} '
               '-q {input.reads1} '
               '--block-size {params.bsize} '
               '> {output.m8} ') 
        shell(cmd)


ruleorder: unzip_vfdb_blastm8 > vfdb_make_blastm8

rule vfdb_quantify:
    input:
        m8 = config['vfdb_quantify']['m8'][:-3],
        readstats = config['read_stats']['json'],
        ags = config['microbe_census']['stats'],
        fasta = config['vfdb_quantify']['fasta_db']['filepath']
    output:
        tbl = config['vfdb_quantify']['table']
    params:
        script = config['vfdb_quantify']['script'],
    resources:
        time = int(config['vfdb_quantify']['time'])
    run:
        cmd = ('{params.script} '
               '-s {input.readstats} '
               '-a {input.ags} '
               '-f {input.fasta} '
               '{input.m8} '
               '> {output.tbl} ') 
        shell(cmd)


rule gzip_m8_vfdb:
    input:
        m8 = config['vfdb_quantify']['m8'][:-3]
    output:
        gzm8 = config['vfdb_quantify']['m8']
    run:
        cmd = 'gzip {input.m8}'
        shell(cmd)
