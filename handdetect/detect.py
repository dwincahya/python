import cv2
import numpy as np

def detect_hand():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        
        frame = cv2.flip(frame, 1)
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        lower_skin = np.array([0, 20, 70], dtype=np.uint8)
        upper_skin = np.array([20, 255, 255], dtype=np.uint8)
        
        mask = cv2.inRange(hsv, lower_skin, upper_skin)
        
        mask = cv2.erode(mask, np.ones((3,3), np.uint8), iterations=1)
        mask = cv2.dilate(mask, np.ones((3,3), np.uint8), iterations=2)
        
        mask = cv2.GaussianBlur(mask, (5, 5), 100)
        
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        if contours:
            cnt = max(contours, key=lambda x: cv2.contourArea(x))
            cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 2)
            
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        cv2.imshow("Hand Detection", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_hand()
