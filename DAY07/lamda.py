people = [
    {"Name": "Rajib", "District": "Bagerhat"},
    {"Name": "Moonmoon", "District": "Dhaka"},
    {"Name": "Raisha", "District": "Khulna"}
]
people.sort(key=lambda person: person["Name"])
print(people)
