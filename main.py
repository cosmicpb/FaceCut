from pytube import YouTube
from pytube.cli import on_progress
import cv2
from datetime import timedelta
import numpy as np
import os
from pathlib import Path
from tqdm import tqdm


def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    print(f"Download video: {round(pct_completed, 2)} %")


def format_timedelta(td):
    """Utility function to format timedelta objects in a cool way (e.g 00:00:20.05)
    omitting microseconds and retaining milliseconds"""
    result = str(td)
    try:
        result, ms = result.split(".")
    except ValueError:
        return (result + ".00").replace(":", "-")
    ms = int(ms)
    ms = round(ms / 1e4)
    return f"{result}.{ms:02}".replace(":", "-")

def get_saving_frames_durations(cap, saving_fps):
    """A function that returns the list of durations where to save the frames"""
    s = []
    # get the clip duration by dividing number of frames by the number of frames per second
    clip_duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)
    # use np.arange() to make floating-point steps
    for i in np.arange(0, clip_duration, 1 / saving_fps):
        s.append(i)
    return s

def cutvideo(video_file):
    filename, _ = os.path.splitext(video_file)
    filename += "-opencv"
    # make a folder by the name of the video file
    if not os.path.isdir(filename):
        os.mkdir(filename)
    # read the video file
    cap = cv2.VideoCapture(video_file)
    # get the FPS of the video
    fps = cap.get(cv2.CAP_PROP_FPS)
    # if the SAVING_FRAMES_PER_SECOND is above video FPS, then set it to FPS (as maximum)
    saving_frames_per_second = min(fps, SAVING_FRAMES_PER_SECOND)
    # get the list of duration spots to save
    saving_frames_durations = get_saving_frames_durations(cap, saving_frames_per_second)
    # start the loop
    count = 0
    while True:
        is_read, frame = cap.read()
        if not is_read:
            # break out of the loop if there are no frames to read
            break
        # get the duration by dividing the frame count by the FPS
        frame_duration = count / fps
        try:
            # get the earliest duration to save
            closest_duration = saving_frames_durations[0]
        except IndexError:
            # the list is empty, all duration frames were saved
            break
        if frame_duration >= closest_duration:
            # if closest duration is less than or equals the frame duration,
            # then save the frame
            frame_duration_formatted = format_timedelta(timedelta(seconds=frame_duration))
            cv2.imwrite(os.path.join(filename, f"{count}.jpg"), frame)
            # drop the duration spot from the list, since this duration spot is already saved
            try:
                saving_frames_durations.pop(0)
            except IndexError:
                pass
        # increment the frame count
        count += 1

link = input("Insira a URL do vídeo do YT: ")
name = input("Dê um título ao vídeo: ")
fps = input("Quantos frames por segundo deseja capturar? (Ex.: 0.1): ")


SAVING_FRAMES_PER_SECOND = float(fps)
YouTube(link,on_progress_callback=on_progress).streams.first().download(filename=name)
print('Download Concluído.')
print(f'Capturando frames a uma taxa de {SAVING_FRAMES_PER_SECOND} fps.')
cutvideo(name)
os.mkdir(name + '-faces')
print('Classificando imagens')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

folder_dir = "C:\\Users\\paulo.baldacim\\Documents\\GitHub\\FascistFree2\\" + name + "-opencv\\"

for images in tqdm(os.listdir(folder_dir)):
    image = cv2.imread(folder_dir + images)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    faces = face_cascade.detectMultiScale(gray_image)


    if(len(faces)>=1):
        Path("C:\\Users\\paulo.baldacim\\Documents\\GitHub\\FascistFree2\\"+ name + "-opencv\\" + images).rename("C:\\Users\\paulo.baldacim\\Documents\\GitHub\\FascistFree2\\" + name + "-faces\\" + images)
        print(images)

