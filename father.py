from win32com.client import Dispatch

def speak(str1):
	speak=Dispatch(("SAPI.SpVoice"))
	speak.Speak(str1)

if __name__=="__main__":
	with open("dad.txt") as f:
		for item in f.readlines():
			speak(item)
			print(item)