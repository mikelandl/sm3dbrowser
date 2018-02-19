from openpyxl import Workbook

class Excel():

    """Class to work with Excel files"""

    def __init__(self, filename, worksheetTitle):
        self.filename = filename
        self.workbook = Workbook()

        # one worksheet is created by default so add it to dictionary of
        # worksheets and assign its title
        self.worksheets = {worksheetTitle: self.workbook.active}
        self.worksheets[worksheetTitle].title = worksheetTitle


    def writeFile(self):
        self.workbook.save(filename=self.filename)

    def addWorksheet(self, worksheetTitle):
        self.worksheets[worksheetTitle] = self.workbook.create_sheet(worksheetTitle)


    def writeRows(self, worksheet, startRow, startColumn, data):
        """Write a 2-dimensional list of 'data' to a given worksheet,"""
        """starting at a given row and column"""

        ws = self.workbook[worksheet]

        for rowIndex, row in enumerate(data):
            for columnIndex, column in enumerate(row):
                ws.cell(row=startRow + rowIndex, column=startColumn + columnIndex).value = column
