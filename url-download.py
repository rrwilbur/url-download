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


with open('url-list.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        create_output_directory(row["directory"])
        create_directories(row["directory"], row["image_folder"])
        download_image(row["directory"], row["image_folder"], row["image_1"], '1.jpg')
        download_image(row["directory"], row["image_folder"], row["image_2"], '2.jpg')
        download_image(row["directory"], row["image_folder"], row["image_3"], '3.jpg')
        download_image(row["directory"], row["image_folder"], row["image_4"], '4.jpg')
       
  




        print(f'\t{row["directory"]} {row["image_folder"]} {row["image_1"]} {row["image_2"]} {row["image_3"]} {row["image_4"]}.')
        line_count += 1
    print (f'Processed {line_count} lines.')
