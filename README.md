[![Build Status](https://travis-ci.org/inkeye/wav_to_video.svg?branch=master)](https://travis-ci.org/inkeye/wav_to_video)
[![Coverage Status](https://coveralls.io/repos/github/inkeye/cyscore/badge.svg?branch=master)](https://coveralls.io/github/inkeye/cyscore?branch=master)

# cyscore
Score abstraction for [Csound](https://github.com/csound/csound) written in Python.

```
pip3 install cyscore
```

A score consists of voices which consist of an instrument and notes.

A note consists of a duration, an entry delay for the next note and an arbitrary number of p-fields.
