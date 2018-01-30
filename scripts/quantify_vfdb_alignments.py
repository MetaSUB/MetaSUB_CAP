#! /usr/bin/env python3

import click
from json import loads as jloads
import pandas as pd
from sys import stdout


million = 1000 * 1000


def getAGS(agsf):
    with open(agsf) as mcf:
        for line in mcf:
            if 'average_genome_size' in line:
                return float(line.strip().split()[1]) / million
    return -1


def getNReads(readStatsF):
    readStats = jloads(open(readStatsF).read())
    nreads = int(readStats['microbial']['num_reads'])
    nreads = nreads / (1000 * 1000)
    return nreads


def getSeqLens(fastaf):
    lenout = {}
    memoout = {}
    curRec, curMemo, curLen = None, None, 0
    with open(fastaf) as ff:
        for line in ff:
            line = line.strip()
            if line[0] == '>':
                if curRec is not None:
                    lenout[curRec] = curLen / 1000
                    memoout[curRec] = curMemo
                curRec = line.split()[0][1:]
                curMemo = ' '.join(line.split()[1])
                curLen = 0
            else:
                curLen += len(line)
    lenout[curRec] = curLen / 1000
    memoout[curRec] = curMemo
    return lenout, memoout


def parseM8(m8f):
    out = {}
    with open(m8f) as m8:
        for line in m8:
            tkns = line.strip().split()
            rid, sid = tkns[:2]
            try:
                out[sid].add(rid)
            except KeyError:
                out[sid] = set()
                out[sid].add(rid)
    out = {sid: len(rids) for sid, rids in out.items()}
    return out


def makeTable(readsPerSeq, seqMemos, seqLens, nreadsInSample, ags):
    out = {}
    for sid, nreads in readsPerSeq.items():
        out[sid] = {}
        out[sid]['memo'] = seqMemos[sid]
        out[sid]['reads'] = nreads
        out[sid]['RPK'] = nreads / seqLens[sid]
        out[sid]['RPKM'] = nreads / (seqLens[sid] * nreadsInSample)
        out[sid]['RPKMG'] = nreads / (seqLens[sid] * nreadsInSample * ags)
    out = pd.DataFrame(out)
    return out


@click.command()
@click.option('-s', '--read-stats')
@click.option('-a', '--ags')
@click.option('-f', '--fasta')
@click.argument('m8')
def main(read_stats, ags, fasta, m8):
    readsPerSeq = parseM8(m8)
    seqLens, seqMemos = getSeqLens(fasta)
    nreadsInSample = getNReads(read_stats)
    ags = getAGS(ags)
    tbl = makeTable(readsPerSeq, seqMemos, seqLens, nreadsInSample, ags)
    stdout.write(tbl.to_csv())


if __name__ == '__main__':
    main()
