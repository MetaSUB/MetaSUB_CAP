from snakemake import snakemake

class PipelineInstance:
    '''
    This is the class that handles actually running the pipeline.

    This is also used for other more basic calls (like seeing what 
    end points exist) which is why running is not automatic.

    Basically this class does a lot of setup work then calls
    snakemake
    '''
    
    def __init__(self, pipelineDef):
        self.fileTypes = util.parseFileTypes(pipelineDef['FILE_TYPES'])
        self.sampleTypes = pipelineDef['SAMPLE_TYPES']
        self.origins = pipelineDef['ORIGINS']
        self.endpoints = util.parseEndpoints(pipelineDef)
        self.resultSchema = [ResultSchema(schema) for schema in pipelineDef['RESULT_TYPES']]
        self.snakemakeConf = util.findSnakemakeConf(pipelineDef)

    def run(self,
            endpts=None, groups=None, samples=None, results=None,
            dryrun=False, unlock=False, njobs=1, local=False):
        snakefile = self.preprocessSnakemake()
        clusterScript = self.getClusterScript(local)
        confWithData = self.addEndpointsAndDataToSnakemakeConf( endpts, groups, samples, results)

        snakemake( snakefile,
                   config=,
                   cluster=clusterScript,
                   keepgoing=True,
                   printshellcmds=True,
                   dryrun=dryrun,
                   unlock=unlock,
                   force_incomplete=True,
                   nodes=njobs)

    def preprocessSnakemake(self):
        pass

    def getClusterScript(self, runLocally):
        pass

    def addEndpointsAndDataToSnakemakeConf(self, endpts, groups, samples, results):
        pass
