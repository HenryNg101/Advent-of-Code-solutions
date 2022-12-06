# This is a bit special, the question is pretty much similar, the only difference is the size
# That's why I only wrote code in one file
content = open("input").read().rstrip('\n')

# Only need to change this var to fit the question a or b, a is 4, b is 14
sz = 14

# Sliding window, until found the one that satisfy the condition
for i in range(sz-1, len(content)):
    s = content[i-sz+1:i+1]

    # Set to count unique chars
    if len(set(s)) == sz:
        print(i+1)
        break
