#cdxml2sdf.py
## what cdxml2sdf.py does:
It creates cdxml2sdf.sdf file unless specified otherwise with an argument (e.g. file.sdf) with the contents of 
.cdxml files. 
It can be fed individual files or read wildcard symbols (e.g. rx*.cdxml). 
After creating an .sdf file the program will print out two most similar molecules and their similarity value
according to Tanimoto.

## how to use cdxml2sdf.py:
```bash
git clone git@github.com:M-aXim-F/ci2.git
cd ci2/A05/
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements
python3 cdxml2sdf.py *.cdxml name_of_file.sdf
``` 
