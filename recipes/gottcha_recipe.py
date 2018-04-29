from packagemega import BaseRecipe, SourceFile
from glob import glob


class GOTTCHARecipe(BaseRecipe):

    def __init__(self):
        super(GOTTCHARecipe, self).__init__()
        self.bact_species = SourceFile(self.repo,
                             "GOTTCHA_BACTERIA_c4937_k24_u30.species")
        self.bact_strains = SourceFile(self.repo,
                             "GOTTCHA_BACTERIA_c4937_k24_u30.strain")
        self.virus_species = SourceFile(self.repo,
                             "GOTTCHA_VIRUSES_c5900_k24_u30.species")
        self.virus_strains = SourceFile(self.repo,
                             "GOTTCHA_VIRUSES_c5900_k24_u30.strain")

    def name(self):
        return 'gottcha'

    def fileTypes(self):
        return ['gottcha_index']

    def resultSchema(self):
        return {
            'bact_species': ['gottcha_index'] * 6,
            'bact_strains': ['gottcha_index'] * 6,
            'virus_species': ['gottcha_index'] * 6,
            'virus_strains': ['gottcha_index'] * 6,
        }

    def makeRecipe(self):

        def resolve(name, source):
            source.resolve()
            indices = glob(source.filepath() + '*')
            self.repo.saveFiles(self, name, *indices)

        resolve('bact_species', self.bact_species)
        resolve('bact_strains', self.bact_strains)
        resolve('virus_species', self.virus_species)
        resolve('virus_strains', self.virus_strains)
