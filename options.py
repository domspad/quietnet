rate = 44100  #pitch related (diff with freq?)
freq = 500			# chosen because it is outside most people's hearing and worked for my microphone and speakers
channels = 1   #pitch and speed related - only can be 1 or 2
frame_length = 10 #size of beeps
chunk = 256		#size of beeps
datasize = chunk * frame_length
sigil = "00"

"""
For making sense of psk:
freq 500
frame_length = 20

"""