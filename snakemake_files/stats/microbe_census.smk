
# MicrobeCensus
rule microbe_census:
    input:
        reads1 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read1'),
        reads2 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read2'),
    output:
        main = config['microbe_census']['stats']
    threads: int( config['microbe_census']['threads'])
    version: config['microbe_census']['exc']['version']
    params:
        mic_census = config['microbe_census']['exc']['filepath'],
    resources:
        time=int(config['microbe_census']['time']),
        n_gb_ram=int(config['microbe_census']['ram'])
    run:
        cmd = ('{params.mic_census} '
                   '-t {threads} '
                   '{input.reads1},{input.reads2} '
                   '{output.main}')
        shell(cmd)


rule microbe_census_single:
    input:
        reads1 = getOriginResultFiles(config, 'filter_human_dna_single', 'nonhuman_reads'),
    output:
        main = config['microbe_census']['stats']
    threads: int(config['microbe_census']['threads'])
    version: config['microbe_census']['exc']['version']
    params:
        mic_census = config['microbe_census']['exc']['filepath'],
    resources:
        time=int(config['microbe_census']['time']),
        n_gb_ram=int(config['microbe_census']['ram'])
    run:
        cmd = ('{params.mic_census} '
                   '-t {threads} '
                   '{input.reads1} '
                   '{output.main}')
        shell(cmd)
