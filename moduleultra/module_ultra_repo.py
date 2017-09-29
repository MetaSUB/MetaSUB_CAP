

class ModuleUltraRepo:
    '''
    Represents a directory where moduleultra pipelines are run
    '''

    def __init__(self):
        self.muConfig = ModuleUltraConfig.load()
        pass


    def addPipeline(self, pipelineDefinitionFilename):
        '''
        Add a pipeline that has already been installed
        to this repo.

        Add relevant types to the datasuper repo.
        '''
        pass

    def getPipelineInstance(self, pipelineName):
        pipelineDef =
        return PipelineInstance(self, pipelineDef)

    def listPipelines(self):
        '''
        List the names of pipelines that have been added to this repo
        '''
        pass

    def makeTempFile(self):
        '''
        Make a temporary file within the mu repo dir, 
        returns the name of that file
        '''
        pass

    def getResultDir(self):
        '''
        Get the directory where the actual result files are stored.
        '''
        pass

    def makeVirtualSampleDir(self, dname, sample):
        '''
        Create a directory named <dname> with all the results for a given sample
        '''
        pass

    def makeVirtualGroupDir(self, dname, group, flat=False):
        '''
        Create a directory named <dname> with all the results for a given groups
        
        unless flat is true make subdirectories for each sample plus a 
        'group_result' dir
        '''
        pass
    
    

    @staticmethod
    def initRepo():
        '''
        Create a datasuper repo.

        Create a .mu directory 
        '''
        pass 
