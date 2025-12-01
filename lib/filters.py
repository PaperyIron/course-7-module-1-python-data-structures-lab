# This module contains functions for filtering student data.

def filter_students_by_major(student_list, major):
    filtered_students = [student for student in student_list if major in student]
    return filtered_students
    
