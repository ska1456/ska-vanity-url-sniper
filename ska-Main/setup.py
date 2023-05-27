import os

# Title : 1456
# Date : 27/05/2023
# Author : https://github.com/ska1456

if os.name == "posix":
	os.system('python3 -m pip install -U colorama\n')
	os.system('python3 -m pip install -U requests\n')
	os.system('python3 -m pip install -U psutil\n')
elif os.name == "nt":
	os.system('py -3 -m pip install -U colorama\n')
	os.system('py -3 -m pip install -U requests\n')
	os.system('py -3 -m pip install -U psutil\n')
else:
	print("Unsupported system.")