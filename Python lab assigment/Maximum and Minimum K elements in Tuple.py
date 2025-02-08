'''Python - Maximum and Minimum K elements in Tuple'''

# Sample tuple
data = (5, 2, 9, 1, 5, 6, 8, 3)

# Define the value of K
K = int(input("Enter the value :: "))

# Convert the tuple to a sorted list
sorted_data = sorted(data)

# Extract the smallest K elements
min_k_elements = sorted_data[:K]

# Extract the largest K elements
max_k_elements = sorted_data[-K:]

print(f"The {K} smallest elements are :: {min_k_elements}")
print(f"The {K} largest elements are :: {max_k_elements}")
