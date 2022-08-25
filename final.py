from imagehash import phash
from PIL import Image
import requests
from io import BytesIO
  
def encode(image_link):
    # Encoding the image.
    response = requests.get(image_link)
    image = Image.open(BytesIO(response.content))
    image = Image.open(image_link)
    HEX = str(phash(image))
    BIN = bin(int(HEX, 16))[2:].zfill(64)
    return BIN

def find_plagiarism(check_image_link, image_links, threshold=10):
    """
    It takes an image link and a list of image links, and returns a tuple of a boolean and a string. 
    The boolean is True if the image link is similar to any of the images in the list, and False
    otherwise. 
    The string is the link of the image in the list that is most similar to the image link. 
    The threshold parameter is the maximum distance between the two images for them to be considered
    similar. 
    The default value is 10. 
    The function uses the compare function from the previous section to compare the images. 
    The encode function is used to encode the images. 
    The encode function takes an image link and returns the encoding of the image. 
    The url parameter is True by default, and if it is True, the function downloads the image from the
    link and encodes it. 
    If it is False, the function assumes that the image link is

    :param check_image_link: The link of the image you want to check for plagiarism
    :param image_links: a list of image links to compare against
    :param threshold: The minimum distance between the two images. If the distance is less than the
    threshold, then the images are considered to be similar, defaults to 10 (optional)
    :return: a tuple of two values. The first value is a boolean value that indicates whether the image
    is plagiarized or not. The second value is the link of the image that is plagiarized.
    """
    min_dist = 64
    flag = False
    result_link = ''

    check_encoded = encode(check_image_link)
    for image_link in image_links:
        encoded = encode(image_link, url=False)
        
        tmp = 64-sum([encoded[i]==check_encoded[i] for i in range(len(encoded))])
        if tmp < min_dist and tmp<threshold:
            tmp = min_dist
            result_link = image_link
            flag = True

    return flag, result_link


print('Import successfully')