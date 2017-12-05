from packagemega import BaseRecipe, SourceFile


class CARDRecipe(BaseRecipe):
    '''
    Recipe for the comprehensive antibiotic resistance
    database
    '''

    def __init__(self):
        super(CARDRecipe, self).__init__()
        self.source = SourceFile(self.repo, "card.faa.gz")

    def name(self):
        return 'card'

    def fileTypes(self):
        return ['fasta']

    def resultSchema(self):
        return {
            'fasta': 'gz_fasta_aa'
        }

    def makeRecipe(self):
        self.source.resolve()
        self.repo.saveFiles(self,
                            'fasta',
                            self.source.filepath())
