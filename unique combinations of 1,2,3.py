# Define the elements
elements = [1, 2, 3]
# Loop through each element and print all combinations
for i in range(len(elements)):
for j in range(i + 1, len(elements) + 1):
print(elements[i:j]