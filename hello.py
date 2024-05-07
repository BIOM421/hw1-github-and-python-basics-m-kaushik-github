def hello_world(): #Function to return specified string
    return "Hello World!" #Returning the string

def hello_world_n(N):
    N = int(N)  # Convert string N to int N
    result_1 = "Hello World! " * (N-1) + "Hello World!"   # Perform string multiplication
    return result_1  # Return the result