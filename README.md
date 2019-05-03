# ICARIS
cd [filepath] - navigating from the current folder downward
Use quotation marks for folders with more than one word
eg
Documents/"Senior Design"/repo/ICARIS
Want (master) to appear
cd.. - up a folder
ls - list all files in current folder

git pull - update your repo
One of these:
git add [files] - any files changed
git add [folder]/* - add a whole folder

git commit -m "[message]" - commit changes, must have a message, even if it's just "message"

git push origin master - push changes to repo. Always push after committing to avoid merge errors

If you get a merge error - SHUT IT DOWN. Restart, push, then pull.

Git-lfs

git lfs install - set up git-lfs to upload large files. Not needed for pulling them

git lfs track "*.[filetype]* - manage all large files of this type, can then add them as normal

Extra commands:

git status - status of repo, good for if you've added files

git log - log of changes - will require exit

exit command - Q control M or Q control

Commit merge error:

    press "i"
    go to the bottom, add a couple empty lines
    write your merge message
    press "esc"
    write ":wq"
    then press enter

git rm - remove file from repo, only in emergencies

git stash - if you commit a file at the same time as someone else, run this to go back to a clean directory. Add your file back in pulling their commit
