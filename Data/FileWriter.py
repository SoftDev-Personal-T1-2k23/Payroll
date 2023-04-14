"""A class for writing data to files"""
from Data.CSVData import CSVData

class FileWriter():
    
    @staticmethod
    def write_csv(file_path:str, csv_data:CSVData):
        """Write all CSVData to a file

            Params:
                file_path: The CSV file path
                csv_data: The CSV data to write
            Returns:
                success: Whether the data was successfully written
        """
        #TODO: Avoid overriding unchanged information
        # I suggest adjusting the CSVData class to keep track of changes
        try:
            with open(file_path, mode='w') as f:
                # Write header
                csv_header = csv_data.delimiter.join(csv_data.columns) +"\n"
                f.write(csv_header)
                # Write data
                for row in csv_data.rows:
                    csv_row = csv_data.delimiter.join([str(v) for v in row]) +"\n"
                    f.write(csv_row)
        except:
            RuntimeError(f"Failed to write to CSV file [{file_path}]")
        return True