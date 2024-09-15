import cv2 #Import module cv2

# Message to show that Resizer has started
print("Image Resizer Started") 

# function to resize image
def img_resizer(image, save_image, reduce):

    # Read input image by cv2
    img = cv2.imread(image)

    # Calculate the new width and height as giver given reduce size
    new_width = int(img.shape[0] * reduce / 100)  
    new_height = int(img.shape[1] * reduce / 100) 

    # Resize the image using the calculated dimensions
    output = cv2.resize(img, (new_width, new_height))

    # Save the resized image to given name 
    cv2.imwrite(save_image, output)

    # Wait for a key press (optional) not necessary to save the image
    cv2.waitKey(0)

    # Message after save resized image
    print(f"Resized image {image} saved as {save_image} successfully")

# Take user input for the image file, output file, and reduce percent
image = input("Enter Image-:")         # Input: original image path
save_image = input("Image save as-:")  # Input: path to save the resized image
reduce = int(input("Reduce-:" ))       # Input: reduction percent for resize

# Call the img_resizer function with the user inputs
img_resizer(image, save_image, reduce)
