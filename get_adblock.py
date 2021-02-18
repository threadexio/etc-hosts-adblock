#!/usr/bin/env python3
from shutil import copyfile
import requests
import re

list = 'adlists.list'
out = 'hosts.new'

backup = 'hosts.bak'

class COLOR:
	Green  = '\033[0;32m'
	Yellow = '\033[0;33m'
	Blue   = '\033[0;34m'
	Reset  = '\033[0m'

urls = []
# \b([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}\b
# Read the urls
with open(list, 'r') as f:
	for line in f.readlines():
		urls.append(line.strip())
	f.close()

print(COLOR.Blue + '\n[*]' + COLOR.Reset + f' Urls to get: {len(urls)}')
print(COLOR.Blue + '[*]' + COLOR.Reset + f' Writting to: {out}\n')

# Get the original size of hosts
with open(backup) as f:
	original_size = len(f.readlines())
	f.close()

# Backup the current hosts file
copyfile('/etc/hosts', backup)
copyfile('/etc/hosts', out)

new_size = original_size
with open(out, 'a') as f:
	f.write('\n')
	for url in urls:
		print(COLOR.Blue + '[*]' + COLOR.Reset + f' Getting {url}\r', end='')
		res = requests.get(url)
		if res.status_code != 200:
			print(COLOR.Yellow + '[!]' + COLOR.Reset + f' Failed to get {url}')
			continue
		lines = res.text.split('\n')

		for line in lines:
			line = line.strip()
			if line != "":
				if line[0] != "#" and "localhost" not in line:
					if re.search("^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}(\\s+|\\t+)\\b([a-z0-9]+(-[a-z0-9]+)*\\.)+[a-z]{2,}\\b$", line):
						f.write(line + '\n')
					elif re.search("\\b([a-z0-9]+(-[a-z0-9]+)*\\.)+[a-z]{2,}\\b", line):
						f.write('0.0.0.0 ' + line + '\n')


		print(COLOR.Green + '[✔]' + COLOR.Reset + f' Got url {url} with {len(lines)} domains')
	print(COLOR.Blue + '\n[*]' + COLOR.Reset + f' New hosts file: {out}')
	print(COLOR.Blue + '[*]' + COLOR.Reset + f' Domains on blocklist: {new_size-original_size}')
	f.close()
