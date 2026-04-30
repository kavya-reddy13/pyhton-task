# Basic String Handling

# 1. Combine first name and last name
# first = "manoj"
# last = "parlapalli"
# print("Full Name:", first + " " + last)


# 2. String slicing examples
# text = "manoj"
# print("First 2 chars:", text[:2])      
# print("Last 3 chars:", text[-3:])     
# print("Skip characters:", text[::2])   


# 3. Reverse a string
# print("Reversed string:", text[::-1])



# String Indexing and Substring Extraction

# text = "manoj"

# 4. First and last character
# print("First & Last:", text[0] + text[-1])   # mj


# 5. First two and last two characters
# print("First 2 & Last 2:", text[:2] + text[-2:])  # manoj → maoj


# 6. First and last letter, middle replaced with *
# middle_hidden = text[0] + "*" * (len(text) - 2) + text[-1]
# print("Middle hidden:", middle_hidden)   # m***j


# 7. First 2 and last 2, middle replaced with *
# middle_hidden_2 = text[:2] + "*" * (len(text) - 4) + text[-2:]
# print("Partial hidden:", middle_hidden_2)  # ma*oj



# String Splitting into Halves

# text = "parlapalli"

# 8. First half of the string
# first_half = text[:len(text)//2]
# print("First half:", first_half)


# 9. Last half of the string
# last_half = text[len(text)//2:]
# print("Last half:", last_half)



# 10. String Repetition

# name = "manoj"
# number = 3
# print((name + " ") * number)


