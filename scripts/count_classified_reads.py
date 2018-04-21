#!/usr/bin/env python3

import sys
import subprocess as sp
import json
import click

'''
A simple script which counts how many reads are human contamination,
of unknown origin or belong to one of the domains bacteria, archaea,
or virus.
'''


def countFastq(fname):
    raw = sp.getoutput('zcat {} | wc -l'.format(fname)).split()[0]
    return int(raw) / 4


def reads_in_json(read_stats_file):
    readStats = json.loads(open(read_stats_file).read())
    nreads = int(readStats['num_reads'])
    nreads = nreads / (1000 * 1000)
    return nreads


def reads_in_macrobe(macrobe_file):
    macrobes = json.loads(open(macrobe_file).read())
    tot_reads = 0
    for val in macrobes.values():
        tot_reads += int(val['total_reads'])
    return tot_reads


def countMPA(fname):
    nBact, nArch, nViral = 0, 0, 0
    with open(fname) as mf:
        # only look through first 10 lines
        for arb in range(10):
            line = mf.readline().strip().lower()
            if '|' in line:
                continue
            if 'd__bacteria' in line:
                nBact = int(line.split()[-1])
            if 'd__archaea' in line:
                nArch = int(line.split()[-1])
            if 'd__viruses' in line:
                nViral = int(line.split()[-1])
    return nBact, nArch, nViral


def formatOut(humanReads,
              macrobeReads,
              unknownReads,
              bactReads,
              archReads,
              viralReads,
              totalReads):
    totals = {
        'total': totalReads,
        'host': humanReads,
        'unknown': unknownReads,
        'nonhost_macrobial': macrobeReads,
        'bacterial': bactReads,
        'archaeal': archReads,
        'viral': viralReads
    }
    out = {}
    out['totals'] = totals
    out['proportions'] = {k: v / totalReads for k, v in totals.items()}
    return out


@click.command()
@click.argument('all_fastq')
@click.argument('read_stats')
@click.argument('macrobes')
@click.argument('microbe_mpa')
def main(all_fastq, read_stats, macrobes, microbe_mpa):
    nAll = countFastq(all_fastq)
    nNonHum = reads_in_json(read_stats)
    nHum = nAll - nNonHum
    nMacrobe = reads_in_macrobe(macrobes)
    nBact, nArch, nViral = countMPA(microbe_mpa)
    nMicrobial = nBact + nArch + nViral

    totalReads = nHum + nNonHum
    unknownReads = nNonHum - nMacrobe - nMicrobial

    assert unknownReads >= 0

    out = formatOut(nHum,
                    nMacrobe,
                    unknownReads,
                    nBact,
                    nArch,
                    nViral,
                    totalReads)
    sys.stdout.write(json.dumps(out))


if __name__ == '__main__':
    main()
