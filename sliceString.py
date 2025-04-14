# Slices
msg = "I <3 cat"
# first is start index , next is last index
# msg[2:6]
print(msg[2:6])
# this one tell python, you want to all after string
print(msg[3:])
# this one tell python, you want to get before 6 char
print(msg[:6])
# It will not error, just ""
print(msg[-1:-5])

# test
ssn = "#811876543"
print(ssn[1:])

# Slices with Step
#         start    stop       Step
print(ssn[ 1      :  2     :    6    ])

# Escape Characters
# Newline \n
# Doubile Quote \"
# Tab \t
# Single Quoto \'
# Backslash \\
phrase = "hello \n world"
print(phrase)

phraseTow = "hello \t world"
print(phraseTow )

phraseThree = "hello \"QOO\""
print(phraseThree)