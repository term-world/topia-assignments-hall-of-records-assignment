import json
import narrator

from rich.table import Table
from rich.console import Console
from inventory import FixtureSpec

# Do not alter -----------------------------------------------
DATA = None

class Processor(FixtureSpec):

    def __init__(self):
        super().__init__()
        self.filename = "records/data.json"
        self.data = self.__load()

    def __load(self) -> dict:
        fh = open(self.filename, "r")
        data = json.load(fh)
        for item in data:
            idx = data.index(item)
            id = {"#": idx + 1}
            id.update(data[idx])
            data[idx] = id
        return data

    def display_menu(self) -> any:
        n = narrator.Narrator()
        q = narrator.Question({
            "question": "\nOperation to perform:\n",
            # You might alter this to add a feature ------------
            "responses": [
                {"choice": "1 search rows ", "outcome": 1},
                {"choice": "2 total a column ", "outcome": 2},
                {"choice": "3 average a column ", "outcome": 3},
                {"choice": "4 print table ", "outcome": 4},
                {"choice": "5 quit", "outcome": False}
            ]
            # You might alter this to add a feature ------------
        })
        return q.ask()
    
    def display_table(self) -> None:
        cols = list(self.data[0].keys())
        table = Table(title="term-world CITIZEN DATA")
        for col in cols:
            table.add_column(col)
        for row in self.data:
            entry = [str(item) for item in list(row.values())]
            table.add_row(*entry)
        console = Console()
        console.print(table)
# Do not alter -----------------------------------------------

# TODO: Write search_rows function per guidelines in the README

# TODO: Write total_column function per guidelines in the README

def main():

    # Do not alter -------------------------------------------
    global DATA
    obj = Processor()
    DATA = obj.data
    response = obj.display_menu()
    # Do not alter -------------------------------------------

    # Note: Use f-strings to print the values requested below
    
    while True:
        if not response:
            break
        if response == 1:
            choice = input("Field to search: ")
            value = input("Value to search for: ")
            # TODO: Implement correct call to search_rows
            # TODO: Print the number of rows found
        if response == 2:
            choice = input("Field to total: " )
            # TODO: Implement correct call to total_column
            # TODO: Print result of totaling operation
        if response == 3:
            choice = input("Field to average: ")
            # TODO: Implement correct call to total_column
            # TODO: Implement correct call to search_rows
            # TODO: Use the above information to calculate
            #       a column's average using total_column and search_rows
        if response == 4:
            obj.display_table()
        response = obj.display_menu()

if __name__ == "__main__":
    main()
