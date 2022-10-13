import cv2

import easyocr
reader = easyocr.Reader(lang_list=['en'], gpu=True, model_storage_directory=None,
                        user_network_directory=None, detect_network="craft", 
                        recog_network='standard', download_enabled=True, 
                        detector=True, recognizer=True, verbose=True, 
                        quantize=True, cudnn_benchmark=False)

file = '../seminar.mp4'
cap = cv2.VideoCapture(file)
scale = 1
ctr = 0


while True:
    ret, frame = cap.read()
    ctr+=1
    if ret is False:
        break
    
    val = ctr%10

    if val:
        continue
    print(val,ctr)

    h, w, c = frame.shape
    nw, nh = int(w/scale), int(h/scale)
    frame = cv2.resize(frame, (nw, nh))
    
    t = reader.readtext(frame)
    print(t)

    cv2.imshow("Player",frame)  
    key = cv2.waitKey(1)
    
    if key==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()