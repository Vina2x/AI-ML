info= {
    "name": "Vina",
    "cgpa": 8.3,
    "subjects": ["english", "CS"]
}
print(info.keys())
print(info.values())
print(info.items())

# get method

print(info.get("cgpa"))

info.update({
    "city" : "Delhi"
})

print(info)