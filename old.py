import cv2
import face_recognition
import base64
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
#from flask import Flask
import time
from threading import Thread


def read_imgs(nums: int)-> list:

    images=[]

    for i in range(1, nums+1):
        images.append( cv2.imread('images/getty'+str(i)+'.jpg', cv2.IMREAD_UNCHANGED) )

    return images


def load_classifiers()-> list:

    classifers = []


    # classifers.append( cv2.CascadeClassifier('classifiers/haarcascade_frontalcatface.xml') )
    #
    # classifers.append(cv2.CascadeClassifier('classifiers/haarcascade_frontalcatface_extended.xml'))
    #
    # classifers.append(cv2.CascadeClassifier('classifiers/haarcascade_frontalface_alt.xml'))

    classifers.append(cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml'))

    return classifers




class ThreadedCamera(object):
    def __init__(self, src=0):

        self.me = face_recognition.load_image_file('images\\me.jpg')
        self.me_enc = face_recognition.face_encodings(self.me)[0]
        self.known_faces = [self.me_enc]

        #self.capture = cv2.VideoCapture(src)
        self.capture = cv2.VideoCapture(0)

        self.capture.set(cv2.CAP_PROP_BUFFERSIZE, 3)

        # # FPS = 1/X
        # # X = desired FPS
        self.FPS = 1 / 30
        self.FPS_MS = int(self.FPS * 1000)

        # Start frame retrieval thread
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()


    def update(self):
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()

            time.sleep(self.FPS)

    def show_frame(self):
        #gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        #rgb_small_frame = self.frame[:, :, ::-1]
        small_frame = cv2.resize(self.frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        #
        #
        # mathes = face_recognition.compare_faces(self.me_enc, face_encodings[0])
        # face_distances = face_recognition.face_distance(self.me_enc, face_encodings[0])
        #
        for (top,right, bottom, left), name in zip(face_locations,["unknown"]):

            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
        #
        # # Draw a box around the face
            cv2.rectangle(self.frame, (left, top), (right, bottom), (0, 0, 255), 2)
        #
        # # Draw a label with a name below the face
            cv2.rectangle(self.frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(self.frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


        name = "Unknown"



        cv2.imshow('frame', self.frame)
        cv2.waitKey(self.FPS_MS)


if __name__ == '__main__':

    # images = read_imgs(3)
    #
    # cass = load_classifiers(1)
    #
    #
    #
    # for image in images:
    #
    #     pos = 1
    #
    #     for classi in cass:
    #
    #         buf = image.copy()
    #
    #         faces = classi.detectMultiScale( buf )
    #
    #         for (x, y, w, h) in faces:
    #
    #             cv2.rectangle(buf ,(x,y), (x+w, y+h), (255, 0))
    #
    #         cv2.imshow(str(pos), buf)
    #
    #         pos+=1
    #
    #         cv2.waitKey()
    #         cv2.destroyAllWindows()
    #
    #
    #

    # class myHandlerTCP(BaseHTTPRequestHandler):
    #
    #     def do_GET(self):
    #
    #         self.send_response(200)
    #         self.send_header('Content-type', 'text/html')
    #         self.end_headers()
    #
    #         #ret, frame = vid.read()
    #         # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #         # ret, png = cv2.imencode('.png', gray)
    #
    #         png = cv2.imread('images/getty'+'1'+'.jpg', cv2.COLOR_RGB2BGR)
    #
    #         self.wfile.write(bytes("<p>" +   str( png.tobytes() )   + "</p>", "utf8"))
    #
    #
    # #'<img src=data:image/jpg;base64,' "'/>"
    # server=socketserver.TCPServer(('localhost',9999),myHandlerTCP)
    # server.serve_forever()

    cass = load_classifiers()


    cam='rtsp://192.168.100.4:8080/h264_ulaw.sdp'



    # get=0.1
    # now = time.time()
    # print(1 / (now - get))
    # get = now

    thr_cam=ThreadedCamera(cam)


    while True:

        try :
            thr_cam.show_frame()
        except:
            pass





        # face_loc=face_recognition.face_locations(rgb_small_frame)
        # face_enc=face_recognition.face_encodings(rgb_small_frame,face_loc)
        #
        # found=False
        # for face_en in face_enc:
        #
        #     print("face foubded")
        #     matches=face_recognition.compare_faces(known_faces,face_en)
        #
        #     if True in matches:
        #         print("yes")
        #         found=True
        #
        # else:
        #     pass
        #     # print("nobody")

        # for (top, right, bottom, left), name in zip(face_loc, ['kirill']):
        #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        #
        #     # Draw a label with a name below the face
        #     cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        #     font = cv2.FONT_HERSHEY_DUPLEX
        #     cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        #
        #     #cv2.imshow('frame', frame)

        # cv2.imshow('frame', frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    # vid.release()
    cv2.destroyAllWindows()


    #img.release()