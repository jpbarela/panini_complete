from Accumulator import Accumulator
import math
from nose import with_setup
from nose.tools import assert_almost_equal


def setupFunction():
    global test_accumulator
    test_accumulator = Accumulator.Accumulator()
    for i in [3, 5, 6, 8]:
        test_accumulator.add_value(i)

@with_setup(setupFunction)
def test_average():
    assert_almost_equal(test_accumulator.average(), 5.5, msg="Average is {0}".format(test_accumulator.average()))

@with_setup(setupFunction)
def test_variance():
    assert_almost_equal(test_accumulator.variance(), 3.25, msg="Variance is {0}".format(test_accumulator.variance()))

@with_setup(setupFunction)
def test_standard_deviation():
    assert_almost_equal(test_accumulator.standard_deviation(),
                        math.sqrt(3.25),
                        msg="Standard deviation is {0}".format(test_accumulator.standard_deviation()))