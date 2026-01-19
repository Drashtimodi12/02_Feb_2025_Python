# *****
# *****
# *****
# *****
# *****

# lines = 7
# for j in range(lines):
#     for i in range(lines):
#         print("*",end="")
#     print()

# *
# **
# ***
# ****
# *****

# lines = 5
# for i in range(lines):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# lines = 5
# stars = 1
# for i in range(lines):
#     for j in range(stars):
#         print("*",end="")
#     print()
#     stars+=1


# *****
# ****
# ***
# **
# *

# lines = 5
# stars = lines
# for i in range(lines):
#     for j in range(stars):
#         print("*",end="")
#     print()
#     stars-=1

#     *
#    **
#   ***
#  ****
# *****

# lines = 5
# stars = 1
# space=lines-1
# for i in range(lines):
#     for k in range(space):
#         print(" ",end="")
#     for j in range(stars):
#         print("*",end="")
#     print()
#     stars+=1
#     space-=1


# *****
#  ****
#   ***
#    **
#     *


# lines = 5
# stars = lines
# space=0
# for i in range(lines):
#     for k in range(space):
#         print(" ",end="")
#     for j in range(stars):
#         print("*",end="")
#     print()
#     stars-=1
#     space+=1

#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# lines = 5
# stars = 1
# space=lines-1
# for i in range(lines):
#     for k in range(space):
#         print(" ",end="")
#     for j in range(stars):
#         print("*",end=" ")
#     print()
#     stars+=1
#     space-=1

#     *
#    ***
#   *****
#  *******
# *********
# lines = 5
# stars = 1
# space=lines-1
# for i in range(lines):
#     for k in range(space):
#         print(" ",end="")
#     for j in range(stars):
#         print("*",end="")
#     print()
#     stars+=2
#     space-=1

#   *
#  ***
# *****
#  ***
#   *

#     *
#    * *
#   *   *
#    * *
#     *


# lines = 7
# stars = 1
# space=lines-1
# mid =( lines//2)+1
# for i in range(1,lines+1):
#     for k in range(space):
#         print(" ",end="")
#     for j in range(stars):
#         print("*",end="")
#     print()
#     if i<mid:
#         stars+=2
#         space-=1
#     else:
#         stars-=2
#         space+=1


# lines = 7
# stars = 1
# space=lines-1
# mid =( lines//2)+1
# for i in range(1,lines+1):
#     for k in range(space):
#         print(" ",end="")
#     for j in range(stars):
#         if j==0 or j==stars-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
#     if i<mid:
#         stars+=2
#         space-=1
#     else:
#         stars-=2
#         space+=1


# *
# **
# * *
# *  *
# * *
# **
# *

# lines = 7
# stars = 1
# space=lines-1
# mid =( lines//2)+1
# for i in range(1,lines+1):
    
#     for j in range(stars):
#         if j==0 or j==stars-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
#     if i<mid:
#         stars+=2
#         space-=1
#     else:
#         stars-=2
#         space+=1


# 1
# 12
# 123
# 1234
# 12345

# lines = 5
# stars = 1
# for i in range(lines):
#     for j in range(stars):
#         print(j+1,end="")
#     print()
#     stars+=1





# 1
# 2  3
# 4  5  6
# 7  8  9  10
# 11 12 13 14 15

# lines = 5
# stars = 1
# num=1
# for i in range(lines):
#     for j in range(stars):
#         print(num,end="")
#         num+=1
#     print()
#     stars+=1


# 0
# 10
# 010
# 1010
# 01010

# lines = 5
# stars = 1
# for i in range(lines):
#     for j in range(stars):
#         print((i+j)%2,end="")
#     print()
#     stars+=1

# 0
# 01
# 010
# 0101
# 01010

# lines = 5
# stars = 1
# for i in range(lines):
#     for j in range(stars):
#         print(j%2,end="")
#     print()
#     stars+=1

# A 
# BC 
# DEF 
# GHIJ 
# KLMNO

# lines = 5
# stars = 1
# k = 'A'
# for i in range(lines):
#     for j in range(stars):
#         print(k,end="")       
#         c = ord(k)
#         c+=1
#         k = chr(c)
#     print()
#     stars+=1

lines = 5
stars = 1
k = 65
for i in range(lines):
    for j in range(stars):
        print(chr(k),end="")       
        k+=1
    print()
    stars+=1
