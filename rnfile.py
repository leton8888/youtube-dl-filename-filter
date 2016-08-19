import os
import re
import fnmatch

directory = "/var/www/html/yd/download"
for file in os.listdir(directory):
	if fnmatch.fnmatch(file, '*'):
		path = os.path.join(directory, file)
		old_name = file
		file = re.sub('\#','',file)
		file = re.sub('\&','',file)
		target = os.path.join(directory, file)
		os.rename(path, target)


