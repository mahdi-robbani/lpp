#1 Use bzip2 to compress the file, but in a way that preserves the original.
bzip2 -k experimental_results.txt

#2 Use ls to output how large the two files are. The output should contain two lines - the first displaying the size of the original file, and the second displaying the size of the compressed file. The two line should each contain only the size, i.e. just a single number. (Hint: first use tr to squeeze all spaces and then use cut with space as a delimiter).
ls -l | awk '/results.txt/ {print$5;}' # ls -l experimen* | tr -s " " " " | cut -d " " -f 5


#3 The tr command has the functionality to recognise digits (see the man page). Use this to replace all the number in the original file with "0.000000" (i.e. replace each digit with a zero), and save this to a file called experimental_results_zeros.txt.
cat experimental_results.txt | tr [0-9] 0 > experimental_results_zeros.txt

#4 Check that the experimental_results_zeros.txt file has the same size as the experimental_results.txt file, using the same output format as in question 2.
ls -l | awk '/s.txt$/ {print$5;}'

#5 Use bzip2 to compress the experimental_results_zeros.txt file (again keeping the original), and print out the sizes of the original and compressed files, in the same output format as in question 2.
bzip2 -k experimental_results_zeros.txt
ls -l | awk '/zeros.txt/ {print$5;}'

#6 Try to explain why there is a difference - use echo and tee to write the explanation both to a file called explanation.txt and to stdout.
echo "Since the new file only has zero, it is more efficiently compressed." | tee explanation.txt
