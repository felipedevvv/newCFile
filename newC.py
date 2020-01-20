#!/usr/bin/env python3

import subprocess
import sys

fileName = sys.argv[1]
fileName0 = fileName[:-2]

mainFunction = '#include <stdio.h> \n/* \n* \n*/ \nint main() { \n\nreturn 0; \n}'

subprocess1 = subprocess.run('cat > {}'.format(fileName), shell=True, capture_output=True, text=True,
                             input=mainFunction, check=True)

subprocess2 = subprocess.run('open {}'.format(fileName), shell=True, capture_output=True, text=True)

subprocess3 = subprocess.run('chmod +x {}'.format(fileName), shell=True, capture_output=True, text=True)

subprocess4 = subprocess.run('gcc -Wall -std=gnu99 -g -o {} {}'.format(fileName0, fileName), shell=True,
                             capture_output=True, text=True)