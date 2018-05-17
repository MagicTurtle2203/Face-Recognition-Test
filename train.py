#based on tutorial found here: https://www.superdatascience.com/opencv-face-recognition/
import os
import cv2
import numpy as np

def detect_face(image):
	gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	face_cascade = cv2.CascadeClassifier("face_cascades/lbpcascade_frontalface.xml")
	faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.2, minNeighbors = 5)
	
	if (len(faces) == 0):
		return None, None
	
	(x, y, w, h) = faces[0]
	
	#returns a cutout of the subjects face as well as the rectangle around the subject
	return gray_img[y:y+h, x:x+w], faces[0]

def prepare_training_data(data_path):
	#gets a list of each folder containing the subjects' images
	dirs = os.listdir(data_path)
	faces = []
	labels = []
	
	for dir_name in dirs:
		if not dir_name.startswith('s'):
			continue
		#creates a label for each subject by removing the s from the directory name and converting to an int
		label = int(dir_name.replace('s', ''))
		subject_path = data_path + '/' + dir_name
		subject_images = os.listdir(subject_path)
		
		for image_name in subject_images:
			image_path = subject_path + '/' + image_name
			image = cv2.imread(image_path)
			cv2.imshow("Training...", image)
			cv2.waitKey(100)
			
			face, rect = detect_face(image)
			
			if face is not None:
				faces.append(face)
				labels.append(label)
				
			cv2.destroyAllWindows()
			cv2.waitKey(1)
			cv2.destroyAllWindows()
			
	return faces, labels

print("Preparing data...")
faces, labels = prepare_training_data("training-data")
print("Data prepared")

print("Total faces: {}".format(len(faces)))
print("Total labels: {}".format(len(labels)))

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces, np.array(labels))
face_recognizer.save('trainer.xml')
