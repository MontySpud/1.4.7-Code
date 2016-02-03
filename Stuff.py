# -*- coding: utf-8 -*-
App_Mode = raw_input("Do you need: Image/Help? ")
if App_Mode == "Image":
    file_name = raw_input(" What file do you want to use? ")
    Mode = raw_input(" What brightness mod do you want to use? ")
    Logo = raw_input(" Do you want to use a logo? ")
    print " Ok, you are now using the %r image, with the %r mod, with logo mode set to %r!" % (file_name, Mode, Logo)
    
    '''
    JDoe_JSmith_1_4_3: Change pixels in an image.
    '''
    import matplotlib.pyplot as plt 
    import os.path
    import numpy as np      # â€œasâ€ lets us use standard abbreviations

    '''Read the image data'''
    # Get the directory of this python script
    directory = os.path.dirname(os.path.abspath(__file__)) 
    # Build an absolute filename from directory + filename
    filename = os.path.join(directory, file_name)
    # Read the image data into an array
    img = plt.imread(filename)
    
    '''Imports Logo'''
    '''logo = Image.open('C:\Users\olsonco71\Desktop\142\trumplogo.png')'''
    
    '''Show the image data'''
    # Create figure with 1 subplot
    fig, ax = plt.subplots(1, 1)
    # Show the image data in a subplot
    ax.imshow(img, interpolation='none')
    ###
    # Change a region if condition is True
    ###
    
    if Mode == "1":
        height = len(img)
        width = len(img[0])
        for r in range(height):
            for c in range(width):
                if sum(img[r][c])>762: # brightness R+G+B goes up to 3*255=765
                    img[r][c]=[100,0,0] # R + B = magenta
                else:
                    img[r][c]=[0,0,100]
    
    if Mode == "2":
        height = len(img)
        width = len(img[0])
        for r in range(height):
            for c in range(width):
                if sum(img[r][c])>700: # brightness R+G+B goes up to 3*255=765
                    img[r][c]=[100,0,0] # R + B = magenta
                else:
                    img[r][c]=[0,0,100]
    
    if Mode == "3":
        height = len(img)
        width = len(img[0])
        for r in range(height):
            for c in range(width):
                if sum(img[r][c])>762: # brightness R+G+B goes up to 3*255=765
                    img[r][c]=[0,0,100] # R + B = magenta
                else:
                    img[r][c]=[100,0,0]
    
    if Mode == "4":
        height = len(img)
        width = len(img[0])
        for r in range(height):
            for c in range(width):
                if sum(img[r][c])>700: # brightness R+G+B goes up to 3*255=765
                    img[r][c]=[0,0,100] # R + B = magenta
                else:
                    img[r][c]=[100,0,0]         
    '''.paste(earth_small, (1162, 966), mask=earth_small) '''
    
    ###
    # Show the image data
    ###
    # Show the figure on the screen
    fig.show()
    
    img = plt.imread(filename)
if App_Mode == "Help":
    print " For the Image Field, type in a JPG with a white backdrop"
    print " For the Mod field, type in a value 1 - 4"
    print " 1 is in D colours but with a higher brightness limit"
    print " 2 is in D colours but with a lower brightness limit"
    print " 3 is the same as 1, but with R colours"
    print " 4 is the same as 2, but with R colours"
print 'done!'
