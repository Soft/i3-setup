#!/usr/bin/env python3

import i3

# Unfortunatelly this doesn't seem to be reliable

outputs = sorted((out for out in i3.get_outputs() if out["active"]), key=lambda o: o["rect"]["x"])
outputs.append(outputs[0])

for left, right in zip(outputs, outputs[1:]):
	i3.workspace(left["current_workspace"])
	i3.move("workspace to output {}".format(right["name"]))
	
