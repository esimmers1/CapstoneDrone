import cv2

def splice(video):
    capture = cv2.VideoCapture(video)
    
    frameNr = 0
    
    while (True):
    
        success, frame = capture.read()
    
        if success:
            cv2.imwrite(f'Spliced/frame_{frameNr}.jpg', frame)
    
        else:
            break
    
        frameNr = frameNr+1
    
    capture.release()