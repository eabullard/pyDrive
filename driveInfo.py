import commands
from prettytable import PrettyTable

class Drive:
   def __init__(self, blkID):
      self.vendor = "Unknown"
      self.model = "Unknown"
      self.size = 0
      self.spaceAvailable = 0
      self.isUSB = False
      self.blkID = blkID

   def setManufacturer(self, vendorName):
      self.vendor = manufacturerName
      return self.vendor

   def setModel(self, modelName):
      self.model = modelName
      return self.model

   def setSize(self, diskSize):
      self.size = diskSize
      return self.size

   def setSpaceAvailable(self, diskSpaceAvailable):
      self.spaceAvailable = diskSpaceAvailable
      return self.spaceAvailable

   def setIsUSB(self, usbStatus):
      self.isUSB = usbStatus
      return self.isUSB

   def setBlockID(self, driveBlockID):
      self.blkID = driveBlockID
      return self.blkID


if __name__ == "__main__":
   drives = []
   driveTable = PrettyTable(["Block ID", "Vendor", "Model"])
   driveTable.align="l"

   driveStrings = commands.getoutput('lsblk -o Name | grep "^s"')
   driveObjects = driveStrings.split()

   for i in driveObjects:
      i = Drive(i)
      drives.append(i)

   for i in drives:
      i.vendor = commands.getoutput('cat /sys/block/'+i.blkID+'/device/vendor').strip()
      i.model = commands.getoutput('cat /sys/block/'+i.blkID+'/device/model').strip()
      driveTable.add_row([i.blkID, i.vendor, i.model])

   print driveTable
