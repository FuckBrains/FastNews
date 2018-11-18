import os
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip, concatenate_videoclips, TextClip
from nltk.corpus import stopwords
import datetime
from time import strftime

stopwords = set(stopwords.words('english'))

def createCredits(script):
    f = open("credit.txt", "r")
    credits = f.read()
#    fsc = open("script.txt", "r")
#    script = fsc.read()
    textBellow = script + credits
    return textBellow

def createKeywords(script):


    querywords = script.split()

    resultwords  = [word for word in querywords if word.lower() not in stopwords]
    script = ' '.join(resultwords)






    script = script.replace(" ", ",")
    script = script[:499]

    return script


def uploadVid(title, script, titleMP4, publishTime):
    sect = createCredits(script)
    epep = "python2.7 upload.py --file='"
    epep = epep + titleMP4
    epep = epep + "' --title='"
    epep = epep + title
    epep = epep + "' --description='"
    epep = epep + sect

    keyWords = createKeywords(script)

    epep = epep + "' --keywords='" + keyWords
    epep = epep + "' --category='25' --privacyStatus='private' --publishAt='" + str(publishTime.strftime("%Y-%m-%dT%H:%M:%S.0Z"))  + "'"
    print(epep)
    os.system(epep)
    os.system("rm *.mp*")


def createVideo(title, script, publishTime):
    intro = VideoFileClip("clips/intro.mp4")
    body = VideoFileClip("clips/body.mp4")
    loop = VideoFileClip("clips/loop.mp4")
    outro = VideoFileClip("clips/outro.mp4")


    titleMP3 = ''.join(e for e in title if e.isalnum())
    titleMP3 = titleMP3 + ".mp3"
 # title +  ".mp3"

    audioclip = AudioFileClip(titleMP3)

    scriptLen = audioclip.duration
    loopLen = loop.duration

    multiplier = scriptLen / loopLen

    new_audioclip = CompositeAudioClip([body.audio, audioclip])
    body.audio = new_audioclip

    x = [intro, body]
    multiplier = multiplier - 1
    while multiplier > 0 :
        x.extend([loop])
        multiplier = multiplier - 1

    x.extend([outro])
    final_clip = concatenate_videoclips(x)

    titleMP4 = ''.join(e for e in title if e.isalnum())
    titleMP4 = titleMP4 + ".mp4"


#    titleMP4 = title + ".mp4"
    final_clip.write_videofile(titleMP4)
    uploadVid(title, script, titleMP4, publishTime)

