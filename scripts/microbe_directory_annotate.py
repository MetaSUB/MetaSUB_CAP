#! /usr/bin/env python3

import pandas as pd
import click
from json import dumps
from sys import stderr

'''
{
    "gram_stain": {"1.0": 0.6348978175655748, "0.0": 0.12937136867380725 "2.0": 0.006112381332830759},
    "microbiome_location": {"1.0": 0.6608044522412223"0.0": 0.036777353150309416}, 
    "antimicrobial_susceptibility": {"1.0": 0.7089475834039308, "0.0": 0.0015535635887611514},
    "optimal_temperature": {"37.0": 0.49118901314628005, "30.0": 0.06614712870345012, "34.0": 0.05548622530432669, "26.0": 0.04929267068039149, "35.0": 0.0041728923907680072},
    "extreme_environment": {"0.0": 0.7163033574855482, "1.0": 0.06774566814776313},
    "biofilm_forming": {"1.0": 0.5861109356029197, "0.0": 0.00208828857982829632}, 
    "optimal_ph": "7.25": 0.02771531432216563 "11.0": 0.006112381332830759, "6.6": 0.002753822866440241, "6.75": 0.0026091414997854705, "6.0": 0.00155356358876115142},
    "animal_pathogen":"0.0": 0.06777243690998316 "1.0": 0.03244135554844371},
    "spore_forming": {"0.0": 0.6757222390866626, "1.0": 0.0015535635887611514},
    "pathogenicity": {"2.0": 0.6319251844524858, "1.0": 0.06675771658339989},
    "plant_pathogen": {"0.0": 0.6890774671722312}
}
'''
class LevelNotFoundException(Exception):
    pass


def checkLevel(taxon, level):
    if level == 'species':
        return ('s__' in taxon) and ('t__' not in taxon)
    elif level == 'genus':
        return ('g__' in taxon) and ('s__' not in taxon)
    raise LevelNotFoundException()


def getColumnDist(mdb, sample, col, key_conversion=lambda x: x):
    out = {}
    for taxonkey, abund in sample.iterTaxa():
        #print(taxonkey)
        try:
            val = str(key_conversion(mdb[taxonkey][col]))
        except KeyError:
            val = 'unknown'
        if 'nan' in val:
            val = 'unknown'
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
        taxonList = [t.split('__')[1]
                     for t in taxon.split('|')
                     if taxon.strip() != 'unclassified']
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


def chooser(*choices):
    def foo(val):
        try:
            val = int(val)
            return choices[val]
        except ValueError:
            return val
        except IndexError:
            print('{}, {}'.format(val, choices), file=stderr)
            raise
    return foo

def strOrUnk(func):
    def bar(val):
        try:
            return func(val)
        except ValueError:
            return 'unknown'
    return bar

@click.command()
@click.argument('microbe_directory')
@click.argument('sample_name')
@click.argument('mpa')
def main(microbe_directory, sample_name, mpa):
    mdb = parseMDB(microbe_directory)
    sample = Sample.parseMPA(sample_name, mpa)
    keys = [
        ('gram_stain', chooser('gram_negative', 'gram_positive', 'indeterminate')),
        ('microbiome_location', chooser('non_human', 'human')),
        ('antimicrobial_susceptibility', chooser('no_known_abx', 'known_abx')),
        ('optimal_temperature', strOrUnk(lambda x: str(int(x)) + 'c')),
        ('extreme_environment', chooser('mesophile', 'extremophile')),
        ('biofilm_forming', chooser('no', 'yes')),
        ('optimal_ph', strOrUnk(lambda x: 'ph' + '_'.join(str(x).split('.')))),
        ('animal_pathogen', chooser('no', 'yes')),
        ('spore_forming', chooser('no', 'yes')),
        ('pathogenicity', strOrUnk(lambda x: 'cogem_' + str(int(x)))),
        ('plant_pathogen', chooser('no', 'yes')),
    ]

    obj = {key: getColumnDist(mdb, sample, key, key_conversion=converter)
           for key, converter in keys}
    print(dumps(obj))


if __name__ == '__main__':
    main()
