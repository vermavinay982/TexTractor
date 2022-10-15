from time import perf_counter
import sys
# import os
# os.environ["CUDA_VISIBLE_DEVICES"]=""
# set CUDA_VISIBLE_DEVICES=1

start = perf_counter()

import easyocr
reader = easyocr.Reader(lang_list=['en'], gpu=True, model_storage_directory=None,
                 user_network_directory=None, detect_network="craft", 
                 recog_network='standard', download_enabled=True, 
                 detector=True, recognizer=True, verbose=True, 
                 quantize=True, cudnn_benchmark=False)

# file = 'images/npaper.jpg'
file = 'images/code.png'

end = perf_counter()
time_taken = end-start
print("Total Time Taken to Start:",time_taken)


while True:
    try:
        start = perf_counter()
        result = reader.readtext(file)
        # print(result)

        text = []

        for data in result:
            word = data[1]
            text.append(word)

        # print(text)
        end = perf_counter()
        time_taken = end-start
        print("Total Time Taken to Process:",time_taken)
    except KeyboardInterrupt as e:
        print("Closing code smoothly",e)
        sys.exit(0)
