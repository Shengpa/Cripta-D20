from kit import Canvas
import math,json,random
random.seed(7)
B='bcde';C=Canvas(70,96,14);C.th=(.6,.1,-.45)
def ch(pts,w,T=B):
  for a,b in zip(pts,pts[1:]): C.cap(a,b,w,T)
# pierna de atrás (derecha en pantalla)
ch([(44,62),(49,75)],5);C.ell(49,76,3,2.6,B);ch([(49,77),(47,90)],4.2);C.cap((51,78),(50,89),2,B)
ch([(47,92),(52,93.5)],3.4);C.ell(47,91.5,2.6,2,B)
# brazo del escudo (atrás)
ch([(52,31),(57,41)],4);C.ell(57,42,2.4,2.4,B);ch([(57,43),(53,50)],3)
# pelvis
C.ell(32,60,5.5,4,B);C.ell(44,60,5.5,4,B);C.ell(38,59.5,2.6,3.6,B)
for (x,y) in ((31,60),(32,60),(44,60),(45,60)): C.px(x,y,'y')
# columna encorvada
for i,y in enumerate(range(45,58,2)): C.ell(38.5+math.sin(i*.4)*.6,y+1,2.4 if i%2 else 2,1.15,B)
# caja torácica
C.ell(38,39,13,10,'yyyy')
for i in range(5):
  y=31.5+i*3;sp=12-i*.9
  ch([(36.5,y),(31.5,y+.5),(38-sp,y+3),(38-sp+1.2,y+6)],2.4)
  ch([(39.5,y),(44.5,y+.5),(38+sp,y+3),(38+sp-1.2,y+6)],2.4)
C.cap((38,29),(38,43),3.4,B)
# pierna de adelante (izquierda en pantalla), flexionada
ch([(32,62),(25,74)],5.6);C.ell(25,75,3.4,3,B);ch([(25,76),(27,91)],4.6);C.cap((22.6,77),(24,90),2.2,B)
ch([(27,93),(20,94.5),(16,94.5)],3.6);C.ell(27,92.5,2.8,2.2,B)
# hombros altos y clavículas
C.cap((37,29.5),(24,28),3,B);C.cap((39,29.5),(52,28.5),3,B);C.ell(52,30,3.4,3.2,B)
# brazo de la espada: codo afuera, mano arriba al lado de la cabeza
ch([(24,29),(15,34)],4.2);C.ell(15,34.5,2.6,2.6,B);ch([(15,34),(16,23)],3.4)
# espada casi vertical, inclinada hacia adentro (no sale del ancho del cuerpo)
for i in range(30):
  y=19-i;x=15.5+i*.22;xi=int(round(x))
  for k,c in enumerate('anoopa'): C.px(xi-2+k,y,c)
for k in range(3): C.px(int(round(15.5+30*.22))-1+k,-11,'a')
C.px(int(round(15.5+29*.22)),-11,'o')
for x in range(10,23): C.px(x,20,'s' if x<16 else 't');C.px(x,21,'t')
for x in range(9,24):
  for y in (19,22):
    if C.c[y+C.oy][x]=='.': C.px(x,y,'a')
C.px(9,20,'a');C.px(9,21,'a');C.px(23,20,'a');C.px(23,21,'a')
C.ell(16,23.5,3.2,2.8,B)
for x in (14,16,18): C.px(x,23,'e')
# cráneo un poco girado y bajo (encorvado)
C.ell(36.5,14,9.6,9.2,B,1.15)
C.poly([(30,18),(43,18),(42,23),(31,23)],B)
for cx,cy in ((32.5,14.5),(40.5,14.5)):C.ell(cx,cy,3,3.3,'yyyy')
for cx in (32,40):
  C.px(cx,14,'u');C.px(cx+1,14,'v');C.px(cx,15,'v');C.px(cx+1,15,'v')
  for (x,y) in ((-1,14),(2,14),(-1,15),(2,15),(0,13),(1,13),(0,16),(1,16)): 
    if C.c[y+C.oy][cx+x]=='y': C.px(cx+x,y,'z')
for (x,y) in ((36,18),(37,18),(36,19),(37,19),(35,20),(38,20)): C.px(x,y,'y')
for x in range(31,43): C.px(x,22,'a')
for x in range(31,43,2): C.px(x,23,'b');C.px(x+1,23,'y')
for x in range(31,43): C.px(x,24,'y');C.px(x,25,'y')
C.poly([(31,26),(42,26),(40,30),(33,30)],B)
for x in range(32,42,2): C.px(x,26,'c');C.px(x+1,26,'y')
C.px(29,9,'a');C.px(30,10,'a');C.px(30,11,'e');C.px(31,11,'a')
# escudo adelante (derecha), oscuro y gastado
cx,cy,R=55,53,13.5
pts=[(x,y) for y in range(-14,96) for x in range(70) if math.hypot(x+.5-cx,y+.5-cy)<=R];S=set(pts)
for (x,y) in pts:
  for a,b in((1,0),(-1,0),(0,1),(0,-1)):
    if (x+a,y+b) not in S: C.px(x+a,y+b,'a')
for (x,y) in pts:
  dx,dy=x+.5-cx,y+.5-cy;d=math.hypot(dx,dy);v=(dx*-.62+dy*-.78)/R
  if d>R-2.2: c='j' if v>.4 else 'k' if v>-.15 else 'l' if v>-.6 else 'm'
  else:
    c='f' if v>.5 else 'g' if v>-.05 else 'h' if v>-.5 else 'i'
    if (dx+R)%5<.9: c='i'
  C.px(x,y,c)
for k in range(10):
  a=k*math.pi/5;C.px(int(cx+math.cos(a)*(R-1.1)),int(cy+math.sin(a)*(R-1.1)),'j')
em=['..wwwww..','.wwwwwww.','wwwwwwwww','wyywwwyyw','wyywwwyyw','.wwwywww.','..wywyw..','..wwwww..']
for j,r in enumerate(em):
  for i,c in enumerate(r):
    if c=='w': C.px(51+i,47+j,'w' if i<5 else 'x')
    elif c=='y': C.px(51+i,47+j,'i')
# suciedad: motas oscuras en el hueso
for y in range(len(C.c)):
  for x in range(70):
    if C.c[y][x] in 'bc' and random.random()<.07: C.c[y][x]='d' if C.c[y][x]=='c' else 'c'
json.dump(C.rows(),open('skel4.json','w'))
