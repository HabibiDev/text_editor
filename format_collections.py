from abc import ABC, abstractmethod
from xlrd import open_workbook, biffh
from xlwt import Workbook
from xlutils.copy import copy


class FileObject(ABC):

    def __init__(self, file):
        self.file = file

    def check_file_data(self):
        with open(str(self.file), 'r') as read_file:
            data = read_file.readlines()
            if len(data) >= 5:
                return data
            else:
                raise Exception('In your file less then 5 line')

    @abstractmethod
    def read_text(self):
        pass

    @abstractmethod
    def write_text(self):
        pass


class FileTXT(FileObject):

    def read_text(self):
        data = self.check_file_data()
        for i in data[:5]:
            print(i, end='')

    def write_text(self):
        with open(str(self.file), 'a+') as edit_file:
            edit_file.write('Default line\n')
        return 'write'


class FileCSV(FileObject):

    def read_text(self):
        data = self.check_file_data()
        for i in data[:5]:
            print(i, end='')

    def write_text(self):
        with open(str(self.file), 'a+') as edit_file:
            edit_file.write('Default line\n')
        return 'write'


class FileXLS(FileObject):

    def check_file_data(self):
        read_file = open_workbook(str(self.file))
        data = read_file.sheet_by_index(0)
        if data.nrows >= 5:
            return data
        else:
            raise Exception('In your file less then 5 line')

    def read_text(self):
        data = self.check_file_data()
        for i in range(5):
            print(data.row_values(i))

    def write_text(self):
        try:
            rb = open_workbook(str(self.file))
            wb = copy(rb)
            rs = rb.sheet_by_index(0)
            ws = wb.get_sheet(0)
            ws.write(rs.nrows, 0, 'Default Line')
            wb.save(str(self.file))
        except biffh.XLRDError:
            rb = Workbook()
            ws = rb.add_sheet('A Test Sheet')
            ws.write(0, 0, 'Default Line')
            rb.save(str(self.file))
        return 'write'
