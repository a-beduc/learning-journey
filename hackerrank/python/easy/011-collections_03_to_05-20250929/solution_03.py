import re
from collections import namedtuple

if __name__ == "__main__":
    N = int(input())
    Student = namedtuple('Student', re.sub(r'\s+', ' ', input()).split())
    students = []
    total = 0
    for _ in range(N):
        student = Student(*re.sub(r'\s+', ' ', input()).split())
        total += int(student.MARKS)
    average = total / N
    print(round(average, 2))


# more compact but less readable solution

# import re
# from collections import namedtuple
#
# if __name__ == "__main__":
#     N = int(input())
#     Student = namedtuple('Student', re.sub(r'\s+', ' ', input()).split())
#     total = sum(
#         int(Student(*re.sub(r'\s+', ' ', input()).split()).MARKS) for _ in
#         range(N))
#     print(round((total / N), 2))
