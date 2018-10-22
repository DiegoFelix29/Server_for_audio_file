from pydub import AudioSegment
from pydub.playback import play
import controller
<<<<<<< HEAD
=======

#RUTA DE EL ARCHIVO A MODIFICAR
#link='/home/diego/Escritorio/quechua.mp3'

#FUNCION PARA EJECUTAR EL CAMBIO DE EXTRACCION DE SONIDO
>>>>>>> master

def Extrac_Sonido(paths,filename):

	sound_stereo = AudioSegment.from_file(paths+"/"+filename, format="mp3")

	sound_monoL = sound_stereo.split_to_mono()[0]

	sound_monoR = sound_stereo.split_to_mono()[1]

	sound_monoR_inv = sound_monoR.invert_phase()

	sound_CentersOut = sound_monoL.overlay(sound_monoR_inv)

<<<<<<< HEAD
=======
# EXPORTACION DEL DOCUMENTO
>>>>>>> master
	destino=paths+"/"+filename[0]+"fondo.wav"
	sound_CentersOut.export(destino, format="wav")

	#ingreso a bd
<<<<<<< HEAD
	controller.main(destino,duration,date)
=======
	controller.main(destino)
>>>>>>> master


	fil=filename[0]+"fondo.wav"

	return fil
