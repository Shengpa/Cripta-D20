# Copia del juego con la vista nueva y los monstruos redibujados (muestra; no toca el repo)
import json,sys,glob,os
h=open('/home/claude/cripta-d20/index.html').read()
ent=[]
def add(k,rows,P):
  pal=' '.join(P.get(c,'000000') for c in 'abcdefghijklmnopqrstuvwxyz');ent.append(" "+k+":{p:'"+pal+"',d:"+json.dumps(rows)+"},")
add('skeleton',json.load(open('skel4.json')),json.load(open('pal4.json')))
for f in sorted(glob.glob('mon/*.json')):
  d=json.load(open(f));add(os.path.basename(f)[:-5],d['rows'],d['pal'])
i=h.index('\n};\nconst HCH=');h=h[:i]+'\n'+'\n'.join(ent)+h[i:]
h=h.replace('const VW=240,VH=160,F=100;','const VW=180,VH=270,F=185;')
ZM='(function(){const d0=drawSprite;drawSprite=function(kind,cx,by,s,k,fl,sw){if(MON[kind]&&F/s<2.6){const z=1.5;s*=z;by=VH/2+(by-VH/2)*z;cx=VW/2+(cx-VW/2)*z}d0(kind,cx,by,s,k,fl,sw)}})();'
i=h.rindex('initDemo();refreshTitle();');h=h[:i]+ZM+h[i:]
open(sys.argv[1],'w').write(h)
