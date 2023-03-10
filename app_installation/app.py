from flask import Flask, render_template, request, url_for, redirect

from record_mult import *
from save_wav_channel import *
from pred_audio import *
from mfccs import *
from icns import *
from instr import *
from filename import *
from normalise2 import *
from spedisci import *
from match import *
from salva_audio import *

import time # time.sleep
import requests # requests.get, requests.post
import random
import threading # for background job
import pyaudio # get_device_count, get_device_info_by_index

# mics 1, 2 e 3 -> contact mics
# mic 4 -> record instruments/voice
# mic 5 -> record installation

mic_instruments = 1
mic_installation = 2

recording_device = 5


webserver_url = 'https://www.amotion.cc'
#webserver_url = 'http://localhost:8000'

listen_port = 5000


app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def menu():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        if request.form.get("submit_a"):
            coeff1=0

            
            
# record from mic 4, save into f0.wav, extract a single channel and save it to recorded.wav       
            record_mult('f0.wav', recording_device)
            wav = wave.open('f0.wav')
            save_wav_channel('recorded.wav', wav, mic_instruments - 1)

# submit recorded.wav to the web server
            with open('recorded.wav', mode='rb') as file:
                wavData = file.read()

            try:
                print('submitting recording to web server')
                url = webserver_url + '/submit_recording'
                print('url: ' + url)
                res = requests.post(
                    url = url,
                    data = wavData,
                    headers = { 'Content-Type': 'application/octet-stream' })
                print('response: (' + str(res.status_code) + ') ' + res.text)
            except Exception as e:
                print('failed to submit recording to web server: ' + str(e))

    return render_template('index.html')


# try to fetch the recording from the global app
def fetchRecording():
    try:
        url = webserver_url + '/fetch_recording'
        #print('fetching recording from url: ' + url)
        res = requests.get(url)
        if res.status_code == 200:
            print('received a recording!')
            return res.content
        else:
            print('no recording received')
        return None
    except:
        print('failed to fetch recording from web server')
        return None


# analyse the recording and make a prediction
def analyzeRecording(wavData):
    with open('f0.wav', mode='wb') as file:
        file.write(wavData)
    wav = wave.open('f0.wav')
    print('wav nframes: ' + str(wav.getnframes()))
    save_wav_channel('recorded.wav', wav, 0)

    a, b, c, d, MFCCs = mfccs('recorded.wav')
    result = pred_audio(a, b, c, d)
    print(result)
    r1 = random.randint(1,8)
    r2 = random.randint(9,16)
    r3 = random.randint(17,24)
    r4 = random.randint(24,38)
    print(r1, r2, r3, r4)
    
# save the classified files in the corresponding folders
    salva_audio('recorded.wav', result)

# select action (Imitation, Contradiction, New, Silence)
    k = icns()
    if k==0:
        print('imitate')
    elif k==1:
        print('contradict')
    elif k==2:
        print('something new')
    else:
        print('something quiet')

# generate the name of the file from which to extract the MFCCs          
    fn=filename(k, result)

# extract MFCCs
    a, b, c, d, MFCCs = mfccs(fn)
    
# normalize mfccs 
    norm = normalise2(MFCCs)
            
    res1 =['/','/','/','/']
    res2 =['/','/','/','/']
    res3 =['/','/','/','/']
    m1=[]
    m2=[]
    m3=[]
     
    m=0
    count=0
    p1=p2=p3=' '
    while m<3:
        if count<3:
            

            
# send data to Pd
            spedisci(norm[r1], norm[r2], norm[r3], norm[r4])
    
# select instrumentation and diffusion

            s = instr(r1,r2,r3,r4)
    
           
# record with mic 5, save into f0.wav, extract a single channel and save it to objects.wav 
            record_mult('f0.wav', recording_device)
            wav = wave.open('f0.wav')
            save_wav_channel('objects.wav', wav, mic_installation - 1)
    

# new feature extraction and prediction
            a, b, c, d, MFCCs = mfccs('objects.wav')
            result3 = pred_audio(a, b, c, d)
            if count==0:
                res1=result3
            elif count==1:
                res2=result3
            else:
                res3=result3
            print(result3)

# comparison between two consecutive predictions
            m=match(result, result3)
            print(m)

# Loop until either a match has been found or 3 consecutive re-syntheses were triggered and classified

            if m>4:
                print('MATCH!')
                if count==0:
                    p1='match!'
                elif count==1:
                    p2='match'
                else:
                    p3='match!'
                count=3
            else:
                print('NO MATCH!')
                if count==0:
                    p1='no match!'
                elif count==1:
                    p2='no match'
                else:
                    p3='no match!'

                count=count+1
        else:
            break            

    return


# this function will indefinitely try to fetch and
# analyze recordings it got from the global app
@app.before_first_request
def activate_job():
    def run_job():
        while True:
            print("Run recurring task")
            wavData = fetchRecording();
            if wavData is not None:
                analyzeRecording(wavData)
            time.sleep(2)

    thread = threading.Thread(target=run_job)
    thread.start()

# this function attempts to send a web request to the
# current Flask app. Once Flask handles its first request,
# the @app.before_first_request function above will run.
def start_runner():
    def start_loop():
        not_started = True
        url = 'http://127.0.0.1:' + str(listen_port) + '/'
        print('try url: ' + url)
        while not_started:
            print('In start loop')
            try:
                r = requests.get(url)
                if r.status_code == 200:
                    print('Server started, quiting start_loop')
                    not_started = False
                print(r.status_code)
            except:
                print('Server not yet started')
            time.sleep(2)

    print('Started runner')
    thread = threading.Thread(target=start_loop)
    thread.start()



if __name__ == '__main__':
    start_runner()
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        print(p.get_device_info_by_index(i))
    app.run(debug=True, port=listen_port)
