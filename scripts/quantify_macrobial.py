#! /usr/bin/env python3

import click
from json import loads, dumps
from sys import stdout


def millions_of_reads(read_stats_file):
    readStats = loads(open(read_stats_file).read())
    nreads = int(readStats['num_reads'])
    nreads = nreads / (1000 * 1000)
    return nreads


def reads_per_chrm(bamf):
    pass


def agg_reads(chrs, read_tbl):
    tot_reads = 0
    for chrm in chrs:
        try:
            tot_reads += read_tbl[chrm]
        except KeyError:
            pass
    return tot_reads


@click.command()
@click.option('-s', '--read-stats')
@click.argument('biases')
@click.argument('bam')
def main(read_stats, biases, bam):
    biases = loads(biases)
    read_tbl = reads_per_chrm(bam)
    tbl = {}
    for gname, bias in biases:
        reads = agg_reads(bias['chrs'], read_tbl)
        rpk = reads / (bias['effective_length'] / 1000)
        rpkm = rpk / millions_of_reads(read_stats)
        common_name = bias['common_name']
        tbl[common_name] = rpkm
    stdout.write(dumps(tbl))


if __name__ == '__main__':
    main()
