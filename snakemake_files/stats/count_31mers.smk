from random import choices as rchoices


rule count_31mers:
    input:
        reads1 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read1'),
        reads2 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read2'),
    output:
        jf = config['count_31mers']['jf']
    params:
        jf=config['count_31mers']['exc']['filepath']
    threads: int(config['count_31mers']['threads'])
    resources:
        time=int(config['count_31mers']['time']),
        n_gb_ram=int(config['count_31mers']['ram'])
    run:
    
        bloom_counter = ''.join(rchoices(string.ascii_uppercase + string.digits, k=10)) + '.temp.bc'
        # First Pass: Count 31mers
        cmd = (
            'zcat {input.reads1} {input.reads2} '
            '| {params.jf} bc -m 31 -C -s 100G -t {threads} '
            '  -o ./' + bloom_counter + ' /dev/fd/0'
        )
        shell(cmd)

        # Second Pass: Remove Singletons
        cmd = (
            'zcat {input.reads1} {input.reads2} '
            '| {params.jf} count -m 31 -C -s 100G -t {threads} '
            '  --bc ./temp.bc -o {output.jf} /dev/fd/0'
        )
        shell(cmd)

        # Remove Temporary Bloom Counter
        shell('rm ' + bloom_counter)
