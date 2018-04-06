

rule align_reads_to_megares:
    input:
        reads1 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read1'),
        reads2 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read2'),
    output:
        sam = config['resistome_amrs']['sam']
    threads: int( config['resistome_amrs']['threads'])
    params:
        bt2=config['bt2']['exc']['filepath'],
        db = config['resistome_amrs']['db']['bt2']
    resources:
        time=int(config['resistome_amrs']['bt2_time']),
        n_gb_ram=int(config['resistome_amrs']['bt2_ram'])
    run:
        cmd = (' {params.bt2} '
         '-p {threads} '
         '--very-sensitive '
         ' -x {params.db} '
         ' -1 {input.reads1} '
         ' -2 {input.reads2} '
         '| samtools view -F 4  '
         '> {output.sam} ')
        shell(cmd)


rule analyze_with_resistome:
    input:
        sam = config['resistome_amrs']['sam'],
        fasta = config['resistome_amrs']['db']['fasta'],
        annot = config['resistome_amrs']['db']['annotations']
    output:
        gene = config['resistome_amrs']['gene'],
        group = config['resistome_amrs']['group'],
        classus = config['resistome_amrs']['classus'],
        mech = config['resistome_amrs']['mech']        
    threads: 1
    params:
        thresh = config['resistome_amrs']['thresh'],
        resistome = config['resistome_amrs']['exc']['filepath'],        
    resources:
        time=1,
        n_gb_ram=5
    run:
       cmd = ('{params.resistome} '
              '-ref_fp {input.fasta} '
              '-sam_fp {input.sam} '
              '-annot_fp {input.annot} '
              '-gene_fp {output.gene} '
              '-group_fp {output.group} '
              '-class_fp {output.classus} '
              '-mech_fp {output.mech} '
              '-t {params.thresh}')
       shell(cmd)


rule quantify_resistome_gene:
    input:
        gene = config['resistome_amrs']['gene'],
        fasta = config['resistome_amrs']['db']['fasta'],
        annot = config['resistome_amrs']['db']['annotations']
        readstats = config['read_stats']['json'],
        ags = config['microbe_census']['stats'],
    output:
        norm_tbl = config['resistome_amrs']['gene_normalized']
    threads: 1
    params:
        script = config['resistome_amrs']['script']
    resources:
        time = 1,
        n_gb_ram = 5
    run: 
        cmd = (
            '{params.script} '
            '-s {input.readstats} '
            '-a {input.ags} '
            '-f {input.fasta} '
            '-c {input.annot} '
            'gene '
            '{input.gene} '
            '> {output.norm_tbl}'
        )
        shell(cmd)


rule quantify_resistome_group:
    input:
        group = config['resistome_amrs']['group'],
        fasta = config['resistome_amrs']['db']['fasta'],
        annot = config['resistome_amrs']['db']['annotations']
        readstats = config['read_stats']['json'],
        ags = config['microbe_census']['stats'],
    output:
        norm_tbl = config['resistome_amrs']['group_normalized']
    threads: 1
    params:
        script = config['resistome_amrs']['script']
    resources:
        time = 1,
        n_gb_ram = 5
    run: 
        cmd = (
            '{params.script} '
            '-s {input.readstats} '
            '-a {input.ags} '
            '-f {input.fasta} '
            '-c {input.annot} '
            'group '
            '{input.group} '
            '> {output.norm_tbl}'
        )
        shell(cmd)


rule quantify_resistome_classus:
    input:
        classus = config['resistome_amrs']['classus'],
        fasta = config['resistome_amrs']['db']['fasta'],
        annot = config['resistome_amrs']['db']['annotations']
        readstats = config['read_stats']['json'],
        ags = config['microbe_census']['stats'],
    output:
        norm_tbl = config['resistome_amrs']['classus_normalized']
    threads: 1
    params:
        script = config['resistome_amrs']['script']
    resources:
        time = 1,
        n_gb_ram = 5
    run: 
        cmd = (
            '{params.script} '
            '-s {input.readstats} '
            '-a {input.ags} '
            '-f {input.fasta} '
            '-c {input.annot} '
            'classus '
            '{input.classus} '
            '> {output.norm_tbl}'
        )
        shell(cmd)


rule quantify_resistome_mech:
    input:
        mech = config['resistome_amrs']['mech'],
        fasta = config['resistome_amrs']['db']['fasta'],
        annot = config['resistome_amrs']['db']['annotations']
        readstats = config['read_stats']['json'],
        ags = config['microbe_census']['stats'],
    output:
        norm_tbl = config['resistome_amrs']['mech_normalized']
    threads: 1
    params:
        script = config['resistome_amrs']['script']
    resources:
        time = 1,
        n_gb_ram = 5
    run: 
        cmd = (
            '{params.script} '
            '-s {input.readstats} '
            '-a {input.ags} '
            '-f {input.fasta} '
            '-c {input.annot} '
            'mech '
            '{input.mech} '
            '> {output.norm_tbl}'
        )
        shell(cmd)
