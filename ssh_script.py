import subprocess

input_test_case = 1
input_test_case = "input_str_"+ str(input_test_case)

def command_executor(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output

command = "python3 test_cases.py "+ input_test_case
x = command_executor(command)
print(x)