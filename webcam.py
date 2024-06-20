import cv2
import numpy as np
from tensorflow.keras.models import load_model
from time import sleep
import json
model_path = r'D:\projects\aishwarya\ECOHUB.h5'
model = load_model(model_path)


classes = ['metal', 'plastic', 'paper', 'trash', 'glass', 'cardboard']


timer = 5 


prev_detected_class = None


cap = cv2.VideoCapture(0)



while True:
    
    ret, frame = cap.read()

   
    if not ret:
        print("Error: Failed to capture frame")
        break

    
    timer -= 1

    
    if timer == 0:
       
        timer = 5

       
        frame = cv2.resize(frame, (224, 224))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = frame / 255.0
        frame = np.expand_dims(frame, axis=0)

       
        predictions = model.predict(frame)

        
        predicted_class_index = np.argmax(predictions)
        predicted_class = classes[predicted_class_index]

       
        if predicted_class != prev_detected_class:
            if predicted_class in ['paper', 'plastic', 'trash']:
                
                print(json.dumps({"Detected": predicted_class}))
            else:
                
                print("Detected:", predicted_class)
            prev_detected_class = predicted_class

    
    if frame is not None and frame.shape[0] > 0 and frame.shape[1] > 0 and frame.shape[2] == 3:
        cv2.imshow('Frame', frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()