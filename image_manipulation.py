import cv2
import os
import numpy as np
import cv2
import numpy as np
import io

def image_manipulation(image_obj, time, longitude, latitude):
    print(time)
    print(longitude)
    print(latitude)
    # Decode the raw image data into a NumPy array
    nparr = np.frombuffer(image_obj.file_contents, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)

    # Apply Canny edge detection
    edges = cv2.Canny(image, threshold1=100, threshold2=200)

    # Return the edges image
    _, buffer = cv2.imencode(".jpg", edges)

    # Convert the memory buffer to a bytes object
    bytes_obj = buffer.tobytes()

    # Create a file-like object from the bytes object
    file_obj = io.BytesIO(bytes_obj)

    # save the image
    return file_obj

