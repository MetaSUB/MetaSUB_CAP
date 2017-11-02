import unittest
from datasuper import *
from datasuper.database import *
import os
import tempfile


class TestDataSuperAPI( unittest.TestCase):

    def setUp(self):
        tdir = tempfile.mkdtemp()
        os.chdir(tdir)
        self.tdir = tdir

    def tearDown(self):
        rmtree(self.tdir)

    def testInit(self):
        Repo.initRepo()        


if __name__ =='__main__':
    unittest.main()
