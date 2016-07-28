from PIL import Image
import os.path
import glob
def convertjpg(jpgfile,outdir,width=720,height=1280):
    img=Image.open(jpgfile)   
    newImg = Image.new("RGBA",(width,height),(255,255,255))
    box=(0,0,480,720)
    region = img.crop(box)
    box2=(120,280,480+120,720+280)
    newImg.paste(region,box2)
    #new_img=img.resize((width,height),Image.BILINEAR)   
    #new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    newImg.save(os.path.join(outdir,os.path.basename(jpgfile)))

    
for jpgfile in glob.glob("D:/yingshuang_android/*.jpg"):
    convertjpg(jpgfile,"D:/yingshuang_android/new_file")
    print jpgfile
    