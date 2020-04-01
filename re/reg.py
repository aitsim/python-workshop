# A regular expression (sometimes called a rational expression) 
# is a sequence of characters that define a search pattern,


# According to Python docs, raw string notation (r"text")
#  keeps regular expressions meaningful and confusion-free.
# Without it, every backslash ('\') in a regular expression would have
#  to be prefixed with another one to escape it
#  for example 
print("\\n hi")

print(r"\n mohamed \t si mail")


import re
# multi line string 
text='''hi my name is mohamed 
srry,im late
i've to go know we'll talk later.



i made 5 fugure a day 

i've been learning english since yesterday

she got pragnent 
my phone number is 475-313-8851


samir s number is 475-313-7851


ibrahim 475-313-3851


'''
# search for patterns


pattern = re.compile(r"^hi")
pattern = re.compile(r"i've.be")

pattern = re.compile(r"\d") #get 5

pattern = re.compile(r"\d\d\d.\d\d\d.[37]\d\d\d") # last number start with 7 or 3

pattern = re.compile(r"\d\d\d.\d\d\d.[1-7]\d\d\d") # last number start from 1 to 7 (.) means any caracter see more at the snippets file 


print("--------------------")

pattern = re.compile(r"[^b]at")# not started with a b


matches = pattern.finditer(text)

for match in matches:
    print(match)


