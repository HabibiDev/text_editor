def read_text(file=None):
	if file:
		with open(str(file), 'r') as read_file:
			data = read_file.readlines()
			for i in data[:5]:
				print(i) 

def write_text(file=None):
	if file:
		with open(str(file), 'a+') as edit_file:
			edit_file.write('\nDefault line')

if __name__ == '__main__':
	actions = {'r': read_text, 'w': write_text}
	formats = ['txt', 'csv']
	while True:
		action = input('please input what you want to do(r - read, w - write): ')
		if action not in actions.keys():
			print('wrong input, please try again')
		else:
			break
	while True:
		file = input('please write full path to your file(it\'s must be .txt or .csv): ')
		if file[-3:] not in formats:
			print('wrong input file format, please try again')
		else:
			break		
	actions[action](file)

	