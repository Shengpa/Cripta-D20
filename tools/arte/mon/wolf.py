from common import *
P={'a':'140a08','b':'b4aca0','c':'827a70','d':'565048','e':'322e2a','f':'e6dfd0','g':'bcb4a6','h':'8a8276','i':'5a5248','u':'fff4a0','v':'f0c020','y':'140a08','w':'f4eedc','x':'b8ae94','r':'7a2a2a'}
C=Canvas(76,58,4,4);C.th=(.42,-.18,-.62);F='bcde';L='fghi'
C.path([(64,22),(70,24),(75,30)],7,F,3)                               # cola en alto
C.path([(56,30),(60,42),(55,48),(57,56)],8,F,3.4);C.ell(58,56,3.4,1.8,'cdde')     # pata trasera atrás
C.path([(30,36),(27,46),(28,56)],5.4,F,3.4);C.ell(27,56,3.2,1.8,'cdde')     # pata delantera atrás
C.poly([(22,20),(40,15),(56,16),(66,22),(66,32),(58,38),(42,38),(28,42),(20,34)],F)     # cuerpo
for x in range(26,64,3):
  for y in range(17,24): 
    if C.c[y+C.oy][x+C.ox]=='b' and (x+y)%2: C.px(x,y,'c')
C.poly([(24,34),(34,36),(50,35),(58,37),(46,39),(30,43)],'ghhi')                  # panza clara
C.path([(62,28),(67,40),(61,47),(63,56)],9,F,3.6);C.ell(64,56,3.6,2,'cdde')
C.path([(34,36),(33,47),(35,56)],6.4,F,3.8);C.ell(36,56,3.6,2,'cdde')
C.poly([(14,14),(30,12),(34,26),(26,36),(14,32)],F)                       # cuello y melena
for (x,y) in ((18,16),(24,15),(28,20),(20,24),(26,28),(16,28)): C.px(x,y,'c');C.px(x+1,y+1,'d')
C.ell(16,18,10,8.5,F,1.1)                                                  # cabeza
C.poly([(5,13),(10,4),(14,12)],F);C.poly([(16,10),(22,1),(25,11)],F)       # orejas
C.poly([(8,10),(10,6),(12,11)],'hhii');C.poly([(18,9),(21,4),(23,10)],'hhii')
C.poly([(8,18),(-2,20),(-2,27),(10,27)],F)                                 # hocico
C.ell(0,20,2,1.6,'eeee')
for x in range(0,10): C.px(x,24,'y');C.px(x,25,'r')                        # boca gruñendo
for x in (1,3,6,8): C.px(x,23,'w');C.px(x,26,'w')
C.px(2,22,'w');C.px(7,27,'w')
C.poly([(1,26),(10,26),(10,29),(2,28)],'cdde')
C.ell(10,14,2.4,1.6,'yyyy');C.px(9,14,'u');C.px(10,14,'v');C.px(11,14,'v')
C.ell(17,13,2.4,1.6,'yyyy');C.px(16,13,'u');C.px(17,13,'v');C.px(18,13,'v')
for x in range(7,13): C.px(x,12,'e')
for x in range(15,20): C.px(x,11,'e')
dirt(C,[F],.07)
save('wolf',C,P)
