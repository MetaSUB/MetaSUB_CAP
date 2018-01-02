from packagemega import BaseRecipe, SourceFile, ConstructedFile
from glob import glob

class CommonMacrobialRecipe(BaseRecipe):
    '''
    Recipe for database of common macrobial genomes
    '''

    def __init__(self):
        super(CommonMacrobialRecipe, self).__init__()
        self.source = SourceFile(self.repo, "macrobes.fna.gz")
        self.bt2 = ConstructedFile(self.repo, "common_macrobial.bt2")

    def name(self):
        return 'common_macrobial'

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