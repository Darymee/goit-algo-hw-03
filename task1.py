import os
import shutil
import argparse

def copy_files(source, dest):
    try:
        for item in os.listdir(source):
            item_path = os.path.join(source, item)

            if os.path.isdir(item_path):
               
                copy_files(item_path, dest)
            else:
               
                ext = os.path.splitext(item)[1][1:]
                if ext == "":
                    ext = "no_extension"

               
                ext_dir = os.path.join(dest, ext)
                if not os.path.exists(ext_dir):
                    os.makedirs(ext_dir)

   
                try:
                    shutil.copy2(item_path, ext_dir)
                    print(f"Copied: {item} -> {ext_dir}")
                except Exception as e:
                    print(f"Error copying {item}: {e}")
    except Exception as e:
        print(f"Error accessing {source}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy files into subdirectories based on their extensions")
    parser.add_argument("source_dir", help="Source directory")
    parser.add_argument("destination_dir", nargs="?", default="dist", help="Destination directory (default: dist)")
    args = parser.parse_args()

    source_dir = args.source_dir
    destination_dir = args.destination_dir

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    if not os.path.exists(source_dir):
        print(f"Source directory {source_dir} does not exist")
    else:
        copy_files(source_dir, destination_dir)
        print("Copying completed!")
