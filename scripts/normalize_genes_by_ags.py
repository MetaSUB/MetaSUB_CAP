#! /usr/bin/env python3

import click

'''
Normalize the output of humann2 using
Average Genome Size from microbe census

Gene output from humann2 is already in reads per kilobase (RPK)

In a previous step we normalize by sample depth to get 
reads per kilobase millions of reads (RPKM)

Produces output in reads per kilobase per genome (RPKMG)

The source paper for microbe census describes this normalization
in detail
'''


def mcParse(mcFile):
    with open(mcFile) as mcf:
        for line in mcf:
            if 'average_genome_size' in line:
                return float(line.strip().split()[1])
    return -1


@click.command()
@click.argument('humann2_genes')
@click.argument('microbe_census')
def main(humann2_genes, microbe_census):
    ags = mcParse(microbe_census) / (1000 * 1000)
    print('# Normalized RPKMG\tAGS={}M'.format(ags))
    with open(humann2_genes) as hgs:
        for line in hgs:
            line = line.strip()
            if line[0] == '#':
                print(line)
                continue
            grp, val = line.split('\t')
            nval = float(val) / ags
            print('{}\t{}'.format(grp, nval))


if __name__ == '__main__':
    main()
