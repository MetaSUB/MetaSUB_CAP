#! /usr/bin/env python3

import pandas as pd
import click
from json import dumps


class LevelNotFoundException(Exception):
    pass


def checkLevel(taxon, level):
    if level == 'species':
        return ('s__' in taxon) and ('t__' not in taxon)
    elif level == 'genus':
        return ('g__' in taxon) and ('s__' not in taxon)
    raise LevelNotFoundException()


def getColumnDist(mdb, sample, col):
    out = {}
    for taxonkey, abund in sample.iterTaxa():
        #print(taxonkey)
        try:
            val = mdb[taxonkey][col]
        except KeyError:
            val = 'NaN'
        try:
            out[val] += abund
        except KeyError:
            out[val] = abund
    return out


class Sample:

    def __init__(self, sname):
        self.sname = sname
        self.abunds = {}
        self.total = 0.0

    def addLine(self, line):
        if line[0] == '#':
            return
        taxon, abund = line.split()
        taxonList = [t.split('__')[1] for t in taxon.split('|')]
        if checkLevel(taxon, 'species'):
            self.abunds['__'.join(taxonList).lower()] = float(abund)
            self.total += float(abund)

    def iterTaxa(self):
        for taxa, abund in self.abunds.items():
            yield taxa, abund / self.total

    @classmethod
    def parseMPA(ctype, name, mpaFile):
        sample = Sample(name)
        with open(mpaFile) as mF:
            for line in mF:
                sample.addLine(line)
        return sample


def parseMDB(mdbf):
    mdb = {}
    ranks = 'kingdom', 'phylum', 'class', 'order', 'family', 'genus', 'species'
    for rowname, row in pd.read_csv(mdbf).iterrows():
        key = ''
        for rank in ranks:
            key += row.loc[rank]
            key += '__'
        key = '_'.join(key[:-2].lower().split())
        mdb[key] = row
    return mdb


@click.command()
@click.argument('microbe_directory')
@click.argument('sample_name')
@click.argument('mpa')
def main(microbe_directory, sample_name, mpa):
    mdb = parseMDB(microbe_directory)
    sample = Sample.parseMPA(sample_name, mpa)
    keys = ['gram_stain',
            'microbiome_location',
            'antimicrobial_susceptibility',
            'optimal_temperature',
            'extreme_environment',
            'biofilm_forming',
            'optimal_ph',
            'animal_pathogen',
            'spore_forming',
            'pathogenicity',
            'plant_pathogen']

    obj = {key: getColumnDist(mdb, sample, key)
           for key in keys}
    print(dumps(obj))


if __name__ == '__main__':
    main()
