(A)=>{
 const V=document.getElementById('view'),WW=V.width,VH3=V.height,TOT=960,o=cnv(WW,TOT),x=o.getContext('2d');x.imageSmoothingEnabled=false;
 x.fillStyle='#120c0a';x.fillRect(0,0,WW,TOT);x.drawImage(V,0,0);
 const PAL={a:'140a08',b:'d8dce4',c:'9aa0ac',d:'666c78',e:'3e424c',f:'8a5a30',g:'6a4220',h:'4a2c14',i:'30200c',j:'8a6a40',k:'6a4e2c',l:'4a361e',m:'302214',n:'a83a2a',o:'7a2a20',
  p:'eef2f6',q:'a8b2bc',r:'5e6672',s:'e0b448',t:'9a7424',u:'8a6038',v:'5e4026',w:'3a2614',x:'f0d8ff',y:'a854ff',z:'5a2a9a',
  F:'e8b890',G:'c08a64',H:'8e5e42',I:'5e3a28',J:'4a3a8a',K:'34286a',L:'241c4c',M:'160f30'};
 const gc=(rows,dark)=>{const c=cnv(rows[0].length,rows.length),g=c.getContext('2d');rows.forEach((r,j)=>{for(let i=0;i<r.length;i++){const k=r[i];if(k==='.')continue;g.fillStyle='#'+PAL[k];g.fillRect(i,j,1,1)}});
  if(dark){g.globalCompositeOperation='source-atop';g.fillStyle=`rgba(12,6,2,${dark})`;g.fillRect(0,0,c.width,c.height)}return c};
 const gc2=(rows,P)=>{const c=cnv(rows[0].length,rows.length),g=c.getContext('2d');rows.forEach((r,j)=>{for(let i=0;i<r.length;i++){const k=r[i];if(k==='.')continue;g.fillStyle='#'+P[k];g.fillRect(i,j,1,1)}});return c};
 const put=(c,px,py,s)=>x.drawImage(c,px,py,c.width*s,c.height*s);
 const s=6,bob=A.bob||0;
 if(A.cls==='g'){
  const L=gc(A.H.L,.18),R=gc(A.H.R,.12);put(L,-30,VH3-L.height*s+6+bob*s,s);put(R,WW-R.width*s+6,VH3-R.height*s-6-bob*s,s);
 }else{
  const M=gc(A.H.M,.15),S=gc(A.H.S,.12);
  // resplandor violeta en escalones sobre la palma y luz sobre la escena cercana
  const cx=13*s+10,cy=VH3-M.height*s+16*s+6+bob*s;
  x.globalCompositeOperation='lighter';[[150,.06],[105,.08],[70,.11]].forEach(([r,a])=>{x.fillStyle=`rgba(150,70,255,${a})`;x.beginPath();x.arc(cx,cy,r,0,7);x.fill()});x.globalCompositeOperation='source-over';
  put(M,10,VH3-M.height*s+6+bob*s,s);
  [[30,'#7a30d0'],[22,'#a854ff'],[14,'#d8a8ff'],[7,'#ffffff']].forEach(([r,c])=>{x.fillStyle=c;for(let j=-r;j<=r;j+=6)for(let i=-r;i<=r;i+=6)if(i*i+j*j<=r*r)x.fillRect(Math.round((cx+i)/6)*6-3,Math.round((cy-30+j)/6)*6-3,6,6)});
  put(S,WW-S.width*s+10,VH3-S.height*s+10-bob*s,s);
 }
 x.strokeStyle='#0a0605';x.lineWidth=6;x.strokeRect(3,3,WW-6,VH3-6);x.strokeStyle='#8a6a34';x.lineWidth=2;x.strokeRect(7,7,WW-14,VH3-14);
 const font=(n)=>`${Math.round(n*.78)}px "DejaVu Sans Mono", monospace`;
 const panel=(px,py,pw,ph)=>{x.fillStyle='rgba(14,9,7,.82)';x.fillRect(px,py,pw,ph);x.strokeStyle='#0a0605';x.lineWidth=4;x.strokeRect(px,py,pw,ph);x.strokeStyle='#8a6a34';x.lineWidth=2;x.strokeRect(px+3,py+3,pw-6,ph-6)};
 const R=6,cs=9,mw=(2*R+1)*cs+12;panel(14,14,mw,mw);
 const [f0,f1]=DIRS[pos.d],[r0,r1]=DIRS[(pos.d+1)%4];
 for(let j=-R;j<=R;j++)for(let i=-R;i<=R;i++){const wx=pos.x+r0*i-f0*j,wy=pos.y+r1*i-f1*j;let v=(wx<0||wy<0||wx>=MW||wy>=MH)?0:map[wy*MW+wx];if(v!==1&&v<3)continue;x.fillStyle=v===1?'#7a6a54':'#a0703a';x.fillRect(20+(i+R)*cs,20+(j+R)*cs,cs-1,cs-1)}
 for(const m of mons){const dx=m.x-pos.x,dy=m.y-pos.y,i=dx*r0+dy*r1,j=-(dx*f0+dy*f1);if(Math.abs(i)<=R&&Math.abs(j)<=R){x.fillStyle='#b070ff';x.fillRect(20+(i+R)*cs+2,20+(j+R)*cs+2,cs-5,cs-5)}}
 const pcx=20+R*cs+cs/2-.5,pcy=20+R*cs+cs/2;x.fillStyle='#ffd860';x.beginPath();x.moveTo(pcx,pcy-5);x.lineTo(pcx+4,pcy+4);x.lineTo(pcx-4,pcy+4);x.closePath();x.fill();
 x.fillStyle='#e8d2a0';x.font=font(22);x.fillText('Piso '+floorN+' de 5',18,mw+36);
 const ox=WW-14-246,oy=14;panel(ox,oy,246,112);x.fillStyle='#e0b850';x.font=font(22);x.fillText('OBJETIVOS DEL PISO',ox+14,oy+28);
 [['Encontrá la llave',A.n>0],['Resolvé el acertijo',true],['Derrotá al jefe',false]].forEach(([t,dn],k)=>{const yy=oy+54+k*24;x.strokeStyle='#c8b080';x.lineWidth=2;x.strokeRect(ox+16,yy-13,13,13);
  if(dn){x.strokeStyle='#ffd860';x.lineWidth=3;x.beginPath();x.moveTo(ox+18,yy-7);x.lineTo(ox+22,yy-2);x.lineTo(ox+31,yy-16);x.stroke()}
  x.fillStyle=dn?'#8a7a60':'#f0e4c8';x.font=font(22);x.fillText(t,ox+38,yy);if(dn)x.fillRect(ox+38,yy-7,x.measureText(t).width,2)});
 // abajo: un solo héroe
 const by=VH3;x.fillStyle='#231d26';x.fillRect(0,by,WW,TOT-by);
 const m=party[A.cls==='g'?0:2],pc=gc2(A.P[A.cls],A.PP);x.fillStyle='#2a2018';x.fillRect(10,by+6,72,72);x.drawImage(pc,10,by+6,72,72);x.strokeStyle='#c8a050';x.lineWidth=2;x.strokeRect(10,by+6,72,72);
 x.fillStyle='#f0e4c8';x.font=font(24);x.fillText(m.name+(A.cls==='g'?' · Guerrero':' · Mago')+' · Nv 1',92,by+26);
 const f=.8;x.fillStyle='#120c0a';x.fillRect(92,by+36,WW-104,16);x.fillStyle='#b83020';x.fillRect(93,by+37,(WW-106)*f,14);x.fillStyle='#e85a3a';x.fillRect(93,by+37,(WW-106)*f,4);
 x.fillStyle='#fff';x.font=font(18);x.fillText((A.cls==='g'?'13/16':'10/12')+' PV',98,by+49);
 x.fillStyle='#c8b8e0';x.font=font(18);x.fillText(A.cls==='g'?'Aliento 2/2   CA 16':'Conjuros ■■□   CA 11',92,by+70);
 // barra de objetos con iconos propios
 const IC={pr:['..aa..','.abba.','.acca.','adccda','adddda','.aaaa.'],pa:['..aa..','.abba.','.aeea.','afeefa','affffa','.aaaa.'],
  sc:['aaaaaa','aggg ga','agggga','ahhhha','agggga','aaaaaa'],ke:['.aa...','aiia..','aiiaaa','.aaiia','....aa','......'],to:['.jj...','.kj...','.al...','.al...','.al...','.aa...']};
 const ICP={a:'140a08',b:'e0d8c8',c:'e04030',d:'a02820',e:'4080e0',f:'2850a0',g:'e8d8a8',h:'b8a070',i:'e0b448',j:'ffd860',k:'ff8030',l:'6e4a22'};
 const slots=['pr','pa','sc','ke','to',null],sw=50,sx=10,sy=by+86;
 slots.forEach((k,i)=>{const bx=sx+i*(sw+4);x.fillStyle='#3a3344';x.fillRect(bx,sy,sw,sw);x.strokeStyle='#0a0605';x.lineWidth=2;x.strokeRect(bx,sy,sw,sw);
  x.fillStyle='#b8b0c8';x.font=font(16);x.fillText(String(i+1),bx+3,sy+13);
  if(k){const g=IC[k];g.forEach((r,j)=>{for(let q=0;q<r.length;q++){const ch=r[q];if(ch==='.'||ch===' ')continue;x.fillStyle='#'+ICP[ch];x.fillRect(bx+10+q*5,sy+12+j*5,5,5)}})}});
 const bx0=sx+6*(sw+4)+6,bw=(WW-bx0-10)/3;['↰','↑','↱'].forEach((t,k)=>{const bx=bx0+k*bw;x.fillStyle='#4a4236';x.fillRect(bx+2,sy,bw-4,sw);x.fillStyle='#5e5444';x.fillRect(bx+2,sy,bw-4,5);x.strokeStyle='#0a0605';x.strokeRect(bx+2,sy,bw-4,sw);x.fillStyle='#e8d2a0';x.font=font(34);const tw=x.measureText(t).width;x.fillText(t,bx+(bw-tw)/2,sy+36)});
 return o.toDataURL()}
