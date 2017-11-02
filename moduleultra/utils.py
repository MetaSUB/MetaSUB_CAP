
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


def getHighestVersion(rawNums, cur=0, raw=True):
    if len(rawNums) == 1:
        return rawNums[0]
    if raw:
        nums = []
        for rawNum in nums:
            nums.append( [int(el) for el in rawNum.split('.')])
    else:
        nums = rawNums
        
    nums = sorted( [int(el) for el in nums], reverse=True, key=lambda x: x[cur])

    if nums[0] > nums[1]:    
        return '.'.join(nums[0])
    
    i = 1
    while nums[i][cur] == nums[0][cur]:
        i += 1
                
    return getHighestVersion(nums[:i], cur=cur+1, raw=False)
