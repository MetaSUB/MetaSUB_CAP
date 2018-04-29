from packagemega import BaseRecipe, SourceFile
from glob import glob
from os.path import basename, dirname, join


class CentrifugeRecipe(BaseRecipe):

    def __init__(self):
        super(CentrifugeRecipe, self).__init__()
        self.nt = SourceFile(self.repo, "nt.1.cf")
        self.phv = SourceFile(self.repo, "p+h+v.1.cf")

    def name(self):
        return 'centrifuge'

    def fileTypes(self):
        return ['centrifuge_index']

    def resultSchema(self):
        return {
            'nt': ['centrifuge_index'] * 3,
            'p_h_v': ['centrifuge_index'] * 3
        }

    def makeRecipe(self):

        def resolve(name, source):
            source.resolve()
            base = basename(source.filepath())
            dirpath = dirname(source.filepath())
            pattern = base.split('.')
            pattern = pattern[0] + '.*.' + pattern[2]
            pattern = join(dirpath, pattern)
            indices = glob(pattern)
            self.repo.saveFiles(self, name, *indices)

        resolve('nt', self.nt)
        resolve('p_h_v', self.phv)
