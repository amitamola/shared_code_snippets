'''
If you don't want to upload images on web but want to combine them into a PDF, you can simply use Pillow(PIL) library.
'''
from PIL import Image

im1 = Image.open("folder/subfolder/image1.jpg")
im2 = Image.open("folder/subfolder/image2.jpg")

im_list = [im2] #Just add additional image object beside im1

pdf1_filename = "filename.pdf"

im1.save(pdf1_filename, "PDF", save_all=True, append_images=im_list)
