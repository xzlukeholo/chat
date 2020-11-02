def read_file(filename):
	dialogue = []
	with open(filename,'r', encoding='utf-8-sig') as f:
		for line in f:
			line = line.strip()
			dialogue.append(line)
	return dialogue

def convert(dialogue, username1, username2):
	new = []
	username = None
	for line in dialogue:
		if line == username1:
			username = username1
			continue
		elif line == username2:
			username = username2
			continue
		if username:
			new.append(username + ': ' + line)
	return new

def write_file(filename, dialogue, username1, username2):
	with open(filename,'w', encoding='utf8') as f:
		for line in dialogue:
			f.write(line + '\n')

def main():
	dialogue = read_file('input.txt')
	dialogue = convert(dialogue, 'Allen', 'Tom')
	write_file('output.txt', dialogue, 'Allen', 'Tom')

main()