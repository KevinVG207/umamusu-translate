import os
import UnityPy
import common
from common import GAME_ASSET_ROOT, TranslationFile

file = "c:\\Users\\kevin\\AppData\\LocalLow\\Cygames\\umamusume\\dat\\CH\\CHKFEUAOFQWXFHJCMSWMHBQY3W4NSQ3A"

env = UnityPy.load(file)
mainFile = next(iter(env.container.values())).get_obj()
assetList = mainFile.assets_file.files
textasset = assetList[-110588895963452470].read_typetree()
asset1 = assetList[-110588895963452470].read_typetree()
# asset2 = assetList[-2692799123397480503].read_typetree()
# asset3 = assetList[-7869419158137661574].read_typetree()
# asset4 = assetList[-2169800901024725473].read_typetree()
mainTree = mainFile.read_typetree()
pass