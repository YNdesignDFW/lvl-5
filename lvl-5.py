import pickle, pprint
from cStringIO import StringIO

datPickle = pickle.load(open('C:/python27/pychallenge/lvl-5/banner.p','rb'))
pp = pprint.PrettyPrinter()
pp.pprint(datPickle)
print datPickle