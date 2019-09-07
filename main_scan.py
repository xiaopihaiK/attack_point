import os
import time
import random
# import httptitle
import requests
import re
#import check_weblogic
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}

print '-'*70
print '*'*20 + 'Masscan + WebFin (SealGod of NanJing)' + '*'*20
print '-'*70

# def login(url , web_content,title_login,headers_login):
# 	# host_ip = url.split('http://')[1].split(':')[0]
# 	if 'login.as' in web_content or 'login.ph' in web_content or 'login.js' in web_content:
# 		print str(title_login) + '----' + str(url) + '---- Possible is Login Page!!!'
# 		print str(headers)
# 		print '-'*70


def title(ip_port):
	for i in ip_port:
		all_headers=[]
		all_headers_res = []
		try:
			url = 'http://'+i
			r=requests.get(url=url,timeout=5,headers=headers)
			for v in r.headers:
				res_headers = str(v)+':'+str(r.headers[v])
				all_headers.append(str(r.headers[v]))
				all_headers_res.append(res_headers)
			# content = r.content
			title = re.findall('<title>(.*?)</title>',r.content)
			if len(title) != 0:
				#login(url = url ,web_content = r.content , title_login = str(title[0].decode('utf-8')) , headers_login = str(all_headers_res))
				if '.jsp' in r.content or '.action' in r.content or 'JSESSIONID' in all_headers:
					print str(title[0].decode('utf-8')) + '----' + str(url) + '---- Possible is Struts2!!!'
					print str(all_headers_res)
					print '-'*70
				else:
					print str(title[0].decode('utf-8')) + '----' + str(url)
					print str(all_headers_res)
					print '-'*70
			else:
				title_weblogic = re.findall('<TITLE>(.*?)</TITLE>',r.content)
				if len(title_weblogic) !=0:
					if 'From RFC 2068' in r.content or 'WebLogic' in all_headers or 'Servlet/' in all_headers:
						print str(url) + '---- Weblogic!!!'
						print str(all_headers_res)
						print '-'*70
						#check_weblogic.check(url=i)
				else:
					pass
		except Exception as e:
			print str(url) + '---- Error'


def deal_ip(masscan_need_deal):
	f=open(masscan_need_deal,'r')
	for i in f.readlines():
		line = i.strip('\n')
		if '#' in line:
			pass
		else:
			line_data = line.split(' ')[3]+':'+line.split(' ')[2]
			masscan_scan_ip.append(line_data)
	title(ip_port = masscan_scan_ip)


def masscan(ip_c,flag,masscan_flag):
	filename = str(flag)+'.txt'
	masscan_filename = str(masscan_flag)+'.txt'
	print 'Create tmp file is %s\n'%str(filename)
	print 'Create masscan file is %s\n'%str(masscan_filename)
	# print filename
	f=open(filename,'a')
	masscan_command = './masscan -p80-90,7000-10000 --max-rate 10000 -oL %s'%str(masscan_filename)+ ' %s'%str(ip_c)
	os.popen(masscan_command)
	deal_ip(masscan_need_deal=masscan_filename)


if __name__ == "__main__":
	masscan_scan_ip = []
	ips = raw_input('Please input IPS:')
	ip = []
	ip_3 = ips.split('.')[0]+'.'+ips.split('.')[1]+'.'+ips.split('.')[2]
	if '/' in ips:
		flag = random.randint(0,99999)
		masscan_flag = random.randint(0,200000)
		masscan(ip_c=str(ips),flag=flag,masscan_flag=masscan_flag)
		for i in range(0,255):
			ip_main = ip_3 + '.'+ str(i)
			ip.append(ip_main)
	else:
		ip.append(ips)
