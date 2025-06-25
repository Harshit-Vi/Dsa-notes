# Implemention of loops and recursion through example of Fibonacci Number

# Using Loop
prev2 = 0
prev1 = 1
print(prev2)
print(prev1)
for fibo in range (18):
    newfibo = prev1 + prev2
    print(newfibo)
    prev2 = prev1    # To assign a new previous value as it is sum of last 2 numbers
    prev1 = newfibo  # here prev1 got new value and we already assigned prev1 value to prev1 in last line


#implemention using recursion

print(0)
print(1)
count = 2

def fibonacci (prev1, prev2):
    global count
    if count < 19:
        newfibo = prev1 + prev2
        print(newfibo)
        prev2 = prev1
        prev1 = newfibo
        count += 1
        fibonacci(prev1 , prev2)
    else:
        return

fibonacci(1,0)

# Finding nth fibonacci number using recursion
#           Formula : F(n) = F(n-1) + F(n-2)
# The formula uses 0 based index ( means For example to generate 20 fibonacci numbers we must write F(19))

def F(n):
    if n<=1:
        return n
    else:
        return F(n-1) + F(n-2)

print (F(19))

