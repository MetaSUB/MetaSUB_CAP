from packagemega import BaseRecipe, SourceFile, ConstructedFile
import os.path


class KrakenHLLRecipe(BaseRecipe):
    '''
    Recipe for krakenhll dbs
    '''

    def __init__(self):
        super(KrakenHLLRecipe, self).__init__()
        self.refseq = SourceFile(self.repo, "refseq-db")
        self.nt = SourceFile(self.repo, "nt")

    def name(self):
        return 'krakenhll'

    def fileTypes(self):
        return ['krakenhll-db']

    def resultSchema(self):
        return {
            'refseq': ['krakenhll-db'] * 4,
            'nt': ['krakenhll-db'] * 4,
        }

    def makeRecipe(self):

        def save(source, name):
            source.resolve()
            dbIdx = os.path.join(source.filepath(), 'database.idx')
            kDb = os.path.join(source.filepath(), 'database.kdb')
            kDbCounts = os.path.join(source.filepath(), 'database.kdb.counts')
            taxDb = os.path.join(source.filepath(), 'taxDB')
            fs = [dbIdx, kDb, kDbCounts, taxDb]

            self.repo.saveFiles(self, name, *fs)

        save(self.refseq, 'refseq')
        save(self.nt, 'nt')
