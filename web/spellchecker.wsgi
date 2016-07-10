#!/usr/bin/python
import sys
import logging
import os
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, os.path.realpath(os.path.dirname(__file__)))

from spellcheckerweb import app as application
