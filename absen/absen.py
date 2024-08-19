import cv2
import os

def capture_face_and_save():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    
    face_id = input("Masukkan ID atau nama pengguna untuk data absen: ")
    save_path = "data_absen"
    
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    count = 0
    
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            count += 1
            face_img = gray[y:y+h, x:x+w]
            file_name = os.path.join(save_path, f"{face_id}_{count}.jpg")
            cv2.imwrite(file_name, face_img)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        cv2.imshow('Capturing Face', frame)

        if cv2.waitKey(1) & 0xFF == ord('q') or count >= 10:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_face_and_save()
