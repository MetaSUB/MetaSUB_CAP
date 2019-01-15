"""Test suite for metasub cap."""

from unittest import TestCase
from os import chdir
from subprocess import check_call
from functools import wraps
from tempfile import mkdtemp
from os.path import dirname

TEST_DIR = dirname(__file__)


def my_call(cmd):
    cmd = f'/bin/bash -c "{cmd}"'
    check_call(cmd, shell=True)


def in_mu_repo(func):
    """Run the test in an initialized MU repo."""
    @wraps(func)
    def decorated_function(self, *args, **kwargs):
        repo_dir = mkdtemp()
        chdir(repo_dir)
        my_call('moduleultra init')
        my_call('datasuper add type sample microbiome')
        my_call('moduleultra add pipeline metasub_cap')
        return func(self, *args, **kwargs)

    return decorated_function


def add_data_to_mu(func):
    """Run the test in an initialized MU repo."""
    @wraps(func)
    def decorated_function(self, *args, **kwargs):
        my_call((
            'datasuper bio add-fastqs '
            '-1 _1.fastq.gz -2 _2.fastq.gz '
            'microbiome '
            f'{TEST_DIR}/sample_data/zymo_control_1.fq.gz '
            f'{TEST_DIR}/sample_data/zymo_control_2.fq.gz'
        ))
        return func(self, *args, **kwargs)

    return decorated_function


class TestCAP(TestCase):
    """Test suite for metasub cap."""

    @add_data_to_mu
    @in_mu_repo
    def test_druyrun(self):
        my_call('moduleultra run -p metasub_cap --dryrun')
