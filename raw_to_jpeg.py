#utf-8
from PIL import Image
import rawpy
import os

print('Converting .ARW to Jpeg..!!')

# List of directories from where the images needs to be converted .

dir_to_search = ["../sony/",
                 "../sony_2/",
                 "../sony_3/"]

# Output directory
output_path = "../processed_images/"

for base_path in dir_to_search:
    print ("Working in directory {}".format(base_path))
    for root, dirs, files in os.walk(base_path):
        total_file_count = len(files)
        i = 1
        for filename in files:
            if '.ARW' in filename:
                print("Processing RAW file {} \n".format(filename))
                raw = rawpy.imread(base_path + filename)
                rgb = raw.postprocess(use_camera_wb=True)
                rgb2 = raw.postprocess(use_auto_wb=True)
                Image.fromarray(rgb).save(output_path+"{}_.jpeg".format(filename), quality=90, optimize=True)
                raw.close()
                print("Files Remaining {}".format(total_file_count-i) )
                i=i+1

