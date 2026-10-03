from kit import Canvas
import json
STEEL='jklm';SKIN='FGHI';BEARD='NOPQ';HAT='VWXY'
def eyes(C,y,xs):
  for x in xs:
    C.px(x-1,y,'Z');C.px(x,y,'a');C.px(x+1,y,'Z')
    for k in range(-1,2): C.px(x+k,y-2,'P')
def warrior():
  C=Canvas(40,40);C.th=(.35,-.25,-.7)
  C.poly([(1,40),(5,31),(13,28),(27,28),(35,31),(39,40)],STEEL)
  for x in range(4,37,4): C.px(x,35,'m');C.px(x,36,'l')
  C.poly([(14,27),(26,27),(25,31),(15,31)],'kkll')
  C.ell(20,21,7.6,8,SKIN)
  C.ell(12.6,20,1.4,2.2,SKIN);C.ell(27.4,20,1.4,2.2,SKIN)            # orejas
  C.poly([(13.5,25),(26.5,25),(25.5,29.5),(20,31),(14.5,29.5)],BEARD)             # barba corta abajo
  C.poly([(16,23.5),(24,23.5),(23,24.6),(17,24.6)],BEARD)            # bigote
  C.px(19,26,'I');C.px(20,26,'I');C.px(21,26,'I');C.px(19,27,'P');C.px(20,27,'P');C.px(21,27,'P')                    # boca
  eyes(C,18,(16,24))
  C.px(20,20,'G');C.px(21,20,'H');C.px(20,21,'H');C.px(19,21,'H')  # nariz
  C.ell(20,9,9.5,7,STEEL,1.1)
  C.poly([(10,10),(30,10),(30,13),(10,13)],'jkkl')
  for x in range(11,30,3): C.px(x,11,'j')
  C.poly([(19,13),(21,13),(21,19),(19,19)],'jjkl')
  C.px(20,2,'j')
  return C.rows()
def mage():
  C=Canvas(40,40);C.th=(.55,.05,-.5)
  C.poly([(1,40),(6,30),(14,27),(26,27),(34,30),(39,40)],HAT)
  for y in range(31,40): C.px(20,y,'s')
  C.ell(20,21,7,8,SKIN)
  C.ell(13.2,21,1.3,2,SKIN);C.ell(26.8,21,1.3,2,SKIN)
  C.poly([(13,24),(27,24),(26,33),(20,39),(14,33)],'bbcd')
  C.poly([(15,23.5),(25,23.5),(24,25.5),(16,25.5)],'bbcd')
  for y in range(28,37,3): C.px(18,y,'c');C.px(22,y+1,'c')
  C.px(19,27,'I');C.px(20,27,'I');C.px(21,27,'I')
  eyes(C,19,(16,23))
  for x in range(14,19): C.px(x,17,'b')
  for x in range(22,27): C.px(x,17,'b')
  C.px(20,20,'G');C.px(20,21,'G');C.px(21,21,'H');C.px(20,22,'H');C.px(19,22,'H')
  C.poly([(22,0),(31,14),(9,14)],HAT)
  C.poly([(5,13),(35,13),(33,16),(7,16)],HAT)
  for (x,y) in ((19,7),(24,10),(15,11),(22,4)): C.px(x,y,'s')
  return C.rows()
json.dump({'g':warrior(),'m':mage()},open('port.json','w'))
