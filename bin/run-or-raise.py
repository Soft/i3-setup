#!/usr/bin/env python3

import i3
import sys
import subprocess
from utils import find_matching, property

if __name__ == "__main__":
	if len(sys.argv) < 4:
		print("{} property regexp command".format(sys.argv[0]), file=sys.stderr)
		sys.exit(1)
	_, prop, regexp, *command = sys.argv
	window = next(find_matching(property(prop, regexp)), None)
	if window:
		i3.focus(con_id=window["id"])
	else:
		subprocess.call(command)

