import os
import argparse
from format_collections import *


class TextEditor:
	def __init__(self, input_action, input_file_path):
		self.action = input_action
		self.file = input_file_path
		self.file_format = os.path.splitext(input_file_path)[-1]
		self.data = None
		self.formats = {
						'.txt': FileTXT,
						'.csv': FileCSV,
						'.xls': FileXLS
						}
		try:
			self.actions = {
							'r': self.formats[self.file_format](self.file).read_text,
							'w': self.formats[self.file_format](self.file).write_text
							}
		except KeyError:
			raise KeyError('You must input full path of your file')

	def check_action(self):
		if str(self.action) not in self.actions.keys():
			raise ValueError('wrong input, you must choose "r" or "w"')

	def check_file(self):
		if self.file_format not in self.formats.keys():
			raise ValueError('wrong file, you must input file in formats ".txt" or ".csv"')
		if not os.path.exists(self.file):
			raise FileNotFoundError('No such file {} or wrong input filepath'.format(self.file))

	def check_input(self):
		if not self.action:
			raise AttributeError('You must choose, what do you want to do: r - read or w - write')

	def edit_or_read(self):
		self.check_input()
		self.check_action()
		self.check_file()
		return self.actions[self.action]()


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("r", help='r - read first five line in file', type=str, default='r')
	parser.add_argument("w", help='w - write new line at the end', type=str, default='w')
	parser.add_argument("f", help='full path to your file', type=str)
	args = parser.parse_args()
	TextEditor(args.r, args.f).edit_or_read()
