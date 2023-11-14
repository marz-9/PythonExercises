#With fixed numbers
width=100
blocksize=5
blocknum=width//blocksize
B_black=blocknum//2
B_white=B_black-1
B_total=B_black+B_white
gap=blocksize/2
print("Number of blocks that fits the wall: "+str(blocknum))
print("Gap size: "+str(gap))
print("Total number of black and white blocks: "+str(B_total))

#By entering input
width=int(input("Enter the wall's width: "))
blocksize=int(input("Enter the size of the blocks: "))
blocknum=width//blocksize
B_black=blocknum//2
B_white=B_black-1
B_total=B_black+B_white
gap=blocksize/2
print("Number of blocks that fits the wall: "+str(blocknum))
print("Gap size: "+str(gap))
print("Total number of black and white blocks: "+str(B_total))
