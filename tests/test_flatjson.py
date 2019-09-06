from flatjson import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_flatjson():
    data = {
        "list":[{"a":1},{"b":True}],
        "dict":{"c":1.1,"d":{"e":"string"}}
    }
    assert dumps(data) == {'list[0].a': 1, 'list[1].b': True, 'dict.c': 1.1, 'dict.d.e': 'string'}