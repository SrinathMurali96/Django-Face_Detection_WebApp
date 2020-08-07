import cv2
from django.shortcuts import render
from Django.settings import face_path
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods



@require_http_methods(["GET","POST"])
@csrf_exempt
def detect_face(request):
    print("Inside the face detection method")
    try:
        print("Inside the face detection method")
        # Load the cascade
        print("face_path is ",face_path)
        face_cascade = cv2.CascadeClassifier(face_path)
        
        # To capture video from webcam. 
        cap = cv2.VideoCapture(0)
        # To use a video file as input 
        # cap = cv2.VideoCapture('filename.mp4')
        print("Video is about to start")
        while True:
            # Read the frame
            _, img = cap.read()
        
            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
            # Detect the faces
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
            # Draw the rectangle around each face
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
            # Display
            cv2.imshow('img', img)
        
            # Stop if escape key is pressed
            k = cv2.waitKey(30) & 0xff
            if k==27:
                break
                
        # Release the VideoCapture object
        cap.release()
    except:
        print("Error occured")
    return render(request, 'facedetection.html')    
        
        