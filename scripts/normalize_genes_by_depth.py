#! /usr/bin/env python3

import click
from json import loads as jloads
'''
Normalize the output of humann2 using Read Depth

Gene output from humann2 is already in reads per kilobase (RPK)

Produces output in reads per kilobase per millions of reads (RPKM)
'''


@click.command()
@click.argument('humann2_genes')
@click.argument('read_stats')
def main(humann2_genes, read_stats):
    readStats = jloads(open(read_stats).read())
    nreads = int(readStats['microbial']['num_reads'])
    nreads = nreads / (1000 * 1000)
    print('# Normalized RPKM\tNUM_READS={}M'.format(nreads))
    with open(humann2_genes) as hgs:
        for line in hgs:
            line = line.strip()
            if line[0] == '#':
                print(line)
                continue
            grp, val = line.split('\t')
            nval = float(val) / nreads
            print('{}\t{}'.format(grp, nval))


if __name__ == '__main__':
    main()
