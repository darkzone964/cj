import random
import requests
import pyfiglet
import time

Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح

logo = pyfiglet.figlet_format("$ DARK $")
print(Z+logo)
time.sleep(2)
cj = pyfiglet.figlet_format("Ah shit, here we go again")
print(F+cj)

ID = input('ID ==»: ')
print('  ')
token = input(' TOKEN ==» : ')
print('''

''')
print(C+'''[1] USER 4 & 5
[2] USER 4
[3] USER 5
[4] USER 6

''')
H = input(X+' CHOOSE : ')

ku = ('{"account_created": false, "errors": {"email": [{"message": "Too many accounts are using a@gmail.com.", "code": "email_sharing_limit"}], "__all__": [{"message": "Create a password at least 6 characters long.", "code": "too_short_password"}]}, "dryrun_passed": false, "username_suggestions": [], "status": "ok", "error_type": "form_validation_error"}')

if H == '1':
	uus = '._irteaszxcv._1234567890'
	
	while True:
		dark = str(''.join(random.choice(uus) for i in range(5)))
	
		url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
	
		headers_kai={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',
                'content-length': '61',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/emailsignup/',
                'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
                'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
                'x-instagram-ajax': '72bda6b1d047',
                'x-requested-with': 'XMLHttpRequest'

            } 
            
            
		datas_kai={
                'email' : 'a@gmail.com',
                'username': f'{dark}',
                'first_name': 'AA',
                'opt_into_one_tap': 'false'
            }
		
		kd = requests.post(url,headers=headers_kai,data=datas_kai).text
		
		if ku in kd:
			print(F + ' yes HA HA HA HA ==»:  ' + dark)
			
			tlg =(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= 
صدتلك يوزر شبه رباعي

@{dark} ✓

@Ft_r5 π https://t.me/justpython1''')

			i = requests.post(tlg)


		else:
			print(Z + ' poop 💩 ==»:  ' + dark)

if H == '2':
	uus = 'qwertyuiopasdfghjklzxcvbnm._1234567890'
	
	while True:
		Ft_r5 = str(''.join(random.choice(uus) for i in range(4)))
	
		url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
	
		headers_kai={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',
                'content-length': '61',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/emailsignup/',
                'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
                'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
                'x-instagram-ajax': '72bda6b1d047',
                'x-requested-with': 'XMLHttpRequest'

            } 
            
            
		datas_kai={
                'email' : 'a@gmail.com',
                'username': f'{Ft_r5}',
                'first_name': 'AA',
                'opt_into_one_tap': 'false'
            }
		
		kd = requests.post(url,headers=headers_kai,data=datas_kai).text
		
		if ku in kd:
			print(F + ' yes HA HA HA 😎 ==»:  ' + Ft_r5)
			
			tlg =(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= 
صدتلك يوزر رباعي

@{Ft_r5} ✓

@Ft_r5 $ https://t.me/justpython1''')

			i = requests.post(tlg)


		else:
			print(Z + ' زربة ===»: ~ ' + Ft_r5)
			

if H == '3':
	uus = 'ertuioasjlzxcvn1234567890._'
	
	while True:
		nice = str(''.join(random.choice(uus) for i in range(5)))
	
		url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
	
		headers_kai={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',
                'content-length': '61',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/emailsignup/',
                'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
                'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
                'x-instagram-ajax': '72bda6b1d047',
                'x-requested-with': 'XMLHttpRequest'

            } 
            
            
		datas_kai={
                'email' : 'a@gmail.com',
                'username': f'{nice}',
                'first_name': 'AA',
                'opt_into_one_tap': 'false'
            }
		
		kd = requests.post(url,headers=headers_kai,data=datas_kai).text
		
		if ku in kd:
			print(F + ' Y ~ ' + nice)
			
			tlg =(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= 
صدتلك يوزر خماسي

@{nice} ✓

@Ft_r5 ♡ https://t.me/justpython1''')

			i = requests.post(tlg)

		else:
			print(Z + ' NOO ~ ' + nice)


if H == '4':
	uus = 'ertuioasjlzxcvn1234567890._'
	
	while True:
		help = str(''.join(random.choice(uus) for i in range(6)))
	
		url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
	
		headers_kai={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',
                'content-length': '61',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/emailsignup/',
                'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
                'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
                'x-instagram-ajax': '72bda6b1d047',
                'x-requested-with': 'XMLHttpRequest'

            } 
            
            
		datas_kai={
                'email' : 'a@gmail.com',
                'username': f'{help}',
                'first_name': 'AA',
                'opt_into_one_tap': 'false'
            }
		
		kd = requests.post(url,headers=headers_kai,data=datas_kai).text
		
		if ku in kd:
			print(F + ' Y ~ ' + help)
			
			tlg =(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= 
صدتلك يوزر سداسي

@{help} ✓

@Ft_r5 ༺https://t.me/justpython1༻''')

			i = requests.post(tlg)


		else:
			print(Z + ' NOO ~ ' + help)
			
