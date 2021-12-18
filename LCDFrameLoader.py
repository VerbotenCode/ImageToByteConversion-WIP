'''
Function - Convert images to monochrome, then export the byte data
the byte data is recognizable by the LiquidCrystal arduino library
Input - .bmp files exported with the format of ffmpeg contained into a single directory indexed properly

Implementation:
    - Uses the same method

Bitmap images appear to display monochromatic images better, or at least more uniform than jpg

TODO
    - Refactor variable names
'''
from PIL import Image

def convert_to_monochrome(pixels, new_pixel, binary, threshold):
    for pixels in pixels:
        if pixels[0] <= threshold:
            # white
            new_pixel = (0, 0, 0)
            binary.append(0)
        else:
            # black
            new_pixel = (255, 255, 255)
            binary.append(1)
        newPixels.append(new_pixel)

def clear_binary():
    with open(r'/home/ubuntu/Desktop/byteData.txt', 'w') as output:
        # Resizes to 0 bytes
        output.truncate(0)

def parse_binary(binary, new_binary, pixel_width):
    with open(r'/home/ubuntu/Desktop/byteData.txt', 'a') as output:
        for i in range(0, len(binary)):
            output.writelines(',') # enable for commas to parse numbers
            if(i % pixel_width == 0):
                output.writelines('') # Character every certain interval (for visualization)
                new_binary.append('|') # ???
                # output.write('\n')
            output.writelines(str(binary[i]))
            new_binary.append(binary[i])
        print(new_binary)
        print('character length: ' + str(len(new_binary)))

def frame_calculator(frame_number):
        # Calculates the filename shift for ffmpeg exports
        if(len(str(frame_number)) == 1):
            return "00" + str(frame_number)
        elif(len(str(frame_number)) == 2):
            return "0" + str(frame_number)
        else:
            return str(frame_number)

threshold = 25 # Image Conversion Threshold
image_width, image_height, image_save = 200, 160, True
directory,file_extension = r'/home/ubuntu/frames/', '.bmp'
frame_quantity, starting_frame, frame_skip = 1, 100, 2
newPixels, binary, newBinary = [], [], [] # Empty Lists

#CONVERT TO MONOCHROME --- CHANGE TO LAMBDA

for i in range(0, frame_quantity):
    # Opens Image - Converts to monochrome - Resizes - Updates list - Parses textfile (for readability) - Resizes image
    clear_binary()
    img = Image.open(directory + frame_calculator(starting_frame + i) + file_extension)
    img_resized = img.resize((image_width, image_height)) # width, height
    pixels = list(img_resized.getdata())
    convert_to_monochrome(pixels, newPixels, binary, threshold)
    parse_binary(binary, newBinary, 10)
    if(i % frame_skip == 0 and image_save):
        img_resized.save('/home/ubuntu/Desktop/' + str(i) + '.bmp', 'bmp', optimize=True)
print("Complete!")