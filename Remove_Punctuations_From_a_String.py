#Program to Remove Punctuations From a String
#define Punctuation
Punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*'''
my_str = "Hello!!!, he said --- and went."
# To take input from the user
# my_str = input("Enter a string: ")
# remove Punctuation from the string
no_punct = ""
for char in my_str:
    if char not in Punctuation:
        no_punct = no_punct + char

# display the unpunctuated stringprint(no_punct)
print(no_punct)

# === Output ===
Hello he said and went