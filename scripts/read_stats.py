#!/usr/bin/env python3
import sys
from json import dumps as jdumps
import click
from subprocess import getoutput


def sampleFastq(fastqf, n):
    cmd = 'zcat {} | head -{}'.format(fastqf, 4 * n)
    rawOut = getoutput(cmd).split('\n')
    out = [line.strip()
           for i, line in enumerate(rawOut)
           if (i % 4) == 1]
    return out


def gcContent(seqs):
    gc, tot = 0, 0
    for seq in seqs:
        for base in seq:
            if base in ['G', 'C', 'g', 'c']:
                gc += 1
            tot += 1
    return gc / tot


@click.command()
@click.option('-n', '--num-seqs', type=int, default=10000)
@click.argument('raw_reads')
@click.argument('microbial_reads')
def main(num_seqs, raw_reads, microbial_reads):
    rawSeqs = sampleFastq(raw_reads, num_seqs)
    microbeSeqs = sampleFastq(microbial_reads, num_seqs)
    obj = {
        'raw': {
            'gc_content': gcContent(rawSeqs),
        },
        'microbial': {
            'gc_content': gcContent(microbeSeqs),
        }
    }
    sys.stdout.write(jdumps(obj))


if __name__ == '__main__':
    main()
