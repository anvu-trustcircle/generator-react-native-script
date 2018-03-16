from subprocess import call as os_call
import os

def call(array):
  log_call = '$ ' + ' '.join(array)
  print log_call
  os_call(array)

def write_line(filename, line):
  file = open(filename, 'w')
  file.write(line)
  file.close()

def call_cd(directory):
  os.chdir(directory)
