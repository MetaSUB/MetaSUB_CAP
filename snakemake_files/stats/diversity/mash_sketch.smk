

rule mash_sketch:
    input:
        reads1 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read1')
    output:
        sketch = config['mash_sketch']['sketch'],
    threads: 1
    params:
        exc=config['mash']['exc']['filepath'],
    resources:
        time = 1,
        n_gb_ram = 10
    run:
        cmd = '{params.exc} sketch -s 10000000 -o {output.sketch} {input.reads1}'
        shell(cmd)

