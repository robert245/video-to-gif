from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('transform.py', base=base, targetName = 'video-to-gif')
]

setup(name='video-to-gif',
      version = '1.0',
      description = 'Convert a video into a GIF file',
      options = dict(build_exe = buildOptions),
      executables = executables)
