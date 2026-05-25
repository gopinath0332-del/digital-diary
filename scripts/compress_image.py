
import sys
from PIL import Image
import os

def compress_image(input_path, output_path, max_width=1280, quality=85):
    try:
        with Image.open(input_path) as img:
            # Maintain aspect ratio
            w, h = img.size
            if w > max_width:
                new_h = int(h * (max_width / w))
                img = img.resize((max_width, new_h), Image.Resampling.LANCZOS)
            
            # Save as JPEG with quality compression
            img.convert('RGB').save(output_path, 'JPEG', quality=quality, optimize=True)
            return True
    except Exception as e:
        print(f"Error compressing image: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python compress_image.py <input> <output>")
        sys.exit(1)
    
    if compress_image(sys.argv[1], sys.argv[2]):
        print("Success")
    else:
        sys.exit(1)
