# can i be a fallen champion
import sys
w, t = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
    
warriors = [(w, t, "Y")]
    
for _ in range(n):
    wi, ti = map(int, sys.stdin.readline().split())
    warriors.append((wi, ti, "O"))
    
    
warriors.sort(key=lambda x: (-x[0], x[1]))
    
if warriors[0][2] == "Y":
    print("The Champion Saves the Accused")
else:
    print("The Fallen Champion")
