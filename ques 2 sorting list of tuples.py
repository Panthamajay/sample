#tuples =[(5,3,4),(8,2,3),(1,5,6)]
#n=input("enter the number of tuples")
final_list = []
#for i in n:
print("enter data in a format such that One line for one tuple and space inside the line to separate tuple items.")
print("Insert a blank line to mark the end of input")
line = input("Enter the list of tuples: \n")
while(line != ''):
    final_list.append(tuple(line.split()))
    line = input()
 
print("input given:", final_list)
    
tuples2=sorted(final_list,key=lambda x:x[-1])
print(" sorted list of tuples :",tuples2)
