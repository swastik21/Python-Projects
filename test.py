# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
no = int(input())
for i in range(no):
	value = int(input())
	if value > 9: groups = {key: value for key in groups[i]}
	else: groups = {key: "none" for key in groups[i]}

print(groups)