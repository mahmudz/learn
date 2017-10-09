#!/usr/bin/python3

a = 20    # 10
b = 40	# 100


c = 0

# AND
c = a & b;  
print(bin(c))

# OR
c = a | b;     
print(bin(c))

# X-OR
c = a ^ b;
print(bin(c))

# COMPLIMENT
c = ~a;  
print(bin(c))

# LEFT SHIFT
c = a << 2;  
print(bin(c))

# RIGHT SHIFT
c = a >> 2;  
print(bin(c))
