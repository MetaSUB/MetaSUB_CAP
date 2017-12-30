#!/usr/bin/env python3
import sys
from json import dumps as jdumps
import click


def sampleFastq(fastqf, n):
    out = []
    with open(fastqf) as fqf:
        for i, line in enumerate(fqf):
            if (i % 4) != 1:
                continue
            out.append(line.strip())
            if len(out) == n:
                break
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
@click.option('-n', '--num-seqs', type=int, default=100000)
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
