

# file_to_work = open("MyText.txt", "w")
# file_to_work.close()

# file_to_work = open("MyText.txt", 'r')
# content = file_to_work.read()
# print(content)
# file_to_work.close()


# file_to_work = open("MyText.txt", 'r')
#
# print(file_to_work.read())
# file_to_work.close()



# file_to_work = open("MyText.txt", 'w')
# file_to_work.write("My name is Ziaur Rahman Joy")
# file_to_work.close()
#
# file_to_work = open("MyText.txt", 'r')
# print(file_to_work.read())
# file_to_work.close()

# file_to_work = open("MyText.txt", 'w')
# file_write_done = file_to_work.write("My name is Ziaur Rahman Joy")
# file_to_work.close()
#
# file_to_work = open("MyText.txt", 'r')
# print(file_to_work.read())
# file_to_work.close()
#
# if file_write_done:
#     print(f"Yes, {file_write_done} byte(s) has been written!")
# file_to_work.close()


with open("MyText.txt", 'w') as file_to_work:
    file_write_done = file_to_work.write("My name is Ziaur Rahman Joy")
    if file_write_done:
        print(f"Yes, {file_write_done} byte(s) has been written!")

