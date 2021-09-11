

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)


b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(b)


a = "Hello, World!"
print(a[1])

# useing loop because string are array
for i in a:
    print(i)

# length string
print(len(a))

# check string
print("Hello" in a)

# Check condition
if "Hello" in a:
    print("yes, value is in the line")

# check in not

print("Hello" not in a)
print("hell" not in a)

# Check not in condition

if "Hllo" not in a:
    print("Sorry not matching")