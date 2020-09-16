import os
import sys
import imageio
import math
import argparse

def convert_video_to_gif(input, output, fps, compress):
    reader = imageio.get_reader(input, mode='I')
    src_fps = reader.get_meta_data()['fps']
    writer = imageio.get_writer(output, fps=10, format='gif', mode='I')
    try:
        for i, frame in enumerate(reader, 1):
            if i % math.ceil(src_fps / fps) == 0:
                writer.append_data(frame)
    finally:
        reader.close()
        writer.close()

    if compress:
        try:
            from pygifsicle import optimize
            optimize(output, options=['--lossy=80', '--resize-colors=256', '--dither'])
        except ImportError:
            print('pygifsicle is not present, cannot compress gif.')
            exit(1)


class WriteHelpOnErrorParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)


if __name__ == "__main__":
    parser = WriteHelpOnErrorParser(description='Convert a video into a GIF file.')
    parser.add_argument('input',
                        help='Input file to convert to gif')
    parser.add_argument('output',
                        help='Path of the output file to write.  Defaults to the input file with extension .gif',
                        nargs='?')
    parser.add_argument('--fps', metavar='-f', type=int, default=10,
                        help='Number of frames per second (defaults to 10)')
    parser.add_argument('--compress', default=False, action='store_true',
                        help='Whether or not to apply gifsicle (store deltas instead of full images).  ' 
                             'Requires gifsicle to be installed and in the system path.')

    args = parser.parse_args()
    output = args.output or os.path.splitext(args.input)[0] + '.gif'
    convert_video_to_gif(args.input, output, args.fps, args.compress)
