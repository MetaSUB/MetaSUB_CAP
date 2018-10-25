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
    try:
        nreads = int(readStats['raw']['num_reads'])
    except KeyError:
        nreads = int(readStats['num_reads'])
    nreads = nreads
    return nreads


def reads_in_macrobe(macrobe_file):
    macrobes = json.loads(open(macrobe_file).read())
    tot_reads = 0
    for val in macrobes.values():
        tot_reads += int(val['total_reads'])
    return tot_reads


def countMPA(fname):
    nBact, nArch, nViral, nEuk, nFung = 0, 0, 0, 0, 0
    with open(fname) as mf:
        for line in mf:
            line = line.strip().lower()
            if '|' in line:
                continue
            if 'd__bacteria' in line:
                nBact = int(line.split()[-1])
            if 'd__archaea' in line:
                nArch = int(line.split()[-1])
            if 'd__viruses' in line:
                nViral = int(line.split()[-1])
            if 'd__eukaryota' in line:
                nEuk = int(line.split()[-1])
            if 'k__fung' in line:
                nFung = int(line.split()[-1])
    return nBact, nArch, nViral, nEuk, nFung


def formatOut(humanReads,
              macrobeReads,
              unknownReads,
              bactReads,
              archReads,
              viralReads,
              eukReads,
              fungReads,
              totalReads):
    totals = {
        'total': totalReads,
        'host': humanReads,
        'unknown': unknownReads,
        'nonhost_macrobial': macrobeReads,
        'bacterial': bactReads,
        'archaeal': archReads,
        'viral': viralReads,
        'nonfungal_eukaryotic': eukReads,
        'fungal': fungReads
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
    totalReads = countFastq(all_fastq)
    nNonHum = reads_in_json(read_stats)

    nHum = totalReads - nNonHum
    nMacrobe = reads_in_macrobe(macrobes)

    nBact, nArch, nViral, nEuk, nFung = countMPA(microbe_mpa)
    nMicrobial = nBact + nArch + nViral + nEuk

    unknownReads = nNonHum - nMacrobe - nMicrobial

    out = formatOut(nHum,
                    nMacrobe,
                    unknownReads,
                    nBact,
                    nArch,
                    nViral,
                    nEuk - nFung,
                    nFung,
                    totalReads)
    assert unknownReads >= 0, out
    sys.stdout.write(json.dumps(out))

    
    
if __name__ == '__main__':
    main()
