from snakemake import snakemake


class PipelineInstance:
    '''
    This is the class that handles actually running the pipeline.

    This is also used for other more basic calls (like seeing what 
    end points exist) which is why running is not automatic.

    Basically this class does a lot of setup work then calls
    snakemake
    '''
    
    def __init__(self, muRepo, pipelineName, pipelineDef):
        self.muRepo = muRepo
        self.muConfig = self.muRepo.muConfig
        self.pipelineName = pipelineName
        
        self.fileTypes = util.parseFileTypes(pipelineDef['FILE_TYPES'])
        self.sampleTypes = pipelineDef['SAMPLE_TYPES']
        self.resultSchema = []
        for schema in pipelineDef['RESULT_TYPES']:
            self.resultSchema.append( ResultSchema(muRepo, pipelineName, schema) )
        
        self.origins = pipelineDef['ORIGINS']
        self.endpoints = util.parseEndpoints(pipelineDef)

        self.snakemakeConf = self.muConfig.findSnakemakeConf(pipelineName, pipelineDef)

    def run(self,
            endpts=None, groups=None, samples=None, results=None,
            dryrun=False, unlock=False, njobs=1, local=False):
        snakefile = self.preprocessSnakemake()
        clusterScript = None
        if not local:
            clusterScript = self.muRepo.muConfig.clusterSubmitScript()
        confWithData = self.addEndpointsAndDataToSnakemakeConf( endpts, groups, samples, results)

        snakemake( snakefile,
                   config=confWithData,
                   cluster=clusterScript,
                   keepgoing=True,
                   printshellcmds=True,
                   dryrun=dryrun,
                   unlock=unlock,
                   force_incomplete=True,
                   nodes=njobs)

    def preprocessSnakemake(self):
        # add conf

        # add all rule

        # add individual results
        preprocessed = ''
        for resultSchema in self.resultSchema:
            preprocessed += resultSchema.preprocessSnakemake()
            preprocessed += '\n'
        tfile = self.muRepo.makeTempFile()
        with open(tfile, 'w') as tf:
            tf.write(preprocessed)
        return tf
        

    def listEndpoints(self):
        return self.endpoints

    def addEndpointsAndDataToSnakemakeConf(self, endpts, groups, samples, results):
        resultDir = self.muRepo.getResultDir()
        pass
