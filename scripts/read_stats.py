#!/usr/bin/env python3
import sys
from json import dumps as jdumps
import click
from subprocess import getoutput


def nreads(fastqf):
    cmd = 'zcat {} | wc -l'.format(fastqf)
    rawOut = int(getoutput(cmd).split('\n'))
    out = rawOut / 4
    return out


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


def codons(seqs):
    return getChunks(seqs, 3)


def tetramers(seqs):
    return getChunks(seqs, 4)


def getChunks(seqs, k):
    out = {}
    for seq in seqs:
        for chunk in getChunksFromSeq(seq, k):
            try:
                out[chunk] += 1
            except KeyError:
                out[chunk] = 1
    return out


def getChunksFromSeq(seq, k):
    out = []
    rcseq = rc(seq)
    for i in range(len(seq) - k + 1):
        out.append(seq[i:i + k])
        out.append(rcseq[i:i + k])
    return rcseq


def rcBase(base):
    if base == 'A':
        return 'T'
    elif base == 'C':
        return 'G'
    elif base == 'G':
        return 'C'
    elif base == 'T':
        return 'A'
    else:
        return 'N'


def rc(kmer):
    rcseq = ''
    for base in kmer[::-1]:
        rcseq += rcBase(base)
    return rcseq


@click.command()
@click.option('-n', '--num-seqs', type=int, default=10000)
@click.argument('raw_reads')
@click.argument('microbial_reads')
def main(num_seqs, raw_reads, microbial_reads):
    rawSeqs = sampleFastq(raw_reads, num_seqs)
    microbeSeqs = sampleFastq(microbial_reads, num_seqs)
    obj = {
        'raw': {
            'num_reads': nreads(raw_reads),
            'gc_content': gcContent(rawSeqs),
            'codons': codons(rawSeqs),
            'tetramers': tetramers(rawSeqs)
        },
        'microbial': {
            'num_reads': nreads(microbial_reads),
            'gc_content': gcContent(microbeSeqs),
            'codons': codons(microbeSeqs),
            'tetramers': tetramers(microbeSeqs)

        }
    }
    sys.stdout.write(jdumps(obj))


if __name__ == '__main__':
    main()
