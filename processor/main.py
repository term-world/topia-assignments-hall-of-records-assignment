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
                {"choice": "5 quit", "outcome": False},
                {"choice": "6 SECRET AUTO-AVERAGER", "outcome": "SECRET"}
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

# Student minimal solution -----------------------------------
def search_rows(field: str = "#", value: any = 0) -> list:
    rows = []
    for row in DATA:
        if int(row[field]) >= int(value):
            rows.append(row)
    return rows

def total_column(field: str = "#") -> int:
    total = 0
    for row in DATA:
        total += row[field]
    return total
# Student minimal solution -----------------------------------

# Professor trickery -----------------------------------------
def auto_averager() -> dict:
    """ This function is not required. Some students may discover how to do it. """
    # For folks looking for extra-curricular learning,
    # no "if" statement required:
    # fields = [field for field in DATA[0] if field != "ID"]
    # Or, the could remove the ID column temporarily
    # Or, see ideal_matches below
    ideals = {}
    for field in DATA[0]:
        if field != "ID" and field != "#":
            total = 0
            rows = search_rows(field, 0)
            for row in DATA:
                total += row[field]
            ideals[field] = int(round(total/len(rows),0))
    return ideals

def ideal_matches(ideals: dict = {}) -> list:
    """ This is definitely not a function that students need; it's for my trick. """
    # SPOILER: ONLY I MATCH THE CRITERIA; EVERYONE ELSE IS "LOCKED OUT"
    fields = list(ideals.keys())
    for field in fields:
        for row in DATA:
            rows = []
            if int(row[field]) < ideals[field]:
                rows.append(row)
            for row in rows:
                idx = DATA.index(row)
                DATA.pop(idx)
    return DATA
# Professor trickery -----------------------------------------

def main():

    # Do not alter -------------------------------------------
    global DATA
    obj = Processor()
    DATA = obj.data
    response = obj.display_menu()
    # Do not alter -------------------------------------------

    while True:
        if not response:
            break
        if response == 1:
            choice = input("Field to search: ")
            value = input("Value to search for: ")
            rows = search_rows(choice, value)
            print(f"Found {len(rows)} rows.")
        if response == 2:
            choice = input("Field to total: " )
            total = total_column(choice)
            print(f"Total of {choice}: {total}.")
        if response == 3:
            choice = input("Field to average: ")
            total = total_column(choice)
            rows = search_rows(choice, 0)
            print(f"Average of {choice}: {total/len(rows)}.")
        if response == 4:
            obj.display_table()
        # SECRET, obvs --------------------------------------
        if response == "SECRET":
            ideal = auto_averager()
            ideals = ideal_matches(ideal)
            for result in ideals:
                for field in result:
                    print(f"{field}: {result[field]}")
        # SECRET, obvs --------------------------------------
        response = obj.display_menu()

if __name__ == "__main__":
    main()