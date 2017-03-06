# Made by Carter


def main():
    out = []
    for __ in range(int(input())):
        out.append(valid_pairs(num_row_input(), num_row_input()))
        print(out[-1])
    print('\n'.join(out))


def valid_pairs(tutors, students):
    """Return the number of valid pairs between tutors and students."""
    # This is my original very inefficient code:
    # valid = len([print(t, s) for t in tutors for s in students if t < s])
    # return valid

    # Make dictionary of tutor values to closest valid student indices
    closest_student = dict()
    i = 0
    for t in tutors:
        try:
            while t > students[i]:
                i += 1
        except IndexError:
            pass
        closest_student.update({t: i})

    pairs = 0
    # For every tutor, add the number of students with scores below them
    for t in tutors:
        pairs += len(students[:closest_student[t]])
        # print(t, closest_student[t], pairs)
    return pairs


def num_row_input():
    """Return input(), split, as integers, except the first one."""
    return list(int(x) for x in input().split()[1:])

if __name__ == '__main__':
    main()
