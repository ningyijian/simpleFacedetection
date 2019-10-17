import cv2
#  引入Opencv脸部Haar特征分类器,文件来自Opencv安装目录 haarcascades文件夹
face_xml = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_xml = cv2.CascadeClassifier('haarcascade_eye.xml')
#读入准备识别的图片
img =cv2.imread('lena.jpg')

#haar gray
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# detect faces 1 data 2 scale 3 5 最小像素
faces = face_xml.detectMultiScale(gray,1.1,2)
print('face=',len(faces))
#draw
index =0
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(250,0,0),2)
    roi_face = gray[y:y+h,x:x+w]
    roi_color = img[y:y+h,x:x+w]
    fileName = str(index)+'.jpg'
    cv2.imwrite(fileName,roi_color)
    index = index +1
    # 1 gray
    eyes = eye_xml.detectMultiScale(roi_face)
    print('eye=',len(eyes))
    for (e_x,e_y,e_w,e_h)in eyes:
        cv2.rectangle(roi_color,(e_x,e_y),(e_x+e_w,e_y+e_h),(0,255,0),2)
cv2.imshow('dst',img)

cv2.waitKey(0)
cv2.destroyAllWindows()



