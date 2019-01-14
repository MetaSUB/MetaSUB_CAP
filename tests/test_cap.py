"""Test suite for metasub cap."""

from unittest import TestCase
from os import chdir
from subprocess import call
from functools import wraps
from tempfile import mkdtemp


def in_mu_repo(func):
    """Run the test in an initialized MU repo."""
    @wraps(func)
    def decorated_function(self, *args, **kwargs):
        repo_dir = mkdtemp()
        chdir(repo_dir)
        call('moduleultra init', shell=True)
        call('datasuper add type sample microbiome', shell=True)
        call('moduleultra add pipeline metasub_cap', shell=True)
        return func(self, *args, **kwargs)

    return decorated_function


class TestCAP(TestCase):
    """Test suite for metasub cap."""

    @in_mu_repo
    def test_druyrun(self):
        call('moduleultra run -p metasub_cap --dryrun')
