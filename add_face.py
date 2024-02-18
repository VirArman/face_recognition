#!/usr/bin/env python3

from facedb import FaceDB as fdb
import cv2

db = fdb(
    path="facedata",
)

def detect_bounding_box(vid):
    face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 4)
    face_detected = False
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
        face_detected = True
    return faces, face_detected

def face_detection():
    video_capture = cv2.VideoCapture(0)
    counter = 0
    while True:
        result, video_frame = video_capture.read()  # read frames from the video
        if result is False:
            break 
        
        faces, face_detected = detect_bounding_box(
            video_frame
        )

        cv2.imshow(
            "My Face Detection Project", video_frame
        )  


        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    return video_frame


def main():
    name = input("please insert name of person from image : ")
    print("Would you like to add existing photo (insert 1) or make a new one (insert 2)?")
    answer = input("insert 1 or 2 : ")
    if answer == "1":
        path = input("Please insert path to existing photo ")
        face_id = db.add(name, img=path)
    elif answer == "2":
        face_id = db.add(name, img=face_detection())

if __name__ == "__main__":
    main()
