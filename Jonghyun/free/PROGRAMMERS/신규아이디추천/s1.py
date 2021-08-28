new_id = "...!@BaT#*..y.abcdefghijklm"

# first => "...!@bat#*..y.abcdefghijklm"
# second => "...bat..y.abcdefghijklm"
# third => ".bat.y.abcdefghijklm"
# fourth => "bat.y.abcdefghijklm"
# fifth => "bat.y.abcdefghijklm"
# sixth => "bat.y.abcdefghi"
# seventh => "bat.y.abcdefghi"

def solution(new_id):
    answer1 = first_condition(new_id)
    answer2 = second_condition(answer1)
    answer3 = third_condition(answer2)
    answer4 = fourth_condition(answer3)
    answer5 = fifth_condition(answer4)
    answer6 = sixth_condition(answer5)
    answer7 = seventh_condition(answer6)
    return answer7


def first_condition(new_id):
    return new_id.lower()

def second_condition(new_id):
    answer = ''
    remove_str = '-_.'
    for i in new_id:
        if i.isdecimal() or i.isalpha() or i in remove_str:
            answer += i
    return answer

def third_condition(new_id):
    answer = ''
    answer += new_id[0]
    for i in range(1, len(new_id)):
        if new_id[i] == '.' and new_id[i-1] == '.':
            continue
        else:
            answer += new_id[i]
    return answer

def fourth_condition(new_id):
    answer = ''
    for i in range(len(new_id)):
        if i == 0 and new_id[0] == '.':
            continue
        elif i == len(new_id) - 1 and new_id[len(new_id) - 1] == '.':
            continue
        else:
            answer += new_id[i]
    return answer

def fifth_condition(new_id):
    answer = ''
    if not new_id:
        answer = 'a'
    else:
        answer = new_id
    return answer

def sixth_condition(new_id):
    answer = ''
    if len(new_id) >= 16:
        answer = new_id[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    else:
        answer = new_id
    return answer

def seventh_condition(new_id):
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    return new_id


print(solution(new_id))