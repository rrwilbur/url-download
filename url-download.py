import csv

import os

cwd = os.getcwd()

import requests

def create_output_directory(output_directory):
    try:
        os.mkdir(os.path.join(cwd, output_directory))
        print("Created output directory")
    except OSError:
        print("Output directory already exists")


def create_directories(output_directory, image_folder):
    try:
        os.mkdir(os.path.join(cwd, output_directory, image_folder))
        print("Created image folders")
    except OSError:
        print("Directory {} already exists".format(image_folder))

def download_image(output_directory, image_folder, url, image_name):
    print('Beginning file download')

    if url:
        r = requests.get(url)
        with open(os.path.join(cwd, output_directory, image_folder, image_name), 'wb') as f:
            f.write(r.content)


def count_number_of_images_to_download(row: csv.DictReader) -> int:
    number_of_images = 0

    for fieldname in row.fieldnames:
        if "image" in fieldname:
            number_of_images +=1
    
        return number_of_images


with open('url-list.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        create_output_directory(row["directory"])
        create_directories(row["directory"], row["image_folder"])
        number_of_images = count_number_of_images_to_download(row)
        for index, image in enumerate(range(number_of_images)):
            try:
                if row[image]:
                    download_image(row["directory"], row["image_folder"], row[image], f"{index}.jpg")
            except KeyError:
                continue

    print(f'\t{row}')
    line_count += 1
    print (f'Processed {line_count} lines.')
