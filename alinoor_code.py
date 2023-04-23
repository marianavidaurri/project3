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
        return  new_list

def get_student_responses(useful_lines):
    """"""
    responses = {}
    student_answers = False
    for line in useful_lines:
        if not line.startswith("@"):
            line_list = line.split(",")
            student_id = line_list[0]
            answers = line_list[1]
            responses [student_id] = answers
    return responses

def grader(responsess,solution):
         """finds and compares the grades of each student
           with the model answer, and then adds up the 
           total marks scored by each student"""
         dict=responsess
         model_answer=solution
         new_dict = {}
         for key in dict:
                if dict[key] == model_answer:
                    if key in new_dict:
                        new_dict[key] += 1
                    else:
                        new_dict[key] = 1
                else:
                        new_dict[key] = 0
         return new_dict

def marks_range(correct_anss):
    my_dict = correct_anss
    average = sum(my_dict.values()) / len(my_dict)
    minimum = min(my_dict.values())
    maximum = max(my_dict.values())
    print(f"Average mark: {average}")
    print(f"Minimum mark: {minimum}")
    print(f"Maximum mark: {maximum}")

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
    print(f"Number of questions = {exam_data_lines[0][22:]}")
    solution = exam_data_lines[1][16:]
    neew_list=get_exam_data(test_file_name)
    responsess=get_student_responses(exam_data_lines)
    correct_anss=grader(responsess,solution)

    print("-" * 40)
    print(f"Stud_Id Given_name  Family_name  Mark")
    print("-"* 40)
    for student_id, name_list in sorted(student_info.items()):
        print(f"{student_id} {name_list[0]}  {name_list[1]} " + str(correct_anss[student_id]))
    print("-"* 40)
    print("-"* 40)
    marks_range(correct_anss)

main()   
    


