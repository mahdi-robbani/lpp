# 1. Create a directory called "handin1" in your current directory.
mkdir handin1

#2. Inside this directory, create a directory called "test1".
cd handin1
mkdir test1

#3 Use a Unix command to download the following file: https://wouterboomsma.github.io/lpp2019/data/m_scrambled.txt into a file called "m_scrambled.txt" within the "test1" directory.
cd test1
wget https://wouterboomsma.github.io/lpp2019/data/m_scrambled.txt

#4 Make a copy of the "test1" directory, called "test2".
cd ..
cp -r test1 test2

#5 Go to the "handin1" directory, and use the "find" command to output all files and directories under this directory.
find

#6 Remove the "test2" directory.
rm -r test2

#7 Use the "cat" command to take a look at the "m_scrambled.txt" you just downloaded.
cd test1
cat m_scrambled.txt

#8 Find a way to "unscramble" (i.e. make sense of) the image into a new file called "m.txt" (in the "test1" directory).
sort -n m_scrambled.txt > m.txt

#9 Find a way to download, unscramble and save (into "m.txt") in a single (one-line) command (i.e. combine point 3. and 8.). Again, save it to a file called "m.txt" in the "test1" directory.
wget https://wouterboomsma.github.io/lpp2019/data/m_scrambled.txt | sort -n . > m.txt

#10 Delete the "handin1" directory and all directories below it
cd ..
cd ..
rm -r handin1
