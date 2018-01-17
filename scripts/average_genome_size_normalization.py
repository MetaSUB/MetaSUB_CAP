import click
import sys
from json import loads, dumps
import pandas as pd
from numpy.linalg import inv
from numpy import matmul


def jloads(fname):
    return loads(open(fname).read())


def normalizeTbl(ags, tbl):
    itbl = inv(tbl.as_matrix())
    taxaAGS = matmul(itbl, ags)
    normal = tbl.div(taxaAGS, axis=1)
    return normal


@click.command()
@click.argument('ave_genome_size')
@click.argument('taxa_table_json')
def main(ave_genome_size, taxa_table_json):
    ags = jloads(ave_genome_size)
    ags = pd.Series(ags).as_matrix()
    obj = jloads(taxa_table_json)
    normed = {}
    for level, tbl in obj.items():
        tbl = pd.DataFrame(tbl)
        normed[level] = normalizeTbl(ags, tbl).to_dict()
    sys.stdout.write(dumps(normed))


if __name__ == '__main__':
    main()
