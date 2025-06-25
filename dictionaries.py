#Create a dictionary named student_scores where keys are student name
# and values are their scores(integers)
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "charlies": 78,
    "David": 95,
    "Eve": 88,
    "Frank": 70  #aded an extra student for more data
}
print("---Initial Student Scores---")
#iteratie through the dictionary and print each student's name and 
for name, score in student_scores.items():
    print(f"{name}:{score}")
print("\n")
#add a new student and their score to the dictionary
new_student_name = "Grace"
new_student_score = 90
student_scores[new_student_name] = new_student_score
print(f"---Added New student: {new_student_name} with score |{new_student_score}")
for name, score in student_scores.items():
    print(f"{name}:{score}")
print("\n")
#find the student with the highest score and print their name and score
if student_scores:  #ensure the dictionary   is not empty
    highest_score = 0
    highest_score_name = ""
    for name, score in student_scores.items():
        if score > highest_score:
            highest_score = score
            highest_score_name = name
    print(f"---Student with the Highest score---")
    print(f"{highest_score_name}:{highest_score}\n")
else:
    print("The diitionary is empty,cannot find the highest score.\n)")

high_achievers = {}
for name, score in student_scores.items():
    if score >= 90:
        high_achievers[name] = score

print ("--- High Achievers (Score 90 or above)---")
if high_achievers:
    for name, score in high_achievers.items():
        print(f"{name}: {score}")
else:
    print("No student scores 90 or above")
    
