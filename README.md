for install face-recognition - install ???cmake??? and simple pack for console development on c++ in visual studio installer, because face-recognition need dlib and  some specific tools.(https://www.geeksforgeeks.org/how-to-install-dlib-library-for-python-in-windows-10/)  
on linux-based system  simple - just installl face-recognition  
save data in postgres - https://stackoverflow.com/questions/60278766/best-way-to-insert-python-numpy-array-into-postgresql-database  
https://machinelearningmastery.com/how-to-save-a-numpy-array-to-file-for-machine-learning/  
https://stackoverflow.com/questions/28439701/how-to-save-and-load-numpy-array-data-properly  
  
# create POSTGREDB
    sudo docker run -p 5432:5432 -e POSTGRES_USER=userP -e POSTGRES_PASSWORD=mypass -e POSTGRES_DB=facedb -d postgres

# crete db file in container
     pg_dump --host "192.168.126.130" --port "5432" --username "userP"  "facedb" > testDB.sql

# copy db file from container
    sudo docker cp 91a99e6b742a:testDB.sql ./

# get photo from db
    ans = session.query(facesDB).all()
    #dtype = uint8
    nparr = np.frombuffer(ans[1].photo, np.uint8)
    bytes = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imshow('sas',bytes)
    cv2.waitKey(0)

# add new face

    img = fa_re.load_image_file("images\\me2.jpg")
    face_encoding = fa_re.face_encodings(img)[0] 
    for i in range(3):
        #add new face
        face_add = facesDB(
            face_data = face_encoding,
            photo = cv2.imencode('.png', img)[1].tobytes()
        )
        session.add(face_add)
        session.commit()
    sys.exit()

    #db_face = np.frombuffer( get_faces(), np.float64 )

# from bytea to face_enc
    bytes_converted = np.frombuffer( i[1], np.float64)

# add data and that face founded
        face_add = face_check(
            face_id=0
        )
        session.add(face_add)
        session.commit()

ffmpeg path :C:\ffmpeg\bin  


# before start ffmpegtranstaltion start C:\Users\Kirill\Videos\rtsp\mediamtx.exe

# git list of devices
    ffmpeg -list_devices true -f dshow -i dummy

# View available resolutions
    ffmpeg -list_options true -f dshow -i video="1080P Web Camera"

# Stream from one of the available video devices (replace Integrated Camera with the video device name and <ip> with the IP address from the commands above)
     ffmpeg -f dshow -i video="1080P Web Camera" -framerate 30 -video_size 1280x720 -f rtsp -rtsp_transport udp rtsp://192.168.100.8:8554/webcam.h264

