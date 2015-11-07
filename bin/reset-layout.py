#!/usr/bin/env python3

import i3
from utils import find_matching, window, focused_tree, focused_window
from uuid import uuid4 as uuid

if __name__ == "__main__":
	mark = str(uuid())
	workspace = focused_tree()
	focused = focused_window()
	i3.focus(con_id=workspace["id"])
	i3.mark(mark)
	windows = find_matching(window, workspace)
	for w in windows:
		i3.focus(con_id=w["id"])
		i3.move("window to mark {}".format(mark))
	i3.focus(con_id=workspace["id"])
	i3.unmark(mark)
	i3.focus(con_id=focused["id"])
