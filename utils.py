import yolo_utils as y


def image_find_wasted_watter_bottle_demo(img):
    if (y.found(img)):
        print("conversion succeeded")
    else:
        print("conversion failed")
