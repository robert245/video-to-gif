# Video-to-gif
A simple script to transform videos files to .gif files (with optional compression).

## Preresiquites
You will need to install the following
* imageio / imageio-ffmpeg
* Optional: pygifsicle/gifsicle for compression 

You can get all the python dependencies by running
`pip install imageio imageio-ffmpeg pygifsicle`

Gifsicle can be installed on mac/linux via package manager.  For Windows, download gifsicle via https://eternallybored.org/misc/gifsicle/ and add it to the path.

### Creating a standalone exe file
Ensure you have cx_freeze installed, as well as all of the above listed dependencies
```shell script
pip install cx_freeze
```

and run 
```shell-script
python setup.py build
```

The packaged application will be present within `/build`, and can then be added to the system path,
allowing the program can be called directly - e.g.
```shell script
video-to-gif /path/to/input
```

## Usage
To convert a video to a gif, run the program via python
```shell script
python transform.py /path/to/input (/path/to/output) 
```
* Output path is optional, and defaults to the input file with an extension of .gif  
* --compress can be specified to compress the output (requires gifsicle, as above).  
* --fps can also be specified (defaults to 10)

The application uses imageio with ffmpeg and can convert most common (and some uncommon) video formats. 