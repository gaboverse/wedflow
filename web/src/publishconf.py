import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = os.getenv("SITEURL", "")
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True