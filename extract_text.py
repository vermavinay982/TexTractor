import cv2
from pprint import pprint
import easyocr
reader = easyocr.Reader(lang_list=['en'], gpu=True, model_storage_directory=None,
                        user_network_directory=None, detect_network="craft", 
                        recog_network='standard', download_enabled=True, 
                        detector=True, recognizer=True, verbose=True, 
                        quantize=True, cudnn_benchmark=False)

file = '../seminar.mp4'
cap = cv2.VideoCapture(file)

SCALE = 1
ctr = 0
prev_frame = None
PCT_THRESH = 10
TO_FIND = "noob"

while True:
    ret, frame = cap.read()
    if ret is False: break
    # SAVING RESOUCES, REDUCING SEARCH TIME
    ctr+=1
    skip = ctr%10
    if skip: continue

    h, w, c = frame.shape
    nw, nh = int(w/SCALE), int(h/SCALE)
    # DONT RESIZE, IF NOT REQUIRED
    if not SCALE==1:
        frame = cv2.resize(frame, (nw, nh))

    # FRAME DIFFERENCE TO SKIP OCR PROCESSING, SAVING RESOURCES
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if prev_frame is None: prev_frame = gray
    frame_diff = cv2.absdiff(gray, prev_frame)
    cv2.imshow("frame diff",frame_diff)
    total = sum(sum(frame_diff))
    diff_pct = (total/(nw*nh))*100
    prev_frame = gray

    if diff_pct<PCT_THRESH:
        # print(diff_pct,"%")
        continue

    # READING TEXT VALUES FROM IMAGE
    detections = reader.readtext(frame)
    text = ""
    for det in detections:
        line = det[1].lower()
        text+=(line+" ")
    print(text)

    # FINDING REQUIRED TEXT, FROM DETECTED TEXT, AND SHOWING IMAGE 
    if TO_FIND in text:
        cv2.imshow("Found",frame)  
        key = cv2.waitKey(0)        

    cv2.imshow("Player",frame)  
    key = cv2.waitKey(1)
    
    if key==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()