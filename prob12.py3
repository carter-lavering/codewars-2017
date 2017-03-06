# made by Carter
for __ in range(int(input())):
    tutors = [int(x) for x in input().split()][1:]
    students = [int(x) for x in input().split()][1:]
    print(tutors)
    tutors = [t for t in tutors if t > min(students)]
    if not tutors:
    	print(0)
    	continue
    students = [s for s in students if s < max(tutors)]
    if not tutors or not students:
    	print(0)
    	continue
    valid_pairs = 0
    for t in tutors:
        for s in students:
            if t > s:
                valid_pairs += 1
    print(valid_pairs)
