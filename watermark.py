from PIL import Image

def create_watermark(image_path, final_image_path, watermark):
    main = Image.open(image_path)
    mark = Image.open(watermark)

    mask = mark.convert('L').point(lambda x: min(x, 25))
    mark.putalpha(mask)

    mark_width, mark_height = mark.size
    main_width, main_height = main.size
    aspect_ratio = mark_width / mark_height
    new_mark_width = main_width * 0.25
    mark.thumbnail((new_mark_width, new_mark_width / aspect_ratio), Image.ANTIALIAS)

    tmp_img = Image.new('RGB', main.size)

    for i in range(0, tmp_img.size[0], mark.size[0]):
        for j in range(0, tmp_img.size[1], mark.size[1]):
            main.paste(mark, (i, j), mark)
            main.thumbnail((8000, 8000), Image.ANTIALIAS)
            main.save(final_image_path, quality=100)

def watermark_image(image_path, watermark_path):
    image = Image.open(image_path)
    logo = Image.open(watermark_path)

    image_copy = image.copy()

    position = ((image_copy.width - logo.width), (image_copy.height - logo.height))

    # modify the paste by adding the logo as the third argument as per the explanation above.
    image_copy.paste(logo, position, logo)

    image_copy.save(image_path)

if __name__ == '__main__':
    root_dir = os.getcwd()
    WATERMARK = 'watermark.png' if os.path.isfile('./waterkark.png') else (sys.argv[2] if sys.argc > 1 else None)
    if WATERMARK is None:
        print("You really should define a watermark.png in the current directory, or passing it as an argument, or edit this file... you're a big boy")
        return sys.exit(1)

    for filename in find_files_recursive(root_dir):
        
        if os.path.basename(filename) != os.path.basename(WATERMARK):
            print(filename)
            watermark_image(filename, WATERMARK)