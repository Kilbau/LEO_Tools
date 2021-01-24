import numpy


def output_planes_to_cook(cop_node):
    return ("C", "A")


def required_input_planes(cop_node, output_plane):
    return ("0", "C")


def resolution(cop_node):
    # get the resolution of the connected node
    input_cop = cop_node.inputs()[0]
    input_res = [input_cop.xRes(), input_cop.yRes()]

    # scale the imagesize to match the font size
    scale = cop_node.parm("img_scale").eval()
    res = (input_res[0] * scale, input_res[1] * scale)

    # TODO: fix problem when resizing the image with numpy.reshape

    return res


def cook(cop_node, plane, resolution):

    # set background color and size
    num_pixels = resolution[0] * resolution[1]

    # set bg color from parameter
    rgba = cop_node.parmTuple("bg_color").eval()
    pixel = rgba[3:] if plane == "A" else rgba[:3]
    cop_node.setPixelsOfCookingPlane(pixel * num_pixels)

    # calculate ascii chars
    if plane == "C":

        # init output
        output_text = []

        input_cop = cop_node.inputs()[0]
        str_data = input_cop.allPixelsAsString(plane)

        # this only works with dtype=numpy.float32 if the input raster depth is also 32 bit floating point
        # TODO: reshape often failes for some reason //// i guess the problem is that the python nodes is cached and opening cached frames causes problems
        # maybe somehow force houdini to always newly calculate this node instead of relying on caches.
        # resultion numpy array goes from top to bottom of the image
        read_only_float_data = numpy.frombuffer(
            str_data, dtype=numpy.float32
        )  # use convert node to convert image to 32 bit float beforehand
        # TODO: test if there are less problems when the reshaped data is in another variable
        read_only_float_data = read_only_float_data.reshape(
            resolution[1], resolution[0], 3
        )

        for row in read_only_float_data:
            # TODO: fix format issue. maybe add a pixel perfect toggle. if off this will skip every couple lines to match the font format
            for pixel in row:
                char = get_character(cop_node, get_brightness(pixel))
                output_text.append(char)

            output_text.append("\n")

        # convert output to text
        # flip the image vertically to fix the default scanline direction
        output_text = "".join(output_text)

        # set ouput
        # TODO: update the text parm to match the size of the image (if possible)
        cop_node.node("../").parm("text").set(output_text)


def update_text(cop_node, plane, resolution):
    pass


def get_brightness(rgb):
    return numpy.mean(rgb)


def get_character(cop_node, brightness):
    characters = cop_node.parm("characters").evalAsString()

    # remap brightness to get the index from the characters list
    len_characters = len(characters)
    index = int(round(brightness * len_characters))

    # return character
    try:
        return characters[index]
    except IndexError:
        return characters[-1]


def flip_characters(kwargs):
    cop_node = kwargs["node"]
    parm = cop_node.parm("characters")

    orig_characters = parm.evalAsString()
    parm.set(orig_characters[::-1])