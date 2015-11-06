#!/usr/bin/env python3

import i3
import sys
import subprocess
from re import match

def find_windows(pred):
	tree = i3.get_tree()
	queue = [tree]
	for w in queue:
		queue.extend(w["nodes"])
		if w["window"] and pred(w):
			yield w

def property(prop, regexp):
	return lambda w: bool(match(regexp, str(w["window_properties"][prop])))

if __name__ == "__main__":
	if len(sys.argv) < 4:
		print("{} property regexp command".format(sys.argv[0]), file=sys.stderr)
		sys.exit(1)
	_, prop, regexp, *command = sys.argv
	window = next(find_windows(property(prop, regexp)), None)
	if window:
		i3.focus(con_id=window["id"])
	else:
		subprocess.call(command)

