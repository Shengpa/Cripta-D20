# Manos en primera persona: guerrero (espada y escudo) y mago (bastón y mano con magia)
import json
def grid(W,H): return [['.']*W for _ in range(H)]
def put(G,x,y,c):
  if 0<=y<len(G) and 0<=x<len(G[0]): G[y][x]=c
def outline(G):
  H,W=len(G),len(G[0]);O=[r[:] for r in G]
  for y in range(H):
    for x in range(W):
      if G[y][x]=='.' and any(0<=x+a<W and 0<=y+b<H and G[y+b][x+a]!='.' for a,b in((1,0),(-1,0),(0,1),(0,-1))): O[y][x]='a'
  return [''.join(r) for r in O]
def ell(G,cx,cy,rx,ry,t,lx=-.6,ly=-.6):
  for y in range(len(G)):
    for x in range(len(G[0])):
      dx,dy=(x+.5-cx)/rx,(y+.5-cy)/ry
      if dx*dx+dy*dy<=1:
        s=dx*lx+dy*ly;put(G,x,y,t[0] if s>.35 else t[1] if s>-.15 else t[2] if s>-.6 else t[3])
def rect(G,x0,y0,w,h,t):  # t: 3-4 tonos de izq a der
  for y in range(y0,y0+h):
    for x in range(x0,x0+w):
      f=(x-x0+.5)/w;put(G,x,y,t[0] if f<.3 else t[1] if f<.65 else t[2] if f<.9 else t[-1])
# --- mano derecha con espada (32x56). Paleta: b..e acero, f..i guantelete cuero/acero, p q r hoja, s t oro
R=grid(32,56)
for y in range(0,34):   # hoja inclinada hacia arriba a la izquierda
  cx=6+y*0.32
  for k,c in enumerate('pqqr'): put(R,int(cx)+k,y,c)
put(R,6,0,'.');put(R,8,0,'.');put(R,9,0,'.')
for y in range(1,32,1):
  cx=6+y*0.32;put(R,int(cx)+1,y,'p')
for x in range(8,27): put(R,x,34,'s' if x<18 else 't'); put(R,x,35,'t' if x>9 else 's')
put(R,7,34,'s');put(R,27,35,'t')
ell(R,19,44,9,8,['f','g','h','i'])           # puño enguantado
for j,y in enumerate((40,43,46)):              # nudillos/dedos
  for x in range(12,26): 
    if R[y][x] in 'fghi': put(R,x,y,'h')
rect(R,18,48,13,8,['b','c','d','e'])          # brazal de acero
for x in range(18,31): put(R,x,48,'b' if x<24 else 'c')
# --- mano izquierda con escudo (40x44)
L=grid(40,44)
ell(L,14,44,26,26,['j','k','l','m'],-.5,-.7)
for y in range(44):
  for x in range(40):
    dx,dy=x+.5-14,y+.5-44;d=(dx*dx+dy*dy)**.5
    if 23.5<d<=26: put(L,x,y,'b' if dx+dy*0.3<-8 else 'c' if dx<6 else 'd')
    elif d<=3.5: put(L,x,y,'b' if dx+dy<0 else 'd')
    elif d<=5: put(L,x,y,'e')
for y in range(44):   # franja roja pintada
  for x in range(40):
    dx,dy=x+.5-14,y+.5-44;d=(dx*dx+dy*dy)**.5
    if 5<d<23.5 and abs(dx-dy*-0.9)<3.2: put(L,x,y,'n' if dx<0 else 'o')
# --- mago: mano derecha con bastón (30x60)
S=grid(30,60)
for y in range(8,60):
  cx=8+y*0.18
  for k,c in enumerate('uvw'): put(S,int(cx)+k,y,c)
ell(S,10.5,6,5,5.5,['x','y','y','z'])          # gema violeta
for (x,y) in ((7,3),(8,3),(8,4)): put(S,x,y,'x')
for x in range(6,16): put(S,x,11,'t' if x>10 else 's')
ell(S,17,42,8,7,['F','G','H','I'])           # mano (piel) agarrando
for y in (39,42,45):
  for x in range(11,24):
    if S[y][x] in 'FGHI' and x>12: put(S,x,y,'H')
rect(S,15,48,15,12,['J','K','L','M'])         # manga
# --- mago: mano izquierda abierta con magia (34x46)
M=grid(34,46)
rect(M,4,34,16,12,['J','K','L','M'])
ell(M,13,28,8,8,['F','G','H','I'],-.4,-.6)    # palma
for i,(x0,y0,h) in enumerate(((7,12,12),(11,9,14),(15,10,13),(19,14,10))):  # dedos abiertos
  for y in range(y0,y0+h):
    for x in range(x0,x0+3): put(M,x,y,'F' if x==x0 else 'G' if x==x0+1 else 'H')
for y in range(26,32):
  for x in range(21,26): put(M,x,y,'G' if x<23 else 'H')   # pulgar
out={'R':outline(R),'L':outline(L),'S':outline(S),'M':outline(M)}
json.dump(out,open('hands.json','w'))
for k,v in out.items(): print(k);print('\n'.join(v))
