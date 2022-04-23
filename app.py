from flask import *
import speech_recognition as sr
from google_trans_new import google_translator
import pyttsx3 
from playsound import playsound

app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def index():
    if request.method == 'POST':
        global result
        recognizer=sr.Recognizer()
        engine = pyttsx3.init()
        with sr.Microphone() as source: 
            print('Clearing background noise...')
            recognizer.adjust_for_ambient_noise(source,duration=1)
            print('Waiting for message..') 
            audio = recognizer.listen(source,timeout=20)
            print('Done recording..')
        try:
            print('Recognizing..')
            result = recognizer.recognize_google(audio,language='en')
            print(result)
            engine1 = pyttsx3.init()
            engine1.save_to_file(result,r'C:\Users\Zaynab\Desktop\Voice_Web_App\Input/'+ result+'.mp3')
            engine1.runAndWait()
        except Exception as ex:
            print(ex)
        return render_template("translate.html")
    return render_template("index.html")

@app.route("/voice",methods=['POST','GET'])
def voice():
    if request.method == 'POST':
        langinput = request.form['language']
        translator = google_translator()  
        translate_text = translator.translate((result),(langinput))  
        
        print(translate_text)
        engine = pyttsx3.init()
        engine.save_to_file(translate_text, r'C:\Users\Zaynab\Desktop\Voice_Web_App\Output/'+translate_text+'.mp3')
        engine.runAndWait()
        return render_template("translate.html", translate_text=translate_text)



if __name__ == '__main__':
    app.run(debug=True)