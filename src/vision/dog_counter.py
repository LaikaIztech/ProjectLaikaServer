import cv2

def count_doggo(img_path, xml_path):
    dog_cascade = cv2.CascadeClassifier(xml_path)
    img = cv2.imread(img_path)
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dogs = dog_cascade.detectMultiScale(grayscale)
    return len(dogs)
