#!/usr/bin/env python

import os
import sys
import subprocess


def run(args):
    runsolver = os.path.join(os.path.dirname(__file__), "runsolver", "runsolver")
    return subprocess.call([runsolver, *args])


if __name__ == "__main__":
    exit(run(sys.argv[1:]))
