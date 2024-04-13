import cv2
import os
import numpy as np
def image_manipulation(image_path):
  image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
  edges = cv2.Canny(image, threshold1=100, threshold2=200)
  image_name = os.path.splitext(image_path)[0]
  output_path = f"{image_name}_edges.png"
  cv2.imwrite(output_path, edges)
  return output_path
