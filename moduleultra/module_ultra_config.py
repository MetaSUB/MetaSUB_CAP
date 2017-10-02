from yaml_backed_structs import *
import os.path
import os.environ
from json import loads as jloads

class ModuleUltraConfig:
    '''
    This class represents the module ultra config
    directory and lots of associated operations.
    
    Typically this directory is in $HOME/.module_ultra_config
    '''
    configDirName='.module_ultra_config'
    pipelineDirName = 'installed_pipelines'
    pipelineSetName = 'installed_pipelines.yml'    
    configVarsRoot='config_variables.yml'

    def __init__(self, abspath):
        self.abspath = abspath

        varPath = os.path.join(self.abspath, ModuleUltraConfig.configVarsRoot)
        self.configVars = PersistentDict(varPath)

        pipePath = os.path.join(self.abspath, ModuleUltraConfig.pipelineSetName)
        self.installedPipes = PersistentDict(pipePath)
        
        
    def listInstalledPipelines(self):
        return {k:v for k,v in self.installedPipes.items()}

    def getPipelineDefinition(self, pipelineName, version=None):
        '''
        Return the definition for the specified pipeline if installed.
        
        If the version is not specified return the highest version number'
        '''        
        if version is None:
            version = getHighestVersion( self.installedPipes[pipelineName])
            
        pipeName = joinPipelineNameAndVersion(pipelineName, version)
        pipeDef = os.path.join( self.getInstalledPipelinesDir(), pipeName)
        pipeDef = os.path.join(pipeDef, 'pipeline_definition.json')
        pipeDef = jloads(pipeDef)
        return pipeDef

    def clusterSubmitScript(self):
        try:
            cScript = self.configVars['CLUSTER_SUBMIT_SCRIPT']
            return cScript
        except KeyError:
            return None
        
    def getInstalledPipelinesDir(self):
        return os.path.join(self.abspath, ModuleUltraConfig.pipelineDirName)

    def installPipeline(self, uri):
        installer = PipelineInstaller(self, uri)
        installer.install()
    
    @classmethod
    def getConfigDir(ctype):
        '''
        Return the directory where the module ultra config is
        stored
        '''
        try:
            configRoot = os.environ['MODULE_ULTRA_CONFIG']
        except KeyError:
            configRoot = ModuleUltraConfig.configDirName
        return os.path.abspath( configRoot)
            
    @classmethod
    def load(ctype):
        '''
        Get the config object
        '''
        return ModuleUltraConfig( ctype.getConfigDir())

    @classmethod
    def initConfig(ctype, dest=None):
        os.mkdir(ctype.getConfigDir())
