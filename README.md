# Convert Pascal VOC XML Annotation to COCO TXT Annotation

This repository contains a Python script that converts Pascal VOC XML annotation files to COCO TXT annotation files.

## Usage
 To use the script, simply run the following command:

```rb
python convert_xml_to_txt.py <input_dir> <output_dir>
```

where:
<br>
* `input_dir` is the directory containing the Pascal VOC XML annotation files
* `output_dir` is the directory where the COCO TXT annotation files will be saved
<br>
## Example

The following example shows how to convert all of the Pascal VOC XML annotation files in the `input_dir` directory to COCO TXT annotation files in the `output_dir` directory:
```rb
python convert_xml_to_txt.py <input_dir> <output_dir>
```

## Output

The COCO TXT annotation files will be saved in the `output_dir` directory. Each file will contain the following information:
  
* The class ID of the object
* The center coordinates of the object
* The width and height of the object

## Dependencies

* `xml.etree.ElementTree`
*  `tqdm`

## License
This repository is licensed under the MIT License.

## Author
This repository was created by Farhat Rekaya.
