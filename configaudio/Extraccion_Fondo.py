from pydub import AudioSegment
from pydub.playback import play
import controller

def Extrac_Sonido(paths,filename):

	sound_stereo = AudioSegment.from_file(paths+"/"+filename, format="mp3")

	sound_monoL = sound_stereo.split_to_mono()[0]

	sound_monoR = sound_stereo.split_to_mono()[1]

	sound_monoR_inv = sound_monoR.invert_phase()

	sound_CentersOut = sound_monoL.overlay(sound_monoR_inv)

	destino=paths+"/"+filename[0]+"fondo.wav"
	sound_CentersOut.export(destino, format="wav")

	#ingreso a bd
	controller.main(destino)


	fil=filename[0]+"fondo.wav"

	return fil
