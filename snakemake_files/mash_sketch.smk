

rule mash_sketch:
    input:
        # The expandGroup function is imported from moduleUltra (automatically)
        # It gets every file matching the pattern from the group being processed
        allReads1 = config['filter_macrobial_dna']['microbial_read1']
    output:
        sketch = config['mash_sketch']['sketch'],
    threads: 1
    params:
        exc=config['mash']['exc']['filepath'],
    resources:
        time = 1,
        n_gb_ram = 10
    run:
        allReads = ' '.join(input.allReads1)
        cmd = '{params.exc} sketch -s 10000000 -o {output.sketch} '+allReads
        shell(cmd)

