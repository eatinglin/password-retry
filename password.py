password = 'a123456'

"""
#v1.
i = 1
while True:
	usertest = input('請輸入密碼： ')
	if usertest == password:
		print('登入成功！')
		break
	elif usertest != password:
		print('密碼錯誤！還有', 3 - i,'次機會')
		if i == 3:
			break
	i = i + 1		
"""


#v2.
i = 3
while i > 0:
	i = i -1
	usertest = input('請輸入密碼： ')
	if usertest == password:
		print('登入成功！')
		break
	elif usertest != password:
		print('密碼錯誤！')
		if i != 0:
			print('還有', i, '次機會')
		else:
			print('已經沒有機會了')


