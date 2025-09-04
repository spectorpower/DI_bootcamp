MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%''' 
matrix = MATRIX_STR.split('\n')
matrix_rows = [] #making empty list
for row in matrix:
    if row.strip():
        matrix_rows.append(list(row)) # here we made 2d list inside the list 

print(matrix_rows) #here is return for exercise 
#now we need to transpose the matrix by index 
longest_row = len(max(matrix_rows)) #here we finding the longest element in the list 
# print(longest_row) 
matrix_columns = [] #making empty list
for i in range(0,longest_row): #making a loop with range starting from 0 and end at 3 character list
    column = [] #empty list for each column
    for row in matrix_rows: #making a loop on matrix rows
        if i < len(row): #if the row is less than 3 char
            column.append(row[i]) #adding each element from row to the respective column
    matrix_columns.append(column) #adding the column list inside the outside list of matrix columns 
    
print(matrix_columns)#here is return  for exercise 

message = "" #string
symbol = False #making a flag to keep counting how many symbols we have in a internal list
for col in matrix_columns:  #outside loop 
    for char in col: #inside loop 
        if char.isalpha(): #if each char is a letters 
            message += char #adding char to the empty message 
            symbol = False #turn flag down
        else:
            if not symbol: #if flag is turned down we add the space
                message += " "
                symbol = True #resetting the flag 
print(message.strip()) #strip deletes spaces in the beginning and at the eand of string

# review functions and add to the each block of code its function 









