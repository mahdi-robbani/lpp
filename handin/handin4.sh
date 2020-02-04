#Find out how to get the sort command to sort by the second column in a file. Use this to write a command that finds the largest value in the second column of the experimental_results.txt file. Note that the command should just return a single number.
cut -f 2 -d " " experimental_results.txt | sort -g | tail -n 1

#Find documentation on the xargs and the du commands (either in the man pages or online). Using this information, construct a unix pipeline that finds all files under the /usr/share/dict directory containing the word "english" (using the find command), calculates the size of each of them, and then sorts the lines so that the largest files appear at the bottom (hint: you might need to use the -n 1 option for xargs).
find /usr/share/dict/ -name *english* | xargs -n 1 du | sort -g

