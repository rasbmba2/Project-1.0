# Define empty set
s = set()
# Add objects in the set
s.add(1)
s.add(3)
s.add(2)
s.add(4)
s.add(3)  # It will not print any number twice
# print(s)  # It will print out {1,2,3,4} n


# Remove objects in the set

s.remove(2)
print(s)  # It will  print out {1,3,4})

# "len" is used to determine the length of squence.

print(f"The set has {len(s)} elements.")
