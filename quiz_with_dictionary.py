q1 = """ Is Python case sensitive when dealing with Identifiers?
a. Yes
b. No
c. Machind Dependent
d. None """

q2 = """ Which of the following is not a Keyword?
a. eval
b. local
c. assert
d. pass """

q3 = """ Which of these is floor division?
a. /
b. //
c.%
d. None """

q4 = """ What is the output of this 3*1**3?
a. 27
b. 9
c. 3
d. 1 """

q5 = """ "a"+"bc"=?
a. a
b. bc
c. bca
d. abc """

questions = {q1: "a", q2: "a", q3: "b", q4: "c", q5: "d",}

name = input("Enter your name: ")
print("Hello ",name, "Welcome to the quiz world")
score = 0

for i in questions:
	print()
	print(i)
	flag1 = input("Do you want to skip the question (yes/no): ")
	if flag1 == "yes":
		continue

	ans = input("Enter the answer (a/b/c/d): ")
	if ans == questions[i]:
		print("Correct answer you got 1 point")
		score += 1
		print("Current score is: ", score)
	else:
		print("Wrong answer you lost 1 point")
		score -=1
		print("Current score is: ", score)

	flag2 = input("Do you want to quit (yes/no): ")
	if flag2 == "yes":
		break

print("Final score is: ", score)
