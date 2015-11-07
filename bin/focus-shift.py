#!/usr/bin/env python3

import i3
import sys
from utils import find_matching, workspace

def focused_workspace():
	return next((w for w in i3.get_workspaces() if w["focused"]), None)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("{} forward|backward".format(sys.argv[0]), file=sys.stderr)
		sys.exit(1)
	action = sys.argv[1]
	focused = focused_workspace()
	tree = next((w for w in find_matching(workspace()) if w["num"] == focused["num"]), None)
	windows = sorted([w for w in find_matching(lambda w: w["window"], tree)], key=lambda w: w["window"])
	index = next(i for i, w in enumerate(windows) if w["focused"])
	if action == "forward":
		i3.focus(con_id=windows[(index + 1) % len(windows)]["id"])
	elif action == "backward":
		i3.focus(con_id=windows[(index - 1) % len(windows)]["id"])
	else:
		print("Unknown action", file=sys.stderr)
		sys.exit(1)

