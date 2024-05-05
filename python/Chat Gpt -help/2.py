num_variables = int(input("Enter the number of variables you want to create: "))

# Creating variables dynamically and taking input for each
for i in range(1, num_variables + 1):
    variable_name = "variable" + str(i)
    variable_value = input(f"Enter the value for {variable_name}: ")
    
    # Using globals() to create variables dynamically
    globals()[variable_name] = variable_value

# Testing the variables
for i in range(1, num_variables + 1):
    variable_name = "variable" + str(i)
    print(f"{variable_name} = {globals()[variable_name]}")
