from packagemega import BaseRecipe, SourceFile, ConstructedFile
from glob import glob


class StaphAureusN315Recipe(BaseRecipe):

    def __init__(self):
        super(StaphAureusN315Recipe, self).__init__()
        self.source = SourceFile(self.repo, "staph_aureus_n315.fna.gz",
            "https://www.ncbi.nlm.nih.gov/nuccore/NC_002745.2?report=fasta&log$=seqview&format=text")
        self.bt2 = ConstructedFile(self.repo, "staph_aureus_n315.bt2")

    def name(self):
        return 'staph_aureus_n315'

    def fileTypes(self):
        return ['gz_fasta_nucl', 'bt2_index']

    def resultSchema(self):
        return {
            'fasta': 'gz_fasta_nucl',
            'bt2': ['bt2_index'] * 6
        }

    def makeRecipe(self):
        self.source.resolve()
        self.repo.saveFiles(self,
                            'fasta',
                            self.source.filepath())
        self.bt2.resolve()
        bt2Indices = glob(self.bt2.filepath() + '*')
        self.repo.saveFiles(self,
                            'bt2',
                            *bt2Indices)
