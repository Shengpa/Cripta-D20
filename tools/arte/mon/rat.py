from common import *
P={'a':'140a08','b':'9a8270','c':'6e5a4a','d':'4a3a30','e':'2a201a','f':'e0a0a0','g':'b07070','h':'7a4848','i':'4a2a2a','u':'ffb0a0','v':'e02818','y':'140a08','w':'f0e8d0','x':'b0a080'}
C=Canvas(72,46,2);C.th=(.6,.1,-.45);F='bcde';K='fghi'
C.path([(60,30),(66,22),(70,12),(68,4)],3.2,K,1.2)              # cola
ch(C,[(52,34),(56,42)],4.4,F);C.path([(56,42),(52,44)],2.4,K)     # pata trasera atrás
C.ell(44,28,20,13,F,1.05)                                         # cuerpo
for (x,y) in ((34,22),(40,19),(47,20),(53,23),(38,27),(50,27),(44,24)): C.px(x,y,'c')
C.path([(56,30),(60,38),(58,44)],6,F,4);C.path([(58,44),(52,45)],2.6,K)   # pata trasera
C.path([(30,32),(28,40),(24,44)],4.4,F,3);C.path([(24,44),(19,45)],2.2,K)  # pata delantera
C.ell(22,24,11,8.5,F,1.1)                                          # cabeza
C.poly([(13,20),(3,27),(4,30),(14,30)],F)                          # hocico
C.ell(3.5,28,2,1.6,K)                                              # nariz
C.ell(24,15,4.5,5,'cdde');C.ell(24,15.5,2.8,3.2,K)                  # orejas
C.ell(31,16,4.5,5,'cdde');C.ell(31,16.5,2.8,3.2,K)
C.ell(16.5,22,2.2,2,'yyyy');C.px(16,21,'u');C.px(17,22,'v');C.px(16,22,'v')
for x in range(4,13): C.px(x,31,'y')
C.px(6,32,'w');C.px(7,32,'w');C.px(6,33,'x');C.px(7,33,'x')       # dientes
for (x0,y0,x1,y1) in ((6,26,0,24),(6,27,0,28),(8,25,2,21)):
  n=max(abs(x1-x0),abs(y1-y0))
  for t in range(n+1): C.px(round(x0+(x1-x0)*t/n),round(y0+(y1-y0)*t/n),'x')
C.path([(18,32),(17,40),(13,44)],4,F,3);C.path([(13,44),(8,45)],2.2,K)
dirt(C,[F],.08)
save('rat',C,P)
