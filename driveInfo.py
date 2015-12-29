import commands
from prettytable import PrettyTable

class Drive:
   def __init__(self, blkID):
      self.vendor = commands.getoutput('cat /sys/block/' + blkID + '/device/vendor').strip()
      self.model = commands.getoutput('cat /sys/block/' + blkID + '/device/model').strip()
      self.size = commands.getoutput('cat /proc/partitions | grep ' + blkID + '$ | awk \'{print $3}\'')
      self.spaceAvailable = 0
      self.isUSB = False
      self.blkID = blkID

   def setVendor(self):
      self.vendor = commands.getoutput('cat /sys/block/' + self.blkID + '/device/vendor').strip()

   def setModel(self):
      self.model = commands.getoutput('cat /sys/block/' + self.blkID + '/device/model').strip()

   def setSize(self):
      self.size = commands.getoutput('cat /proc/partitions | grep ' + self.blkID + '$ | awk \'{print $3}\'')
      
   def setSpaceAvailable(self, diskSpaceAvailable):
      self.spaceAvailable = diskSpaceAvailable
      
   def setIsUSB(self, usbStatus):
      self.isUSB = usbStatus

if __name__ == "__main__":
   drives = []
   driveTable = PrettyTable(["Block ID", "Vendor", "Model", "Size in Bytes"])
   driveTable.align="l"

   driveStringsSATA = commands.getoutput('lsblk -o Name | grep "^s"')
   driveObjectsSATA = driveStringsSATA.split()

   driveStringsIDE = commands.getoutput('lsblk -o Name | grep "^h"')
   driveObjectsIDE = driveStringsIDE.split()
   
   for i in driveObjectsSATA:
      i = Drive(i)
      drives.append(i)

   for i in driveObjectsIDE:
      i = Drive(i)
      drives.append(i)

   for i in drives:
      driveTable.add_row([i.blkID, i.vendor, i.model, i.size])

   print driveTable
