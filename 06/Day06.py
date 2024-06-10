import fileinput 


def parse_input(data):
    answers = []
    curr_answers = []
    for line in data:
        print(line)
        line = line.strip()
        if not line:
            answers.append(curr_answers)
            curr_answers = []
        else:
            curr_answers.append(line)
    answers.append(curr_answers)
    return answers


ANSWERS = parse_input(fileinput.input())

def positive_answers(answers):
    positive = set()
    for item in answers:
        for char in item:
            positive.add(char)
    return len(positive)

def positive_answers_part_two(answers):
    print(answers)
    yes = {}
    people = 0
    count = 0
    if len(answers) == 1:
        return len(answers[0])
    else:
        for item in answers:
            people += 1
            for char in item:
                yes[char] = 1 + yes.get(char, 0)
        for value in yes.values():
            if value == people:
                count+=1
        return count

print(f"The sum of counts for part 1 is: {sum(positive_answers(a) for a in ANSWERS)}")
print(f"The sum of counts for part 2 is: {sum(positive_answers_part_two(a) for a in ANSWERS)}")