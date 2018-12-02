#!/usr/bin/env python3
'''
file.readlines() -> ['awe3fa8fa4aewfawijfa;fjaweawfeawawefargaefaef5awefasdfeargfasdcds2awea4afadszsdvzxefafzsdva7fasdczdvafedszv6zvczvdsf2awefafzsdccsea']
line -> 'awe3fa8fa4aewfawijfa;fjaweawfeawawefargaefaef5awefasdfeargfasdcds2awea4afadszsdvzxefafzsdva7fasdczdvafedszv6zvczvdsf2awefafzsdccsea'
d -> 'a'
'''
new_string = ""
with open('String.txt', 'r') as file:
	for line in file.readlines():
		for d in line:
			if d.isdigit():
				new_string += d

print(new_string)