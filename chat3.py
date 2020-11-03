
dialogue = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		dialogue.append(line.strip())

for line in dialogue:
	s = line.split()
	time = s[0][:5]
	name = s[0][5:]
	print('取出時間:', time)
	print('取出名子:', name)