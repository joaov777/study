from tqdm import tqdm
from time import sleep
import pytube

with tqdm(total=video.streams.get_highest_resolution().filesize) as pbar:
    for i in range(100):
        sleep(0.1)
        pbar.update(1)