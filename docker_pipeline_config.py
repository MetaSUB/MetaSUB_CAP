
from os.path import join


def in_db_dir(filename):
    return join('/home/metasub', filename)


config = {
    'align_to_sa_n315': {
        'db': {
            'bt2': in_db_dir('microbes', 'staph_aureus_n315.bt2'),
        }
    },
    'filter_human_dna': {
        'db': {
            'filepath': in_db_dir('hg38', 'hg38.bt2'),
        },
    },
    'krakenhll_taxonomy_profiling': {
        'db': {
            'filepath': in_db_dir('krakenhll_refseq', 'krakenhll_refseq_complete')
        },
    },
    'humann2_functional_profiling': {
        'db': {
            'filepath': in_db_dir('genes', 'uniref90_annotated.1.1.dmnd')
        },
    },
    'resistome_amrs': {
        'db': {
            'bt2': in_db_dir('megares', 'megares_database_v1.01.bt2'),
            'fasta': in_db_dir('megares', 'megares_database_v1.01.fasta'),
            'annotations': in_db_dir('megares', 'megares_to_external_header_mappings_v1.01.tsv')
        },
    },
    'align_to_amr_genes': {
        'fasta_db': {'filepath': in_db_dir('card', 'card_oct_2017_prot_seqs.faa')},
        'dmnd': {
            'filepath': in_db_dir('card', 'card_oct_2017_prot_seqs.dmnd'),
        }
    },

    'quantify_macrobial': {
        'biases': in_db_dir('macrobes', 'quantified_bias.json'),
        'db': {'filepath': in_db_dir('macrobes', 'blast_tabulars')},
    },
}
