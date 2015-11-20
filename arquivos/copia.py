logo = open('python-logo.png','rb')
data = logo.read()
logo.close()

logo2 = open('python-logo.png', 'wb')
logo2.write(data)
print logo2
logo2.close
