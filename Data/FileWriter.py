"""A class for writing data to files"""
from Data.csv_data import CSVData
from datetime import datetime

class FileWriter():
    
    @staticmethod
    def write_csv(file_path:str, csv_data:CSVData):
        """Write all CSV data to a file

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
            print(f"Failed to write to CSV file [{file_path}]")
        return True
    
    @staticmethod
    def write_pay_report(file_path:str, employees):
        """Write to the pay report what has been paid to employees
        
            Params:
                file_path: The CSV file path
                employees: A list of employees to log reports for
            Returns:
                success: Whether the data was successfully written
        """
        try:
            todays_date = datetime.today().strftime("%m/%d/%Y")
            with open(file_path, mode='w') as f:
                for emp in employees:
                    _, pay_msg = emp.issue_payment()
                    print(f"{todays_date} | {pay_msg}", file=f,)
        except:
            print(f"Failed to write pay report at [{file_path}]")
        return True