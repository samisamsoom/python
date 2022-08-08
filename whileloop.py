num_of_tries=0
while num_of_tries != 3:
    username = input('please insert your username: ')
    password = input('please insert your password: ')
    if username == 'sami' and password == '123':
       print ('Welocme')
       num_of_tries = 0
       exit()
    else:
        print('Error')
        num_of_tries +=1
        print('you have ' + str(3 - num_of_tries) + " tries left")
