# Import Module
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# open Chrome
driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')

# Open URL 
url = '' #Just Paste Google Form link here
driver.get(url)


# Enter Details:
print("\n****Enter Details****\n")
print("Enter Number of Options in each Multiple Choice Question: ",end = "")
mul_options = int(input())
print("Enter Number of Options in each Checkbox Question: ",end = "")
checkbox_options = int(input())


# Display Details:
print("\n****Display Details****\n")

# No. of Multiple Choice Question
mul_choice = driver.find_elements(By.CLASS_NAME,'exportOuterCircle')
no_of_mul_choice = len(mul_choice)//mul_options
print("No. of Multiple Choice Question: ",no_of_mul_choice)

# No. of Checkbox Question
checkbox = driver.find_elements(By.CLASS_NAME,'exportInnerBox')
no_of_checkbox = len(checkbox)//checkbox_options
print("No. of Checkbox Question: ",no_of_checkbox)

# No. of Short Answer Type Question
short_ans = driver.find_elements(By.CLASS_NAME,'exportInput')
no_of_short_ans = len(short_ans)
print("No. of Short Answer Type Question: ",no_of_short_ans)

# No. of Long Answer Type Question
long_ans = driver.find_elements(By.CLASS_NAME,'exportTextarea')
no_of_long_ans = len(long_ans)
print("No. of Long Answer Type Question: ",no_of_long_ans)



# Enter Answers
print("\n****Enter Answers of Questions****\n")
answers = []

# Short Answer
ans_short_ans_list = []
for i in range(no_of_short_ans):
    ans_short_ans = input(f"For Short Answer {i+1}: ")
    ans_short_ans_list.append(ans_short_ans)
answers.append(ans_short_ans_list)

# Long Answer
ans_long_ans_list = []
for i in range(no_of_long_ans):
    ans_long_ans = input(f"For Long Answer {i+1}: ")
    ans_long_ans_list.append(ans_long_ans)
answers.append(ans_long_ans_list)

# Multiple Choice
ans_mul_list =[]
for i in range(no_of_mul_choice):
    ans_mul = int(input(f"For Multiple Choice {i + 1}, Enter Option number as Answer: "))
    ans_mul_list.append(ans_mul-1)
answers.append(ans_mul_list)

# Checkbox
ans_checkbox_list = []
no_of_checks = []
for i in range(no_of_checkbox):
    no_of_checks.append(int(input(f"Enter Number of boxes to be checked in Checkbox Type Question {i+1}: ")))
    ans_checkbox_list_list = []
    for j in range(no_of_checks[i]):
        ans_checkbox =  int(input(f"For Question {i+1}, Enter checkbox number(one at a time): "))
        ans_checkbox_list_list.append(ans_checkbox-1)
    ans_checkbox_list.append(ans_checkbox_list_list)
answers.append(ans_checkbox_list)


# Fill Answers
print("\n****Filling Answers****\n")

count = 0
# short answer
i = 0
for value in short_ans:
    value.send_keys(answers[count][i])
    i += 1
count+=1

# long answer
i = 0
for value in long_ans:
    value.send_keys(answers[count][i])
    i += 1
count+=1


# multiple choice
count_mul_options = 0
i = 0
for value in mul_choice:
    if i < no_of_mul_choice:
        mul_choice[answers[count][i]+count_mul_options].click()
        i += 1
        count_mul_options+=mul_options
    else:
        break
count +=1

# checkbox
count_checkbox_options = 0
i = 0
j = 0
for value in checkbox:
    if i < no_of_checkbox:
        for j in range(no_of_checks[i]):
            checkbox[answers[count][i][j]+count_checkbox_options].click()
        i+=1
        count_checkbox_options+=checkbox_options
    else:
        break
count+=1


time.sleep(5)
# click on submit button
submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
submit.click()

# # fill another response
# another_response = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
# another_response.click()

# close the window
driver.close()
