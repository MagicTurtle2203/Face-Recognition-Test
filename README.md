# Face-Recognition-Test
### Training a face recognizer using OpenCV

This face recognition program is based on the tutorial found [here](https://www.superdatascience.com/opencv-face-recognition/). I attempted to create a facial recognition program that would be able to differentiate between several subjects. For my subjects, I chose to use several members of the K-Pop group Dreamcatcher, as K-Pop idols have a large amount of fan pictures that are able to be used to train the program. This program doesn't seem to work as well I would have hoped; probably more training data is required to make it work better. 

I ran the training program with both the LBP and Haar face detection algoritms with the LBPH face recognition algorithm to compare the accuracy of each. However, I decided to stick with LBP in the end because the Haar algorithm was much slower without much real benefit. Both the LBP and Haar algorithms often failed to detect a face at all. Many pictures were detected as containing no faces even though I chose only images that showed each idol's face.

Sometimes, it trains to recognize a patch of foliage in the picture as the idol's face instead of the idol's actual face.

<img src="https://github.com/SimpleTurtle/SimpleTurtle/blob/master/images/22344172_1300303463430014_37224820856848384_n.jpg" width="60%">

Or, it detects a doll's face even though there is a much larger face nearby.

<img src="https://github.com/SimpleTurtle/SimpleTurtle/blob/master/images/jiu1.jpg" width="40%">

Originally. I had attempted to train the face recognition program with four idols' faces, but that did not seem to work well. With four different subjects, the program was somehow unable to determine the faces in pictures that it had already been trained with. The percent of faces it was able to guess correctly was also quite low. Reducing the number of subjects to three improved the accuracy a lot, and the program once again became able to recognize faces in pictures that it had been trained with before. 


## new pictures soon
I added successful prediction pictures to show what the face recognition program is able to do when it runs correctly. These are available to view [here](predictions/). 

As one can see, this prediction program is not very accurate. It was only able to classify about half of the pictures correctly, even though some of the same images were used to train the program. The program was able to detect and train off of 1280 faces total, so perhaps many more pictures would be required to make the program more accurate. 
