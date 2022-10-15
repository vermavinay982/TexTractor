import cv2

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


    cv2.imshow("Player",frame)  
    key = cv2.waitKey(1)
    
    if key==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()