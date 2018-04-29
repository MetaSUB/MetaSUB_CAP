from datasuper import *
import click

def groupFastqs(fastqs, forwardSuffix, reverseSuffix):
    grouped = {}
    for fastqf in fastqs:
        fastqBase = os.path.basename(fastqf)
        if forwardSuffix in fastqf:
            root = fastqBase.split(forwardSuffix)[0]
            try:
                grouped[root][0] = fastqf
            except KeyError:
                grouped[root] = [fastqf, None]
        elif reverseSuffix in fastqf:
            root = fastqBase.split(reverseSuffix)[0]
            try:
                grouped[root][1] = fastqf
            except KeyError:
                grouped[root] = [None, fastqf]
        else:
            continue
    return grouped
        
            
@click.command()
@click.option('-1', '--forward-suffix', default='_1.fastq.gz')
@click.option('-2', '--reverse-suffix', default='_2.fastq.gz')
@click.option('-n', '--name-prefix', default='')
@click.argument('sample_type')
@click.argument('fastqs', nargs=-1)
def main(forward_suffix, reverse_suffix, name_prefix, sample_type, fastqs):
    groups = groupFastqs(fastqs, forward_suffix, reverse_suffix)
    with Repo.loadRepo() as repo:
        for root, (fq1, fq2) in groups.items():
            print('{}: {}, {}'.format(root, fq1, fq2))
            if (fq1 is None) or (fq2 is None):
                continue
            fr1 = getOrMakeFile(repo, name_prefix + root + '_1', fq1, 'gz_fastq')
            fr2 = getOrMakeFile(repo, name_prefix + root + '_2', fq2, 'gz_fastq').primaryKey
            res = getOrMakeResult(repo, name_prefix + root + '_rsrd', 'raw_short_read_dna', {'read1': fr1, 'read2': fr2})
            sample = getOrMakeSample(repo, name_prefix + root, sample_type)
            sample.addResult(res)
            sample.save(modify=True)

            
if __name__ == '__main__':
    main()
