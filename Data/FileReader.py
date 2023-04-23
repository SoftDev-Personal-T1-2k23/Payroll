"""Read file data, process, and return the results"""
from Data.CSVData import CSVData

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
        # Read CSV content
        csv_columns = None
        csv_rows = []
        try:
            with open(file_path, mode='r') as f:
                # Get CSV columns
                csv_columns = [v.strip() for v in f.readline().split(delimiter)]
                # Gather and organize CSV data
                for row in f:
                    csv_row = [v.strip() for v in row.split(delimiter)]
                    if row_value_types:
                        csv_row = FileReader.cast_list_values(csv_row)
                    csv_rows.append(csv_row)
        except:
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
        val_count = len(values)
        val_type_count = len(value_types)
        if val_type_count < val_count: RuntimeError(f"Failed to cast values; value_types only contains only [{val_type_count}] elements")

        for i in range(len(values)):
            try:
                values[i] = value_types[i](values[i])
            except:
                values[i] = None
                print(f"Failed to cast value [{i}:{values[i]}] into type [{value_types[i]}]")
        return values

    
