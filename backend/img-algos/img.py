import PIL

def get_adjacent(x, y):
    pass


def is_in_bounds(x, y, width, height):
    return x < width and y < height


def determine_color(r: int, g: int, b: int) -> str:

    pass


def traverse_glacier_image(imgfile):

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

        if determine_color(*last_pixel) != determine_color(*this_pixel):
            # change region num to reflect len of list within regions
            # determine what direction we need to explore in
            get_regions(regions[determine_color(*this_pixel)], this_pixel, (this_pixel[0] + 1, this_pixel[1]), region+1)

        x = this_pixel[0]
        y = this_pixel[1]

        get_regions(regions[determine_color(*this_pixel)], this_pixel, (this_pixel[0] + 1, this_pixel[1]), region+1)
        get_regions(regions[determine_color(*this_pixel)], this_pixel, (this_pixel[0] - 1, this_pixel[1]), region+1)
        get_regions(regions[determine_color(*this_pixel)], this_pixel, (this_pixel[0] + 1, this_pixel[1]), region+1)
        get_regions(regions[determine_color(*this_pixel)], this_pixel, (this_pixel[0] + 1, this_pixel[1]), region+1)


        
        pass

    # get_regions(re)
    return regions


if __name__ == "__main__":
    traverse_glacier_image("./test2.png")