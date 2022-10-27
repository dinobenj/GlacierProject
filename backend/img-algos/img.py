from PIL import Image

def is_in_bounds(x, y, width, height):
    return x >= 0 and x < width and y >= 0 and y < height

def get_adjacent(x, y, width, height):

    return list(filter(lambda point: is_in_bounds(*point, width, height), 
    [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]))


def determine_color(r: int, g: int, b: int) -> str:
    color = None
    if r > g and r > b:
        color = "orange"
    else:
        color = "white"
    return color


def traverse_glacier_image(imgfile):

    img = Image.open(imgfile).convert('RGB')

    pixels_explored = set()
    regions = { 
        "green": [[]],
        "yellow": [[]],
        "orange": [[]],
        "white": [[]]
    }
    # do funky logic to add new region to new list within list in dict
    def get_regions(pixels: list, last_pixel: tuple, this_pixel: tuple, region: int):
        
        if this_pixel in pixels_explored:
            return

        pixels_explored.add(last_pixel)
        pixels_explored.add(this_pixel)
        
        if determine_color(*img.getpixel(last_pixel)) != determine_color(*img.getpixel(this_pixel)):
            # change region num to reflect len of list within regions
            # determine what direction we need to explore in
            color = determine_color(*img.getpixel(this_pixel))
            current_region_number = len(regions[color])
            regions[color].append([])

            x = this_pixel[0]
            y = this_pixel[1]

            neighbors = get_adjacent(x, y, img.width, img.height)

            for n in neighbors:
                get_regions(regions[determine_color(*img.getpixel(this_pixel))], this_pixel, (n[0], n[1]), current_region_number)
            
        x = this_pixel[0]
        y = this_pixel[1]

        neighbors = get_adjacent(x, y, img.width, img.height)

        for n in neighbors:
            get_regions(pixels, this_pixel, (n[0], n[1]), region)
        
    region = 0
    first_pixel = (0, 0)
    # start the search

    get_regions(regions[determine_color(*img.getpixel(first_pixel))], first_pixel, (0, 1), region)
    get_regions(regions[determine_color(*img.getpixel(first_pixel))], first_pixel, (1, 0), region)

    return regions


if __name__ == "__main__":
    regions = traverse_glacier_image("./test2.png")

    print(regions)
    print(get_adjacent(1, 1, 5, 5))