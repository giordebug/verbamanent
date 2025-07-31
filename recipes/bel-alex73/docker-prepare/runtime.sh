#!/bin/bash

cd /a/tts
pip install -e .[all,dev,notebooks]

LANG=C.utf8 bash
