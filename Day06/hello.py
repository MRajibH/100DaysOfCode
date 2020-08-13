name = input("What is your name: ")
print(f'Hello {name}')

age = int(input("Age: "))

if age < 10:
    print(f"You're a kid {name} haaaa  ha ah ahah")
elif age >= 10 and age <= 50:
    print(f"You're a young man {name}")
else:
    print(f"you're are a old man {name}")
