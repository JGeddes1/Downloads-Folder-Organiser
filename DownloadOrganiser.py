from os import scandir, rename
from os.path import exists, join, splitext
from shutil import move
import logging

source_dir = "J:\Downloads"
dest_dir_sfx = "J:\Downloads\sfx"
dest_dir_music = "J:\Downloads\Music"
dest_dir_video = "J:\Downloads\Video"
dest_dir_image = "J:\Downloads\Images"
dest_dir_documents = "J:\Downloads\Documents"
dest_dir_excel = "J:\Downloads\Documents"
dest_dir_exe = "J:\Downloads\Exe"

# image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# Video types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
#  Audio types
audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]

# Document types
document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"]




# exe types
exe_extensions = ".exe"






def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name

def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)

def on_cleaner():
    with scandir(source_dir) as entries:
        for entry in entries:
            name = entry.name
            check_audio_files(entry, name)
            check_exe_files(entry, name)
            check_video_files(entry, name)
            check_image_files(entry, name)
            check_document_files(entry, name)

def check_audio_files(entry, name):  # * Checks all Audio Files
    for audio_extension in audio_extensions:
        if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
            if entry.stat().st_size < 10_000_000 or "SFX" in name:  # ? 10Megabytes
                dest = dest_dir_sfx
            else:
                dest = dest_dir_music
            move_file(dest, entry, name)
            logging.info(f"Moved audio file: {name}")

def check_exe_files(entry, name):  # * Checks all Audio Files

    if name.endswith(exe_extensions) or name.endswith(exe_extensions.upper()):
        move_file(dest_dir_exe, entry, name)
        logging.info(f"Moved exe file: {name}")

def check_video_files(entry, name):  # * Checks all Video Files
    for video_extension in video_extensions:
        if name.endswith(video_extension) or name.endswith(video_extension.upper()):
            move_file(dest_dir_video, entry, name)
            logging.info(f"Moved video file: {name}")

def check_image_files(entry, name):  # * Checks all Image Files
    for image_extension in image_extensions:
        if name.endswith(image_extension) or name.endswith(image_extension.upper()):
            move_file(dest_dir_image, entry, name)
            logging.info(f"Moved image file: {name}")

def check_document_files(entry, name):  # * Checks all Document Files
    for documents_extension in document_extensions:
        if name.endswith(documents_extension) or name.endswith(documents_extension.upper()):
            move_file(dest_dir_documents, entry, name)
            logging.info(f"Moved document file: {name}")




if __name__ == '__main__':
     on_cleaner()
