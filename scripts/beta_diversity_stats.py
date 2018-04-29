#! /usr/bin/env python3


import sys
import click
from scipy.spatial.distance import pdist, squareform
from scipy.stats import gmean, entropy
from numpy.linalg import norm
import numpy as np
from math import sqrt
from json import dumps as jdumps
import pandas as pd


class LevelNotFoundException(Exception):
    pass


def checkLevel(taxon, level):
    if level == 'species':
        return ('s__' in taxon) and ('t__' not in taxon)
    elif level == 'genus':
        return ('g__' in taxon) and ('s__' not in taxon)
    raise LevelNotFoundException()


def clr(X):
    _X = X + 0.0000001
    _X = _X / norm(_X, ord=1)
    g = gmean(_X)
    _X = np.divide(_X, g)
    _X = np.log(_X)
    return _X


def rhoProportionality(P, Q):
    _P, _Q = clr(P), clr(Q)
    N = np.var(_P - _Q)
    D = np.var(_P) + np.var(_Q)
    return 1 - (N / D)


def jensenShannonDistance(P, Q):
    _P = P / norm(P, ord=1)
    _Q = Q / norm(Q, ord=1)
    _M = 0.5 * (_P + _Q)
    J = 0.5 * (entropy(_P, _M) + entropy(_Q, _M))
    return sqrt(J)


class SampleSet:

    def __init__(self, tool, mpas):
        self.tool = tool
        self.mpaFiles = mpas

    def parse(self, level):
        mpas = {name: Sample.parseMPA(name, mpaf, level).abunds
                for name, mpaf in self.mpaFiles}
        self.mpas = pd.DataFrame(mpas).transpose()
        self.mpas.fillna(value=0, inplace=True)

    def distanceMatrix(self, metric):
        X = self.mpas.as_matrix()
        if metric == 'jensen_shannon_distance':
            distm = squareform(pdist(X, jensenShannonDistance))
        elif metric == 'rho_proportionality':
            distm = squareform(pdist(X, rhoProportionality))
        distm = pd.DataFrame(distm, 
                             index=self.mpas.index,
                             columns=self.mpas.index)
        return distm.to_dict()


class Sample:

    def __init__(self, sname, level):
        self.sname = sname
        self.level = level
        self.abunds = {}

    def addLine(self, line):
        taxon, abund = line.split()
        if checkLevel(taxon, self.level):
            self.abunds[taxon] = float(abund)

    @classmethod
    def parseMPA(ctype, name, mpaFile, level):
        sample = Sample(name, level)
        with open(mpaFile) as mF:
            for line in mF:
                sample.addLine(line)
        return sample


@click.command()
@click.option('-t', '--tool-set', nargs=3, multiple=True)
def main(tool_set):
    toolSets = tool_set
    condensed = {}
    for toolSet in toolSets:
        tool = toolSet[0]
        sampleName = toolSet[1]
        mpa = toolSet[2]
        try:
            condensed[tool].append((sampleName, mpa))
        except KeyError:
            condensed[tool] = [(sampleName, mpa)]
    sampleSets = [SampleSet(tool, mpas) for tool, mpas in condensed.items()]

    obj = {
        'species': {
            'jensen_shannon_distance': {},
            'rho_proportionality': {},
        },
        'genus': {
            'jensen_shannon_distance': {},
            'rho_proportionality': {},
        }
    }
    for level in obj.keys():
        for sampleSet in sampleSets:
            sampleSet.parse(level)
            tool = sampleSet.tool
            for metric in obj[level].keys():
                obj[level][metric][tool] = sampleSet.distanceMatrix(metric)
    sys.stdout.write(jdumps(obj))


if __name__ == '__main__':
    main()
