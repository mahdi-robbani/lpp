#Download both files to your current directory using appropriate unix commands.
wget -O british-english http://wouterboomsma.github.io/lpp2019/data/british-english
wget -O british-english-subset http://wouterboomsma.github.io/lpp2019/data/british-english-subset

#In the _subset file, I have excluded words starting with specific letters in the alphabet. Write a command that prints out exactly which letters I ommitted from subset, one letter on each line, and each letter occurring only once. Hint: the diff command will list the differences, and the -b option of the cut command will give you a specific character in each line.
diff british-english british-english-subset | cut -b 3 | uniq -d

#Find a way to reproduce the british-english-subset file from the original british-english file, i.e., write a Unix command involving grep that takes the original british-english file and produces the british-english-subset file. Note that the grep command understands regular expressions (which means, for instance, that you can match something occurring at the beginning of a line). Save the output produced by the command to a file called british-english-subset2.
grep '^[a-W]' british-english > british-english-subset2 # grep "^[^XYZ]"

