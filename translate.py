import re
number = 0
with open('1.srt' , 'r') as file:
    with open('1_1.srt' , 'w') as file_2:

        for line in file:

            if re.search('[a-zA-Z]', line):
                print(line)
                number += 1
                file_2.write(f"{line}\n")

            
file.close()