# Made by Carter

# Splits lines and makes every item an integer
rows, cols, threshold = (int(n) for n in input().split())
word_lens = [int(n) for n in input().split()][1:]  # First item is just len()
# Joins together lines of input
letters = ''.join(input() for __ in range(rows)).replace(' ','')

for char in letters:
    if letters.count(char) >= threshold:
        letters = letters.replace(char, '')

words = []
i, o = 0, 0  # In, out
for l in word_lens:
    i, o = o, o + l  # In becomes previous out, out becomes previous out + l
    words.append(letters[i:o])

print(' '.join(words))
