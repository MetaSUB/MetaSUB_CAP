

class PipelineSetup:
    '''
    Installs a pipeline
    '''

    def __init__(self):
        pass


    def runSetup(self, buildRepo=True):
        self.installPyPiDependencies()
        self.installCondaDependencies()

    def installPyPiDependencies(self):
        pass

    def installCondaDependencies(self):
        pass

