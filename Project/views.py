# i have create this one

from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
import cv2
from django.http import StreamingHttpResponse # type: ignore
import numpy as np
from ultralytics import YOLO
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'models', 'last.pt')
model = YOLO(model_path)



def home(request):
    return render(request,'home.html')

def feature(request):
    return render(request,'feature.html')

def webcam(request):
    return render(request,'webcam.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def Detect_Object(request):


    vid = cv2.VideoCapture(0)
    while True:
        r,frame = vid.read()
        if r==True:
            frame=cv2.flip(frame,1)
            H, W, _ = frame.shape
            

            threshold = 0.2
            results = model(frame, verbose=False)[0]  # Add verbose=False to reduce logs
            


            # Draw detections
            for result in results.boxes.data.tolist():                

                
                x1, y1, x2, y2, score, class_id = result
                if score > threshold:

                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                    cv2.putText(frame, results.names[int(class_id)].upper(), 
                                (int(x1), int(y1 - 10)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)            


            ret, jpeg = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n' 
                b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')


def video_feed(request):
    return StreamingHttpResponse(Detect_Object(request),
        content_type='multipart/x-mixed-replace; boundary=frame')



# import cv2
# from django.http import StreamingHttpResponse

# def gen_frames():
#     cap = cv2.VideoCapture(1)
#     while True:
#         success, frame = cap.read()
#         if not success:
#             break
#         ret, buffer = cv2.imencode('.jpg', frame)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# def video_feed(request):
#     return StreamingHttpResponse(gen_frames(), content_type='multipart/x-mixed-replace; boundary=frame')


