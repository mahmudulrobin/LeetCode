class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        l=len(students)
        while sandwiches and students and sandwiches[0] in students:
            if sandwiches[0]==students[0]:
                sandwiches.pop(0)
                students.pop(0)
            else:
                temp=students.pop(0)
                students.append(temp)
        return len(sandwiches)