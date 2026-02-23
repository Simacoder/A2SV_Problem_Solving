# recursive function with base case
def fact_recuse(n):
    if n == 1:
        return 1
    
    else:
        return n * fact_recuse(n - 1)

print(fact_recuse(5))