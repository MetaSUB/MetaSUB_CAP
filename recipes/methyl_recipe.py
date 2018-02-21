from packagemega import BaseRecipe, SourceFile, ConstructedFile


class MethyltransferaseRecipe(BaseRecipe):
    '''
    Recipe for the comprehensive antibiotic resistance
    database
    '''

    def __init__(self):
        super(MethyltransferaseRecipe, self).__init__()
        self.fasta = SourceFile(self.repo, "methyls.faa")
        self.dmnd = ConstructedFile(self.repo, "methyls.dmnd")

    def name(self):
        return 'methyl'

    def fileTypes(self):
        return ['gz_fasta_aa', 'dmnd-db']

    def resultSchema(self):
        return {
            'fasta': 'gz_fasta_aa',
            'dmnd': 'dmnd-db'
        }

    def makeRecipe(self):
        self.fasta.resolve()
        self.repo.saveFiles(self,
                            'fasta',
                            self.fasta.filepath())
        self.dmnd.resolve()
        self.repo.saveFiles(self,
                            'dmnd',
                            self.dmnd.filepath())

