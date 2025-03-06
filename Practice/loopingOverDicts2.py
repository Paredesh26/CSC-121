students = {'Grade 4': [ # This is the first element.
    {"Student_name":"Chris","Math":87,"Sci": 99},
    {"Student_name":"Sussie","Math":88,"Sci": 100},
    {"Student_name":"George","Math":67,"Sci": 90}
    ],
    'Grade 5': [
    {"Student_name":"Jessica","Math":70,"Sci": 79},
    {"Student_name":"Simon","Math":80,"Sci": 80}
    ]}

# Dictionaries are 
# Grade 4 & 5 are the keys for this:
'''
for x in students:
    print(x)
'''
'''
for x in students:
    # This displays grade 4 & 5 with their lists
    print(x, students[x])
'''
'''
# Makes the information more organized and clear.
for grade, info in students.items():
    print(grade)
    # Iterate over list of scores
    for x in info:
        print(x)
'''

print(f'{"Grade":<8}{"Name":<10}{"Math":<8}{"Sci"}')
for grade, info in students.items():
    # Iterate over list of scores
    for x in info:
        print(x['Student_name'], x['Math'], x['Sci'])
        print(f'{grade:<8}{x["Student_name"]}{x["Math"]:<8}{x["Sci"]}')