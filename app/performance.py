import random 

def Excellent(request):
	list_time_array = ['Excellent Performance','Thumbs UP','Great']
	random_num = random.choice(list_time_array) 
	return random_num
def Good(request):
	list_time_array = ['Good Performance','Try to Get Excellent','Superb']
	random_num = random.choice(list_time_array) 
	return random_num
def Average(request):
	list_time_array = ['Not Okay Improve','Average Skill','Try to Get Good Level']
	random_num = random.choice(list_time_array) 
	return random_num
def Poor(request):
	list_time_array = ['Poor Performance','You need to Improve your Skill','Improve']
	random_num = random.choice(list_time_array) 
	return random_num
def VeryPoor(request):
	list_time_array = ['Very Worst Performance','Better Luck Next Time','Very Poor']
	random_num = random.choice(list_time_array) 
	return random_num	