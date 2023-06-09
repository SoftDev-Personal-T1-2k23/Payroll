"""A script housing a static class for CSV field validation"""
import re

VALIDATION_REGEX = {
    "ID": r"^\d+",
    "Name": r"^([a-zA-Z]+\s([a-zA-Z]+\.*\s)*[a-zA-Z]+)",
    "FirstName": r"(^[a-zA-Z]+$)",
    "LastName": r"(^[a-zA-Z]+$)",
    # "Address": r"^\d+\s([a-zA-Z]\s)+",
    "Address": r".*",
    "City": r"^\D+",
    "State": r"^[A-Z]{2}",
    "Zip": r"^\d+",
    "ClassificationId": r"^\d",
    "PayMethod": r"^\d",
    "Salary": r".*",
    "Hourly": r"^\d+\.\d+",
    "Commission": r".*",
    "Route": r"^\d+\-[0-9K]",
    "Account": r"^\d{6}\-\d{4}",
    #Password skipped
    "StartDate": r"^\d{1,2}\/\d{1,2}\/(\d{4}|\d{2})",
    "Privilege": r"^(administrator|employee)",
    "Department": r"^.*\w.*",
    "Email": r"^(\w|\.)+@(\w|\.)+\.\w+",
    "Phone": r"^\d{3}\-\d{3}\-\d{4}",
    "JobTitle": r"^.*\w.*",
    "IsArchived": r"^\d",
    "SSN": r"^\d{3}-\d{2}-\d{4}",
    "TerminationDate": r"^\d{1,2}\/\d{1,2}\/(\d{4}|\d{2})",
    "ArchivalDate": r"^\d{1,2}\/\d{1,2}\/(\d{4}|\d{2})",
}
VALIDATION_ERROR_LOOKUP = {
    "only_digits": "%s may only include numbers.",
    "no_digits": "%s must not include numbers",
    "one_digit": "%s must include a single digit.",
    "at_least_single_char": "%s must include at least one letter or number.",
    "date": "%s must use digits and backslashes. Year must be 2 or 4 digits. Format: 00/00/00",
}
VERR = VALIDATION_ERROR_LOOKUP
VALIDATION_ERROR_MESSAGE = {
    "ID": VERR["only_digits"],
    "Name": "%s must contain both the first and last name.",
    "FirstName": "%s must contain only letters",
    "LastName": "%s must contain only letters",
    "Address": "%s format: '0000 Street Name'",
    "City": VERR["no_digits"],
    "State": "%s must be composed of two capital letters.",
    "Zip": "%s code must only contain numbers.",
    "ClassificationId": VERR["one_digit"],
    "PayMethod": VERR["one_digit"],
    "Salary": VERR["only_digits"],
    "Hourly": VERR["only_digits"],
    "Commission": VERR["only_digits"],
    "Route": "%s number must end with a dash followed by a digit or 'K'",
    "Account": "%s format: ######-####",
    #Password skipped
    "StartDate": "%s format: ##/##/####",
    "Privilege": "%s must be 'employee' or 'administrator'.",
    "Department": VERR["at_least_single_char"],
    "Email": "%s format: valid@domain.com",
    "Phone": "%s format: 000-000-0000",
    "JobTitle": VERR["at_least_single_char"],
    "IsArchived": VERR["one_digit"],
    "SSN": "%s must be of the format: 000-00-0000",
    "TerminationDate": VERR["date"],
    "ArchivalDate": VERR["date"],
}

class Validation():

    @staticmethod
    def validate_field(field_title, field_value) -> bool:
        """Validate a field, given its title and value
        
            Params:
                field_title: The field title
                field_value: The field value
            Returns:
                validation_result: success: True, failure: validation_error
        """
        # Get field regex
        regex = VALIDATION_REGEX[field_title]
        if not regex:
            print(f"Failed to find validation regex for field [{field_title}]")
            return
        # Cast field value & strip external whitespace
        val = str(field_value).strip()
        # Attempt to match regex pattern & return result
        match = re.fullmatch(regex, val)
        validation_success = match is not None
        if validation_success:
            return True
        else:
            return VALIDATION_ERROR_MESSAGE[field_title] % field_title


if __name__ == "__main__":
    s = Validation.validate_field("ID", "3faef")
    print(s)
