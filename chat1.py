def read_file(filename, username1, username2):
	dialogue = []
	with open(filename,'r', encoding='utf-8-sig') as f:
		for line in f:
			line = line.strip()
			if line == username1:
				username = username1
				continue
			elif line == username2:
				username = username2
				continue
			dialogue.append(username + ':' + line)
	return dialogue


def write_file(filename, dialogue, username1, username2):
	with open(filename,'w', encoding='utf8') as f:
		for line in dialogue:
			f.write(line + '\n')

print(read_file('input.txt', 'Allen', 'Tom'))

def main():
	dialogue = read_file('input.txt', 'Allen', 'Tom')
	write_file('output.txt', dialogue, 'Allen', 'Tom')

main()