import pytest
import pandas

import load

def test_load_file():
    """Test that file is loaded as a dataframe."""
    tracking = load.Load("tests/tracking.txt").getDataframe()
    reference = pandas.read_csv("tests/tracking.txt", sep='\t')
    pandas.testing.assert_frame_equal(tracking, reference)

def test_load_file_error():
    """Test that wrong path lead to Exception."""
    with pytest.raises(Exception):
        tracking = load.Load("tests/tracing.txt").getDataframe()
        assert tracking

def test_object_number():
    """Test number of objects."""
    objectNumber = load.Load("tests/tracking.txt").getObjectNumber()
    assert objectNumber == 207
    
def test_get_object():
    """Test get the data for an object"""
    reference = pandas.read_csv("tests/tracking.txt", sep='\t')
    tracking = load.Load("tests/tracking.txt").getObject(0)
    pandas.testing.assert_frame_equal(tracking, reference[reference.id==0])
    tracking = load.Load("tests/tracking.txt").getObject(1)
    pandas.testing.assert_frame_equal(tracking, reference[reference.id==1])
    
def test_get_frame():
    """Test get the data for a frame"""
    reference = pandas.read_csv("tests/tracking.txt", sep='\t')
    tracking = load.Load("tests/tracking.txt").getFrame(10)
    pandas.testing.assert_frame_equal(tracking, reference[reference.imageNumber==10])
    tracking = load.Load("tests/tracking.txt").getFrame(1)
    pandas.testing.assert_frame_equal(tracking, reference[reference.imageNumber==1])

def test_get_object_in_frame():
    """Test get the data for an frame"""
    reference = pandas.read_csv("tests/tracking.txt", sep='\t')
    tracking = load.Load("tests/tracking.txt").getObjectInFrame(0, 200)
    pandas.testing.assert_frame_equal(tracking, reference[(reference.imageNumber==200)&(reference.id==0)])
    tracking = load.Load("tests/tracking.txt").getObjectInFrame(1, 100)
    pandas.testing.assert_frame_equal(tracking, reference[(reference.imageNumber==100)&(reference.id==1)])

def test_is_object_in_frame():
    """Test get the data for an frame"""
    reference = pandas.read_csv("tests/tracking.txt", sep='\t')
    tracking = load.Load("tests/tracking.txt").isObjectInFrame(0, 0)
    assert tracking
    tracking = load.Load("tests/tracking.txt").isObjectInFrame(0, 1500)
    assert not tracking

