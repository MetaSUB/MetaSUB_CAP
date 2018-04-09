#! /usr/bin/env python3

import click
from json import loads as jloads
import pandas as pd
from sys import stdout

million = 1000 * 1000


def getAGS(agsf):
    """Return the ave genome sixe in millions of bases."""
    with open(agsf) as mcf:
        for line in mcf:
            if 'average_genome_size' in line:
                return float(line.strip().split()[1]) / million
    return -1


def getNReads(readStatsF):
    """Return the number of reads in millions."""
    readStats = jloads(open(readStatsF).read())
    nreads = int(readStats['microbial']['num_reads'])
    nreads = nreads / million
    return nreads


def getSeqLens(fastaf):
    """Return a table with length in kilobases for each seq in fastaf."""
    lenout = {}
    curRec, curLen = None, None, 0
    with open(fastaf) as ff:
        for line in ff:
            line = line.strip()
            if len(line) == 0:
                continue
            if line[0] == '>':
                if curRec is not None:
                    lenout[curRec] = curLen / 1000
                curRec = line.split()[0][1:]
                curLen = 0
            else:
                curLen += len(line)
    lenout[curRec] = curLen / 1000
    return lenout


def getReadsPerCategory(resistome_table):
    out = {}
    with open(resistome_table) as rt:
        rt.readline()
        for line in rt:
            tkns = line.strip().split()
            cat_val, nreads = tkns[1], int(tkns[2])
            out[cat_val] = nreads
    return out


def getCategoryLengths(category_table, category, seq_lengths):
    """Return a table mapping categories to the total bps in that category.

    base pairs are in the same units as getSeqLens.
    """
    if category == 'gene':
        return seq_lengths
    ind = {'classus': 1, 'mech': 2, 'group': 3}[category]
    cat_length_table = {}
    with open(category_table) as ct:
        for line in ct:
            tkns = line.strip().split(',')
            gene, cat_val = tkns[0], tkns[ind]
            gene_len = seq_lengths[gene]
            try:
                cat_length_table[cat_val] += gene_len
            except KeyError:
                cat_length_table[cat_val] = gene_len
    return cat_length_table


def makeTable(reads_per_category, category_lengths, num_reads, ags):
    """Return a pandas dataframe giving reads, RPK, RPKM, and RPKMG."""
    out = {}
    for cat_val, reads_in_cat in reads_per_category.items():
        K, M, G = category_lengths[cat_val], num_reads, ags
        out[cat_val] = {
            'reads': reads_in_cat,
            'RPK': reads_in_cat / K,
            'RPKM': reads_in_cat / (K * M),
            'RPKMG': reads_in_cat / (K * M * G),
        }
    out = pd.DataFrame(out).transpose()
    return out


@click.command()
@click.option('-s', '--read-stats')
@click.option('-a', '--ags')
@click.option('-f', '--fasta')
@click.option('-c', '--category-table')
@click.argument('category')
@click.argument('resistome_table')
def main(read_stats, ags, fasta, category_table,
         category, resistome_table):
    reads_per_category = getReadsPerCategory(resistome_table)
    num_reads = getNReads(read_stats)
    ags = getAGS(ags)
    seq_lengths = getSeqLens(fasta)
    category_lengths = getCategoryLengths(category_table,
                                          category,
                                          seq_lengths)

    tbl = makeTable(reads_per_category,
                    category_lengths,
                    num_reads,
                    ags)
    stdout.write(tbl.to_csv())


if __name__ == '__main__':
    main()
