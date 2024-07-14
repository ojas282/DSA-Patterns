def box(n):
  for i in range(n):
    for j in range(n):
      print("#",end="")
    print()

# box(5)

'''
OP: 
#####
#####
#####
#####
#####
'''

def right_90(n):
  for i in range(n):
    for j in range(i+1):
      print("# ",end="")
    print()

# right_90(5)

'''
OP:
# 
# # 
# # # 
# # # # 
# # # # # 
'''


def right_90_num(n):
  for i in range(1,n+1):
    for j in range(1,i+1):
      print(j,end='')
    print()
  
# right_90_num(5)

'''OP:
1
12
123
1234
12345 '''

def right_90_same(n):
  for i in range(1,n+1):
    for j in range(1,i+1):
      print(i,end="")
    print()

# right_90_same(5)

'''
OP:
1
22
333
4444
55555
'''

def upper_lefthalf_triangle(n):
  for i in range(1,n+1):
    for j in range(0,(n-i)+1):
      print("# ",end="")
    print()


# upper_lefthalf_triangle(5)

'''
OP:
# # # # # 
# # # # 
# # # 
# # 
# 
'''
def left_90(n):
  '''for i in range(1,n+1):
    print(" " * (n-i)+ "#" * i)'''
  
  for i in range(1,n+1):
    for j in range(n-i):
      print(" ",end="")
    for k in range(i):
      print("#",end="")
    print()
# left_90(5)
'''
OP:
    #
   ##
  ###
 ####
#####
'''

def number_left_triangle(n):
  for i in range(n+1):
    for j in range(1,n-i+1):
      print(j,end="")
    print()
# number_left_triangle(5)

'''
OP:
12345
1234
123
12
1
'''
def pyramids(n):
  for i in range(0,n):
    #space
    for j in range(0,n-i-1):
      print(" ",end="")
    #symbol
    for k in range(0,2*i+1):
      print("#",end="")
    #space
    for l in range(n-i-1):
      print(" ",end="")
    print()

# pyramids(5)

#OR
def pyramids2(n):
  for i in range(0,n):
    print(" "*(n-i-1)+"#"*(2*i+1)+" "*(n-i-1))

# pyramids2(5)


'''
OP:
    #    
   ###   
  #####  
 ####### 
#########
'''
def upsiDown_pyramid(n):
  for i in range(0,n):
    print(" "* i + "#" * (2*(n-i)-1) + " "* i)

# upsiDown_pyramid(5)

'''
OP:
#########
 ####### 
  #####  
   ###   
    #  
'''