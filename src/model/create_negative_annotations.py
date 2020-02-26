from glob import glob


def create_neg_annotations() -> None:
    """
    Create a list of negative images as per OpenCV guidlines
    :return: None
    """
    with open("bg.txt", "w+") as file_:
        file_.write('\n'.join(glob("negatives/*.jpg")))


if __name__ == "__main__":
    create_neg_annotations()