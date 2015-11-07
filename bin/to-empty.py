#!/usr/bin/env python3

import i3
import sys
from utils import find_matching, workspace

# This script asumes that workspace names are numbers

DEFAULT_NAMES = set(range(1,11))

def first_free(occupied):
	free = DEFAULT_NAMES - set(occupied)
	return str(min(free)) if free else None

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("{} focus|move".format(sys.argv[0]), file=sys.stderr)
		sys.exit(1)
	first = first_free((int(w["name"]) for w in find_matching(workspace())))
	if not first:
		print("All workspaces are occupied")
		sys.exit(3)
	action = sys.argv[1]
	if action == "focus":
		i3.workspace(first)
	elif action == "move":
		i3.move("container to workspace {}".format(first))
	else:
		print("Unknown action", file=sys.stderr)
		sys.exit(2)
	
	
