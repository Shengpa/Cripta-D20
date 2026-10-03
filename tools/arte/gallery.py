# Galería: monstruo v20 (izq) y nuevo (der) a la misma altura
import json,sys,os,base64,asyncio
from PIL import Image,ImageDraw,ImageFont
from playwright.async_api import async_playwright
def render(d,S):
  rows,P=d['rows'],d['pal'];W,H=len(rows[0]),len(rows);im=Image.new('RGBA',(W,H),(0,0,0,0));px=im.load()
  for j,r in enumerate(rows):
    for i,c in enumerate(r):
      if c!='.': h=P[c];px[i,j]=(int(h[0:2],16),int(h[2:4],16),int(h[4:6],16),255)
  return im
async def old(ks):
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome');pg=await b.new_page()
    await pg.goto('file:///home/claude/cripta-d20/index.html');await pg.wait_for_timeout(800)
    r=await pg.evaluate("ks=>ks.map(k=>{for(const q in SPR)delete SPR[q];return makeSprite(k).toDataURL()})",ks);await b.close();return r
ks=sys.argv[1].split(',')
olds=asyncio.run(old(ks))
from io import BytesIO
H=420;f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',22)
cols=[]
for k,u in zip(ks,olds):
  o=Image.open(BytesIO(base64.b64decode(u.split(',')[1]))).convert('RGBA');bb=o.getbbox();o=o.crop(bb)
  n=render(json.load(open(f'mon/{k}.json')),1);n=n.crop(n.getbbox())
  so=max(1,H//2//o.height);sn=max(1,round(H/n.height))
  o=o.resize((o.width*so,o.height*so),Image.NEAREST);n=n.resize((n.width*sn,n.height*sn),Image.NEAREST)
  cols.append((k,o,n))
W=sum(max(o.width,n.width)+o.width+60 for k,o,n in cols)
out=Image.new('RGB',(max(W,400),H+70),(42,32,24));d=ImageDraw.Draw(out);x=20
for k,o,n in cols:
  d.text((x,8),k,fill=(232,210,160),font=f)
  out.paste(o,(x,H+50-o.height),o);x+=o.width+20;out.paste(n,(x,H+50-n.height),n);x+=n.width+40
out.save(sys.argv[2])
