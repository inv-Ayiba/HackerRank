# Enter your code here. Read input from STDIN. Print output to STDOUT
# Number of test cases
n = int(input())

# Loop through each test case
for _ in range(n):
    try:
        # Read the input values
        a, b = input().split()
        
        # Perform integer division and print the result
        print(int(a) // int(b))
    except ZeroDivisionError as e:
        # Handle division by zero error
        print("Error Code:", e)
    except ValueError as e:
        # Handle invalid literal error
        print("Error Code:", e)
