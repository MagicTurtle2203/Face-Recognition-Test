# Face-Recognition-Test
### Training a face recognizer using OpenCV

This face recognition program is based on the tutorial found [here](https://www.superdatascience.com/opencv-face-recognition/). I attempted to create a facial recognition program that would be able to differentiate between several subjects. For my subjects, I chose to use several members of the K-Pop group Dreamcatcher, as K-Pop idols have a large amount of fan pictures that are able to be used to train the program. This program doesn't seem to work as well I would have hoped, probably more training data is required to make it work better. 

I ran the training program with both the LBP and Haar face detection algoritms with the LBPH face recognition algorithm to compare the accuracy of each. Surprisingly, while Haar is supposedly more accurate, it had a harder time detecting faces than LBP did. It was more likely that Haar detected something other than idol's face as the face, such as a doll or a part of a shirt, rather than LBP. Sometimes, Haar even failed to find faces where LBP did. The prediction confidence was also greater when using the LBP trained face recognition than the Haar trained face recognition. 

However, both the LBP and Haar algorithms often failed to detect a face at all. Using LBP, 1550 faces were detected in the 2310 total pictures, and, with Haar, 1870 faces were detected. I suspect that the increase in number of detected faces with Haar is mostly due to more false positives. Some pictures were detected as containing no faces even though I chose only images that showed each idol's face.

### With LBP 
Sometimes, it trains to recognize a patch of foliage in the picture as the idol's face instead of the idol's actual face.

<img src="https://github.com/SimpleTurtle/SimpleTurtle/blob/master/images/22344172_1300303463430014_37224820856848384_n.jpg" width="60%">

### With Haar
Or, it detects a doll's face even though there is a much larger face nearby.

<img src="https://github.com/SimpleTurtle/SimpleTurtle/blob/master/images/jiu1.jpg" width="40%">

I added successful prediction pictures to show what the face recognition program is able to do when it runs correctly. These are available to view [here](predictions/).
