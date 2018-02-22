import sys

def toBool(answer):
	if answer[0]=='y':
		return True
	else:
		return False

def makeQuestion(question, yes, no):
	return [question, yes, no]

def createQuestion(question, rightAns, wrongAns):
	return [question, rightAns, wrongAns]

def validate(ans):
	if(ans=="yes" or ans=="no"):
		return True
	else:
		return False

def askQuestion(question):
	if (type(question).__name__ == "list"):
		return (raw_input(question[0])).lower()
	else:
		return raw_input("Were you thinking about %s?" % question).lower()

def playAgain():
  return toBool(raw_input("Do you want to play again?"))

def nextQuestion(question, answer):
	global tries
  	tries += 1
	if (type(question).__name__ == "list"):
		if answer: 
			return question[1]
		else:
			return question[2]
	else:
		if answer:
			print("I told you I can do it. I tool " + str(tries) + " tries"  )
			tries = 0
			if playAgain():
				tries = 0
				return firstQues 
			else:
				sys.exit(0)
		else:
			return makeNewQuestion(question)

def replaceAnswer(tree, find, replace):
  if not (type(tree).__name__ == "list"):
    if tree == find:
      return replace
    else:
      return tree
  else:
    return makeQuestion(tree[0], replaceAnswer(tree[1], find, replace), replaceAnswer(tree[2], find, replace))


def makeNewQuestion(wrongAns):
	global firstQues, tries
	correctAns = raw_input("I give up :(, What were you thinking about ??? ")
	question = raw_input("Enter a question that distinguishes %s from %s. "%(correctAns, wrongAns))
	answer = toBool(raw_input("If I asked you this question and you thought about %s, what would the correct answer be?" % correctAns).lower())
	if answer:
		newQuestion = [question, correctAns, wrongAns]
	else:
		newQuestion = [question, wrongAns, correctAns]
	ques = replaceAnswer(firstQues, wrongAns, newQuestion)
	firstQues = ques
	# print(str(answer) , ques)
	tries = 0
	return ques

tries = 0
firstQues = createQuestion("Can it swim ?", "Whale", "Pegion")
ques = firstQues
# print(ques)
while True:
	ans = askQuestion(ques)
	while not validate(ans):
		print("answer in only yes or no")
		ans = askQuestion(ques)
	ques = nextQuestion(ques, toBool(ans))
	
