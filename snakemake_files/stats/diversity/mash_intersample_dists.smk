'''
This is an example of a 'group result' it is a many-to-one result that
produces some sort of synthesis from other results in the group

For a more basic example of a one-to-one result see 
kraken_taxonomy_profiling.snkmk
'''

rule mash_dists:
    input:
        sketch = expandGroup(config['finch_sketch']['sketch'])
    output:
        distTable=config['mash_intersample_dists']['distance_table']
    resources:
        time=1,
        n_gb_ram=10
    threads: 1
    params:
        exc=config['mash']['exc']['filepath'],
    shell:
        '{params.exc} dist {input.sketch} {input.sketch} > {output.distTable}'
