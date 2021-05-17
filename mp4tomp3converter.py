from moviepy.editor import *
import os
print ("""
############################
# Coder: Cüneyt TANRISEVER #
############################
""")
dosyalar = os.listdir()
mp4dosyalar=[]
dosy1a=open("hatali1.txt","w")
dosy1a.close()
dosy1a=open("hatali1.txt","a")
for dosya in dosyalar:
    if dosya.endswith(".mp4") :
        mp4dosyalar.append(dosya)
        print (dosya)
        
for mp41 in mp4dosyalar:
    try:
        print (mp41)
        mp3=mp41.replace(".mp4",".mp3").replace(" ","_")
        dex1=str(mp41)
        videoclip = VideoFileClip(dex1)
        audioclip = videoclip.audio
        audioclip.write_audiofile(mp3)
        audioclip.close()
        videoclip.close()
    except:
        dosy1a.write(str(i))
        continue