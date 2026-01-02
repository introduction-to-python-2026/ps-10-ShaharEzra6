from image_utils2 import load_image, edge_detection
from skimage.filters import median
from skimage.morphology import disk

shahar_img = load_image("baby_me.JPG")
shahar_edge = edge_detection(shahar_img)
shahar_clean = median(shahar_edge, disk(3))
threshold = 100  # adjust if edges look too few or too many
edge_binary = shahar_clean > threshold
edge_image = Image.fromarray(edge_binary)
edge_image.save('my_edges.png')
