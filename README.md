# stt-watson
Speech to text using watson in python with websocket and record from microphone

**Note:** To gain in performance response from watson are streamed and directly send to pyaudio to hear it.

## Requirements

- **Python 2.7**
- **Pip**
- **portaudio**, can be installed with `brew install portaudio` (mac) or `apt-get install portaudio19-dev`(linux)

## Installation

Install with pip: `pip install tts-watson`

## Run the playground

Simply run in command line: `tts-watson text to sound i want` (you will hear: `text to sound i want`)

**At the first launch it will create a config file located to `~/.config-tts-watson.yml` and ask you your watson credentials**

## Usage for developers

Bootstrap example:

```python
from tts_watson.TtsWatson import TtsWatson

ttsWatson = TtsWatson('watson_user', 'watson_password', 'en-US_AllisonVoice') # en-US_AllisonVoice is a voice from watson you can found more to: https://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/doc/text-to-speech/using.shtml#voices
ttsWatson.play("The text which i want to be a sound")
```


