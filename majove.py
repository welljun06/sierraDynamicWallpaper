import datetime
import subprocess


cmd = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

ISOTIMEFORMAT = '%H'
theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
print theTime

if int(theTime) < 8 and int(theTime) >= 6:
    index = 0
elif int(theTime) >=0 and int(theTime) < 6:
    index = 16
else:
    index = int(theTime) - 7

localpath = "/Users/welljun06/Pictures/mojave_dynamic/mojave_dynamic_{0}.jpeg".format(index)
print localpath
try:
    subprocess.Popen(cmd%localpath, shell=True)
#    subprocess.call(["killall Dock"], shell=True)
except KeyboardInterrupt:
    print "The Computer says NO!"
