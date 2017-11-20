# cyscore

[![PyPI version](https://badge.fury.io/py/cyscore.svg)](https://badge.fury.io/py/cyscore)
[![Build Status](https://travis-ci.org/inkeye/cyscore.svg?branch=master)](https://travis-ci.org/inkeye/cyscore)
[![Coverage Status](https://coveralls.io/repos/github/inkeye/cyscore/badge.svg?branch=master)](https://coveralls.io/github/inkeye/cyscore?branch=master)

Score abstraction for [Csound](https://github.com/csound/csound) written in Python.

```
pip3 install cyscore
```

A score consists of voices which consist of an instrument and notes.

A note consists of a duration, an entry delay for the next note and an arbitrary number of p-fields.
