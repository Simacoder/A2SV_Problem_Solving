# solve the password: the dog that decipher
password = input().strip()

n = int(input())

words = [input().strip() for _ in range(n)]

# Case 1 direct match 
if password in words:
    print("YES")
else:
    # Case 2 accross two words
    for w1 in words:
        for w2 in words:
            if w1[1] + w2[0] == password:
                print("YES")
                exit()
    print("NO")