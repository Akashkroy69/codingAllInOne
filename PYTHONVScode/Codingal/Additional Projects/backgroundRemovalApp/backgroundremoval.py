import cv2
import numpy as np

def remove_background(image_path):
    # Read the image
    img = cv2.imread(image_path)
    
    # Create a mask
    mask = np.zeros(img.shape[:2], np.uint8)
    
    # Define the background and foreground models
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)
    
    # Define a rectangle around the object to help the algorithm
    rect = (50, 50, img.shape[1] - 50, img.shape[0] - 50)
    
    # Apply GrabCut algorithm
    cv2.grabCut(img, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)
    
    # Modify the mask to get a binary mask for the foreground
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    
    # Apply the mask to the original image
    result = img * mask2[:, :, np.newaxis]

    return result

if __name__ == "__main__":
    input_image_path = r"Codingal\Additional Projects\backgroundRemovalApp\chacha.jpg"
    output_image = remove_background(input_image_path)

    # Display the original and processed images
    cv2.imshow("Original Image", cv2.imread(input_image_path))
    cv2.imshow("Background Removed", output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
