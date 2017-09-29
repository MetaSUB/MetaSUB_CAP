
def getOrDefault(schema, key, default):
    try:
        return schema[key]
    except KeyError:
        return default

