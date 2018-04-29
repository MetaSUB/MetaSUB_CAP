#! /usr/bin/env python3

import click
from json import loads as jloads
import pandas as pd
from sys import stdout

#from .pybam import pybam

million = 1000 * 1000


def getAGS(agsf):
    with open(agsf) as mcf:
        for line in mcf:
            if 'average_genome_size' in line:
                return float(line.strip().split()[1]) / million
    return -1


def getNReads(readStatsF):
    readStats = jloads(open(readStatsF).read())
    nreads = int(readStats['num_reads'])
    nreads = nreads / (1000 * 1000)
    return nreads


def getSeqLens(fastaf):
    lenout = {}
    memoout = {}
    curRec, curMemo, curLen = None, None, 0
    with open(fastaf) as ff:
        for line in ff:
            line = line.strip()
            if len(line) == 0:
                continue
            if line[0] == '>':
                if curRec is not None:
                    lenout[curRec] = curLen / 1000
                    memoout[curRec] = curMemo
                curRec = line.split()[0][1:]
                curMemo = ' '.join(line.split()[1:])
                curLen = 0
            else:
                curLen += len(line)
    lenout[curRec] = curLen / 1000
    memoout[curRec] = curMemo
    return lenout, memoout


def parseAlignments(alf):
    if '.m8' in alf:
        return parseM8(alf)
    elif '.bam' in alf:
        return parseBAM(alf)
    assert False, f'Cannot parse {alf} file type not recognized'


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


def parseBAM(bamf):
    out = {}
    for rid, sid in pybam.read(bamf, ['sam_qname', 'sam_rname']):
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
    out = pd.DataFrame(out).transpose()
    return out


@click.command()
@click.option('-s', '--read-stats')
@click.option('-a', '--ags')
@click.option('-f', '--fasta')
@click.argument('alignment_file')
def main(read_stats, ags, fasta, alignment_file):
    readsPerSeq = parseAlignments(alignment_file)
    seqLens, seqMemos = getSeqLens(fasta)
    nreadsInSample = getNReads(read_stats)
    ags = getAGS(ags)
    tbl = makeTable(readsPerSeq, seqMemos, seqLens, nreadsInSample, ags)
    stdout.write(tbl.to_csv())


if __name__ == '__main__':
    main()
