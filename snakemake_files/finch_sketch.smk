

rule finch_sketch:
    input:
        reads1 = config['filter_human_dna']['nonhuman_read1']
    output:
        sketch = config['mash_sketch']['sketch'],
    threads: 1
    params:
        exc=config['finch']['exc']['filepath'],
        seed=config['finch']['hash_seed'],
        n_hashes=config['finch']['n_hashes'],
    resources:
        time = 1,
        n_gb_ram = 10
    run:
        cmd = '{params.exc} sketch --no-strict --seed {params.seed} --n-hashes {params.n_hashes} --binary-format -o {output.sketch} {input.reads1}'
        shell(cmd)

