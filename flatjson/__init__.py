__version__ = '0.1.1'

def dumps(data):
    r = {}
    def parse(data, parent=None):
        if isinstance(data, dict):
            for k,v in data.items():
                name = f"{parent}.{k}" if parent else k
                value = v
                parse(value,name)
        elif isinstance(data, list):
            for index,item in enumerate(data):
                name = f"{parent}[{index}]" if parent else f"[{index}]"
                value = item
                parse(value, name)
        else:
            r.update({parent: data})
    parse(data)
    return r