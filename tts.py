from google.cloud import texttospeech
from createVid import *

def scriptTS(title, script, URL, publishTime):
    titleMP3 = ''.join(e for e in title if e.isalnum())
    titleMP3 = titleMP3 + ".mp3"
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.types.SynthesisInput(text=script)

    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-GB',
        name='en-GB-Wavenet-B'
            )

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    with open(titleMP3, 'wb') as out:
    # Write the response to the output file.
        out.write(response.audio_content)

    script = "View the full article and read more at: " + URL + "\n" + script
    createVideo(title, script, publishTime)
