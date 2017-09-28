

def getOrDefault(schema, key, default):
    try:
        return schema[key]
    except KeyError:
        return default

class ResultSchema:

    def __init__(self,  schema):
        self.name = schema['NAME']
        self.dependencies = getOrDefault( schema, 'DEPENDENCIES', [])
        self.module = getOrDefault( schema, 'MODULE', self.name)
        self.level = getOrDefault( schema, 'LEVEL', 'SAMPLE')
        self.files = {}
        files = schema['FILES']
        if type(files) == []:
            self.files = { str(i) : f for i, f in enumerate(files)}
        else:
            self.files = files    
