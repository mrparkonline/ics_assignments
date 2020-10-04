# U2A1 - Marking Program

# import statements
# import os
from os import listdir
from subprocess import check_output
import csv

# Grab the student scripts
files = filter(lambda x : x not in {'marker.py'} and x.endswith('.py'), listdir())

# Test Case Inputs
tests = [
    '9\n6\n6\n8\n',
    '5\n6\n6\n8\n',
    '8\n1\n2\n4\n',
    '8\n2\n2\n7\n'
]

# Test Case Answers
answers = ['Hang Up\n', 'Answer\n', 'Answer\n', 'Answer\n']

# Student results
class_result = []

# Testing each student's scripts
for script in files:
    cmd = 'python3 ' + script
    print('Current Student:', script.replace('.py',''))

    # result is a variable that holds the current student's test results
    result = [script.replace('.py','')]

    for test_num, test_case in enumerate(tests):
        try:
            current_execution = check_output(cmd, universal_newlines=True, input=test_case, shell=True)
        except:
            result += ['fail']
        else:
            result += ['pass']
    # end of for
    class_result.append(result)

class_result = sorted(class_result, key=lambda x : x[0])
# Tracking how many test cases were passed
for student in class_result:
    current_mark = student.count('pass')
    student.append(current_mark)

# Writing The Class Result to CSV
with open('result.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Creating First Row Label
    label = ['Student Number']
    for i in range(len(tests)):
        label.append('Test '+str(i+1))
    label.append('Total Mark out of:' + str(len(tests)))
    csv_writer.writerow(label)

    # Appending student results in order of student number
    for line in class_result:
        csv_writer.writerow(line)
