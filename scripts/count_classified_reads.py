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
@click.argument('human_fastq')
@click.argument('nonhuman_fastq')
@click.argument('nonmacrobe_fastq')
@click.argument('microbe_mpa')
def main(human_fastq, nonhuman_fastq, nonmacrobe_fastq, microbe_mpa):
    nHum = countFastq(human_fastq)
    nNonHum = countFastq(nonhuman_fastq)
    nNonMacrobe = countFastq(nonmacrobe_fastq)
    nBact, nArch, nViral = countMPA(microbe_mpa)

    totalReads = nHum + nNonHum
    nMacrobe = nNonHum - nNonMacrobe
    unknownReads = nNonMacrobe - (nBact + nArch + nViral)
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
