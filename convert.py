#!/usr/bin/env python3

# Created by SD on 02/09/2021
# A tool to import PST archives into Thunderbird

import sys,os,shutil

def checkFolder(folder):
    a = 1
    if os.path.isdir(folder):				# Does out exist?
        while os.path.isdir(folder+str(a)):		# While out+a exists, do...
            a +=1					# increase a by 1
        else:
            return(folder+str(a))
    else:
        return(folder)

def convertPST(pst,mail):
    output		= checkFolder("out")								# Define the filename for the 'out' folder
    os.system("mkdir "+output)
    os.system("readpst -u "+pst+" -o "+output)
    new_dir		= os.listdir(output+"/")
    os.system("mv " + output + "/" + new_dir[0].replace(" ","\ ") + "/* " + output + "/")		# Move everything into the 'out' folder
    shutil.rmtree(output + "/" + new_dir[0], ignore_errors=True)					# Delete the old folder, everything has been moved into the 'out' folder.
    extracted		= os.listdir(output+"/")							# Get the filename of the newly created mailbox folder. This'll go into Thunderbird.
    os.rename(output+"/"+extracted[0],output+"/"+new_dir[0])						# Rename the extracted mailbox folder to match the filename. This'll help with readability when dealing with multiple archives.
    
    # Processing data to send to Thunderbird
    os.system("find " + output + " -type d | tac | grep -v '^" + output + "$' | xargs -d '\n' -I{} mv {} {}.sbd")
    os.system("find " + output + " -name mbox -type f | xargs -d '\n' -I{} echo '\"{}\" \"{}\"' | sed -e 's/\.sbd\/mbox\"$/\"/' | xargs -L 1 mv")
    print("Trying to remove any empty directories if they exist. Disregard any errors about 'rmdir', it just means you don’t have any empty directories to remove.")
    os.system("find " + output + " -empty -type d | xargs -d '\n' rmdir")
    os.system("find " + output + " -type d | egrep '*.sbd' | sed 's/.\{4\}$//' | xargs -d '\n' touch")
    os.system("cp -a " + output + "/* "+mail+"/Local\ Folders/")					# Copying the necessary data over to Thunderbird
    print("Done. You should now see a new mailbox in Thunderbird containing the PST file.")

if len(sys.argv)<3:
    print("Usage: python3 convert.py <path_to_pst> <path to Thunderbird mail folder, typically ~/.thunderbird/XXXXX/Mail/>")
else:
    filepath = sys.argv[1].replace(" ", "\ ")
    mailpath = sys.argv[2]
    print("PST filepath is " + filepath)
    print("Mail filepath is " + mailpath)
    convertPST(filepath,mailpath)

