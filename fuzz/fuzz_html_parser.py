#!/usr/local/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    import html5lib


@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    html5lib.parse(fdp.ConsumeString(len(data)))


# atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()