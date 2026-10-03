import sys,os,json,math,random
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from kit import Canvas
def ch(C,pts,w,T):
  for a,b in zip(pts,pts[1:]): C.cap(a,b,w,T)
def dirt(C,keys,p=.06,seed=3):
  r=random.Random(seed)
  for y in range(len(C.c)):
    for x in range(len(C.c[0])):
      v=C.c[y][x]
      for T in keys:
        i=T.find(v)
        if 0<=i<3 and r.random()<p: C.c[y][x]=T[i+1]
def eye(C,x,y,big=False,col=('u','v')):
  C.px(x,y,col[0]);C.px(x+1,y,col[1])
  if big: C.px(x,y+1,col[1]);C.px(x+1,y+1,col[1])
def save(name,C,pal):
  json.dump({'rows':C.rows(),'pal':pal},open(os.path.join(os.path.dirname(os.path.abspath(__file__)),name+'.json'),'w'))
