
import subprocess
import re

path='/home/diego/Escritorio/quechua_next.wav'

process = subprocess.Popen(['ffmpeg',  '-i',path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdout, stderr = process.communicate()
matches = re.search(r"Duration:\s{1}(?P<hours>\d+?):(?P<minutes>\d+?):(?P<seconds>\d+\.\d+?),", stdout, re.DOTALL).groupdict()

print (matches['hours']+":"+matches['minutes']+":"+matches['seconds'])
#print matches['minutes']
#print matches['seconds']

































