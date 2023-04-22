

#contents = infile.read()

#line = infile.readline()

#1
#key is ID and value is student name
def get_students(filename):
    """return a dictionary that contains student 
    names and ID numbers from the specified file"""
    student_names = {}
    with open(filename, encoding = 'utf8') as file:
        names = file.readlines()
        names.pop(0)
        for lines in names:
            id_num, first_name, last_name = lines.strip().split(",")
            student_names[id_num] = (first_name, last_name)
        return student_names
# insert it in that format
    
   
    
    
students_dict = get_students('class1.txt')
print(students_dict['7576240'])

students_dict = get_students('class1.txt')
for student_id,record in sorted(students_dict.items()):
    print(student_id,':',record)


#task 2

def get_exam_data(filename):
    """return a list containing all non-commented 
    and non-empty lines from the given file."""
    new_list = []
    with open(filename, encoding = 'utf8') as file:
        student_list = file.readlines()
        for line in student_list:
            line = line.strip()
            if line and not line.startswith("#"):
                new_list.append(line)
        return new_list
    

lines = get_exam_data('test1.txt')
# the following line prints out the lines in a nicer format
# your function should still be returning a list
print('\n'.join(lines))


#task 3
def get_student_responses(useful_lines):
    """take a list of lines as a parameter. 
    As described in the overview, it should return a dictionary 
    that has student ID numbers as keys and student responses as values."""
    response_dict = {}
    first_out = useful_lines.pop(0) 
    last_out = useful_lines.pop( len(useful_lines) - 1)
    for line in useful_lines:
        student_info = line.strip().split(",")
        response_dict[student_info[0]] = student_info[1]
    return response_dict 
            
            

test_lines = ['@begin:student_answers',
'123456,111222','@end:student_answers']
students_answers = get_student_responses(test_lines)
print(students_answers)    
    


        
    
    
    
    