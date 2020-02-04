#Create a module called handin5, and inside that module define a function called read_fasta. This function should take one argument: a string that is a filename (or full path) to a fasta file. This function should open and read the supplied fasta file, then create and return a dictionary, where the keys are the names of the proteins (without the > character) and the sequences are the values. Make sure to add a docstring to your function. Hint1: remember to remove the newline characters at the end of each line. Hint2: Think of the exercise like this: for each line, you should check whether the line is a header or not. If it is a header, it should be added to the dictionary as a key - if it is not, it should be added to the dictionary as a sequence - adding to whatever sequence was already there.
def read_fasta(filename):
    '''Creates a dictionary from a fasta file where the key is the protein name and the value is the sequence'''
    seq_dict = {}
    file = open(filename, "r")
    for line in file:  #### FASTER THAN FILE.READLINES.
        line = line.strip()
        if line[0] == ">": # checks if line is header
            # seq_dict[header] = ""
            sequence = ""  # resets sequence
            header = line[1:]  # saves header name as key
        else:
            # seq_dict[header] += line
            sequence = sequence + line # adds non header line to sequence
            seq_dict[header] = sequence  # creates dictionary entry
    return seq_dict

#In the handin5 module, create another function called find_prot that takes a dictionary as first argument, and as second argument takes a protein name (a string). The function should use the provided dictionary to lookup and return the sequence corresponding to the provided name. If the name is not present in the dictionary, the function should print an error message and return None. The error message should be Error: protein name NAME not found, where NAME is the protein name you are searching for. Make sure to include a docstring.
def find_prot(seq_dict, prot_name):
    '''checks if protein name is inside dictionary'''
    if prot_name in seq_dict:
        return seq_dict[prot_name]
    else:
        print("Error: protein name " + prot_name + " not found")
        return None

#In the handin5 module, create a function called find_prot2 that takes a dictionary and regular expression (as a string), and returns a list of all of the keys in the dictionary that the pattern matches. Make sure to include a docstring.
import re
def find_prot2(seq_dict, reg_ex):
    '''Searches protein dictionary using a regular expression'''
    matches = []
    for key in seq_dict.keys():
        if re.search(reg_ex, key) is not None:
            matches.append(re.search(reg_ex, key))
    return matches
