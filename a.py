grades = {"Alex": 85, "Sam": 92, "Chris": 78, "Taylor": 95, "Jordan": 88}

total, highest, lowest = 0, float('-inf'), float('inf')
for score in grades.values():
    total += score
    if score > highest: highest = score
    if score < lowest: lowest = score


print("Class Average: {total / len(grades)}")
print("Highest Score: {highest}\nLowest Score: {lowest}")

name = input("\nWhose score would you like to look up? ").strip()
if name in grades:
    print("Great news! {name}'s current score is {grades[name]}.")
else:
    print("Sorry, we couldn't find a student named '{name}' in the system.")