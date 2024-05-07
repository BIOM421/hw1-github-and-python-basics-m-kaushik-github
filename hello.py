#Function to return specified string
def hello_world():
    return "Hello World!"

#Storing the returned string in a variable
result = hello_world()

#Printing the variable 
print (result)

#Asking user for input N
print("Enter your argument [integer only]")
N = input()    

#Function taking a string N and returning N repetitions of a string 
def hello_world_n(N):
    #Converting string N to int N and performing string multiplication
    N = int(N)
    new_string = "Hello World! "*N
    print (new_string)
    return 0;
#Calling the function after taking input N
hello_world_n(N)