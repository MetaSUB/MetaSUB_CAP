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

    def testPersistentDictAdd(self):
        fpath = os.path.join(self.tdir, 'test.yml')
        pd = PersistentDict(fpath)
        pd['1'] = 'a'
        del pd
        pd = PersistentDict(fpath)
        assert pd['1'] == 'a'

    def testPersistentDictKeys(self):
        fpath = os.path.join(self.tdir, 'test.yml')
        pd = PersistentDict(fpath)
        pd['1'] = 'a'
        assert '1' in pd.keys()
        

    def testPersistentSetAdd(self):
        fpath = os.path.join(self.tdir, 'test.yml')
        ps = PersistentSet(fpath)
        ps.add('1')
        del ps
        ps = PersistentSet(fpath)
        assert '1' in ps
        

if __name__ =='__main__':
    unittest.main()
