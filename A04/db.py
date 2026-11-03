import sys
import csv
import sqlite3


class DataBaser:
    def __init__(self):
        self.db = "db.sqlite"
        self.files = ["city.csv", "country.csv", "countrylanguage.csv"] + sys.argv[1:]
        self.con = sqlite3.connect(self.db)
        for file in self.files:
            self.load(file)
        print(self.albania())

    def load(self, file):
        table = file[:-4]
        exists = self.con.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (table,)
        ).fetchone()
        if exists:
            return
        rows = list(csv.reader(open(file, encoding="utf8"), delimiter=";"))
        self.con.execute(f'CREATE TABLE "{table}" ({", ".join(rows[0])})')
        marks = ",".join("?" * len(rows[0]))
        self.con.executemany(f'INSERT INTO "{table}" VALUES ({marks})', rows[1:])
        self.con.commit()

    def albania(self):
        return self.con.execute(
            "SELECT COUNT(*) FROM city JOIN country ON city.CountryCode = country.Code "
            "WHERE country.Name = ?", ("Albania",)
        ).fetchone()[0]


DataBaser()



        