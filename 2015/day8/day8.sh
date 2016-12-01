# part 1
sed 's/\\"/@/g' input.txt | sed 's/\\x[a-f0-9][a-f0-9]/~/g' | sed 's/\\\\/\\/g' | wc -c

# part 2
sed 's/"/~~/g' input.txt | sed 's/\\/@@/g' | wc -c
