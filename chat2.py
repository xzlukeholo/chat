def read_file(filename):
	dialogue = []
	with open(filename,'r', encoding='utf-8-sig') as f:
		for line in f:
			line = line.strip()
			dialogue.append(line)
	return dialogue


def convert(dialogue):
	username = None
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for line in dialogue:
		s = line.split()
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if  s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		if name == 'Viki':
			if  s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('Allen說了', allen_word_count, '個字')
	print('Allen用了:', allen_sticker_count, '張貼圖')
	print('Allen用了:', allen_image_count, '張圖片')
	print('Viki說了', viki_word_count, '個字')	
	print('Viki用了', viki_sticker_count, '張貼圖')
	print('Viki用了', viki_image_count, '張圖片')



def write_file(filename, dialogue, username1, username2):
	with open(filename,'w', encoding='utf8') as f:
		for line in dialogue:
			f.write(line + '\n')


def main():
	dialogue = read_file('LINE-Viki.txt')
	dialogue = convert(dialogue)
	# write_file('output.txt', dialogue, 'Allen', 'Tom')

main()