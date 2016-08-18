import os
import re

for filename in os.listdir("."):
	old_name = filename
	filename = re.sub('\#','',filename)
	filename = re.sub('\&','',filename)
	print old_name+":"+filename
	os.rename(old_name, filename)

