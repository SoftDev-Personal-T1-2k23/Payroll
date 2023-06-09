"""A class for CSV file related operations"""

class CSVData:
    """A container for CSV data"""
    def __init__(self, csv_columns:list, csv_rows:list, delimiter:str=','):
        self.columns = csv_columns
        self.rows = csv_rows
        self.delimiter = delimiter
        self.column_count = len(self.columns)
        self.row_count = len(self.rows)
    def get_columns(self) ->list:
        """Return the stored columns"""
        return self.columns

    def get_rows(self) ->list:
        """Return the stored rows"""
        return self.rows

    def get_column_index(self, column_title:str) ->int:
        """Return a column's index from a column title"""
        return self.columns.index(column_title)

    def get_row_value(self, row:list, column_title:str):
        """Get a row value, provided the row and a column title"""
        return row[self.get_column_index(column_title)]

    def set_row_value(self, row:list, column_title:str, new_value:str):
        """Get a row value, provided the row and a column title, and set its value"""
        row[self.get_column_index(column_title)] = new_value
        