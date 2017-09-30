from yaml_backed_structs import *
import os.path
import os.environ

class ModuleUltraConfig:
    '''
    This class represents the module ultra config
    directory and lots of associated operations.
    
    Typically this directory is in $HOME/.module_ultra_config
    '''
    configDirName='.module_ultra_config'
    pipelineDirName = 'installed_pipelines'
    configVarsRoot='config_variables.yml'

    def __init__(self, abspath):
        self.abspath = abspath

        varPath = os.path.join(self.abspath, ModuleUltraConfig.configVarsRoot)
        self.configVars = PersistentDict(varPath)
        
    def listInstalledPipelines(self):
        pass

    def getPipelineDefinition(self, pipelineName, version=None):
        '''
        Return the definition for the specified pipeline if installed.
        
        If the version is not specified return the highest version number'
        '''
        pass

    def clusterSubmitScript(self):
        try:
            cScript = self.configVars['CLUSTER_SUBMIT_SCRIPT']
            return cScript
        except KeyError:
            return None
        

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
