import utils
import sys,os
sys.path.insert(1, sys.path[1]+'/configmysql/')
import crud

<<<<<<< HEAD
def main(path,duration,date):
	#user=utils.user()
	#date=utils.date()
	#duration=utils.audio_duration(path)
=======


def main(path):
	user=utils.user()
	date=utils.date()
	duration=utils.audio_duration(path)
>>>>>>> master

	crud.Insert(user,path,duration,date)





