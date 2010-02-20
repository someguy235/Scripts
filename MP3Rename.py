#Move and rename mp3's from one organizational structure to another

import os
import shutil
#from ID3 import *

#ID3Track = ''
#ID3Album = ''

def renameTracks(cdNum, numOfCDs, comboAlbum):
        dirNotEmpty = 0
        for songName in (os.listdir(os.getcwd())):
                try:
                        if (songName.find('.mp3') != -1):
                                newName = ''
                                splitline = songName.split(' - ')
                                lineLoc = 0
                                while ((splitline[lineLoc] < '0') | (splitline[lineLoc] > '50')):
                                        newName = newName + splitline[lineLoc] + ' - '
                                        lineLoc = lineLoc + 1
                                newName = comboAlbum + ' - '
                                newName = newName + (cdNum + splitline[lineLoc])
                                lineLoc = lineLoc + 1
                                while (lineLoc < len(splitline)):
                                        newName = newName + ' - ' + splitline[lineLoc]
                                        lineLoc = lineLoc + 1
                                print newName
                        else:
                                newName = songName
                        if (newName.lower() != 'thumbs.db'):
                                try:
                                        os.rename(songName, newName)
                                        shutil.move(newName, ('..\\' + str(comboAlbum) + '\\' + newName))
                                except Exception, e:
                                        print newName
                                        #print (e)
                                        dirNotEmpty = 1
                except Exception, e:
                        print (str(e))
        return dirNotEmpty

for bandName in (os.listdir(os.getcwd())):
        if (os.path.isdir(bandName)):
                os.chdir(bandName) #down to list of albums
                albumDict = {}
                for albumName in (os.listdir(os.getcwd())):
                        if ((os.path.isdir(albumName)) & (albumName.find('(CD ') != -1)):
                                albumRoot = albumName[:(albumName.find('(CD ') - 1)]
                                if (albumName.find('(CD 1)') != -1):
                                        albumDict[albumRoot] = [[albumName], 1]
                                else:
                                        for key in albumDict.keys():
                                                if (key == albumRoot):
                                                        albumDict[albumRoot][1] = (albumDict[albumRoot][1]+1)
                                                        albumDict[albumRoot][0].append(albumName)
                for key in albumDict.keys():
                        #print albumDict[key]
                        if (albumDict[key][1] > 1):
                                comboAlbum = (key + ' (' + str(albumDict[key][1]) + 'x)')
                                os.mkdir(comboAlbum)
                                #print comboAlbum
                                discNo = 1
                                while (discNo <= albumDict[key][1]):
                                        workingDir = albumDict[key][0][(discNo-1)]
                                        os.chdir(workingDir)
                                        dirState = renameTracks(str(discNo), str(albumDict[key][1]), comboAlbum)
                                        #ID3TagTracks()
                                        os.chdir('..')
                                        if (dirState == 0):
                                                shutil.rmtree(workingDir)
                                        discNo = discNo + 1
                os.chdir('..') #up to list of bands
raw_input("done")

#def ID3TagTracks():
#        for songName in (os.listdir(os.getcwd())):
#                if (songName.find('.mp3') != -1):
#                        try:
#                                ID3Tag = ID3(str(songName))
#                                #does this work?
#                                print ID3Tag['ALBUM']
#                                ID3Tag['ALBUM'] = ID3Album
#                                print ID3Tag['ALBUM']
#                                ID3Tag['TRACKNUMBER'] = ID3Track
#                                #????
#                        except InvalidTagError, message:
#                                print "Invalid ID3 tag:", message
