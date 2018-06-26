import os

from jbeijing import jbeijing

os.environ['PATH'] += os.pathsep + os.path.abspath('./')
e = jbeijing.create_engine()
e.setUserDic((
    u"jbeijing/VnrDictionaries/@jichi/JcUserdic/Jcuser",
    u"jbeijing/VnrDictionaries/@djz020815/JcUserdic/Jcuser",
    u"jbeijing/VnrDictionaries/@najizhimo/JcUserdic/Jcuser",
))

print(e.translate('テスト'))
