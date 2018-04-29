
rule amr_make_blastm8:
    input:
        reads1 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read1'),
        reads2 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read2'),
        dmnd_db = config['align_to_amr_genes']['dmnd']['filepath']
    output:
        m8 = config['align_to_amr_genes']['m8']
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


rule amr_quantify:
    input:
        m8 = config['align_to_amr_genes']['m8'],
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
