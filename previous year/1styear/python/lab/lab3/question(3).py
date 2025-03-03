#question(3)
score1=int(input('enter your number of boy'))
score2=int(input('enetr your number of boy'))
score3=int(input('enetr your number of girl'))
score4=int(input('enetr your number of girl'))
def boy_score(score1,score2):
	'''
	>>>boy_score(10,20)
	15.0
	>>>boy_score(10,10)
	10.0
	'''
	return (score1+score2)
def girl_score(score3,score4):
	'''
	>>>girl_score(10,10)
	10.0
	>>>girl_score(5,5)
	5.0
	'''
	return (score3+score4)
def average():
	 return ((boy_score(score1,score2)+girl_score(score3,score4))/4) 
print(average())