from shutil import copytree
from subprocess import call
import os .path

class PipelineInstaller:
    '''
    Installs a pipeline
    '''

    stagingDir = 'staging'

    def __init__(self, muConfig, uri):
        self.uri = uri
        self.muConfig = muConfig


    def install(self):
        staged = self.stagePipeline()
        pipeDef = self.provisionallyLoadPipeline(staged)
        self.loadPipelineFilesIntoConfig(staged, pipeDef)
        self.installPyPiDependencies(pipeDef)
        self.installCondaDependencies(pipeDef)
        self.addPipelineToManifest(pipeDef)

    
        
    def stagePipeline(self):
        if os.path.exists(self.uri):
            return self.stageFromLocal()
        elif 'git' in self.uri:
            return self.stageFromGithub()
            
            
    def stageFromLocal(self):
        dest = self.muConfig.getInstalledPipelinesDir()
        dest = os.path.join( dest, PipelineInstaller.stagingDir)
        copytree(self.uri, dest)
        return os.path.join(dest)

    def stageFromGithub(self):
        dest = self.muConfig.getInstalledPipelinesDir()
        dest = os.path.join( dest, PipelineInstaller.stagingDir)
        cmd = 'git clone {} {}'.format(self.uri, dest)
        call(cmd, shell=True)
        return os.path.join(dest)

    def provisionallyLoadPipeline(self, staged):
        pipeDef = os.path.join(pipeDef, 'pipeline_definition.json')
        pipeDef = jloads(pipeDef)
        return pipeDef
        
    def loadPipelineFilesIntoConfig(self, staged, pipeDef):
        pipeDir = joinPipelineNameAndVersion(pipeDef['NAME'], pipeDef['VERSION'])
        dest = self.muConfig.getInstalledPipelinesDir()
        pipeDir = os.path.join( dest, pipeDir)
        copytree(staged, dest)
        
    
    def installPyPiDependencies(self):
        pass

    def installCondaDependencies(self):
        pass

    def addPipelineToManifest(self, pipeDef):
        if pipeDef['NAME'] in self.muConfig.installedPipes:
            if pipe['VERSION'] in self.muConfig.installedPipes['NAME']:
                raise PipelineAlreadyInstalledException()
            self.muConfig.installedPipes['NAME'] += [pipeDef['VERSION']]
        else:
            self.muConfig.installedPipes['NAME'] = [pipeDef['VERSION']]
