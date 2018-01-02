#!/usr/bin/env python3

import sys
import json
from scipy.spatial.distance import cosine
import pandas as pd
import os.path
from glob import glob
import click


'''
A simple script which finds the cosine similarity
between a sample and many hmp sites

HMP sites must specify their body site as the first
field in the basename before a '.'

Output is a JSON string to stdout and in the following form:

{
<body site>:    [<dist>...]
}
'''


def mphlanToVec(fname):
    vec = {}
    with open(fname) as f:
        for line in f:
            if 'g__' in line and 's__' not in line:
                taxa, abundance = line.split()
                abundance = float(abundance)
                taxa = taxa.strip()
                vec[taxa] = abundance

    return pd.Series(vec)


def dist(sample, ref):
    df = pd.DataFrame({'sample': sample, 'ref': ref}).fillna(value=0)
    d = 1 - cosine(df['sample'], df['ref'])
    return d


@click.command()
@click.argument('hmp_dir')
@click.argument('mpa')
def main(hmp_dir, mpa):
    out = {}
    refFs = glob(hmp_dir + '/*.metaphlan2.txt')
    sample = mphlanToVec(mpa)
    for refF in refFs:
        refVec = mphlanToVec(refF)
        d = dist(sample, refVec)
        bodySite = os.path.basename(refF).split('.')[0]
        if bodySite not in out:
            out[bodySite] = []
        out[bodySite].append(d)
    sys.stdout.write(json.dumps(out))


if __name__ == '__main__':
    main()
