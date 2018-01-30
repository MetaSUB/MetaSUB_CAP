


rule vfdb_make_blastm8:
    input:
        reads1 = config['filter_human_dna']['nonhuman_read1'],
        reads2 = config['filter_human_dna']['nonhuman_read2'],
        dmnd_db = config['vfdb_quantify']['dmnd_db']['filepath']
    output:
        m8 = config['vfdb_quantify']['m8']
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


rule vfdb_quantify:
    input:
        m8 = config['vfdb_quantify']['m8'],
        readstats = config['read_stats']['json'],
        ags = config['microbe_census']['stats'],
        fasta = config['vfdb_quantify']['fasta_db']['filepath']
    output:
        tbl = config['vfdb_quantify']['table']
    params:
        script = config['vfdb_quantify']['script'],
    run:
        cmd = ('{params.script} '
               '-s {input.readstats} '
               '-a {input.ags} '
               '-f {input.fasta} '
               '{input.m8} '
               '> {output.tbl} ') 
        shell(cmd)