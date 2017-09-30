
def getOrDefault(schema, key, default):
    try:
        return schema[key]
    except KeyError:
        return default

def joinPipelineNameVersion( pipeName, version):
    delim = '::'
    return '{}{}{}'.format(pipeName, delim, version)

def splitPipelineNameVersion( versionedPipeName):
    delim = '::'
    return versionedPipeName.split(delim)
