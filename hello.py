def hello_world(): #Function to return specified string
    return "Hello World!" #Returning the string
result = hello_world() #Storing the returned string in a variable 
print (result) #Printing the variable 

def hello_world_n(N):
    N = int(N)  # Convert string N to int N
    result_1 = "Hello World! " * N  # Perform string multiplication
    return result_1

# Ask user for input N
N = input("Enter your argument [integer only]: ")    

# Call the function after taking input N and print the result
result_1 = hello_world_n(N)
print(result_1)