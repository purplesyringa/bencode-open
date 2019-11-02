# bencode

`bencode-open` is an open-source MIT-licensed library for parsing and converting
objects to and from [Bencode format](https://en.wikipedia.org/wiki/Bencode).


## Rationale

`bencode-open` is MIT-licensed and can thus be included to almost all software,
compared to `bencode` and `bencode.py`.


## Installation

`bencode-open` is available on [GitHub](https://github.com/imachug/bencode-open)
and on [PyPI](https://pypi.org/project/bencode-open/).

Installing `bencode-open` from PyPI is recommended and can be done as follows:

```
pip install bencode-open
```


## Usage

```python
import bencode_open

print(bencode_open.dumps(b"Hello?"))  # Outputs b"6:Hello?"
print(bencode_open.dumps(17))  # Outputs b"i17e"

print(bencode_open.loads(b"6:Hello?"))  # Outputs b"Hello?"
print(bencode_open.loads(b"i17e"))  # Outputs 17
```


## Running tests

```
python test.py
```
