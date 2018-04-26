#! /usr/bin/env python

import click


def floatorna(tkn):
    try:
        return float(tkn)
    except ValueError:
        if tkn == 'NA':
            return tkn
        raise


def handle_tokens(tkns):
    assert len(tkns) == 9
    taxon_name = tkns[8]
    depth = (len(taxon_name) - len(taxon_name.strip())) / 2
    return {
        'percent': float(tkns[0]),
        'reads': int(tkns[1]),
        'tax_reads': int(tkns[2]),
        'kmers': int(tkns[3]),
        'dup': float(tkns[4]),
        'coverage': floatorna(tkns[5]),
        'taxon_id': int(tkns[6]),
        'rank': '_'.join(tkns[7].split()),
        'taxon_name': taxon_name.strip(),
        'depth': depth,
        'children': [],
        'parent': None,
    }


def tokenize(read_assignments_file):
    with open(read_assignments_file) as raf:
        raf.readline()  # header
        for line in raf:
            tkns = line.strip().split('\t')
            parsed = handle_tokens(tkns)
            yield parsed


def build_tree(tokenizer, filter_func):
    ultimate_root = {'children': [], 'parent': None, 'depth': -1}
    tree_root = ultimate_root
    for parsed in tokenizer:
        if not filter_func(parsed):
            continue
        if parsed['depth'] <= tree_root['depth']:
            while parsed['depth'] <= tree_root['depth']:
                tree_root = tree_root['parent']

        tree_root['children'].append(parsed)
        parsed['parent'] = tree_root
        tree_root = parsed
    return ultimate_root


def make_filter(filter_ranks=True, min_kmer=4, min_cov=0.0001):

    def filter_func(parsed):
        """Return False if the parsed does not pass, otherwise True."""
        if min_kmer and (parsed['kmers'] < min_kmer):
            return False
        if min_cov and(parsed['coverage'] < min_cov):
            return False
        if filter_ranks and (parsed['rank'] in ['assembly', 'sequence', 'no_rank']):
            return False
        return True

    return filter_func


def get_short_rank(long_rank):
    if long_rank == 'superkingdom':
        return 'k'
    if long_rank == 'subspecies':
        return 't'
    short_rank = long_rank[0]
    assert short_rank in 'kpcofgst', long_rank
    return short_rank


def as_mpa_r(root, prefix, use_proportions):
    short_rank = get_short_rank(root['rank'])
    new_prefix = prefix + '|{}__{}'.format(short_rank, root['taxon_name'])
    if not prefix:
        new_prefix = '{}__{}'.format(short_rank, root['taxon_name'])
    val = root['reads']
    if use_proportions:
        val = root['percent'] / 100

    name_line = '{}\t{}'.format(new_prefix, val)
    names = [name_line]
    for child in root['children']:
        names += as_mpa_r(child, new_prefix, use_proportions)
    return names


def as_mpa(ultimate_root, use_proportions):
    names = []
    for root in ultimate_root['children']:
        names += as_mpa_r(root, '', use_proportions)
    return names


@click.command()
@click.option('-k', '--min-kmer', default=4)
@click.option('-c', '--min-cov', default=0.0001)
@click.option('-p/-r', '--proportions/--reads', default=False)
@click.argument('read_assignments_file')
def main(min_kmer, min_cov, proportions, read_assignments_file):
    tokenizer = tokenize(read_assignments_file)
    filter_func = make_filter(min_kmer=min_kmer, min_cov=min_cov)
    ultimate_root = build_tree(tokenizer, filter_func)
    names = as_mpa(ultimate_root, proportions)
    for name in names:
        print(name)


if __name__ == '__main__':
    main()
