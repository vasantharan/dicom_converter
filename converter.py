import os
import pydicom
from PIL import Image
def dcm_to_jpg(f_path, o_path):
    dcm_data = pydicom.dcmread(f_path)
    if 'PixelData' in dcm_data:
        image = dcm_data.pixel_array
        image = (image / image.max()) * 255
        jpg_f_path = os.path.join(o_path, os.path.basename(f_path) + '.jpg')
        image = Image.fromarray(image.astype('uint8'))
        image.save(jpg_f_path)
        print(f"Converted: {f_path} -> {jpg_f_path}")

def conv_dcm_to_jpg(f_path, o_path):
    if not os.path.exists(o_path):
        os.makedirs(o_path)
    for root, _, files in os.walk(f_path):
        for file in files:
            if file.endswith('.dcm'):
                file_path = os.path.join(root, file)
                dcm_to_jpg(file_path, o_path)

def convert(folder_path, output_path):
    conv_dcm_to_jpg(folder_path, output_path)
