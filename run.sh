#!/bin/bash
pyfileDir="`dirname "$0"`/py_files"
echo $pyfileDir
$pyfileDir/launchpad_broadc.py & $pyfileDir/play_music.py && fg
