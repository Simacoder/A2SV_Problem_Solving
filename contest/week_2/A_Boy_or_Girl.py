# find the solution for a date for our hero
username = input().strip()

distinct_count = len(set(username))

if distinct_count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")