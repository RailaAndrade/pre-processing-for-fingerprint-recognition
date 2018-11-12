from PIL import Image
import json

sobelOperator = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]

# TODO: Não finalizada
def gradient_orientation(image, block_size):
    size = get_size(image)
    coordinate = get_coordinate(size)
    getPixel = get_pixel(image, (coordinate['x'], coordinate['y']))
    sobelCoordinate = get_sobel_coordinates(sobelOperator)

    result = [[] for i in range(1, coordinate['x'], block_size)]

    for i in range(1, coordinate['x'], block_size):
        for j in range(1, coordinate['y'], block_size):
            print('i,j', (i,j))
            # print('i', i)
            # print('j', j)
    return result

def convert_to_black_and_white(image):
    return image.convert('L')

def get_coordinate(size):
    return json.loads(size)

def get_pixel(image, (coordinateX, coordinateY)):
    image_load = image.load()
    return lambda coordinateX, coordinateY: image_load[coordinateX, coordinateY]

def get_size(image):
    (x,y) = image.size
    size = json.dumps({'x': x, 'y': y})
    return size

def get_sobel_coordinates(sobelOperator):
    sobel = json.dumps({'xSobel': transpose(sobelOperator), 'ySobel': sobelOperator})
    return json.loads(sobel)

def open_image(image):
    imageOpened = Image.open(image)
    return imageOpened

def save_image(image, imgOut):
	imageSaved = image.save('images/' + imgOut + '.jpg')
	return imageSaved    

def show_image(image):
    return image.show()

def transpose(matrix):
    transposedMatrix = list(zip(*matrix))
    return transposedMatrix