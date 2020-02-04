#Use the time command to measure the execution time of handin6_test1.py.
time python handin6_test1.py

#Use the time command to measure the execution time of handin6_test2.py.
time python handin6_test2.py

#Use the time command to measure the execution time of handin6_test3.py.
time python handin6_test3.py

#The diff command can be used to solve the same task as our Python script above. Write a command that does this. The command should just print out the number of differences (i.e. the number of words in file1 that do not occur in file2).
diff -y --suppress-common-lines british-english american-english | cut -d " " -f 1 | grep '[a-Z]' | wc -l

#Repeat the previous question, but now use the time command to measure its performance.
time diff -y --suppress-common-lines british-english american-english | cut -d " " -f 1 | grep '[a-Z]' | wc -l

