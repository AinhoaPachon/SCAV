import os
import numpy as np

# ----------------------------------------------------------------------------------------------------------------------

def RGB_to_YUV(r, g, b):
    # To convert from RGB to YUV I have used the operations shown in theory 1, pg. 46
    # Takes as inputs R, G and B values from 0 to 255
    Y = 0.257 * r + 0.504 * g + 0.098 * b + 16
    U = -0.148 * r - 0.291 * g + 0.439 * b + 128
    V = 0.439 * r - 0.368 * g - 0.071 * b + 128

    return round(Y), round(U), round(V)


print(RGB_to_YUV(50, 61, 70))

def YUV_to_RGB(y, u, v):
    # To convert from YUV space to RGB space
    # Takes as inputs Y, U and V values
    R = 1.164 * (y - 16) + 1.596 * (v - 128)
    G = 1.164 * (y - 16) - 0.813 * (v - 128) - 0.391 * (u - 128)
    B = 1.164 * (y - 16) + 2.018 * (u - 128)

    return round(R), round(G), round(B)


y, u, v = RGB_to_YUV(50, 61, 70)


print(YUV_to_RGB(y, u, v))

# ----------------------------------------------------------------------------------------------------------------------

def resize_images(name, width):
    # Reduces the input image size to the desired width maintaining the aspect ratio
    # Takes as inputs the name of the image and the output width
    command = 'ffmpeg -i ' + name + ' -vf scale="' + str(width) + ':-1" output.jpg'
    os.system(command)


resize_images('animal_crossing.jpg', 320)

# ----------------------------------------------------------------------------------------------------------------------

# Source: https://github.com/getsanjeev/compression-DCT/blob/master/zigzag.py
def serpentine(input):
    # initializing the variables
    # ----------------------------------
    h = 0
    v = 0

    vmin = 0
    hmin = 0

    vmax = input.shape[0]
    hmax = input.shape[1]

    i = 0

    output = np.zeros((vmax * hmax))
    # ----------------------------------

    while ((v < vmax) and (h < hmax)):

        if ((h + v) % 2) == 0:  # going up

            if (v == vmin):
                # print(1)
                output[i] = input[v, h]  # if we got to the first line

                if (h == hmax):
                    v = v + 1
                else:
                    h = h + 1

                i = i + 1

            elif ((h == hmax - 1) and (v < vmax)):  # if we got to the last column
                # print(2)
                output[i] = input[v, h]
                v = v + 1
                i = i + 1

            elif ((v > vmin) and (h < hmax - 1)):  # all other cases
                # print(3)
                output[i] = input[v, h]
                v = v - 1
                h = h + 1
                i = i + 1

        else:  # going down

            if ((v == vmax - 1) and (h <= hmax - 1)):  # if we got to the last line
                # print(4)
                output[i] = input[v, h]
                h = h + 1
                i = i + 1

            elif (h == hmin):  # if we got to the first column
                # print(5)
                output[i] = input[v, h]

                if (v == vmax - 1):
                    h = h + 1
                else:
                    v = v + 1

                i = i + 1

            elif ((v < vmax - 1) and (h > hmin)):  # all other cases
                # print(6)
                output[i] = input[v, h]
                v = v + 1
                h = h - 1
                i = i + 1

        if ((v == vmax - 1) and (h == hmax - 1)):  # bottom right element
            # print(7)
            output[i] = input[v, h]
            break

    # print ('v:',v,', h:',h,', i:',i)
    return output


input = np.matrix([[1, 2, 3, 4, 5, 6, 7, 8],
                   [1, 2, 3, 4, 5, 6, 7, 8],
                   [1, 2, 3, 4, 5, 6, 7, 8],
                   [1, 2, 3, 4, 5, 6, 7, 8],
                   [1, 2, 3, 4, 5, 6, 7, 8],
                   [1, 2, 3, 4, 5, 6, 7, 8],
                   [1, 2, 3, 4, 5, 6, 7, 8],
                   [1, 2, 3, 4, 5, 6, 7, 8]])

print(serpentine(input))

# ----------------------------------------------------------------------------------------------------------------------

def BandW_conversion(name, level):
    # Converts an image to black and white while compressing it
    # Takes as inputs the name of the image and the level of compression
    # The compression level ranges from 0 to 100, being 0 the hardest compression
    command = 'ffmpeg -i ' + name + ' -vf format=gray -compression_level ' + str(level) + ' output_BandW.jpg'
    os.system(command)


BandW_conversion('animal_crossing.jpg', 0)
# In the output we can clearly see the black and white conversion, and if we take a look to the file size before and
# after the command, we can clearly see that we have reduced the file size up to almost nine times

# ----------------------------------------------------------------------------------------------------------------------

def run_length_encoding(prevArray):
    counter = 0  # Counter to keep track of the amount of sequential zeros
    previous = -1  # Previous value of the array to be encoded
    j = 0  # Index of the encoded array
    encodedArray = []

    for i in range(len(prevArray)):
        if prevArray[i] != 0:  # Checks if current byte is different from zero
            if previous == 0:
                encodedArray.append(counter)  # If the current one it is not zero, but the previous one was
                counter = 0  # it appends the counter before appending the current byte
            encodedArray.append(prevArray[i])  # It also resets the counter
            j += 1

        else:
            if previous != 0:  # Appends the first zero from the possible zero sequence
                encodedArray.append(prevArray[i])
                j += 1
            counter += 1

        if i == len(prevArray) - 1 and counter != 0:  # If the last position of the array was a zero
            encodedArray.append(counter)  # it also appends the counter

        previous = prevArray[i]

    return encodedArray

prevArray = [1, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0]

print(run_length_encoding(prevArray))