

rule finch_sketch:
    input:
        reads1 = config['filter_human_dna']['nonhuman_read1']
    output:
        sketch = config['mash_sketch']['sketch'],
    threads: 1
    params:
        exc=config['finch']['exc']['filepath'],
    resources:
        time = 1,
        n_gb_ram = 10
    run:
        cmd = '{params.exc} sketch --no-strict --seed 42 --n-hashes 10000000 --binary-format -o {output.sketch} {input.reads1}'
        shell(cmd)

