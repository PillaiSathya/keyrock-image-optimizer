# app/main.py

from PIL import Image
import argparse
import os

def resize_image(input_path, output_path, width, height):
    image = Image.open(input_path)
    resized_image = image.resize((width, height))
    resized_image.save(output_path)
    print(f"Image saved to {output_path}")

def compress_image(input_path, output_path, quality):
    image = Image.open(input_path)
    image.save(output_path, optimize=True, quality=quality)
    print(f"Compressed image saved to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Image Optimizer CLI")
    parser.add_argument("input", help="Input image path")
    parser.add_argument("output", help="Output image path")
    parser.add_argument("--resize", nargs=2, type=int, metavar=("width", "height"), help="Resize image to width height")
    parser.add_argument("--compress", type=int, metavar="quality", help="Compress image with given quality (1-95)")

    args = parser.parse_args()

    if args.resize:
        resize_image(args.input, args.output, args.resize[0], args.resize[1])
    elif args.compress:
        compress_image(args.input, args.output, args.compress)
    else:
        print("No action specified. Use --resize or --compress")

if __name__ == "__main__":
    main()
