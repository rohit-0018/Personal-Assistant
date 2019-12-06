from termcolor import cprint ,colored

def display_speak():
	speak_display = r'''
	                _____    _____   ______
	               |        |     | |           /\      |     /
	               |        |     | |          /  \     |    /  
	               |_____   |_____| |______   /    \    |   /
	                     |  |       |        /------\   |  /\
	                     |  |       |       /        \  | /  \  
	                _____|  |       |_____ /          \ |/    \ O o . 

	'''

	mic = r'''
			 _____ 
			|-----|
			|-----|
			|_____| 
			  | |
			  | |
			  | |
			'''
	cprint(mic,'yellow',attrs = ['blink'])
	cprint(speak_display,'red')
	# print(speak_display)
# display_speak()
	# cprint(speak_display,'red')
# display_speak()

# def welcome_text()
# 	int t=0;
# 	while(t++)
# 		{
# 			if(t<10)
# 				print('')
# 		}
# welcome_text()