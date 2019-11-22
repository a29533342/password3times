x = 1
password = 'a123456'
while x <= 3:
	password = input('請輸入密碼:')
	if password == 'a123456':
		print('密碼正確')
		break
	else:
		print('密碼錯誤，剩',3-x,'次機會')
		x = x + 1
