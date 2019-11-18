'''
Function Stubs:
'''

'''
**GUI Functions**
'''

#This function will call the file explorer on the user's machine and allows them to select 
#the image they want colorized. The file path will then be displayed within the GUI along with
#an icon version of the selected image
def browse_file():

'''
Machine Learning Algorithm Code:
'''

#Given two image file name strings, and the learned key file name, this procedure compares
#hue and saturation values of each image, and updates this information into the master learned key file 
def compare_images(img1, img2, key):

#Given the name of an image file (String), this function returns a list of 
#tuples containing hue and saturation values of each pixel in the image.
def get_image_values(img_file):

#This function accepts two tuples containing the hue and saturation values of corresponding #pixels 
#between a black and white image and a color image and returns a value to put in the colorization key
def compare_hs_values(black_white_vals, color_vals):

#Colorization Code:

#Procedure that Makes a copy of the black and white image file the user gives, which will be directly 
#changed and made in color.
def copy_image(img_file)

#given a string containing the name of the file containing the learned key, this function returns a 
#list of all the key values
def get_key_values(key_file)

#given a reference to the learned key, and a tuple of black and white hue and saturation values, 
#this function returns a tuple of new colorized hue and saturation values
def predict_hs_val(key, h_s_vals):

#given a string of the name of the original black and white image file and a reference to the key 
#list, this function returns a list of tuples for the hue and saturation values of the colorized image
def get_new_hs_vals(key, bw_file):


#Given strings for the original image file, the copy of this file, and the key file, this procedure puts 
#together all the past helper functions to find the new hue and saturation values for the colorized file 
#and then updates the copy of the original file with these values.
def colorize_copy(copy_file, original_file, key_file): 
