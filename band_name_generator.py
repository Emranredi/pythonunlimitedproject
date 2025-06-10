# from wonderwords import RandomWord
# import random
# pep_name=input("Please enter names separated by commas: ").split(',')
# for name in pep_name:
#     print(f"{name} is in the band")

# band_aim=input("Please enter the aim of the band members(enter it as ahole) like adjective")


# # Initialize Wonderwords RandomWord generator
# rw = RandomWord()

# # Generate a random word using Wonderwords
# random_word = rw.word()

# # Pick a random name from your custom list
# random_name = random.choice(pep_name)

# random_word = rw.word()

# # Pick a random name from your custom list
# random_aim = random.choice(band_aim ) 

# # Get the first word of the name
# # random_aim = random_aim.split()  # Get the first word of the aim
# # random_name = random_name.split()  # Get the first word of the name
#  # Get the first word of the random word 
# # Combine them to create a new name or just use the random name

# letters_aim = list(''.join(random_aim))  # All letters from aim words
# letters_name = list(''.join(random_name))  # All letters from name words
# # Combine letters from both lists
# combined_letters = letters_aim + letters_name
# # Shuffle letters randomly
# random.shuffle(combined_letters)
# # Join letters into a new random string
# combined_random_string = ''.join(combined_letters)
# print(combined_random_string)


# band_name = f"{random_name} {random_aim} results in "

# print(band_name)


# blackbox 
#from wonderwords import RandomWord
from wonderwords import RandomWord
import random

# Get names from user input
pep_name = input("Please enter names separated by commas: ").split(',')
for name in pep_name:
    print(f"{name.strip()} is in the band")  # Strip whitespace from names

# Get the aim of the band members
band_aim = input("Please enter the aim of the band members (enter it as a whole): ")

# Initialize Wonderwords RandomWord generator
rw = RandomWord()

# Generate a random word using Wonderwords
random_word = rw.word()

# Pick a random name from your custom list
random_name = random.choice(pep_name).strip()  # Strip whitespace from the selected name

# Split the band aim into words
aim_words = band_aim.split()  # Split the aim into words

# Pick a random aim from the list of words
random_aim = random.choice(aim_words)  # Select a random aim word

# Get letters from the random aim and random name
letters_aim = list(random_aim)  # All letters from the random aim
letters_name = list(random_name)  # All letters from the random name

# Combine letters from both lists
combined_letters = letters_aim + letters_name

# Shuffle letters randomly
random.shuffle(combined_letters)

# Join letters into a new random string
combined_random_string = ''.join(combined_letters)

# Print the combined random string
print(f"Combined random string: {combined_random_string}")

# Create and print the band name
band_name = f"{random_name} {random_aim} results in "
print(band_name)








# w = RandomWord()
# # genr_word=wonderwords -w
# w.word(include_categories=["adjective"])
# w.word(include_categories=["noun", "verb"])
# print(w.word())
# pep_num=int(input("enter the people in your band"))



# band_leader = input("Please enter the name of the band leader: ")

# def band_namme_bynum():
#   if pep_num > 5:
#    print("enough to be called a band") 
#   else :
#     print("not enough to be called a band") 


# band_namme_bynum()






# band_name = f"{w.word(include_categories=['adjective'])} {w.word(include_categories=['noun'])}"
# print(f"Your band name is: {band_name}")






