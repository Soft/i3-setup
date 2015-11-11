#!/usr/bin/env python3

import i3

scratch = i3.filter(name="__i3_scratch")[0]

if scratch["floating_nodes"]:
	i3.scratchpad("show")
else:
	i3.move("scratchpad")

