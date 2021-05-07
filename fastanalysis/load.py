import pandas
import os

class Load:
    """Base class to load tracking.txt files"""
    
    def __init__(self, path):
        """Constructor for the Load tracking object.

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
        """Get the tracking data in a pandas DataFrame format.

        :raises Exception: The selected file is empty
        :return: Tracking data
        :rtype: DataFrame
        """
        if self.tracking.empty:
            raise Exception("The selected file is empty")
        else:
            return self.tracking

    def getKeys(self):
        """Get the list of keys of the tracking data.

        :return: Keys
        :rtype: List
        """
        return self.tracking.keys().tolist()

    def getDataKeys(self, keys):
        """Get the tracking data in a pandas DataFrame format.

        :raises Exception: The selected file is empty
        :return: Tracking data
        :rtype: DataFrame
        """
        if isinstance(keys, list):
            data = self.tracking[keys]
        else:
            data = self.tracking[[keys]]
        return data

    def getObjectNumber(self):
        """Get the total number of objects in the tracking file.

        :return: [Total number of objects]
        :rtype: [int]
        """
        maxObj = len(set(self.tracking.id.values))
        return maxObj

    def getObjects(self, ids):
        """Get the tracking data for a list of objects.

        :param iD: Id or list of ids of objects.
        :type index: list | int
        :return: Data for the objects with ids.
        :rtype: DataFrame
        """
        if isinstance(ids, list):
            objectData = self.tracking[self.tracking.id.isin(ids)]
        else:
            objectData = self.tracking[self.tracking.id == ids]
        return objectData

    def getFrames(self, indexes):
        """Get the tracking data for a list of images.

        :param indexes: Indexes of the images.
        :type indexes: list | int
        :return: Data for the images with indexes.
        :rtype: DataFrame
        """
        if isinstance(indexes, list):
            objectData = self.tracking[self.tracking.imageNumber.isin(indexes)]
        else:
            objectData = self.tracking[self.tracking.imageNumber == indexes]
        return objectData

    def getObjectsInFrames(self, ids, indexes):
        """Get the tracking data for a list of objects in a list of frames.

        :param ids: Ids of objects.
        :type ids: list | int
        :param index: Indexex of images.
        :type index: list | int
        :return: Data for objects ids in frames indexes.
        :rtype: Dataframe
        """
        if not isinstance(indexes, list):
            indexes = [indexes]
        if not isinstance(ids, list):
            ids = [ids]
        data = self.tracking[(self.tracking.imageNumber.isin(indexes))&(self.tracking.id.isin(ids))]
        return data

    def isObjectsInFrame(self, ids, index):
        """Check if a list of object is in a frame.

        :param ids: Ids of objects.
        :type ids: list | int
        :param index: Index of the image.
        :type index: int
        :return: True if object id in frame index.
        :rtype: bool
        """
        isIn = []
        if isinstance(ids, list):
            for iD in ids:
                data = self.tracking[(self.tracking.imageNumber == index)&(self.tracking.id == iD)]
                if data.empty:
                    isIn.append(False)
                else:
                    isIn.append(True)
            return isIn
        else:
            data = self.tracking[(self.tracking.imageNumber == index)&(self.tracking.id == ids)]
            if data.empty:
                return False
            else:
                return True

    def export(self, path, delimiter='\t', keys=None, ids=None, indexes=None, fmt="csv"):
        """Export the tracking data.

        :param path: Path to the saved file.
        :type path: str
        :param keys: List of features.
        :type keys: list
        :param ids: List of ids of object.
        :type ids: list
        :param indexes: List of indexes of images.
        :type indexes: list
        """
        tracking = self.tracking
        if indexes:
            tracking = tracking[tracking.imageNumber.isin(indexes)]

        if ids:
            tracking = tracking[tracking.id.isin(ids)]

        if keys:
            tracking = tracking[keys]

        if fmt == "csv":
            tracking.to_csv(path, sep=delimiter, index=False)
        elif fmt == "excel":
            tracking.to_excel(path, index=False)
