from num_class import Num
from sym_class import Sym
import re

class Cols:
    def __init__(self, table):
        self.x = []
        self.y = []
        self.names = table
        self.all = []
        self.klass = None

        for all_column_names in table:
            n = table.index(all_column_names)
            all_column_names = all_column_names.strip()
            if all_column_names[0].isupper():
                col = Num(n, all_column_names)
            else:
                col = Sym(n, all_column_names)
            self.all.append(col)

            if not all_column_names[-1] == "X":
                if "!" in all_column_names:
                    self.klass=col
                self.y.append(col) if re.findall("[!+-]$", all_column_names) else self.x.append(col)
    
    def add(self, row):
        for table in [self.x, self.y]:
            for col in table:
                col.add(row.cells[col.at])