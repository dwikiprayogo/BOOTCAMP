from fbthon import Facebook
from fbthon import Web_Login
import time

user_agent = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0.1; SM-J510GF Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36'}
email = "" # Ganti email ini dengan email akun Facebook kamu
password = "" # Ganti password ini dengan password Akun Facebook kamu
login = Web_Login(email,password, headers = user_agent)
cookie = login.get_cookie_str() # Ini adalah cookie akun Facebook kamu
#banned
# cookie = "datr=B5kPZlS6br6rSseoowNyagRZ;sb=B5kPZsPcn1QOxdqklcdZ-LOx;noscript=1;c_user=100081949492595;xs=11%3A1_mFrjp5s2hp1Q%3A2%3A1712298248%3A-1%3A2395;fr=0gmph6HHlo9CTUKpa.AWUWPXa2GaGFi-KmTuNhRIQBF7o.BmD5kI..AAA.0.0.BmD5kI.AWWiaIMebBY;ps_n=0;ps_l=0;m_page_voice=100081949492595;"
# cookie = "c_user=100016091942923;datr=WJ0PZgtJMfFLXcskJ5SV-Wxh;fr=08haX0O5EdplNU9cu.AWV40e76kCbrHlLzFkSp8Xc3bLg.BmD51Z..AAA.0.0.BmD51Z.AWWLzQSEeos;m_page_voice=100016091942923;noscript=1;ps_l=0;ps_n=0;sb=WJ0PZgfbOh6RTYjg92WtxcVa;xs=40%3AsjpVuYi83RVCCA%3A2%3A1712299353%3A-1%3A10087;"
fb = Facebook(cookie)
listOfAccount = ['renzi.prayuda']

for account in listOfAccount:
  profile_info = fb.get_profile(account)
  # profile_info = fb.get_posts(account, 10)
  # printing numbers
  print(profile_info._user_info)
  # print(profile_info)
  # adding 2 seconds time delay
  time.sleep(60)
