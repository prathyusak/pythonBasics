# import <module>
# dir(<module>)  #<returns a list of all module functions>
# help(<module>) #<returns an extensive manual page created from the module's docstrings>
########################
#Operating System Interface
import os
cwd = os.getcwd()      #C:\Users\Rajesh\Desktop\python\learning\tutorial
# os.chdir('/server/accesslogs') 
os.chdir(cwd)
print(cwd)
# os.system('mkdir today')  #Creates directory today in os.getcwd()
# os.system('notepad')

# import shutil
# shutil.copyfile('data.db', 'archive.db')
# shutil.move('today', 'installdir')

import glob
os.chdir('../')
print(os.getcwd())   # C:\Users\Rajesh\Desktop\python\learning
print(glob.glob('*.py')) #['classmethodVSstaticmethod.py', 'decorator_auth.py', 'dunder_methods.py', 'fibnacci.py', 'functions.py', 'lambda_exp.py', 'multiple_inheritance.py', 'polymorphism.py', 'scratch.py']

########################
#Command Line Arguments

import sys
print(sys.argv)          #['c:/Users/Rajesh/Desktop/python/learning/tutorial/stdlibrary.py']

##########################
#Error Output Redirection and Program Termination
sys.stderr.write('Warning, log file not found starting a new one\n')
sys.stdout.write('writing output')
sys.stdin.read(1)