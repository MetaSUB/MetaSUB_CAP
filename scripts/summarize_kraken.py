import click
import sys
from json import dumps


def checkLevel(taxon, level):
    if level == 'species':
        return ('s__' in taxon) and ('t__' not in taxon)
    elif level == 'genus':
        return ('g__' in taxon) and ('s__' not in taxon)
    assert False  # Level not found


def cleanTaxa(taxa):
    # kraken leaves whitespace in taxa names
    # this is somewhat editorial but will make
    # downstream work easier
    return '_'.join(taxa.split())


def krakenParse(mpaF, level):
    vec = {}
    with open(mpaF) as mf:
        for line in mf:
            taxa, val = line.strip().split('\t')
            if checkLevel(taxa, level):
                taxa = cleanTaxa(taxa)
                val = float(val)
                vec[taxa] = val
    return vec


@click.command()
@click.option('-s', '--sample', nargs=2, multiple=True)
def main(sample):
    obj = {}
    for level in ['species', 'genus']:
        obj[level] = {}
        for sname, kFile in sample:
            obj[level][sname] = krakenParse(kFile, level)
    sys.stdout.write(dumps(obj))


if __name__ == '__main__':
    main()
