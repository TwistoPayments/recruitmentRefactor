import csv


def load_data(filepath: str = "startup_funding.csv") -> tuple:
    """
    Loads data from a csv file and returns tuple of columns and rows in a list
    """
    with open(filepath, "rt") as file:
        data = csv.reader(file, delimiter=',', quotechar='"')
        rows = [row for row in data]
        return rows[0], rows[1:]


class FundingRaised:

    @staticmethod
    def where(options: dict) -> list:
        """
        Returns all occurrences matching given options
        """
        columns, csv_data = load_data()
        output = []

        if not(set(options.keys()).issubset(set(columns))):
            raise InvalidOptions

        for row in csv_data:
            options_match = []
            for key, value in options.items():
                if row[columns.index(key)] == value:
                    options_match.append(True)
                else:
                    options_match.append(False)
            if all(match for match in options_match):
                output.append({row_name: row_data for (row_name, row_data) in zip(columns, row)})

        return output

    @staticmethod
    def find_by(options: dict) -> dict:
        """
        Returns first occurrence matching given options
        """
        columns, csv_data = load_data()

        for row in csv_data:
            options_match = []
            for key, value in options.items():
                if row[columns.index(key)] == value:
                    options_match.append(True)
                else:
                    options_match.append(False)
            if all(match for match in options_match):
                return {row_name: row_data for (row_name, row_data) in zip(columns, row)}

        raise RecordNotFound


class RecordNotFound(Exception):
    print("Record not found")


class InvalidOptions(Exception):
    print("Invalid options")

