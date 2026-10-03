# Kit para dibujar monstruos con más detalle: partes de atrás hacia adelante, cada una con su contorno,
# sombreado en 4 tonos por escalones (luz arriba a la izquierda), sin degradé ni tramado.
import math
L=(-0.62,-0.78)
class Canvas:
  def __init__(s,W,H,oy=0,ox=0): s.W,s.H,s.oy,s.ox=W+ox,H+oy,oy,ox;s.c=[['.']*(W+ox) for _ in range(H+oy)]
  def _paint(s,mask,shade):
    sh0=shade;mask=[(x+s.ox,y+s.oy) for (x,y) in mask];shade=lambda x,y:sh0(x-s.ox,y-s.oy)
    # contorno: píxeles vecinos a la máscara que no están en la máscara
    ms=set(mask)
    for (x,y) in mask:
      for a,b in((1,0),(-1,0),(0,1),(0,-1)):
        q=(x+a,y+b)
        if q not in ms and 0<=q[0]<s.W and 0<=q[1]<s.H: s.c[q[1]][q[0]]='a'
    for (x,y) in mask:
      if 0<=x<s.W and 0<=y<s.H: s.c[y][x]=shade(x,y)
  th=(.45,-.05,-.55)
  def tone(s,T,v):  # v: -1 (sombra) .. 1 (luz)
    a,b,c=s.th;return T[0] if v>a else T[1] if v>b else T[2] if v>c else T[3]
  def cap(s,p0,p1,w,T,flat=False):
    (x0,y0),(x1,y1)=p0,p1;dx,dy=x1-x0,y1-y0;ln=math.hypot(dx,dy) or 1;nx,ny=-dy/ln,dx/ln
    if nx*L[0]+ny*L[1]<0: nx,ny=-nx,-ny
    m=[]
    for y in range(int(min(y0,y1)-w-1),int(max(y0,y1)+w+2)):
      for x in range(int(min(x0,x1)-w-1),int(max(x0,x1)+w+2)):
        px,py=x+.5,y+.5;t=max(0,min(1,((px-x0)*dx+(py-y0)*dy)/(ln*ln)));cx,cy=x0+dx*t,y0+dy*t
        if math.hypot(px-cx,py-cy)<=w/2: m.append((x,y))
    def sh(x,y):
      px,py=x+.5,y+.5;t=max(0,min(1,((px-x0)*dx+(py-y0)*dy)/(ln*ln)));cx,cy=x0+dx*t,y0+dy*t
      o=((px-cx)*nx+(py-cy)*ny)/(w/2);return s.tone(T,o*1.1 if not flat else 0)
    s._paint(m,sh)
  def ell(s,cx,cy,rx,ry,T,k=1.0):
    m=[(x,y) for y in range(int(cy-ry-1),int(cy+ry+2)) for x in range(int(cx-rx-1),int(cx+rx+2)) if ((x+.5-cx)/rx)**2+((y+.5-cy)/ry)**2<=1]
    def sh(x,y):
      a,b=(x+.5-cx)/rx,(y+.5-cy)/ry;return s.tone(T,(a*L[0]+b*L[1])*1.25*k+ .1)
    s._paint(m,sh)
  def poly(s,pts,T,grad=True):
    xs=[p[0] for p in pts];ys=[p[1] for p in pts];m=[]
    for y in range(int(min(ys)),int(max(ys))+1):
      for x in range(int(min(xs)),int(max(xs))+1):
        px,py=x+.5,y+.5;ins=False;j=len(pts)-1
        for i in range(len(pts)):
          (xi,yi),(xj,yj)=pts[i],pts[j]
          if (yi>py)!=(yj>py) and px<(xj-xi)*(py-yi)/(yj-yi+1e-9)+xi: ins=not ins
          j=i
        if ins: m.append((x,y))
    cx=sum(xs)/len(xs);cy=sum(ys)/len(ys);rx=(max(xs)-min(xs))/2+.1;ry=(max(ys)-min(ys))/2+.1
    s._paint(m,lambda x,y:s.tone(T,((x+.5-cx)/rx*L[0]+(y+.5-cy)/ry*L[1])*1.2+.1) if grad else T[1])
  def px(s,x,y,c):
    y+=s.oy;x+=s.ox
    if 0<=x<s.W and 0<=y<s.H: s.c[y][x]=c
  def rows(s): return [''.join(r) for r in s.c]

def _seg(px,py,a,b):
  (x0,y0),(x1,y1)=a,b;dx,dy=x1-x0,y1-y0;ln2=dx*dx+dy*dy or 1
  t=max(0,min(1,((px-x0)*dx+(py-y0)*dy)/ln2));cx,cy=x0+dx*t,y0+dy*t
  return math.hypot(px-cx,py-cy),cx,cy,dx,dy
def path(s,pts,w,T,w2=None):
  """Una sola forma a lo largo de varios puntos (sin contornos internos). w2: ancho final (afinado)."""
  w2=w if w2 is None else w2;n=len(pts)-1
  xs=[p[0] for p in pts];ys=[p[1] for p in pts];W=max(w,w2)
  m=[];info={}
  for y in range(int(min(ys)-W-1),int(max(ys)+W+2)):
    for x in range(int(min(xs)-W-1),int(max(xs)+W+2)):
      px,py=x+.5,y+.5;best=None
      for i in range(n):
        d,cx,cy,dx,dy=_seg(px,py,pts[i],pts[i+1]);ww=w+(w2-w)*(i+.5)/n
        if d<=ww/2 and (best is None or d/ww<best[0]): best=(d/ww,cx,cy,dx,dy,ww)
      if best: m.append((x,y));info[(x,y)]=best
  def sh(x,y):
    _,cx,cy,dx,dy,ww=info[(x,y)];ln=math.hypot(dx,dy) or 1;nx,ny=-dy/ln,dx/ln
    if nx*L[0]+ny*L[1]<0: nx,ny=-nx,-ny
    return s.tone(T,((x+.5-cx)*nx+(y+.5-cy)*ny)/(ww/2)*1.1)
  s._paint(m,sh)
Canvas.path=path
