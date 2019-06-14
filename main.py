import os


class TextEditor:
	def __init__(self, input_action, input_file_path):
		self.action = input_action
		self.file = input_file_path
		self.data = None
		self.actions = ['r', 'w']
		self.formats = ['txt', 'csv']
	
	def check_action(self):
		if str(self.action) not in self.actions:
			raise ValueError('wrong input, you must choose "r" or "w"')

	def check_file(self):
		if str(self.file)[-3:] not in self.formats:
			raise ValueError('wrong file, you must input file in formats ".txt" or ".csv"')
		if not os.path.exists(self.file):
			raise FileNotFoundError('No such file {} or wrong input filepath'.format(self.file))

	def check_file_data(self):
		with open(str(self.file), 'r') as read_file:
			self.data = read_file.readlines()
			if len(self.data) >= 5:
				return self.data
			else:
				raise Exception('In your file less then 5 line')

	def read_text(self):
		self.check_file_data()
		for i in self.data[:5]:
			print(i, end='')

	def write_text(self):
		with open(str(self.file), 'a+') as edit_file:
			edit_file.write('Default line\n')
		return 'write'

	def check_input(self):
		if not self.action:
			raise AttributeError('You must choose, what do you want to do: r - read or w - write')
		if not self.file:
			raise AttributeError('You must input full path of your file')

	def edit_or_read(self):
		self.check_input()
		self.check_action()
		self.check_file()
		if self.action == 'r':
			return self.read_text()
		else:
			return self.write_text()


if __name__ == '__main__':
	action = input('please input what you want to do(r - read, w - write): ')
	file = input('please write full path to your file(it\'s must be .txt or .csv): ')
	TextEditor(action, file).edit_or_read()
