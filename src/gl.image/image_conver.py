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

def getSplitImage(jpgfile,outdir):
    img = Image.open(jpgfile)
    startX = 1
    startY = 241
    width= 157
    height = 90
    gapX = 3
    gapY = 9
#    box=(1,240,1+185,240+110)
    for i in range(0, 15):
        startX1 = startX+(width*(i%3)) + gapX*(i%3)
        startY1 = startY+(height*(i/3)) + gapY*(i/3)
        
        
        box=(startX1,startY1,startX1+width,startY1+height)
        region = img.crop(box)
#        region.show()
        region.save(os.path.join(outdir,"num_" + str(i) + ".png" ))
#        newImg = Image.new("RGBA",(width,height),(64,64,64))
#        newImg.paste(region,(0,0,width,height))
#    newImg.show()
#    newImg.save(os.path.join(outdir,os.path.basename(jpgfile)))
   
    
#for jpgfile in glob.glob("D:/yingshuang_android/*.jpg"):
    #convertjpg(jpgfile,"D:/yingshuang_android/new_file")
#    print jpgfile

#newImg = Image.new("RGBA",(300,300),(255,0,255))
#newImg.show()



getSplitImage("D:/work/n5/PCI/shouying.jpg","D:/images")
