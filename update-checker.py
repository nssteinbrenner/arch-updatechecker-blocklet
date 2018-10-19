#!/usr/bin/env python

from subprocess import CalledProcessError, check_output

try:
    output = check_output(['pacman', '-Qu'])
    returncode = 0
except CalledProcessError as e:
    returncode = e.returncode

if returncode == 0:
    print('')
