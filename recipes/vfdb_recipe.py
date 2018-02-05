from packagemega import BaseRecipe, SourceFile, ConstructedFile


class VFDBRecipe(BaseRecipe):
    '''
    Recipe for uniref90 with diamond index
    '''

    def __init__(self):
        super(VFDBRecipe, self).__init__()
        self.fasta = SourceFile(self.repo, "vfdb.faa")
        self.dmnd = ConstructedFile(self.repo, "vfdb.dmnd")

    def name(self):
        return 'vfdb'

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
