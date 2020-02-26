from xml.etree import ElementTree
from create_positives import copy_from_subdirectories, list_subdirectories
from typing import List, Tuple
from math import floor
from os import getcwd


def aggragate_annotations():
    subdirectories = list_subdirectories("Annotation/")
    copy_from_subdirectories(subdirectories, r"annotations/", "")


def convert_coordinates(x_min, y_min, x_max, y_max, w, h) -> tuple:
    x_width = x_max - x_min
    y_height = y_max - y_min
    return tuple(map(lambda x: floor(x), (x_min, y_min, x_width, y_height)))


def combine_annotations():
    positives_index = ""
    for image_count in range(6000):
        tree = ElementTree.parse(f'annotations/{image_count:04}.xml')
        root: ElementTree.Element = tree.getroot()
        objects = root.findall("object")
        coords_converted: List[str] = []
        w = int(root.find("size").find('width').text)
        h = int(root.find("size").find('height').text)
        for object_ in objects:
            box = object_.find('bndbox')
            coords = tuple(int(box.find(coord).text) for coord in ["xmin", "ymin", "xmax", "ymax"])
            converted_coords = convert_coordinates(*coords, w, h)
            coords_converted.append(' '.join(tuple(map(lambda x: str(x), converted_coords))))
        positives_index += f"positive_images/{image_count:04}.jpg   {len(objects)}   {'   '.join(coords_converted)}\n"
    with open("info.dat", "w+") as file_:
        file_.write(positives_index)

if __name__ == "__main__":
    aggragate_annotations()
    combine_annotations()
