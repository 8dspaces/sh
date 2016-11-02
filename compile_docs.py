#!/usr/bin/env python

import sh
from os.path import abspath, join, dirname 
import logging
import sys


THIS_DIR = dirname(abspath(__file__))
DOCS_DIR = join(THIS_DIR, "_docs_sources")


if __name__ == "__main__":
    version_file = join(DOCS_DIR, "sh_version")

    try:
        sh_version = sys.argv[1]
    except IndexError:
        pass
    else:
        with open(version_file, "r+") as version_h:
            version_h.write(sh_version)

    logging.basicConfig(level=logging.INFO)
    logging.getLogger("sh").setLevel(logging.ERROR)
    
    logging.info("compiling docs with sphinx")
    print sh.make("html", _cwd=DOCS_DIR, _err_to_out=True)
    
    logging.info("cleaning up cruft")
    sh.rm(join(THIS_DIR, "objects.inv"))
    sh.rm(join(THIS_DIR, "doctrees"), "-rf")
