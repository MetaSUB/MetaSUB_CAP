from packagemega import BaseRecipe, SourceFile, ConstructedFile
from glob import glob


class MegaresRecipe(BaseRecipe):

    def __init__(self):
        super(MegaresRecipe, self).__init__()
        self.fasta = SourceFile(self.repo, "megares.fa")
        self.bt2 = ConstructedFile(self.repo, "megares.bt2")
        self.csv = SourceFile(self.repo, "megares.csv")

    def name(self):
        return 'megares'

    def fileTypes(self):
        return ['fasta_nucl', 'bt2_index', 'csv']

    def resultSchema(self):
        return {
            'fasta': 'fasta_nucl',
            'bt2': ['bt2_index'] * 6,
            'csv': 'csv'
        }

    def makeRecipe(self):
        self.fasta.resolve()
        self.repo.saveFiles(self,
                            'fasta',
                            self.fasta.filepath())
        self.csv.resolve()
        self.repo.saveFiles(self,
                            'csv',
                            self.csv.filepath())
        self.bt2.resolve()
        bt2Indices = glob(self.bt2.filepath() + '*')
        self.repo.saveFiles(self,
                            'bt2',
                            *bt2Indices)
