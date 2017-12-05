'''
This is an example of a 'group result' it is a many-to-one result that
produces some sort of synthesis from other results in the group

For a more basic example of a one-to-one result see 
kraken_taxonomy_profiling.snkmk
'''


rule mash_sketch:
    input:
        # The expandGroup function is imported from moduleUltra (automatically)
        # It gets every file matching the pattern from the group being processed
        allReads1 = expandGroup( config['filter_microbial_dna']['microbial_reads1'])
    output:
        sketch = config['mash_intersample_distances']['sketch'],
    threads: 1
    params:
        exc=config['mash']['exc']['filepath'],
        job_name=config['JOB_NAME_PREFIX'] + 'mash_sketch_{group_name}',
    resources:
        time = 1,
        n_gb_ram = 10
    run:
        allReads = ' '.join(input.allReads1)
        cmd = '{params.exc} sketch -s 10000000 -o {output.sketch} '+allReads
        shell(cmd)


rule mash_dists:
    input:
        sketch= config['mash_intersample_dists']['sketch']
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