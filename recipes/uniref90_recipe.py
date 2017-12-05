from packagemega import BaseRecipe, SourceFile, ConstructedFile


class Uniref90Recipe(BaseRecipe):
    '''
    Recipe for uniref90 with diamond index
    '''

    def __init__(self):
        super(Uniref90Recipe, self).__init__()
        self.source = SourceFile(self.repo, "uniref90.faa.gz")
        self.dmnd = ConstructedFile(self.repo, "uniref90.dmnd")

    def name(self):
        return 'uniref90'

    def fileTypes(self):
        return ['gz_fasta_aa', 'dmnd-db']

    def resultSchema(self):
        return {
            'fasta': 'gz_fasta_aa',
            'dmnd': 'dmnd-db'
        }

    def makeRecipe(self):
        self.source.resolve()
        self.repo.saveFiles(self,
                            'fasta',
                            self.source.filepath())
        self.dmnd.resolve()
        self.repo.saveFiles(self,
                            'dmnd',
                            self.dmnd.filepath())
