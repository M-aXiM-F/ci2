import sys

class Texter:
    def __init__(self, subor):
        self.subor = subor

    def funkcia(self):

        with open(self.subor, "r", encoding="utf-8") as f:
            slova = f.read().split()

        print("Word count:", len(slova))
        count=0
        for i in slova:
            if i[0].isupper():
                count +=1
            else:
                pass
        print("Words with capital letter", count)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Texter(sys.argv[1]).funkcia()
    else:
        print("Please enter a file name" \n
        "" \n
        "Example:" \n
        "python texter.py example.txt") 
