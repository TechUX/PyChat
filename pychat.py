#PyChat by Devesh
import os,time
from datetime import datetime

def login():
	print("\nEnter Username to continue...")
	global username
	username = input("Username : ")
	print("\nUsername setted to ", username)
	time.sleep(2)
	chat()

def logout():
    username = 0
    if username == 0:
        print("Successfully Logout")
        time.sleep(2)
        os.system("clear")
        main()
    else:
        print("Something Wrong")
        main()

def message(user,msg):
    try:
        myfile = open("chat.txt","a")
    except FileNotFoundError:
        file = open("chat.txt","w")
        file.write("PyChat by Devesh")
        file.flush()
        file.close()
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    data = str(user)+" : ["+time+"] : "+str(msg)+"\n"
    myfile.write(data)
    myfile.flush()
    myfile.close()

def main():
	print("\t\t PyChat")
	print("\t\t\t -By Devesh Singh\n")
	print("Join the Conversation now \nLogin to proceed\n\nPress 1 for login or q for exit app\n")
	a = input("Press 1 to continue : ")
	if a =="1":
		login()
	elif a.lower()=="q":
		print("Exiting the program, wait for a while")
		time.sleep(1)
		os.system("clear")
		exit()
	else:
		about()

def chat():
	os.system("clear")
	print("Welcome to PyChat \n")
	print(" Enter 'logout' to logout when you want \n")
	try:
		file=open("chat.txt","r")
		str=file.read()
		print(str)
		file.close()
	except:
		print("No Chat  Present \nSomething Wrong")
		chatinput()
	chatinput()

def chatinput():
	content=input("Enter message : ")
	if username==0:
		print(" You are not Logged in ")
		main()
	else:
		if content=="logout":
			logout()
		elif content=="":
			chat()
		else:
			message(username,content)
	chat()

def about():
	os.system("clear")
	print("PyChat is a python based chat application Developed by Devesh Singh\n\n")
	login()

main()