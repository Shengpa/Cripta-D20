"""Prueba rápida de Cripta d20 sin teléfono.

Uso:  python3 tools/prueba.py            -> juega un rato, revisa errores y mide el rendimiento
      python3 tools/prueba.py --capturas -> además guarda capturas en /tmp/cripta/ (portada, combate, pisos 1 a 5)

Carga index.html con el Chromium de Playwright. Las fuentes de Google se bloquean (el juego usa las de respaldo).
Sale con código 1 si hubo errores de JavaScript.
"""
import asyncio, os, sys
from playwright.async_api import async_playwright

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
CAPT = '--capturas' in sys.argv
OUT = '/tmp/cripta'

async def main():
    os.makedirs(OUT, exist_ok=True)
    async with async_playwright() as p:
        kw = {'executable_path': CHROME} if os.path.exists(CHROME) else {}
        b = await p.chromium.launch(**kw)
        ctx = await b.new_context(viewport={'width': 432, 'height': 768}, device_scale_factor=2)
        pg = await ctx.new_page()
        await pg.route('**/fonts.g*/**', lambda r: r.abort())
        errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        await pg.goto('file://' + os.path.join(RAIZ, 'index.html'))
        await pg.wait_for_timeout(2000)
        if CAPT: await pg.screenshot(path=f'{OUT}/portada.png')
        await pg.click('#tQuick'); await pg.wait_for_timeout(1200)
        await pg.click('#nBtn'); await pg.wait_for_timeout(600)
        await pg.evaluate("setAuto(true)")
        for mv in ['f', 'tr', 'f', 'f', 'tl', 'f', 'sl', 'sr', 'b']:
            await pg.evaluate(f"act('{mv}')"); await pg.wait_for_timeout(300)
        await pg.evaluate("(()=>{const q=cellAt(1,0);if(map[q.y*MW+q.x]===1)spawn('skeleton',q.x,q.y)})()")
        await pg.wait_for_timeout(4000)
        if CAPT: await pg.screenshot(path=f'{OUT}/combate.png')
        ms = []
        for f in [1, 2, 3, 4, 5]:
            await pg.evaluate(f"genFloor({f});buildTextures()"); await pg.wait_for_timeout(400)
            ms.append(await pg.evaluate("(()=>{const t=performance.now();for(let i=0;i<20;i++)drawView();return (performance.now()-t)/20})()"))
            if CAPT: await pg.screenshot(path=f'{OUT}/piso{f}.png')
        caja = await pg.evaluate("document.getElementById('err').textContent")
        await b.close()
    print('ms por cuadro (pisos 1-5):', ' '.join(f'{m:.1f}' for m in ms))
    print('VERSION en sw.js:', open(os.path.join(RAIZ, 'sw.js')).read().split("VERSION='")[1].split("'")[0])
    if errs or caja:
        print('ERRORES:', errs, caja); sys.exit(1)
    print('OK, sin errores' + (f' — capturas en {OUT}/' if CAPT else ''))

asyncio.run(main())
