"""A script housing a static class for CSV field validation"""
import re

VALIDATION_REGEX = {
    "ID": r"^\d+",
    "Name": r"^([a-zA-Z]+\s([a-zA-Z]+\.*\s)*[a-zA-Z]+)",
    "Address": r"^\d+\s([a-zA-Z]\s)+",
    "City": r"^\D+",
    "State": r"^[A-Z]{2}",
    "Zip": r"^\d+",
    "ClassificationId": r"^\d",
    "PayMethod": r"^\d",
    "Salary": r"^\d+\.\d+",
    "Hourly": r"^\d+\.\d+",
    "Commission": r"^\d+\.\d+",
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
}
VALIDATION_ERROR_LOOKUP = {
    "only_digits": "%s may only include numbers.",
    "no_digits": "%s must not include numbers",
    "one_digit": "%s must include a single digit.",
    "at_least_single_char": "%s must include at least one letter or number.",
}
VERR = VALIDATION_ERROR_LOOKUP
VALIDATION_ERROR_MESSAGE = {
    "ID": VERR["only_digits"],
    "Name": "%s must contain both the first and last name.",
    "Address": "%s must be of the format: '0000 Street Name'",
    "City": VERR["no_digits"],
    "State": "%s must be composed of two capital letters.",
    "Zip": "%s code must only contain numbers.",
    "ClassificationId": VERR["one_digit"],
    "PayMethod": VERR["one_digit"],
    "Salary": VERR["only_digits"],
    "Hourly": VERR["only_digits"],
    "Commission": VERR["only_digits"],
    "Route": "%s number must end with a dash followed by a digit or 'K'",
    "Account": "%s number must be 6 digits followed by a dash and 4 digits.",
    #Password skipped
    "StartDate": "%s must use digits and backslashes. Year must be 2 or 4 digits.",
    "Privilege": "%s must be 'employee' or 'administrator'.",
    "Department": VERR["at_least_single_char"],
    "Email": "%s must of of the format: valid@domain.com",
    "Phone": "%s number must be of the format: 000-000-0000",
    "JobTitle": VERR["at_least_single_char"],
    "IsArchived": VERR["one_digit"]
}

class Validation():

    @staticmethod
    def validate_field(field_title, field_value) -> bool:
        """Validate a field, given its title and value
        
            Params:
                field_title: The field title
                field_value: The field value
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
        return validation_success


if __name__ == "__main__":
    s = Validation.validate_field("ID", "3faef")
    print(s)
