import cv2 as cv

base = "Week 1"

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter(f'{base}/output.mp4', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    out.write(frame)
    cv.imshow('frame', gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()