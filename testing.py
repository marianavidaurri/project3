def get_students(filename):
    """return a dictionary that contains student 
    names and ID numbers from the specified file"""
    student_names = {}
    with open(filename, encoding = 'utf8') as file:
        names = file.readlines()
        names.pop(0)
        for lines in names:
            id_num, first_name, last_name = lines.strip().split(",")
            student_names[id_num] = [first_name, last_name]
        return student_names

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

def get_student_responses(useful_lines):
    """"""
    responses = {}
    student_answers = False
    for line in useful_lines:
        if not line.startswith("@"):
            line_list = line.split(",")
            print(line_list)
            student_id = line_list[0]
            answers = line_list[1]
            responses [student_id] = answers
    return responses


def grade_student(solution, answer):
    """take the correct answers for an exam and the answer 
    one student provided, and calculate the student's grade.""" 
    number_correct = []
    for idx in range(len(solution)):
        if solution[idx] == answer[idx]:
            number_correct.append(1)
    return len(number_correct)

print(grade_student('44121124334342412313', '44222221213334422314'))
print(grade_student('44121124334342412313', '33124114324423412341'))


     

    
def main():
    """the main function to call the other functions"""
    class_file_name = input("Enter class list file name:")
    test_file_name = input("Enter test data file name:")
    
    #two print statements with the file names
    print(f"Class file name = {class_file_name}")
    print(f"Test file name = {test_file_name}" )
    
    #4 - num qs
    student_info = get_students(class_file_name)
    exam_data_lines = get_exam_data(test_file_name)
    
    print(get_student_responses(exam_data_lines))
    
    print(f"Number of questions = {exam_data_lines[0][22:]}")
    solution = exam_data_lines[1][16:]
    
    #print(get_exam_data(test_file_name))
    print("-" * 40)
    print(f"Stud_Id Given_name  Family_name  Mark")
    #how to format this 
    print("-"* 40)
    for student_id, name_list in sorted(student_info.items()):
        print(f"{student_id} {name_list[0]}  {name_list[1]}  Mark")
        #[given_name, family_name] = value
        
#class1.txt
#test1.txt
    
main()   
    



