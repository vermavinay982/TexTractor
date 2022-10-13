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

""" with CUDA
Total Time Taken to Start: 6.0725491
Total Time Taken to Process: 3.8361412999999995
Total Time Taken to Process: 3.126423000000001
Total Time Taken to Process: 3.451420200000001
Total Time Taken to Process: 3.1697615
Total Time Taken to Process: 3.1470497
Total Time Taken to Process: 3.2217537000000007
Total Time Taken to Process: 3.3143147999999982
Total Time Taken to Process: 3.1435480000000027
Total Time Taken to Process: 3.1576017000000007
Total Time Taken to Process: 3.1008004000000042
Total Time Taken to Process: 3.107650999999997
Total Time Taken to Process: 3.2374253999999993
Total Time Taken to Process: 3.1702987999999976


Without CUDA
Using CPU. Note: This module is much faster with a GPU.
Total Time Taken to Start: 3.280307
Total Time Taken to Process: 13.369948100000002
Total Time Taken to Process: 13.3022052
Total Time Taken to Process: 14.051367000000003
Total Time Taken to Process: 13.164816600000002
Total Time Taken to Process: 12.931808400000001
Total Time Taken to Process: 12.99822660000001
"""