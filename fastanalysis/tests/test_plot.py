import pytest
import pandas
import numpy as np

import load
import plot


def test_velocity_dist_default_key():
    """Test velocity distribution."""
    tracking = load.Load("tests/tracking.txt")
    plotObj = plot.Plot(tracking)
    velocityTest = plotObj.velocityDistribution(ids=[0, 1])
    refData = tracking.getObjects(0)
    a = (np.sqrt(np.diff(refData.xBody.values)**2 + np.diff(refData.yBody.values)**2)) / np.diff(refData.imageNumber.values)
    refData = tracking.getObjects(1)
    b = (np.sqrt(np.diff(refData.xBody.values)**2 + np.diff(refData.yBody.values)**2)) / np.diff(refData.imageNumber.values)
    pooled = np.concatenate((a, b))
    np.testing.assert_array_equal(pooled, velocityTest[1][0])

    velocityTest = plotObj.velocityDistribution(ids=[0, 1], pooled=False)
    np.testing.assert_array_equal(a, velocityTest[1][0])
    np.testing.assert_array_equal(b, velocityTest[1][1])

    refData = tracking.getObjectsInFrames(0, indexes=list(range(0, 100)))
    a = (np.sqrt(np.diff(refData.xBody.values)**2 + np.diff(refData.yBody.values)**2)) / np.diff(refData.imageNumber.values)
    velocityTest = plotObj.velocityDistribution(ids=[0], pooled=True, indexes=(0, 100))
    np.testing.assert_array_equal(a, velocityTest[1][0])

def test_velocity_dist_head():
    """Test velocity distribution."""
    tracking = load.Load("tests/tracking.txt")
    plotObj = plot.Plot(tracking)
    velocityTest = plotObj.velocityDistribution(ids=[0, 1], key="Head")
    refData = tracking.getObjects(0)
    a = (np.sqrt(np.diff(refData.xHead.values)**2 + np.diff(refData.yHead.values)**2)) / np.diff(refData.imageNumber.values)
    refData = tracking.getObjects(1)
    b = (np.sqrt(np.diff(refData.xHead.values)**2 + np.diff(refData.yHead.values)**2)) / np.diff(refData.imageNumber.values)
    pooled = np.concatenate((a, b))
    np.testing.assert_array_equal(pooled, velocityTest[1][0])

    velocityTest = plotObj.velocityDistribution(ids=[0, 1], pooled=False, key="Head")
    np.testing.assert_array_equal(a, velocityTest[1][0])
    np.testing.assert_array_equal(b, velocityTest[1][1])

    refData = tracking.getObjectsInFrames(0, indexes=list(range(0, 100)))
    a = (np.sqrt(np.diff(refData.xHead.values)**2 + np.diff(refData.yHead.values)**2)) / np.diff(refData.imageNumber.values)
    velocityTest = plotObj.velocityDistribution(ids=[0], pooled=True, indexes=(0, 100), key="Head")
    np.testing.assert_array_equal(a, velocityTest[1][0])
