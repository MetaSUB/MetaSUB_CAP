#!/usr/bin/env python3

import sys
import subprocess as sp
import json




msg = '''
A simple script which counts how many reads are human contamination, 
of unknown origin or belong to one of the domains bacteria, archaea, 
or virus.

Arguments are rudimentary and positional:

     <cmd> [human read fastq.gz] [non human reads fastq.gz] [non macrobial reads fastq.gz] [kraken mpa report]

Output is a JSON string to stdout and in the following form:

{
host:    <proportion>
non_host_macrobial: <proportion>
unknown:  <proportion>
bacteria: <proportion>
viral:    <proportion>
archaea:  <proportion>
}
'''

if len(sys.argv) != 4:
    sys.stderr.write(msg)
    sys.exit(1)

hum = sys.argv[1]
nonHum = sys.argv[2]
nonMacrobe = sys.argv[3]
mpa = sys.argv[4]


def countFastq(fname):
    raw = sp.getoutput('zcat {} | wc -l'.format(hum)).split()[0]
    return int(raw) / 4


nHum = countFastq(hum)
nNonHum = countFastq(nonHum)
nNonMacrobe = countFastq(nonMacrobe)

nBact = 0
nArch = 0
nViral = 0

with open(mpa) as mf:

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


nMacrobe = nNonHum - nNonMacrobe
nUnk = nNonMacrobe - nBact - nArch - nViral
tot = nNonHum + nHum

assert nUnk >= 0

out = {
    'host': nHum / tot,
    'non_host_macrobial': nMacrobe / tot,
    'unknown': nUnk / tot,
    'bacteria': nBact / tot,
    'archaea': nArch / tot,
    'virus': nViral / tot,
}

sys.stdout.write(json.dumps(out))
