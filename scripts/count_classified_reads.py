#!/usr/bin/env python3

import sys
import subprocess as sp
import json




msg = '''
A simple script which counts how many reads are human contamination, 
of unknown origin or belong to one of the domains bacteria, archaea, 
or virus.

Arguments are rudimentary and positional:

     <cmd> [human read fastq.gz] [non human read fastq.gz] [kraken mpa report]

Output is a JSON string to stdout and in the following form:

{
host:    <proportion>
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
non = sys.argv[2]
mpa = sys.argv[3]


nHum = int( sp.getoutput('zcat {} | wc -l'.format(hum)).split()[0]) / 4
nNon = int( sp.getoutput('zcat {} | wc -l'.format(non)).split()[0]) / 4


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


nUnk = nNon - nBact - nArch - nViral
tot = nNon + nHum

assert nUnk >= 0

out={
    'host': 100.0*nHum / tot,
    'unknown': 100.0*nUnk / tot,
    'bacteria': 100.0*nBact / tot,
    'archaea': 100.0*nArch / tot,
    'virus': 100.0*nViral / tot,
    }

sys.stdout.write(json.dumps(out))
