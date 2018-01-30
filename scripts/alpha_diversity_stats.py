#! /usr/bin/env python3

import sys
import math
import argparse as ap
from json import dumps as jdumps
from random import choices


class LevelNotFoundException(Exception):
    pass


def checkLevel(taxon, level):
    if level == 'species':
        return ('s__' in taxon) and ('t__' not in taxon)
    elif level == 'genus':
        return ('g__' in taxon) and ('s__' not in taxon)
    raise LevelNotFoundException()


class Sample:

    def __init__(self, tool, level):
        self.tool = tool
        self.level = level
        self.abunds = {}
        self._total = None

    def addLine(self, line):
        taxon, abund = line.split()
        if checkLevel(taxon, self.level):
            self.abunds[taxon] = float(abund)

    @classmethod
    def parseMPA(ctype, tool, mpaFile, level):
        sample = Sample(tool, level)
        with open(mpaFile) as mF:
            for line in mF:
                sample.addLine(line)
        return sample

    def subset(self, n):
        if n == self.total():
            return self

        brkpoints = [0]
        rmap = {}
        for i, (key, val) in enumerate(self.abunds.items()):
            brkpoints.append(brkpoints[i] + val)
            rmap[i] = key

        i = 0
        outAbunds = {}
        indices = sorted(choices(range(self.total()), k=n))
        for ind in indices:
            while ind >= brkpoints[i + 1]:
                i += 1
            key = rmap[i]
            try:
                outAbunds[key] += 1
            except KeyError:
                outAbunds[key] = 1

        outSamp = Sample(self.tool, self.level)
        outSamp.abunds = outAbunds
        return outSamp

    def total(self):
        if self._total is None:
            self._total = sum(self.abunds.values())
        return self._total

    def richness(self):
        return len(self.abunds)

    def shannonIndex(self):
        H = 0
        for count in self.abunds.values():
            p = count / self.total()
            assert p <= 1
            H += p * math.log(p)
        if H < 0:
            H *= -1
        return H

    def ginisimpson(self):
        H = 0
        for count in self.abunds.values():
            p = count / self.total()
            assert p <= 1
            H += p * p
        H = 1 - H
        return H

    def chao1(self):
        sings, doubs = 0, 0
        for val in self.abunds.values():
            if val == 1:
                sings += 1
            elif val == 2:
                doubs += 1
        est = (sings * sings) / (2 * doubs)
        return self.richness() + est


def getSubsets(N):
    vals = [1, 5, 10, 20, 40, 80, 160, 320, 640, 128, 256, 512, 1024, 2048]
    vals = [el * 100 * 1000 for el in vals]
    out = []
    for val in vals:
        if val < N:
            out.append(val)
        else:
            out.append(N)
            break
    return out


def handleCounts(tool, fname):
    obj = {
        'species': {
            'richness': {},
            'shannon_index': {},
            'gini-simpson': {}
        },
        'genus': {
            'richness': {},
            'shannon_index': {},
            'gini-simpson': {}
        }
    }
    for level in obj.keys():
        sample = Sample.parseMPA(tool, fname, level)
        for subsetSize in getSubsets(sample.total()):
            subsample = sample.subset(subsetSize)
            obj[level]['richness'][subsetSize] = subsample.richness()
            obj[level]['shannon_index'][subsetSize] = subsample.shannonIndex()
            obj[level]['gini-simpson'][subsetSize] = subsample.ginisimpson()
            obj[level]['chao1'][subsetSize] = subsample.chao1()
    return obj


def handleProportions(tool, fname):
    obj = {
        'species': {
            'richness': {},
            'shannon_index': {},
            'gini-simpson': {}
        },
        'genus': {
            'richness': {},
            'shannon_index': {},
            'gini-simpson': {}
        }
    }
    for level in obj.keys():
        sample = Sample.parseMPA(tool, fname, level)
        key = 'all_reads'
        obj[level]['richness'][key] = sample.richness()
        obj[level]['shannon_index'][key] = sample.shannonIndex()
        obj[level]['gini-simpson'][key] = sample.ginisimpson()
    return obj


def main():
    args = parseArgs()
    outobj = {}
    for mpaFilePair in args.mpa_files:
        tool, mpaFile = mpaFilePair.split(',')
        if tool.lower() == 'kraken':
            outobj['kraken'] = handleCounts(tool, mpaFile)
        elif tool.lower() == 'metaphlan2':
            outobj['metaphlan2'] = handleProportions(tool, mpaFile)
        else:
            sys.stderr.write('tool {} unsupported'.format(tool))
    sys.stdout.write(jdumps(outobj))


def parseArgs():
    parser = ap.ArgumentParser()
    parser.add_argument('mpa_files', nargs='+',
                        help='pairs of tool_name,mpa_file')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
