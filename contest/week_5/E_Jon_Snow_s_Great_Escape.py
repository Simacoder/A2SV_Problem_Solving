
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    s = input().strip()
        

    pos = x - 1
        
      
    left_empty = 0
    for i in range(pos - 1, -1, -1):
        if s[i] == '.':
            left_empty += 1
        else:
            break
        
        
    right_empty = 0
    for i in range(pos + 1, n):
        if s[i] == '.':
            right_empty += 1
        else:
            break
        
       
        
    can_escape_left = (pos - left_empty == 0)  
    can_escape_right = (pos + right_empty == n - 1)  
        
    if can_escape_left or can_escape_right:
         
        print(1)
    else:
            
            
        left_dist = pos
        right_dist = n - 1 - pos
            
            
        answer = min(left_dist, right_dist) + 1
        print(answer)

