import sys

file_path = r"C:\Users\HP\Documents\computer_course-2024\word_for_file.txt"

try:
    with open(file_path, "r") as file:
        file_contents = file.read().split()
except FileNotFoundError:
    print(f"File not found: {file_path}")
    sys.exit(1)

word_count = {}

# Count the occurrences of each word in 'file_contents' and store the results in 'word_count'
for word in file_contents:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

# N parameter using sys.argv
if len(sys.argv) > 1: #checks if there is an argument
    N = int(sys.argv[1]) #gets the argument and put it in a parameter
else:
    N = 0 

sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

# Check if N is not a good input
if N > len(sorted_word_count) or N <= 0:
    print("ERROR! N is bigger/smaller than the words available. Printing all keys and values:")
    print(sorted_word_count.items())
else:
    most_common_words = list(sorted_word_count.keys())[:N]
    print(most_common_words)

