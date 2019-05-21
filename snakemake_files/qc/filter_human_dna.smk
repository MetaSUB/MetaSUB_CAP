

def replaceDiff(c, s1, s2):
    out = ''
    for c1, c2 in zip(s1, s2):
        if c1 == c2:
            out += c1
        else:
            out += c
    return out


rule filter_human_dna:
    input:
        reads1 = config['adapter_removal']['clean_read1'],
        reads2 = config['adapter_removal']['clean_read2'],
    output:
        nonhuman_reads1 = config['filter_human_dna']['nonhuman_read1'],
        nonhuman_reads2 = config['filter_human_dna']['nonhuman_read2'],
        bam = config['filter_human_dna']['bam']
    params:
        bt2 = config['bt2']['exc']['filepath'],
        db = config['filter_human_dna']['db']['filepath']
    threads: int(config['filter_human_dna']['threads'])
    resources:
        time = int(config['filter_human_dna']['time']),
        n_gb_ram = int(config['filter_human_dna']['ram'])
    run:
        nonhumanPattern = replaceDiff('%', output.nonhuman_reads1, output.nonhuman_reads2)
        cmd = (' {params.bt2} '
           '-p {threads} '
           '--sensitive '
           ' --un-conc-gz ' + nonhumanPattern,
           ' -x {params.db} '
           ' -1 {input.reads1} '
           ' -2 {input.reads2} '
           '| samtools view -F 4 -b '
           '> {output.bam} ')
        cmd = ''.join(cmd)
        shell(cmd)
