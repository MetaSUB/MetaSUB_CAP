from packagemega import BaseRecipe, SourceFile, ConstructedFile


class MiniKrakenRecipe(BaseRecipe):
    '''
    Recipe for minikraken db
    '''

    def __init__(self):
        super(MiniKrakenRecipe, self).__init__()
        self.source = SourceFile(self.repo, "minikraken.db")

    def name(self):
        return 'minikraken'

    def fileTypes(self):
        return ['kraken-db']

    def resultSchema(self):
        return {
            'minikraken': 'kraken-db'
        }

    def makeRecipe(self):
        self.source.resolve()
        self.repo.saveFiles(self,
                            'minikraken',
                            self.source.filepath())
