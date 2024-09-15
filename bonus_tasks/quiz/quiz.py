import json

with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, " - ", alternative)
    user_answer = int(input("Enter your answer: "))
    question["user_answer"] = user_answer

score = 0
for index, question in enumerate(data):
    if question["user_answer"] == question["correct_answer"]:
        score = score + 1
        result = "Correct answer"
    else:
        result = "Wrong answer"
    message = f"{result} {index + 1}. Your answer: '{question['user_answer']}', " \
        f"correct answer: '{question['correct_answer']}'"
    print(message)

print(f"{score}\\{len(data)}")
