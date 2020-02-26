import cv2
from glob import glob


def resize_greyscale_image(image_file: str, target_pixel: int, output_file: str) -> None:
    """
    Resize and turn the image into greyscale and save it.
    :param image_file: Image file.
    :param target_pixel: Target width/height
    :param output_file: Output file
    :return: None.
    """
    image = cv2.imread(image_file)
    larger = max(image.shape[0], image.shape[1])
    scale_factor = target_pixel/larger
    resized_image = cv2.resize(image, (round(image.shape[0] * scale_factor),
                                       round(image.shape[1] * scale_factor)))
    grayscale = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_file, grayscale)


def generate_images(src: str, output: str, target_pixel: int) -> None:
    """
    Generate images
    :param src: Source folder
    :param output: Output folder
    :param target_pixel: Target pixel width/height
    :return: None.
    """
    for i, image in enumerate(glob(src + "*.jpg")):
        resize_greyscale_image(image, target_pixel, f"{output}{i:04}.jpg")


def generate_positive_images(positive_src: str, output_src: str) -> None:
    """
    Preprocess positive images.
    :param positive_src: Positive image source.
    :param output_src: Output source.
    :return: None.
    """
    generate_images(positive_src, output_src, 50)


def generate_negative_images(negative_src: str, output_src: str) -> None:
    """
    Preprocess negative images.
    :param negative_src: Negative images folder.
    :param output_src: Output folder.
    :return: None.
    """
    generate_images(negative_src, output_src, 100)


def preprocess(negative_source: str, positive_source: str, negative_output: str, positive_output: str) -> None:
    """
    Preprocess images.
    :param negative_source: Source folder for negatives
    :param positive_source: Source folder for positives
    :param negative_output: Output folder for negatives
    :param positive_output: Output folder for positives.
    :return: None.
    """
    generate_negative_images(negative_source, negative_output)
    generate_positive_images(positive_source, positive_output)


if __name__ == "__main__":
    generate_positive_images("positive_images/", "positives/")
    #preprocess("negative_images/", "positive_images/", "negatives/", "positives/")