from PIL import Image
from numpy import asarray
from mtcnn.mtcnn import MTCNN
from os import listdir
from os import remove
import cv2
 
# extract a single face from a given photograph
def faceaccept(directory):
    for filename in listdir(directory):
        path=directory+'/'+filename
        
        image = Image.open(path)
        required_size=(160,160)
            
        image = image.convert('RGB')
                
        pixels = asarray(image)
                    
        detector = MTCNN()
                    
        results = detector.detect_faces(pixels)
        
                
                
        rows=len(results)
        if rows==0 or rows>1:
            
            print(filename+' Rejected')
            remove(path)
        else:
            print('Image '+filename+'accepted')	 
            x1, y1, width, height = results[0]['box']
                            
            x1, y1 = abs(x1), abs(y1)
            x2, y2 = x1 + width, y1 + height
                        
            face = pixels[y1:y2, x1:x2]
                    
            image = Image.fromarray(face)

            image = image.resize(required_size)
            image.show()
            #now save this image in a common folder containg all the students with folder-name same as student name

                    
                
faceaccept('./RithikaS')        


        
    
