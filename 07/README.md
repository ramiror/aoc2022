execute:

python sol2.py < input.txt | head -210 | sort -nr

then take the outmost dir size (from first line)

$ expr 70000000 - outmost_size
free_space
$ expr 30000000 - free_space
space_to_clean

then manually search the smallest larger number and that's your answer
