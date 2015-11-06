#!/usr/bin/env python3

import i3

for output in [out for out in i3.get_outputs() if out["active"]]:
	i3.workspace(output['current_workspace'])
	i3.command('move', 'workspace to output right')
	
