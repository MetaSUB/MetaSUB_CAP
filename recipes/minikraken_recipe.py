from packagemega import BaseRecipe, SourceFile, ConstructedFile
import os.path


class MiniKrakenRecipe(BaseRecipe):
    '''
    Recipe for minikraken db
    '''

    def __init__(self):
        super(MiniKrakenRecipe, self).__init__()
        self.source = SourceFile(self.repo, "minikraken-db")

    def name(self):
        return 'minikraken'

    def fileTypes(self):
        return ['kraken-db']

    def resultSchema(self):
        return {
            'db': ['kraken-db'] * 4
        }

    def makeRecipe(self):
        self.source.resolve()
        dbIdx = os.path.join(self.source.filepath(), 'database.idx')
        kDb = os.path.join(self.source.filepath(), 'database.kdb')
        taxa = os.path.join(self.source.filepath(), 'taxonomy')
        taxaNames = os.path.join(taxa, 'names.dmp')
        taxaNodes = os.path.join(taxa, 'nodes.dmp')
        fs = [dbIdx, kDb, taxaNames, taxaNodes]

        self.repo.saveFiles(self, 'minikraken', *fs)
