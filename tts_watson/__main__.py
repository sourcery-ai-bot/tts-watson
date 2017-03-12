import os.path
import argparse
import anyconfig
from tts_watson.TtsWatson import TtsWatson
import bunch
import requests
import sys


def main():
    
    py3_input_conversion = lambda x: input(x) if sys.version_info.major >=3 else raw_input(x)
    
    requests.packages.urllib3.disable_warnings()
    defaultConfig = {
        'url': 'https://stream.watsonplatform.net/text-to-speech/api',
        'user': 'user',
        'password': 'password',
        'voice': 'en-US_AllisonVoice',
        'chunk': 2048
    }
    home = os.path.expanduser("~")
    defaultConfigFile = home + '/.config-tts-watson.yml'
    parser = argparse.ArgumentParser(
        description='Text to speech using watson')

    parser.add_argument('-f', action='store', dest='configFile', default=defaultConfigFile,
                        help='config file',
                        required=False)
    parser.add_argument('text_to_transform', action='store', nargs='+')
    args = parser.parse_args()
    conf = anyconfig.container(defaultConfig)
    if not os.path.isfile(args.configFile):
        print("Config file '" + args.configFile + "' doesn't exist.")
        print("Creating it ...")
        user = py3_input_conversion("Watson user: ")
        password = py3_input_conversion("Watson password: ")
        bconf = bunch.bunchify(conf)
        bconf.user = user
        bconf.password = password
        anyconfig.dump(bconf.toDict(), args.configFile)
    else:
        conf = anyconfig.load(args.configFile)
    bconf = bunch.bunchify(conf)
    ttsWatson = TtsWatson(bconf.user, bconf.password, bconf.voice, bconf.url, bconf.chunk)
    ttsWatson.play(" ".join(args.text_to_transform))


if __name__ == "__main__":
    main()
