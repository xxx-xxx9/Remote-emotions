from flask import Flask, render_template, request, jsonify
import os # os.remove
import os.path # os.path.isfile
from exceptions import *



listen_port = 8000

minimum_recording_duration = 4.0 # local app analyses 4x 1 second
recording_sample_rate = 16000    # Web Audio page records at 16kHz
recording_sample_size = 2        # Web Audio page transmits 16 bit samples

app_global = Flask(
    __name__,
    static_url_path='', 
    static_folder='static')


@app_global.route('/', methods=['GET'])
def menu():
    return render_template('record.html')

# used by the local app to fetch recordings.
@app_global.route('/fetch_recording', methods=['GET'])
def fetch_recording():
    try:
        if os.path.isfile('recording-web.wav'):
            with open('recording-web.wav', mode='rb') as file:
                wavData = file.read()
            os.remove('recording-web.wav')
            return wavData
        else:
            raise WebhookException("no recording", status_code=203)
    except:
        raise WebhookException("failed to fetch recording", status_code=203)



# used by the local app and the Web Audio web page to submit recorded
# wave files.
@app_global.route('/submit_recording', methods=['POST'])
def submit_recording():
    
    print("submit_recording", flush=True);
    
    if request.content_length == 0:
        request.get_data()
        raise WebhookException("missing data", status_code=620)
    if request.content_length < recording_sample_rate*recording_sample_size*minimum_recording_duration:
        request.get_data()
        raise WebhookException("not enough data", status_code=620)
    if request.content_length > 256*1000:
        raise WebhookException("data too large", status_code=621)
    
    if os.path.isfile('recording-web.wav'):
        request.get_data()
        raise WebhookException("a recording already exists and is waiting to be processed", status_code=622)

    try:
        print("got data", flush=True);
        data = request.get_data()
    except Exception:
        raise WebhookException("failed to get data", status_code=500)
    
    try:
        print("writing data to file", flush=True);
        f = open("recording-web.wav", "wb")
        f.write(data)
        f.close()
    except Exception:
        raise WebhookException("failed to store data", status_code=500)

    response = jsonify(success=True)
    return response



# error handler
@app_global.errorhandler(WebhookException)
def handle_exception(e):
    # pass through HTTP errors
    #if isinstance(e, HTTPException):
    #    return e
    print("error: " + e.message, flush=True);
    return "<p>" + e.message + "</p>", e.status_code
    #return "oops!", 500



if __name__ == '__main__':
    #ssl_context=('server.crt', 'server.key')
    #debug=True
    app_global.run(debug=True, host="0.0.0.0", port=listen_port)
    
## funded by RIXC ##
