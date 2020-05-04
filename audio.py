import asyncio
from asyncio import sleep

import hashlib
import os

from pydub import AudioSegment
from pydub.playback import play

import requests
import boto3

import configparser

working = True


async def speak():
    conf = configparser.ConfigParser()
    conf.read('conf.ini')

    polly_client = boto3.Session(
        aws_access_key_id=conf['aws']['access_key_id'],
        aws_secret_access_key=conf['aws']['secret_access_key'],
        region_name='eu-west-1').client('polly')

    #    aws_access_key_id='***REMOVED***',
    #    aws_secret_access_key='***REMOVED***',

    speech_dir = os.path.join(os.path.dirname(__file__), "speech_data")
    if not os.path.exists(speech_dir):
        os.mkdir(speech_dir)

    previous_hash = ''
    while working:
        response = requests.get('http://localhost:8000/active/sunday-quiz-15883998427516189/speech/')
        response.raise_for_status()
        json_response = response.json()

        speech = json_response['speech']
        speech_hash = hashlib.sha224(speech.encode('utf-8')).hexdigest()

        if speech_hash != previous_hash:
            filename = f"{speech_hash}.mp3"
            full_path = os.path.join(speech_dir, filename)

            if not os.path.exists(full_path):
                print("Fetching speech")
                print(speech)
                response = polly_client.synthesize_speech(
                    VoiceId='Emma',
                    OutputFormat='mp3',
                    Text=speech,
                    Engine='neural'
                )

                with open(full_path, 'wb') as file:
                    file.write(response['AudioStream'].read())

            voice = AudioSegment.from_mp3(full_path)
            play(voice)

        previous_hash = speech_hash
        await sleep(1)


def main():
    loop = asyncio.get_event_loop()
    try:
        asyncio.ensure_future(speak())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing Loop")
        loop.close()


if __name__ == '__main__':
    main()
