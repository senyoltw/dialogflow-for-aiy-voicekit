# dialogflow-for-aiy-voicekit
Dialogflow API for AIY Voice Kit.    
Add your AIY Voice Kit Dialogflow API.

# Before How to install
Buy The AIY Voice Kit and complete the tutorial.  
dialogflow-for-aiy-voicekit use lowlevel api AIY Voice Kit.

https://aiyprojects.withgoogle.com/voice/

and Enable the API Cloud Speech API,Dialogflow API.

https://aiyprojects.withgoogle.com/voice/#makers-guide--custom-voice-user-interface

Are you work your voice kit this program?
```
src/examples/voice/cloudspeech_demo.py
```
If the demo has worked,next step.

# How to install

```
cd /home/pi/
git clone https://github.com/senyoltw/dialogflow-for-aiy-voicekit

# copy Dialogflow module and sample program.
cp -ipr dialogflow-for-aiy-voicekit/mod AIY-projects-python/src/
cp -ip dialogflow-for-aiy-voicekit/cloudspeech_dialogflow_text.py AIY-projects-python/src/examples/voice/
```

# How to use

```
cd AIY-voice-kit-python
chmod a+x src/examples/voice/cloudspeech_dialogflow_text.py
src/examples/voice/cloudspeech_dialogflow_text.py 
```
Press the button and speak your Dialogflow APP!

