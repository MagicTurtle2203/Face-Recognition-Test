import os
import cv2
from train import detect_face

subjects = []

#function to draw rectangle on image according to given (x, y) coordinates and given width and height
def draw_rectangle(img, rect):
	(x, y, w, h) = rect
	cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
 
#function to draw text on give image starting from passed (x, y) coordinates. 
def draw_text(img, text, x, y):
	cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_DUPLEX, 1.5, (0, 255, 0), 2)

def predict(image):
	img = image.copy()
	face, rect = detect_face(img)
	label, confidence = face_recognizer.predict(face)
	label_text = subjects[label]
	
	draw_rectangle(img, rect)
	draw_text(img, label_text + " " + confidence, rect[0], rect[1]-5)
	
	return img

for file in os.listdir("test-data"):
	os.remove("test-data/" + file)

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read("trainer.yml")

print("Predicting images...")
for num, image in enumerate(os.listdir("test-data")):
	test_image = cv2.imread("test-data/" + image)
	predicted_image = predict(test_image)
	cv2.imwrite("predictions/" + str(num) + ".jpg", predicted_image)
print("Prediction complete!")
