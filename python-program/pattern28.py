for i in range(1,6):
 print()
 x=65
 for j in range(5,0,-1):
      if j>i:
         print(" ",end="")
      else:
         print(chr(x),end="")
         x=x+1