b = "Hello World"

print(b)
print("=================")
print(b[::-2])  # Step -2: every second character in reverse order
print("++++++++++++++++++")
print(b[::2])   # Step 2: every second character in normal order
print("=================")
print(b[-1])   # Last character
# getting the ascii value of last character
print(ord(b[-1]))
print("=================")

# for loop numbers 
num = 1
for num in range(5 + 1):
    print(num)
    num += 1

print("=================")
# print negative numbers using for loop 

print("=================")
for num in range(-1, -6, -1):
    print(num)
print("=================")