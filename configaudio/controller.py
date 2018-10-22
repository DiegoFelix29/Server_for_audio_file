import utils
import sys,os
sys.path.insert(1, sys.path[1]+'/configmysql/')
import crud

def main(path,duration,date):
	#user=utils.user()
	#date=utils.date()
	#duration=utils.audio_duration(path)

	crud.Insert(user,path,duration,date)





