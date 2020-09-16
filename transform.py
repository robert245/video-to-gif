import sys
import imageio
import math


def convert_video_to_gif(input, output, options=None):
    if options is None:
        options = {}

    reader = imageio.get_reader(input, mode='i')
    fps = reader.get_meta_data()['fps']
    writer = imageio.get_writer(output, fps=10, format='gif')
    for i, frame in enumerate(reader):
        if i % math.ceil(fps / 10) != 0:
            writer.append_data(frame)

    writer.close()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Video to GIF - by RWave")
        print("USAGE: %0s path/to/target/video path/to/output" % sys.argv[0])
        sys.exit(1)

    convert_video_to_gif(sys.argv[1], sys.argv[2])
