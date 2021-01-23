import calendar
import os
import shutil
import time

import barcode
from barcode.writer import ImageWriter
from docx import Document

timestamp = calendar.timegm(time.gmtime())


def get_path(path):
    path = path.replace("\\", "\\\\")
    path = path.replace("\"", "")
    return path


def generate_barcodes(eans):
    for el in eans:
        ean = barcode.get('ean13', str(el), writer=ImageWriter())
        ean.save(f'images\\{el}_{timestamp}', {
            'module_height': 4.5,
            'module_width': 0.12,
            'text_distance': 0.25,
            'font_size': 4,
            'quiet_zone': 0.5,
        })


def get_img_paths():
    basepath = 'images/'
    images = []

    for image in os.listdir(basepath):
        if str(timestamp) not in image:
            pass
        else:
            if os.path.isfile(os.path.join(basepath, image)):
                images.append(image)

    return images


def word_document(date):
    document = Document('demo3.docx')

    images = get_img_paths()
    print(f'Input has {len(images)} items')

    for img in images:
        document.add_picture(f'images/{img}')

    new_file_path = f'documents/barcodes_from_{date}_{timestamp}.docx'

    document.save(new_file_path)
    print('File successfully created!')


def delete_images():
    folder = './images'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
