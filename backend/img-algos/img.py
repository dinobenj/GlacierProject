import PIL


def determine_color(r: int, g: int, b: int) -> str:

    pass


def traverse_glacier_image(imgfile):

    regions = { 
        "green": [[]],
        "yellow": [[]],
        "orange": [[]],
        "white": [[]]
    }
    # do funky logic to add new region to new list within list in dict
    def get_regions(pixels: list, last_pixel: tuple, next_pixel: tuple, region: int):
        
        if determine_color(*last_pixel) != determine_color(*next_pixel):
            # change region num to reflect num
            get_regions(regions[determine_color(*next_pixel)], next_pixel, region+1)

            return
        pass

    # get_regions(re)
    return regions


if __name__ == "__main__":
    traverse_glacier_image("./test2.png")