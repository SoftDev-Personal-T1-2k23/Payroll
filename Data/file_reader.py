"""Read file data, process, and return the results"""
from Data.csv_data import CSVData

class FileReader():
    """A class for reading text content from various files"""
    @staticmethod
    def read_csv(file_path:str, delimiter:str=",", row_value_types:list=None):
        """Read and return all content in a csv file

            Params:
                file_path: The CSV file path
                delimiter: The CSV delimiter
                row_value_types: The types to cast CSV values into
            Returns:
                csv_data: Returns a CSVData object
        """
        assert(file_path is str)
        assert(delimiter is str)
        assert(row_value_types is list)

        # Read CSV content
        csv_columns = None
        csv_rows = []
        try:
            with open(file_path, mode='r', encoding="UTF-8") as file:
                # Get CSV columns
                csv_columns = [v.strip() for v in file.readline().split(delimiter)]
                # Gather and organize CSV data
                for row in file:
                    csv_row = [v.strip() for v in row.split(delimiter)]
                    if row_value_types:
                        csv_row = FileReader.cast_list_values(csv_row, row_value_types)
                    csv_rows.append(csv_row)
        except FileNotFoundError:
            print(f"Failed to read CSV file [{file_path}]")

        if csv_columns is None:
            print(f"Failed to find CSV content [{file_path}]")
        return CSVData(csv_columns, csv_rows)
    @staticmethod #Should probably belong in a different file
    def cast_list_values(values:list, value_types:list):
        """Casts a list of values based upon a list of types
        
            Params:
                values: The list to cast
                value_types: The types to cast the values into
            Returns:
                casted_values: A list of casted values
        """
        assert(values is list)
        assert(value_types is list)

        val_count = len(values)
        val_type_count = len(value_types)
        if val_type_count < val_count:
            print(f"Failed cast; value_types only has [{val_type_count}] elements")
            return None

        for (i, _) in enumerate(values):
            try:
                values[i] = value_types[i](values[i])
            except ValueError:
                values[i] = None
                print(f"Failed to cast value [{i}:{values[i]}] into type [{value_types[i]}]")
        return values
