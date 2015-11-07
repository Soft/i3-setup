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
	return lambda w: w["window"] and match(regexp, str(w["window_properties"][prop]))

def workspace(hide_internal=True):
	return lambda w: w["type"] == "workspace" and \
		(not w["name"].startswith("__") if hide_internal else True)

