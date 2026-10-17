import sys

class Texter:
    def __init__(self, subor):       #initializing of object 
        self.subor = subor

    def funkcia(self):

        with open(self.subor, "r", encoding="utf-8") as f:      
            slova = f.read().split()                     #opens file, reads it and creates a list of all strings separated by whitespace (words)

        print("Word count:", len(slova))                #prints the amount of "words"
        count=0                                  #creates a counter at 0 counts
        for i in slova:
            if i[0].isupper():
                count +=1                        #checks every string; for those that begin with an uppercase letter adds 1 to the "count"
            else:
                pass                         
        print("Words with capital letter", count)      #prints amount of words starting with uppercase

if __name__ == "__main__":                #checks if in main
    if len(sys.argv) > 1:                 #if amount of arguments given is greater than 1 create an object of class "Texter", give texter the argument of the file name and run "funkcia" on the object 
        Texter(sys.argv[1]).funkcia()
    else:
        print("Please enter a file name\nExample:\npython texter.py example.txt\nMake sure both file and texter.py are in the same directory")   #if file name is missing, print a message informing of how to use the script
