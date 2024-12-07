new_password = input('Enter new password: ')
while len(new_password) < 12:
   print('Password too short (min. 12 chars)')
   new_password = input('Enter new password: ')