from packagemega import BaseRecipe, SourceFile, ConstructedFile


class CARDRecipe(BaseRecipe):
    '''
    Recipe for the comprehensive antibiotic resistance
    database
    '''

    def __init__(self):
        super(CARDRecipe, self).__init__()
        self.source = SourceFile(self.repo, "card.faa.gz")
        self.sbred = ConstructedFile(self.repo, "card.shortbred_markers.faa")
        self.dmnd = ConstructedFile(self.repo, "card.dmnd")

    def name(self):
        return 'card'

    def fileTypes(self):
        return ['gz_fasta_aa', 'fasta_aa', 'dmnd-db']

    def resultSchema(self):
        return {
            'fasta': 'gz_fasta_aa',
            'sbred': 'fasta_aa',
            'dmnd': 'dmnd-db',
        }

    def makeRecipe(self):
        self.source.resolve()
        self.repo.saveFiles(self,
                            'fasta',
                            self.source.filepath())
        self.sbred.resolve()
        self.repo.saveFiles(self,
                            'sbred',
                            self.sbred.filepath())
        self.dmnd.resolve()
        self.repo.saveFiles(self,
                            'dmnd',
                            self.dmnd.filepath())
