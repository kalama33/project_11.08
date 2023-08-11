from my_package import greet_module_a, greet_module_b

with open("output.txt", "w") as f:
    f.write(greet_module_a() + "\n")
    f.write(greet_module_b() + "\n")
    
with open("output.txt", "r") as f:
    contents = f.read()
    print(contents)
    
