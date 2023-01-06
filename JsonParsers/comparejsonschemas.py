import json
# convert to dict using load and compare dicts
with open("C:\\Users\\VARUN\\Desktop\Varun_Personal\\Automation_API\\courses.json") as f1:
    courses=json.load(f1)
    print(courses)


with open("C:\\Users\\VARUN\\Desktop\Varun_Personal\\Automation_API\\courses2.json") as f2:
    courses2=json.load(f2)
    print(courses2)

print(courses==courses2) # False as both contents are different
assert courses==courses2 # AssertionError