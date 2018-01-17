from packagemega import BaseRecipe, SourceFile, ConstructedFile


class MethyltransferaseRecipe(BaseRecipe):
    '''
    Recipe for the comprehensive antibiotic resistance
    database
    '''

    def __init__(self):
        super(MethyltransferaseRecipe, self).__init__()
        self.source = SourceFile(self.repo, "methyl.faa.gz")
        self.sbred = ConstructedFile(self.repo, "methyl.shortbred_markers.faa")

    def name(self):
        return 'methyls'

    def fileTypes(self):
        return ['gz_fasta_aa', 'fasta_aa']

    def resultSchema(self):
        return {
            'fasta': 'gz_fasta_aa',
            'sbred': 'fasta_aa'
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
