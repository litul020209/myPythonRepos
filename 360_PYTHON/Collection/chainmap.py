from collections import ChainMap
d1={1:10,2:20,3:30}
d2={1:2,2:3,3:4}

d=dict(ChainMap(d1,d2))