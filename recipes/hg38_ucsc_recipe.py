from packagemega import BaseRecipe, SourceFile, ConstructedFile


class HG38UCSCGenomeRecipe(BaseRecipe):
    '''
    Recipe for the hg38 genome from UCSC.
    This genome is used in the CAP because:
    - hg38 is the most recent as of December 2017
    - it includes alt contigs. Bad for variant calling, good for filtering
    - it uses human readable chromosome names
    - it uses the rCRS mitochondrial sequence
    '''

    def __init__(self):
        super(HG38UCSCGenomeRecipe, self).__init__()
        self.source = SourceFile(self.repo, "hg38_ucsc.fna.gz",
            "http://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/hg38.fa.gz")
        self.bt2 = ConstructedFile(self.repo, "hg38_ucsc.bt2")

    def name(self):
        return 'hg38_ucsc'

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
        self.repo.saveFiles(self,
                            'bt2',
                            self.bt2.filepath())
