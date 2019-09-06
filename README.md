## Flatjson

Flatten json.

## Installation

`pip install flatjson`

## Usage

```python
import flatjson

data = {
    "list":[{"a":1},{"b":True}],
    "dict":{"c":1.1,"d":{"e":"string"}}
}
flatjson.dumps(data)

# {'list[0].a': 1, 'list[1].b': True, 'dict.c': 1.1, 'dict.d.e': 'string'}
```
