# I have given you two variables, name and age. Use the format() function to create a sentence that reads:

# Hi my name is julie and I am 42 years old

# Set that equal to the variable called sentence


name = "Julie"

age = "42"

sentence = f'Hi my name is {name} and I am {age} years old'                         #f string

sentence2 = "Hi my name is {} and I am {} years old".format(name, age)               #format function

print(sentence)
print(sentence2)