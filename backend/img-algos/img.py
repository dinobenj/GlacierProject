import this
from PIL import Image

# import sys
# sys.setrecursionlimit(10000)
# depth = 0


def is_in_bounds(x, y, width, height):
    return x >= 0 and x < width and y >= 0 and y < height

def get_adjacent(x, y, width, height):

    return list(filter(lambda point: is_in_bounds(*point, width, height), 
    [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]))


def determine_color(r: int, g: int, b: int) -> str:
    if g > r and g > b:
        if g - r >= 50:
            return "green"
        return "yellow"

    if r - g >= 50:
        return "orange"
    return "white"


def traverse_glacier_image(imgfile):

    img = Image.open(imgfile).convert('RGB')
    test = Image.new(mode="RGB", size=(img.width, img.height))
 
# This method will show image in any image viewer
    pixels_explored = set()
    regions = { 
        "green": [],
        "yellow": [],
        "orange": [],
        "white": []
    }

    rgb = {
        "green": (0, 255, 0),
        "yellow": (255, 255, 0),
        "orange": (255, 128, 0),
        "white": (255, 255, 255)
    }

    def get_regions_iter():

        for i in range(img.width):
            for j in range(img.height):
                current_pixel = (i, j)
                color = determine_color(*img.getpixel(current_pixel))

                regions[color].append(current_pixel)



    # do funky logic to add new region to new list within list in dict
    def get_regions(pixels: list, last_pixel: tuple, this_pixel: tuple, region: int):
        # global depth
        #pixels_explored.add(last_pixel)
        # pixels_explored.add(this_pixel)

        # print(last_pixel)
        # if depth == 5000:
        #     return

        if this_pixel in pixels_explored:
            return

        pixels_explored.add(last_pixel)
        # pixels_explored.add(this_pixel)



        if determine_color(*img.getpixel(last_pixel)) != determine_color(*img.getpixel(this_pixel)):
            # change region num to reflect len of list within regions
            # determine what direction we need to explore in
            color = determine_color(*img.getpixel(this_pixel))
            current_region_number = len(regions[color])
            regions[color].append([])
            regions[color][current_region_number].append(this_pixel)

            x = this_pixel[0]
            y = this_pixel[1]

            neighbors = get_adjacent(x, y, img.width, img.height)
            depth += len(neighbors)

            for n in neighbors:
                get_regions(regions[determine_color(*img.getpixel(this_pixel))], this_pixel, (n[0], n[1]), current_region_number)
        else:    
            pixels.append(this_pixel)
            x = this_pixel[0]
            y = this_pixel[1]

            neighbors = get_adjacent(x, y, img.width, img.height)
            depth += len(neighbors)
            for n in neighbors:
                get_regions(pixels, this_pixel, (n[0], n[1]), region)
        
    region = 0
    first_pixel = (0, 0)
    # start the search
    get_regions_iter()
    # print(regions)

    for region in regions.keys():
        r, g, b = rgb[region] 
        # print(regions[region] == [])
        for pixel in regions[region]:

            test.putpixel((pixel[0], pixel[1]), (r, g, b))
    # get_regions(regions[determine_color(*img.getpixel(first_pixel))], first_pixel, (0, 1), region)
    # get_regions(regions[determine_color(*img.getpixel(first_pixel))], first_pixel, (1, 0), region)
    test.show()
    return regions


if __name__ == "__main__":
    regions = traverse_glacier_image("./test2.png")

    # print(regions)
    # print(get_adjacent(1, 1, 5, 5))