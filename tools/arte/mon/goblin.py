from common import *
# Goblin: encorvado, cabeza grande, orejas largas, ojos amarillos, armadura de cuero, cimitarra y escudo chico
P={'s':'d4a838','t':'8a6a20','a':'140a08','b':'a8c860','c':'74963a','d':'4c6a26','e':'2c4216',  # piel
 'f':'9a7044','g':'74502c','h':'4e341c','i':'2e1e10',                  # cuero
 'j':'b8bcc4','k':'7e828c','l':'4e525a','m':'2c2e34',                  # metal
 'n':'6a4a2a','o':'4a321c','p':'301f10','q':'1c120a',                  # madera escudo
 'u':'fff2a0','v':'f0b020','y':'1a0c08','w':'f0ead8','x':'b0a888','r':'8a3020'}
C=Canvas(60,72,6);C.th=(.6,.1,-.45)
S='bcde';L='fghi';M='jklm';W='nopq'
# pierna atrás
ch(C,[(34,50),(38,60)],5,S);ch(C,[(38,60),(36,69)],4.4,S);C.ell(38,70,4,1.8,L)
# brazo del escudo atrás + escudo chico redondo (izquierda en pantalla, adelante)
# cuerpo: torso encorvado con chaleco de cuero
C.poly([(18,30),(40,28),(44,40),(40,52),(22,53),(16,42)],L)
for y in range(32,52,4): 
  for x in range(19,42):
    if C.c[y+C.oy][x] in 'fghi' and x%3==0: C.px(x,y,'i')
C.poly([(20,47),(42,46),(43,52),(19,53)],'ghhi')   # cinturón
C.px(30,49,'v');C.px(31,49,'v');C.px(30,50,'v');C.px(31,50,'v')
C.poly([(20,52),(42,52),(44,58),(18,58)],'ghhi')    # faldón
for x in range(20,43,4): C.px(x,56,'a')
# pierna adelante
ch(C,[(26,56),(22,64)],5.4,S);ch(C,[(22,64),(24,70)],4.6,S);C.ell(23,71,4.4,2,L)
# brazo derecho con cimitarra (lado derecho en pantalla)
ch(C,[(41,31),(48,40)],4.6,S);ch(C,[(48,40),(52,32)],4,S);C.ell(52,31,3,3,S)
pts=[(52+math.sin(i/12*1.5)*6,28-i*1.7) for i in range(13)]
C.path(pts,4.2,'jjkl',2.2)
C.cap((47,30),(57,30),2.2,'ssst');
C.ell(52,31,3,3,S)
# brazo izquierdo + escudo
ch(C,[(19,32),(13,42)],4.6,S)
cx,cy,R=13,46,9.5
pts=[(x,y) for y in range(-6,72) for x in range(60) if math.hypot(x+.5-cx,y+.5-cy)<=R];SS=set(pts)
for (x,y) in pts:
  for a,b in((1,0),(-1,0),(0,1),(0,-1)):
    if (x+a,y+b) not in SS: C.px(x+a,y+b,'a')
for (x,y) in pts:
  dx,dy=x+.5-cx,y+.5-cy;d=math.hypot(dx,dy);v=(dx*-.62+dy*-.78)/R
  c=('j' if v>.4 else 'k' if v>-.2 else 'l') if d>R-1.8 else ('n' if v>.45 else 'o' if v>-.1 else 'p' if v>-.55 else 'q')
  C.px(x,y,c)
C.ell(13,46,2.4,2.4,M)
# cabeza grande: orejas largas puntiagudas
C.poly([(18,16),(1,9),(5,14),(16,22)],S)
C.poly([(42,16),(59,9),(55,14),(44,22)],S)
for x in range(5,16): C.px(x,14+ (x-5)//3,'d')
for x in range(45,56): C.px(x,14+(55-x)//3,'d')
C.ell(30,17,13,11,S,1.1)
C.poly([(20,20),(40,20),(37,30),(23,30)],S)   # mandíbula
# ceño y ojos amarillos
for x in range(20,29): C.px(x,13+(x-20)//4,'e')
for x in range(31,40): C.px(x,15-(x-31)//4,'e')
C.ell(24.5,17,3.2,2.2,'yyyy');C.ell(35.5,17,3.2,2.2,'yyyy')
for ex in (23,34):
  C.px(ex,16,'u');C.px(ex+1,16,'u');C.px(ex+2,16,'v');C.px(ex,17,'v');C.px(ex+1,17,'y');C.px(ex+2,17,'v')
# nariz ganchuda
C.poly([(28.5,17),(31.5,17),(32.5,23),(29,22)],'cdde')
# boca con colmillos
for x in range(23,38): C.px(x,26,'y')
for x in range(24,37): C.px(x,27,'y')
for (x,y) in ((24,25),(25,25),(35,25),(36,25),(24,24),(36,24)): C.px(x,y,'w')
for x in range(27,34,2): C.px(x,27,'x')
C.px(27,6,'d');C.px(31,5,'d');C.px(34,7,'d')   # verrugas/pelos
dirt(C,[S,L],.05)
save('goblin',C,P)
