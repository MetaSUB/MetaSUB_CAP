import sys
import math
import argparse as ap
from json import dumps as jdumps


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

    def richness(self):
        return len(self.abunds)

    def shannonIndex(self):
        H = 0
        for count in self.abunds.values():
            p = count / sum(self.abunds.values())
            assert p <= 1
            H += p * math.log(p)
        if H < 0:
            H *= -1
        return H


def main():
    args = parseArgs()
    obj = {
        'species': {
            'richness': {},
            'shannon_index': {}
        },
        'genus': {
            'richness': {},
            'shannon_index': {}
        }
    }
    for level in obj.keys():
        for mpaFilePair in args.mpa_files:
            tool, mpaFile = mpaFilePair.split(',')
            sample = Sample.parseMPA(tool, args.mpa_file, level)
            obj[level]['richness'][tool] = sample.richness()
            obj[level]['shannon_index'][tool] = sample.shannon_index()
    sys.stdout.write(jdumps(obj))


def parseArgs():
    parser = ap.ArgumentParser()
    parser.add_argument('mpa_files', nargs='+',
                        help='pairs of tool_name,mpa_file')
    args = parser.parse_args()
    return argip


if __name__ == '__main__':
    main()
