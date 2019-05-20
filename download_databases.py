#! /usr/bin/env python3

import click
import tarfile

from os import makedirs
from os.path import isfile, join
from urllib.request import urlretrieve
from concurrent.futures import ThreadPoolExecutor


DOWNLOAD_JOBS = (
    ('genes', 'https://s3.amazonaws.com/metasub-cap-databases/uniref90_annotated.1.1.dmnd', False),
    ('card', 'https://s3.amazonaws.com/metasub-cap-databases/card_oct_2017_prot_seqs.faa', True),
    ('card', 'https://s3.amazonaws.com/metasub-cap-databases/card_oct_2017_prot_seqs.dmnd', True),
    ('megares', 'https://s3.amazonaws.com/metasub-cap-databases/megares_v1.0.1.tar.gz', True),
    ('hg38', 'https://s3.amazonaws.com/metasub-cap-databases/hg38_alt_contigs.tar.gz', True),
    ('krakenhll_refseq', 'https://s3.amazonaws.com/metasub-cap-databases/krakenhll_refseq_complete.tar.gz', False),
    ('microbes', 'https://s3.amazonaws.com/metasub-cap-databases/staph_aureus_n315.tar.gz', True),
    ('macrobes', 'https://s3.amazonaws.com/metasub-cap-databases/macrobe_quantification.tar.gz', False),
    ('macrobes', 'https://raw.githubusercontent.com/MetaSUB/macrobial-genomes/master/quantified_bias.json', False),
)


def get_downloader(top_dir, dirname, uri, dryrun=True):
    """Return a function that takes no args and downloads the file."""
    def downloader():
        if not dryrun:
            makedirs(dirname, exist_ok=True)
        fpath = join(dirname, uri.split('/')[-1])
        if isfile(fpath):
            return
        print(f'Downloading {uri}')
        if not dryrun:
            urlretrieve(uri, filename=fpath)
        print(f'Finished {uri}')
        if not dryrun and ('.tar.gz' in fpath or '.tgz' in fpath):
            tar = tarfile.open(fpath)
            tar.extractall(path=dirname)
            tar.close()
    return downloader


@click.command()
@click.option('-t', '--threads', default=1)
@click.option('-d/-w', '--dryrun/--wetrun', default=True)
@click.option('-l/-n', '--light/--normal', default=False, help='Only download small databases')
@click.argument('target_dir', default='.')
def main(threads, dryrun, light, target_dir):
    """Download databases to the target dir."""
    executor = ThreadPoolExecutor(max_workers=threads)
    futures = [
        executor.submit(get_downloader(target_dir, inner_dir, uri, dryrun=dryrun))
        for inner_dir, uri, is_light in DOWNLOAD_JOBS
        if not light or is_light
    ]
    for future in futures:
        future.result()


if __name__ == '__main__':
    main()
