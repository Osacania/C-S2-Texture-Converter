from PIL import Image
from tkinter import messagebox

def conbine_image(path, filename):
    #画像の読み込み
    img_m = Image.open(path + filename + "_metallic.png") #Metallic
    img_c = Image.open(path + filename + "_coat.png") #Coat
    img_g = Image.open(path + filename + "_glossiness.png") #Glossiness
    #モノクロに変換（エラー回避のため）
    img_m = img_m.convert("L")
    img_c = img_c.convert("L")
    img_g = img_g.convert("L")
    if img_m.width == img_c.width == img_g.width and img_m.height == img_c.height == img_g.width:
        size_x = img_m.width
        size_y = img_m.height
        
        img_result = Image.new("RGBA", (size_x, size_y))
        
        for y in range(size_y):
            for x in range(size_x):
                r = img_m.getpixel((x,y))
                g = img_c.getpixel((x,y))
                b = 0
                a = img_g.getpixel((x,y))
                
                img_result.putpixel((x,y),(r,g,b,a))
        
        img_result.save("test_MaskMap.png")
        messagebox.showinfo("確認", "処理が完了しました。")