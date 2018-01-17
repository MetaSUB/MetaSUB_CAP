import click
import sys
from json import dumps


def mcParse(mcFile):
    with open(mcFile) as mcf:
        for line in mcf:
            if 'average_genome_size' in line:
                return float(line.strip().split()[1])
    return -1


@click.command()
@click.option('-s', '--sample', nargs=2, multiple=True)
def main(sample):
    vec = {}
    for sname, mcFile in sample:
        vec[sname] = mcParse(mcFile)
    sys.stdout.write(dumps(vec))


if __name__ == '__main__':
    main()
