import i3
from re import match

def find_matching(pred, tree=None):
	tree = tree or i3.get_tree()
	queue = [tree]
	for w in queue:
		queue.extend(w["nodes"])
		if pred(w):
			yield w

def property(prop, regexp):
	return combine(window, lambda w: match(regexp, str(w["window_properties"][prop])))

def workspace(hide_internal=True):
	return lambda w: w["type"] == "workspace" and \
		(not w["name"].startswith("__") if hide_internal else True)

def window(w):
	return bool(w["window"])

def combine(*fns):
	return lambda w: all(fn(w) for fn in fns)

def focused_tree():
	focused = next(w for w in i3.get_workspaces() if w["focused"])
	return next(find_matching(combine(workspace(), lambda w: w["num"] == focused["num"])))

def focused_window():
	return next(find_matching(combine(window, lambda w: w["focused"])))
