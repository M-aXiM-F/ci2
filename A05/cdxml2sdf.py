import sys
import glob

from openbabel import pybel


def main(args):
    output_name = "cdxml2sdf.sdf"
    patterns = []

   
    for arg in args:
        if arg.lower().endswith(".sdf"):
            output_name = arg
        else:
            patterns.append(arg)


    filenames = []
    for pattern in patterns:
        filenames.extend(sorted(glob.glob(pattern)))

 
    if not filenames:
        print("No .cdxml file was specified or found.")
        return

 
    molecules = []
    output = pybel.Outputfile("sdf", output_name, overwrite=True)
    for filename in filenames:
        for mol in pybel.readfile("cdxml", filename):
            mol.title = filename
            output.write(mol)
            molecules.append((filename, mol))
    output.close()

   
    best_similarity = -1.0
    best_pair = None
    fingerprints = [(name, mol.calcfp()) for name, mol in molecules]
    for i in range(len(fingerprints)):
        for j in range(i + 1, len(fingerprints)):
            similarity = fingerprints[i][1] | fingerprints[j][1]
            if similarity > best_similarity:
                best_similarity = similarity
                best_pair = (fingerprints[i][0], fingerprints[j][0])

    print(best_pair[0], best_pair[1], best_similarity)


if __name__ == "__main__":
    main(sys.argv[1:])
