import pandas
import os

class Load:
    """Base class to load tracking.txt files"""
    
    def __init__(self, path):
        """Constructor for Load class.

        :param path: Path to the tracking.txt file.
        :type path: str
        :raises Exception 
        """
        self.path = os.path.abspath(path)
        try: 
            self.tracking = pandas.read_csv(path, sep='\t')
        except Exception as e:
            raise e

    def getDataframe(self):
        """Get the tracking data in a DataFrame.

        :raises Exception: The selected file is empty
        :return: Tracking data
        :rtype: DataFrame
        """
        if self.tracking.empty:
            raise Exception("The selected file is empty")
        else:
            return self.tracking

    def getObjectNumber(self):
        """Get the total number of objects.

        :return: [Total number of objects]
        :rtype: [int]
        """
        maxObj = len(set(self.tracking.id.values))
        return maxObj

    def getObject(self, iD):
        """Get the data for the object with id.

        :param iD: Id of the object.
        :type index: int
        :return: Data for the object id.
        :rtype: DataFrame
        """
        objectData = self.tracking[self.tracking.id == iD]
        return objectData

    def getFrame(self, index):
        """Get the data for the image number index.

        :param index: Index of the image.
        :type index: int
        :return: Data for the image index.
        :rtype: DataFrame
        """
        objectData = self.tracking[self.tracking.imageNumber == index]
        return objectData

    def getObjectInFrame(self, iD, index):
        """Get the data for an object id is in a frame index.

        :param iD: [Id of the object.]
        :type iD: int
        :param index: Index of the image.
        :type index: int
        :return: True if object id in frame index.
        :rtype: bool
        """
        data = self.tracking[(self.tracking.imageNumber == index)&(self.tracking.id == iD)]
        return data

    def isObjectInFrame(self, iD, index):
        """Check if an object id is in a frame index.

        :param iD: Id of the object.
        :type index: int
        :param index: Index of the image.
        :type index: int
        :return: True if object id in frame index.
        :rtype: bool
        """
        data = self.tracking[(self.tracking.imageNumber == index)&(self.tracking.id == iD)]
        if data.empty:
            return False
        else:
            return True
