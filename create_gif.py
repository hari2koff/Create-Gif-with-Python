# First Import our library  
import imageio.v3 as iio 



# adding the file name with extension for iio.read method in lib to read the image

file_names = ['team-pic1.png', 'team-pic2.png']   

#Creating an empty list so the image read can be stored 
 
images = []    

# Creating a function that will create Gif 

def create_gif():
    # for loop to iterate over the list & , so it will iterate over all the elements 

    for img in file_names:
        images.append(iio.imread(img))  # .imread is a built in method which will read image and store th pixel data in memeory 

    # Save as Gif by using the .imwrite method (which writes the stored pixel memory into file )    

    iio.imwrite('Generated.gif', images, duration = 500, loop = 0)   


create_gif()









        






