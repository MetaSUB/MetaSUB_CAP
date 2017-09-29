

class ModuleUltraConfig:
    default_dir_name='.module_ultra_config'
    '''
    This class represents the module ultra config
    directory and lots of associated operations.
    
    Typically this directory is in $HOME/.module_ultra_config
    '''

    def __init__(self, dirname):
        self.root = dirname

        
    def listInstalledPipelines(self):
        pass

    def clusterSubmitScript(self):
        pass

    @classmethod
    def getConfigDir(ctype):
        '''
        Return the directory where the module ultra config is
        stored
        '''
        pass

    @classmethod
    def load(ctype):
        '''
        Get the config object
        '''
        pass
