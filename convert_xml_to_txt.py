import os
import xml.etree.ElementTree as ET
from tqdm import tqdm


# Define class labels
classes = ["Arabic_Box", "Latin_Box", "Number","Mixed_Box"]

# Define input and output directories
input_dir = "C:\\Users\\farha\\OneDrive\\Desktop\ASAYAR_TXT\\Annotations\\Line-Level\\Train"
output_dir = "Train\\Images"

def convert_xml_to_txt(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    filename = os.path.basename(xml_file)[:-4] + ".txt"
    output_file = os.path.join(output_dir, filename)

    width = int(root.find("size/width").text)
    height = int(root.find("size/height").text)

    with open(output_file, "w") as f:
        for obj in root.findall("object"):
            class_label = obj.find("name").text
            class_id = classes.index(class_label)

            xmin = int(obj.find("bndbox/xmin").text)
            ymin = int(obj.find("bndbox/ymin").text)
            xmax = int(obj.find("bndbox/xmax").text)
            ymax = int(obj.find("bndbox/ymax").text)

            x = (xmin + xmax) / 2 / width
            y = (ymin + ymax) / 2 / height
            w = (xmax - xmin) / width
            h = (ymax - ymin) / height

            line = f"{class_id} {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n"
            f.write(line)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

xml_files = os.listdir(input_dir)
for xml_file in tqdm(xml_files):
    if not xml_file.endswith(".xml"):
        continue
    xml_path = os.path.join(input_dir, xml_file)
    convert_xml_to_txt(xml_path)