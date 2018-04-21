#! /usr/bin/env python3

import pysam
import click
from json import loads, dumps
from sys import stdout


def millions_of_reads(read_stats_file):
    readStats = loads(open(read_stats_file).read())
    nreads = int(readStats['num_reads'])
    nreads = nreads / (1000 * 1000)
    return nreads


def reads_per_chrm(bamf):
    samfile = pysam.AlignmentFile(bamf, "rb")
    read_weights = {}
    raw_chrm_tbl = {}
    for rec in samfile:
        try:
            read_weights[rec.query_name] += 1
        except KeyError:
            read_weights[rec.query_name] = 1
        try:
            raw_chrm_tbl[rec.reference_name].append(rec.query_name)
        except KeyError:
            raw_chrm_tbl[rec.reference_name] = [rec.query_name]
    samfile.close()
    chrm_tbl = {}
    for chrm, reads in raw_chrm_tbl.items():
        weight = 0
        for read in reads:
            weight += 1 / read_weights[read]
        chrm_tbl[chrm] = weight
    return chrm_tbl
    
            
    

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
    biases = loads(open(biases).read())
    read_tbl = reads_per_chrm(bam)
    tbl = {}
    for gname, bias in biases.items():
        reads = agg_reads(bias['chrs'], read_tbl)
        rpk = reads / (bias['effective_length'] / 1000)
        rpkm = rpk / millions_of_reads(read_stats)
        common_name = bias['common_name']
        tbl[common_name] = {'total_reads': reads, 'rpkm': rpkm}
    stdout.write(dumps(tbl))


if __name__ == '__main__':
    main()
