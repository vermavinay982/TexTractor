import cv2
import easyocr
reader = easyocr.Reader(lang_list=['en'], gpu=True, model_storage_directory=None,
                        user_network_directory=None, detect_network="craft", 
                        recog_network='standard', download_enabled=True, 
                        detector=True, recognizer=True, verbose=True, 
                        quantize=True, cudnn_benchmark=False)



def extract_text(file, debug=False):
    cap = cv2.VideoCapture(file)
    fps = cap.get(cv2.CAP_PROP_FPS)
    skip_count = fps
    PCT_THRESH = 10
    prev_frame = None
    SCALE = 1
    ctr = 0
    op_ext = ".txt"
    op_base = "images/output"
    op_file = f"{op_base}_{file.replace(' ','_')}{op_ext}"
    whole_text = ""
    
    while True:
        ret, frame = cap.read()
        if ret is False: break
        # SAVING RESOUCES, REDUCING SEARCH TIME
        ctr+=1
        skip = ctr % skip_count
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

        if debug:
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

        whole_text+=f"{ctr}:{text}\n"

        if debug:
            print(text)

        # FINDING REQUIRED TEXT, FROM DETECTED TEXT, AND SHOWING IMAGE 
        if debug:
            cv2.imshow("Player",frame)  
            key = cv2.waitKey(1)
            
            if key==ord('q'):
                break

    if debug:
        cap.release()
        cv2.destroyAllWindows()

    return whole_text

def find_text_video(file, search, start_ctr, debug=False):
    cap = cv2.VideoCapture(file)
    fps = cap.get(cv2.CAP_PROP_FPS)
    skip_count = fps
    PCT_THRESH = 10
    prev_frame = None
    SCALE = 1
    ctr = 0
    op_ext = ".png"
    op_base = "images/output"

    while True:
        ret, frame = cap.read()
        if ret is False: break
        # SAVING RESOUCES, REDUCING SEARCH TIME
        ctr+=1
        skip = ctr % skip_count
        if ctr<=start_ctr or skip: continue

        op_file = f"{op_base}_{search.replace(' ','_')}_{ctr}{op_ext}"

        h, w, c = frame.shape
        nw, nh = int(w/SCALE), int(h/SCALE)
        # DONT RESIZE, IF NOT REQUIRED
        if not SCALE==1:
            frame = cv2.resize(frame, (nw, nh))

        # FRAME DIFFERENCE TO SKIP OCR PROCESSING, SAVING RESOURCES
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if prev_frame is None: prev_frame = gray
        frame_diff = cv2.absdiff(gray, prev_frame)

        if debug:
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

        if debug:
            print(text)

        # FINDING REQUIRED TEXT, FROM DETECTED TEXT, AND SHOWING IMAGE 
        if search in text:
            if debug:
                cv2.imshow("Found",frame)  
            key = cv2.waitKey(0)
            flag = cv2.imwrite(op_file,frame)
            if flag:
                print(f'Output written: {op_file}')
                return op_file, ctr
            else:
                print(f'Failed Output: {op_file}')        

        if debug:
            cv2.imshow("Player",frame)  
            key = cv2.waitKey(1)
            
            if key==ord('q'):
                break

    if debug:
        cap.release()
        cv2.destroyAllWindows()

    return None, 0

if __name__=="__main__":
    file = '../seminar.mp4'
    TO_FIND = "noob"
    # find_text_video(file, TO_FIND)
    text = extract_text(file)
    print(text)
