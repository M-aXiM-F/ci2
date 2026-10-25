from bs4 import BeautifulSoup as bs
import sys

class Parser:
    def __init__(self, file):
        self.file = file
    def parse(self):
        with open(self.file, encoding="utf-8") as f:
            soup = bs(f, "xml")
        rows = soup.find_all("row")          
        print("Compounds found:", len(rows))

        for row in rows:                 
            print(row.find("iupacname").get_text(strip=True))

if __name__ == "__main__":                #checks if in main
    if len(sys.argv) > 1:
        Parser(sys.argv[1]).parse()
    else:
        print("Please enter a file name\nExample:\npython parser.py example.xml\nMake sure both file and texter.py are in the same directory")   
