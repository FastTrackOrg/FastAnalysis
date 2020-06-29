import pandas
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Plot:
    """Base class for plotting"""

    def __init__(self, loadObject):
        """Constructor for the plot object.

        :param loadObject: A Load object containing the data.
        :type index: Load
        """
        self.data = loadObject.getDataframe()

    def velocityDistribution(self, ids, indexes=None, key="Body", pooled=True, subplots=False):
        """Plot the velocity distribution.

        :param ids: Ids of objects.
        :type ids: list
        :param indexes: Sub part of data based on indexes [min:max[ to select. Default: all the indexes.
        :type ids: list
        :param key: Head, Body or Tail. default: Body
        :type key: str
        :param pooled: Concatenate the objects distributions.
        :type pooled: bool
        :param subplots: Plot the distribution on separate subplots.
        :type pooled: bool
        :return: Matplotlib axe and raw data.
        :rtype: (ax, list)
        """
        if not indexes:
            indexes = (0, len(self.data.imageNumber.values))
        if pooled:
            subplots = False
            tmpData = self.data[(self.data.id == ids[0])&(self.data.imageNumber.isin(range(indexes[0], indexes[1])))]
            pooledData = (np.sqrt(np.diff(tmpData["x"+key].values)**2 + np.diff(tmpData["y"+key].values)**2)) / np.diff(tmpData.imageNumber.values)
            for i in ids[1::]:
                tmpData = self.data[(self.data.id == i)&(self.data.imageNumber.isin(range(indexes[0], indexes[1])))]
                pooledData = np.concatenate((pooledData, (np.sqrt(np.diff(tmpData["x"+key].values)**2 + np.diff(tmpData["y"+key].values)**2)) / np.diff(tmpData.imageNumber.values)))
            outputData = [pooledData]
        else:
            data = []
            for i in ids:
                tmpData = self.data[(self.data.id == i)&(self.data.imageNumber.isin(range(indexes[0], indexes[1])))]
                data.append((np.sqrt(np.diff(tmpData["x"+key].values)**2 + np.diff(tmpData["y"+key].values)**2)) / np.diff(tmpData.imageNumber.values))
            outputData = data

        if subplots:
            fig, axs = plt.subplots(len(ids), 1, sharey=True)
            for i, j in enumerate(outputData):
                sns.distplot(j, ax=axs[i], label=ids[i])
                axs[i].legend()
            axs[-1].set_xlabel("Velocity")
        else:
            fig, axs = plt.subplots()
            for i, j in enumerate(outputData):
                sns.distplot(j, ax=axs, label=ids[i])
            axs.legend()
            axs.set_xlabel("Velocity")

        return (axs, outputData)
