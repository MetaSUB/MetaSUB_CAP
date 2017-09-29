

class PipelineSetup:
    '''
    Installs a pipeline
    '''

    def __init__(self):
        pass


    def runSetup(self, buildRepo=True):
        self.installPyPiDependencies()
        self.installCondaDependencies()
        if buildRepo:
            self.initRepo()
    
    def installPyPiDependencies(self):
        pass

    def installCondaDependencies(self):
        pass

    def initRepo(self):
        '''
        Create a datasuper repo and add the relevant
        result and sample types.

        Create a .mu directory and a <pipeline name> subdirectory
        with all appropriate file
        '''
        pass 
