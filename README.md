# Attendance-system<br>
This project is meant to help collection of attendance through a video source.<br>
Building blocks:<br>
  Detection-MTCNN-pretrained detector <uses tensor flow 1.14 or 1.13><br>
  Recognition-Face net Mimic for embedding generation and vector machine for classification<br><br>

Files:<br><b>facerecogvideo</b> is used to take a video as input(function facerecog is the starting of the program) and returns  a list of the people who are  present as the output<br>
          <b>filetanddvideo</b> is called by facerecog to take video file,identify the slot and save one in every 100 frames<br>
          <b>fdmtcnnfxn</b> is used totest a group of training images to check if  a face and only one face is present in the image.<br>
          it takes a folder of all the training images as input and deletes the files which are rejected.<br>
 
 Do install the required libraries before executing the code.<br>
 
 Reference:<br> https://machinelearningmastery.com/how-to-develop-a-face-recognition-system-using-facenet-in-keras-and-an-svm-classifier/
 <br>This blog was the basic step towards this project.
 
 <br>Tip: in the vector machine try changing the kernel settings to 'rbf' or'poly' instead of leniar to find out ehich gives the best results.
