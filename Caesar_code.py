plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if char==" ":
        encrypted_text=encrypted_text+" "
        continue
    if char=="z":
        encrypted_text=encrypted_text+"a"
        continue
    if char=="Z":
        encrypted_text=encrypted_text+"A"
        continue
    a = ord(char)+1
    a=chr(a)
    encrypted_text=encrypted_text+a

print(plain_text)
print(encrypted_text)