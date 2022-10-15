import cv2

file = '../seminar.mov'
cap = cv2.VideoCapture(file)
orig_fps = cap.get(cv2.CAP_PROP_FPS)
count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

fps = 4
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # 4CC
scale = 4

target = 'output.mp4'

ret, frame = cap.read()
h, w, c = frame.shape
nw, nh = int(w/scale), int(h/scale)
size=(nw,nh)

out = cv2.VideoWriter(target, fourcc, fps , size)
ctr = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break 

    ctr+=1
    if ret is False:
        break
    
    val = ctr%20

    if val:
        continue
    print(val,ctr,count)

    frame_copy = cv2.resize(frame, (nw, nh))
    print(nw,nh)

    out.write(frame_copy)

out.release()
cap.release()