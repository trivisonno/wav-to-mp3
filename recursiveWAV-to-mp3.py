#!/usr/bin/env python
import subprocess
import fnmatch
import os

sourceFolder = os.path.dirname(os.path.realpath(__file__))
#print sourceFolder

matches = []
for root, dirnames, filenames in os.walk(sourceFolder):
  for filename in fnmatch.filter(filenames, '*.WAV'):
    matches.append(root.replace(sourceFolder,''))

folders = set(matches)
#print(folders)

for folder in folders:
    #print sourceFolder+folder+'.wav'
    cwd = os.path.realpath(sourceFolder+'/'+folder)
    os.chdir(cwd)
    print os.path.realpath(os.curdir)
    print "Joining WAV files"
    print sourceFolder+folder+'.wav'
    subprocess.call(['sox', '*.WAV', sourceFolder+folder+'.wav'])
    print "Join complete!"

    print "Converting WAV file to mp3"
    #print sourceFolder+folder+'.mp3'
    subprocess.call(['sox', sourceFolder+folder+'.wav', sourceFolder+folder+'.mp3', 'rate', '24000', 'channels', '1'])
    print "Conversion complete!\n"
