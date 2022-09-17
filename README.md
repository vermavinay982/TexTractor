# TexTractor

Goal: Trying to find the specific text in a video
Motivation: While watching tutorial, need to find a specific word on screen, but had to watch the whole video. So thought to make it for the world.
Benefits: faster inference on videos, better analytics, threading for performance, multi processing


it will give the frame, or timestamp where the text was present

for all words - timestamps will be generated 
if the user searched few words - all those timestamps will be returned to user

- search all at once
- search more 
- getting range of video where text can be present - for faster search
- location of detected text also can be mentioned 
- tracking of text can be done - for each frame - to reduce load on processing
- for each time stamp the text can be found out
- option to give frame skipping option to user is beneficial
- showing range where the word was present, some words are constantly present
- can highlight for each word by user where it was present
- close to it, could also be added - to make suggestion to user
- streamlit for deployment and params 

Mini Goals
- find best text detection model
- infer it on single frames
- generate frames using cv2
- save data and present it in csv form 
- use trees and other algorithms to merge the presense of word in all images

