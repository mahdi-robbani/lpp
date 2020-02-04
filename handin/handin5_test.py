#Create a new file, called handin5_test.py where you import the handin5 module. Then call the read_fasta function and save the result in a variable called fasta_dict. Print the number of keys in this dictionary to screen
import handin5
fasta_dict = handin5.read_fasta("Ecoli.prot.fasta")
print(len(fasta_dict))

#In the handin5_test.py file, call the find_prot function on the protein name YHCN_ECOLI. Save the result to a variable called yhcn.
yhcn = handin5.find_prot(fasta_dict, "YHCN_ECOLI")

#In the handin5_test.py file, call the find_prot function on the protein name BOOM_ECOLI. Save the result to a variable called boom. Note that this case should print an error, since this is not an actual Ecoli protein name.
boom = handin5.find_prot(fasta_dict, "BOOM_ECOLI")

#In handin5_test.py, use the find_prot2 function to return all the protein names in Ecoli that only consist of three characters before _ECOLI (e.g. EX1_ECOLI). Save the result in a variable called matches". Print the number of matches to screen.
matches = handin5.find_prot2(fasta_dict, "^.{3}_ECOLI$")
print(len(matches))
