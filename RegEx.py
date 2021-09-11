



import re

# pattern = r"Bangla"
# result = re.match(pattern, "Bangladesh")
# if result:
#     print("Match Found")
# else:
#     print("Not Found")

# pattern = r"Bangladesh"
# result = re.search(pattern, "There is country named Bangladesh in south asia!")
# if result:
#     print("Match Found")
# else:
#     print("Not Found")


# pattern = r"bangla"
# result = re.findall(pattern, "Bangladeshi bangla and indian bangla are differnet.")
# print(result)
#
# pattern = r"bangla"
# result = re.finditer(pattern, "Bangladeshi bangla and indian bangla are differnet.")
# print(result)



# pattern = r"bin"
#
# match = re.search(pattern, "combination")
# if match:
#     print(match.group())
#     print(match.start())
#     print(match.end())
#     print(match.span())




# pattern = r"gr.y"
# if re.match(pattern, 'grey'):
#     print("Match 1")
# if re.match(pattern, "gray"):
#     print("Match 2")
# if re.match(pattern, "grby"):
#     print("Match 3")

# pattern = r"^wr.te$"
#
# if re.match(pattern, "write"):
#    print("Match 1")
#
# if re.match(pattern, "wrote"):
#    print("Match 2")
#
# if re.match(pattern, "writer"):
#    print("Match 3")
#
#
# # A character set containing all vowels
# pattern = r"[aeiou]"
#
# # Lets check whether a word got a vowel in it or not
# if re.search(pattern, "grey"):
#    print("The word 'grey' got at least one vowel!")
# else:
#    print("No vowel found!")
#
# if re.search(pattern, "qwertyuiop"):
#    print("The word 'qwertyuiop' got at least one vowel!")
# else:
#    print("No vowel found!")
#
# if re.search(pattern, "rhythm myths"):
#    print("The word 'rhythm myths' got at least one vowel!")
# else:
#    print("No vowel found!")




# pattern = r"[A-Z][A-Z][0-9]"
#
# if re.search(pattern, "NS1 is prefix of first name server address."):
#    # Found NS1 as match
#    print("OK")
#
# if re.search(pattern, "You should put a second one with NS2 as prefix."):
#    # Found NS2 as match
#    print("OK")
#
# if re.search(pattern, "I don\'t have any nameserver."):
#    print("NS3")
# else:
#    print("Not OK!")
#
# if re.search(pattern, "PY3K"):
#    # Found PY3 as match
#    print("OK")


# pattern = r"[0][1][3-9][0-9]"
# if re.match(pattern, "017718336l4"):
#     print("Match 1")
# if re.match(pattern, "057718336l4"):
#     print("Match 2")
# if re.match(pattern, "007718336l4"):
#     print("Match 3")


# pattern = r"[0][1][3-9][0-9]"
# phone_number = input("Enter Then Number")
# if re.match(pattern, phone_number):
#     print("Your Number is "+phone_number)
# else:
#     print("Please first 01(3-9)")



