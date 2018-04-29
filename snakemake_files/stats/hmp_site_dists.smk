

rule measure_hmp_dists_metaphlan2:
	input:
		mpa= config['metaphlan2_taxonomy_profiling']['mpa'],
	output:
		main=config['hmp_site_dists']['metaphlan2']
	resources:
		time=2,
		n_gb_ram=4
	threads: 1
	params:
		script=config['pipeline_dir'] + '/scripts/hmp_sites_metaphlan_dists.py',
        db=config['pipeline_dir'] + '/scripts/hmp_sites_metaphlan2'
	shell:
		'{params.script} {params.db} {input.mpa} > {output.main}'

'''
rule measure_hmp_dists_kraken:
	input:
		mpa= config['kraken_taxonomy_profiling']['mpa'],
                db=config['pipeline_dir'] + '/references/hmp_site_dists/kraken.csv'
	output:
		main=config['hmp_site_dists']['kraken']
	resources:
		time=1,
		n_gb_ram=2
	threads: 1
	params:
		script=config['pipeline_dir'] + '/scripts/hmp_site_dists/find_mpa_dists.py',
	shell:
		'{params.script} {input.db} {input.mpa} > {output.main}'
                


rule measure_hmp_dists_mash:
	input:
            sketch = config['mash_sketch']['sketch'],
            db=config['pipeline_dir'] + '/references/hmp_site_dists/hmp_sites.msh'
	output:
	    main=config['hmp_site_dists']['mash']
	resources:
		time=1,
		n_gb_ram=2
	threads: 1
	params:
		script=config['pipeline_dir'] + '/scripts/hmp_site_dists/find_mash_dists.py',
	shell:
		'{params.script} {input.db} {input.mpa} > {output.main}'
'''
