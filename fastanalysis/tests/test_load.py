import pytest
import pandas

import load


def test_load_file():
    """Test that file is loaded as a dataframe."""
    tracking = load.Load("tests/tracking.txt").getDataframe()
    reference = pandas.read_csv("tests/tracking.txt", sep='\t')
    pandas.testing.assert_frame_equal(tracking, reference)

def test_load_database():
    """Test that file is loaded as a dataframe."""
    tracking = load.Load("tests/tracking.db").getDataframe()
    reference = pandas.read_csv("tests/tracking.txt", sep='\t')
    pandas.testing.assert_frame_equal(tracking, reference)

def test_load_file_error():
    """Test that wrong path lead to Exception."""
    with pytest.raises(Exception):
        tracking = load.Load("tests/tracing.txt").getDataframe()
        assert tracking


def test_object_number():
    """Test number of objects."""
    reference = pandas.read_csv("tests/tracking.txt", sep='\t')
    objectNumber = load.Load("tests/tracking.txt").getObjectNumber()
    assert objectNumber == reference.id.max() + 1


def test_object_ids():
    """Test number of objects."""
    reference = pandas.read_csv("tests/tracking.txt", sep='\t')
    objectNumber = load.Load("tests/tracking.txt").getIds()
    assert objectNumber == list(set(reference.id))


def test_get_keys():
    """Test get list of keys."""
    keys = load.Load("tests/tracking.txt").getKeys()
    assert keys == [
        "xHead",
        "yHead",
        "tHead",
        "xTail",
        "yTail",
        "tTail",
        "xBody",
        "yBody",
        "tBody",
        "curvature",
        "areaBody",
        "perimeterBody",
        "headMajorAxisLength",
        "headMinorAxisLength",
        "headExcentricity",
        "tailMajorAxisLength",
        "tailMinorAxisLength",
        "tailExcentricity",
        "bodyMajorAxisLength",
        "bodyMinorAxisLength",
        "bodyExcentricity",
        "imageNumber",
        "id"]


def test_data_keys():
    """Test get data from list of keys."""
    reference = pandas.read_csv("tests/tracking.txt", sep='\t')
    pandas.testing.assert_frame_equal(load.Load(
        "tests/tracking.txt").getDataKeys(["yHead", "tHead"]), reference[["yHead", "tHead"]])
    pandas.testing.assert_frame_equal(
        load.Load("tests/tracking.txt").getDataKeys("yHead"), reference[["yHead"]])


def test_get_objects():
    """Test get the data for an object"""
    reference = pandas.read_csv("tests/tracking.txt", sep='\t')
    tracking = load.Load("tests/tracking.txt").getObjects(0)
    pandas.testing.assert_frame_equal(tracking, reference[reference.id == 0])
    tracking = load.Load("tests/tracking.txt").getObjects([0, 1])
    pandas.testing.assert_frame_equal(
        tracking, reference[(reference.id == 1) | (reference.id == 0)])


def test_get_frames():
    """Test get the data for a frame"""
    reference = pandas.read_csv("tests/tracking.txt", sep='\t')
    tracking = load.Load("tests/tracking.txt").getFrames(10)
    pandas.testing.assert_frame_equal(
        tracking, reference[reference.imageNumber == 10])
    tracking = load.Load("tests/tracking.txt").getFrames([1, 10])
    pandas.testing.assert_frame_equal(tracking, reference[(
        reference.imageNumber == 1) | (reference.imageNumber == 10)])


def test_get_objects_in_frames():
    """Test get the data for an frame"""
    reference = pandas.read_csv("tests/tracking.txt", sep='\t')
    tracking = load.Load("tests/tracking.txt").getObjectsInFrames(0, 200)
    pandas.testing.assert_frame_equal(tracking, reference[(
        reference.imageNumber == 200) & (reference.id == 0)])
    tracking = load.Load(
        "tests/tracking.txt").getObjectsInFrames([1, 2], [0, 100])
    pandas.testing.assert_frame_equal(tracking, reference[((reference.imageNumber == 100) | (
        reference.imageNumber == 0)) & ((reference.id == 1) | (reference.id == 2))])


def test_is_objects_in_frame():
    """Test check if objects in frame"""
    reference = pandas.read_csv("tests/tracking.txt", sep='\t')
    tracking = load.Load("tests/tracking.txt").isObjectsInFrame(0, 0)
    assert tracking
    tracking = load.Load("tests/tracking.txt").isObjectsInFrame(0, 1500)
    assert not tracking


def test_export_csv():
    """Test set the data in a file"""
    reference = pandas.read_csv("tests/tracking.txt", sep='\t')
    tracking = load.Load("tests/tracking.txt")

    tracking.export("tests/test.csv")
    test = pandas.read_csv("tests/test.csv", sep='\t')
    pandas.testing.assert_frame_equal(reference, test)

    tracking.export("tests/test.csv", delimiter=',')
    test = pandas.read_csv("tests/test.csv", sep=',')
    pandas.testing.assert_frame_equal(reference, test)

    tracking.export("tests/test.csv", keys=["imageNumber"])
    test = pandas.read_csv("tests/test.csv", sep='\t')
    pandas.testing.assert_frame_equal(reference[["imageNumber"]], test)

    tracking.export("tests/test.csv", indexes=[1])
    test = pandas.read_csv("tests/test.csv", sep='\t')
    pandas.testing.assert_frame_equal(
        reference[reference.imageNumber == 1].reset_index(drop=True), test)

    tracking.export("tests/test.csv", ids=[0])
    test = pandas.read_csv("tests/test.csv", sep='\t')
    pandas.testing.assert_frame_equal(
        reference[reference.id == 0].reset_index(drop=True), test)

    tracking.export("tests/test.csv", ids=[0], indexes=[0])
    test = pandas.read_csv("tests/test.csv", sep='\t')
    pandas.testing.assert_frame_equal(reference[(reference.id == 0) & (
        reference.imageNumber == 0)].reset_index(drop=True), test)


def test_export_excel():
    """Test set the data in an excel file"""
    reference = pandas.read_csv("tests/tracking.txt", sep='\t')
    tracking = load.Load("tests/tracking.txt")

    tracking.export("tests/test.xlsx", fmt="excel")
    test = pandas.read_excel("tests/test.xlsx")
    pandas.testing.assert_frame_equal(reference, test)

    tracking.export("tests/test.xlsx", keys=["imageNumber"], fmt="excel")
    test = pandas.read_excel("tests/test.xlsx")
    pandas.testing.assert_frame_equal(reference[["imageNumber"]], test)

    tracking.export("tests/test.xlsx", indexes=[1], fmt="excel")
    test = pandas.read_excel("tests/test.xlsx")
    pandas.testing.assert_frame_equal(
        reference[reference.imageNumber == 1].reset_index(drop=True), test)

    tracking.export("tests/test.xlsx", ids=[0], fmt="excel")
    test = pandas.read_excel("tests/test.xlsx")
    pandas.testing.assert_frame_equal(
        reference[reference.id == 0].reset_index(drop=True), test)

    tracking.export("tests/test.xlsx", ids=[0], indexes=[0], fmt="excel")
    test = pandas.read_excel("tests/test.xlsx")
    pandas.testing.assert_frame_equal(reference[(reference.id == 0) & (
        reference.imageNumber == 0)].reset_index(drop=True), test)
