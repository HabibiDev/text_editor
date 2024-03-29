import unittest
from unittest import mock
from main import TextEditor
from format_collections import *
import os
import io


class TextEditorTestCase(unittest.TestCase):

    def setUp(self):
        with open('test_file_success_read.txt', 'a+') as success_file:
            for i in range(6):
                success_file.write('line number {}\n'.format(i))
        with open('test_file_another_format.csv', 'a+') as success_file:
            for i in range(6):
                success_file.write('line number {}\n'.format(i))
        with open('test_file_failed_read.txt', 'a+') as success_file:
            for i in range(4):
                success_file.write('line number{}'.format(i))
        with open('test_file_failed_format.doc', 'a+') as success_file:
            for i in range(5):
                success_file.write('line number{}'.format(i))
        with open('test_file_success_read.xls', 'a+') as success_file:
            pass
        self.action_read = 'line number 0\nline number 1\nline number 2\nline number 3\nline number 4\n'

    def tearDown(self):
        os.remove("test_file_success_read.txt")
        os.remove("test_file_another_format.csv")
        os.remove("test_file_failed_read.txt")
        os.remove("test_file_success_read.xls")
        os.remove("test_file_failed_format.doc")

    def test_action_read_success(self):
        editor = TextEditor('r', 'test_file_success_read.txt')
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            editor.edit_or_read()
        self.assertMultiLineEqual(fake_stdout.getvalue(), self.action_read)

    def test_action_write_success(self):
        editor = TextEditor('w', 'test_file_success_read.txt')
        self.assertEqual(editor.edit_or_read(), 'write')

    def test_check_input_action_failed(self):
        editor = TextEditor('', 'test_file_success_read.txt')
        with self.assertRaises(AttributeError):
            editor.edit_or_read()

    def test_check_input_file_failed(self):
        with self.assertRaises(KeyError):
            TextEditor('r', '')

    def test_check_action_failed(self):
        editor = TextEditor('g', 'test_file_success_read.txt')
        with self.assertRaises(ValueError):
            editor.edit_or_read()

    def test_check_action_success(self):
        editor = TextEditor('w', 'test_file_success_read.txt')
        self.assertIsNone(editor.check_action())
        editor = TextEditor('r', 'test_file_success_read.txt')
        self.assertIsNone(editor.check_action())

    def test_check_file_failed_wrong_format(self):
        with self.assertRaises(KeyError):
            TextEditor('w', 'test_file_success_read.doc')

    def test_check_file_success(self):
        editor = TextEditor('w', 'test_file_success_read.txt')
        self.assertIsNone(editor.check_file())
        editor = TextEditor('r', 'test_file_another_format.csv')
        self.assertIsNone(editor.check_file())

    def test_check_file_failed_wrong_path(self):
        editor = TextEditor('w', 'test_file_success_reads.txt')
        with self.assertRaises(FileNotFoundError):
            editor.check_file()

    def test_check_file_data_success(self):
        editor = FileTXT('test_file_success_read.txt')
        self.assertGreaterEqual(len(editor.check_file_data()), 5)

    def test_check_file_data_failed(self):
        editor = FileTXT('test_file_failed_read.txt')
        with self.assertRaises(Exception):
            editor.check_file_data()

    def test_check_file_data_xls(self):
        editor = FileXLS("test_file_success_read.xls")
        with self.assertRaises(Exception):
            editor.check_file_data()

    def test_write_text_xls(self):
        editor = FileXLS("test_file_success_read.xls")
        self.assertEqual(editor.write_text(), 'write')