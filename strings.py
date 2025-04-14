# example
helleword = "hello word"
print(helleword)
print(type(helleword))

# error
# 'I can't love you anymore'
# ok
# "I can't love you anymore"
# ok
# 'he said "haha"'

# python can change data type
age = 85
print(type(age))
age = "85"
print(type(age))

# String Operators
# + -> plus
# String uses plus operator is concat the string
print("hello" + " " + "world")
last_name = "jhu"
first_name = "lorn"
print(last_name + " " + first_name)

# * -> multuply
print("ha" * 3)

# error , because data type diff
# "ha" + 3

# String Are Ordered/Indexed
# first one start with 0
# 0 1 2 3 4
# H e L L O
msg = "I <3 Cats"
print(msg[0])
print(msg[5])
print("hello"[1])
# Erro
# string index out of range
# msg[99]

# other o rdered
#  0  1  2  3  4  5  6  7  8
# -9 -8 -7 -6 -5 -4 -3 -2 -1
#  I     <  3     C  a  t  s
print(msg[-1])

# None
# It is not the same as Zero or ""
none = None
print(type(none))