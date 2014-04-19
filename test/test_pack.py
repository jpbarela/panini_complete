from nose import with_setup
from Panini import Pack
import Panini

def setupFunction():
    global pack
    global size
    size = Panini.STICKERS_PER_PACK
    pack = Pack.generate_pack(size, Panini.NUMBER_OF_STICKERS)

@with_setup(setupFunction)
def test_pack_contains_size_stickers():
    assert len(pack) == size, "Pack contains did not contain 7 stickers. Contains {0} stickers".format(len(pack))

@with_setup(setupFunction)
def test_pack_does_not_contain_duplicates():
    assert len(pack) == len(set(pack)), "Pack contained duplicates. Pack {0}".format(pack)

@with_setup(setupFunction)
def test_pack_contents_are_sorted():
    assert sorted(pack), "Pack is not sorted. Pack {0}".format(pack)

def sorted(testList):
    return all(testList[i] < testList[i+1] for i in range(len(testList)-1))
