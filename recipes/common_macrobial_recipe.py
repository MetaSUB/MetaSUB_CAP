from packagemega import BaseRecipe, SourceFile


class CommonMacrobialRecipe(BaseRecipe):
    '''
    Recipe for database of common macrobial genomes
    '''

    def __init__(self):
        super(CommonMacrobialRecipe, self).__init__()
        self.source = SourceFile(self.repo, "macrobes.fna.gz")

    def name(self):
        return 'common_macrobial_genomes'

    def fileTypes(self):
        return ['gz_fasta_nucl']

    def resultSchema(self):
        return {
            'fasta': 'gz_fasta_nucl'
        }

    def makeRecipe(self):
        self.source.resolve()
        self.repo.saveFiles(self,
                            'fasta',
                            self.source.filepath())
