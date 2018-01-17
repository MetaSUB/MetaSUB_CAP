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
    for taxa, abund in sample.iterTaxa():
        try:
            val = mdb.loc[sample][col]
        except KeyError:
            val = 'NA'
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
        taxon, abund = line.split()
        if checkLevel(taxon, 'species'):
            self.abunds[taxon] = float(abund)
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
    mdb = pd.DataFrame.from_csv(mdbf)
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
