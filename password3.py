password = 'a123456'
x = 3 #剩餘機會
while x > 0:
	x = x - 1
	pwd = input('請輸入密碼:')
	if pwd == password:
		print('密碼正確')
		break
	else:
		print('密碼錯誤!')
		if x > 0:
			print('還有' , x ,'次機會')
		else:
			print('掰掰~')
