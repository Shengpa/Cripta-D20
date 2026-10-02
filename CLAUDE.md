# Cripta d20 — guía para Claude

Juego para celular (Android y iPhone) estilo dungeon crawler retro en primera persona, inspirado en Eye of the Beholder, con reglas de la quinta edición (SRD 5.2, CC-BY-4.0). Nunca usar el nombre "Dungeons & Dragons" (la atribución al SRD está en la portada). Todo el arte es propio y se genera con código: no copiar gráficos ni interfaz de juegos comerciales. El dueño es Chelo: habla en español rioplatense y la interfaz del juego también va en español rioplatense.

## Cómo trabajamos (leer primero)
- **Los pendientes son los issues de GitHub** de este repo. Al empezar, mirá los issues abiertos (`curl -sS https://api.github.com/repos/Shengpa/cripta-d20/issues`) y trabajá en el que pida Chelo.
- **Una rama por issue** (`issue-N-descripcion`). Al terminar: probar, subir la rama, abrir un PR que diga `Closes #N`, mergearlo y borrar la rama. La API de GitHub funciona con `curl` sin token (la sesión ya está autenticada).
- **Antes de mergear:** subir `VERSION` en `sw.js` (`cripta-d20-vNN`) y correr `python3 tools/prueba.py`. Para cambios visuales, correr `python3 tools/prueba.py --capturas` y mirar las capturas.
- **A Chelo le gusta ver imágenes antes de que se cambie el juego** cuando el cambio es de estilo: primero una muestra (antes y después), después el cambio.
- **No leer `index.html` entero** (son unas 2800 líneas). Buscar con `grep -n` la función que hace falta y leer solo esa parte.
- Si aprendés algo nuevo sobre los gustos de Chelo, sumalo en "Estilo" más abajo. La historia detallada versión por versión está en `docs/traspaso.md`: leer solo si hace falta.

## Publicación
- PWA de archivos sueltos en la raíz: `index.html` (todo el juego, sin librerías; solo fuentes de Google Fonts: Jacquard 12, Pirata One, VT323), `sw.js`, `manifest.webmanifest`, 4 íconos y `social.png` (tarjeta del link, 1200×630).
- Se publica en Netlify desde la rama `main` (`cripta-d20.netlify.app`, para no mostrar el usuario de GitHub). Las etiquetas `og:*` y `twitter:*` del `index.html` apuntan a esa dirección.
- Guardado local: `cripta-save` (partida), `cripta-party` (grupo), ajustes y `cripta-heroes` (Salón de héroes).

## Cómo está armado `index.html`
El script tiene el juego base y, al final, secciones que **reemplazan funciones de dibujo** definidas más arriba (el orden importa: la última asignación gana). Todas quedan antes de `initDemo();refreshTitle();`.
- **Datos:** `MON` (monstruos), `HGT` (altura en metros de cada monstruo), `CL`, `SP`, `BG`, `SPL`, `CAT` (objetos y tesoros), `DIFF`, `CAMPS` (aventuras), `RIDDLES`, `SYMS`.
- **Flujo:** `startGame`, `continueGame`, `genFloor`, `genMap`, `addVault`, `descend`, `openShop`, `finalChoice`, `ending`, `toTitle`.
- **Combate:** `memberAttack`, `attackRoll`, `castSpell`, `useAbility`, `monAttack`, `hurtMember`, `killMon`, `levelUp`.
- **Dibujo base:** `drawView`, `castFloor`, `frontFace`, `sideFace`, `buildTextures`, `drawPortrait` (retratos 32×32), `drawMap`.
- **v16 (estilo 90):** paredes de bloques con luz por escalones, paletas `PALS` por piso, decoraciones por ambiente (`DEC`, `deco90`), marco de mármol.
- **v17:** tamaños reales (`HGT`, `monFrac`, `spriteTop`) y lienzo de 720×480 (`VS=3`) dibujando en coordenadas de 240×160.
- **v18 (monstruos en pixel art grueso):** `pixArt` rasteriza `spriteArt` con 4 tonos en bloques (`band`, `edge`); `HAND` tiene goblin, esqueleto, lobo y ogro dibujados a mano; `OVR` tiene dibujos rehechos.
- **v19 (relieve y luces):** `blockWall` (piedras irregulares con relieve, solo paredes); `buildLM` (mapa de luz de antorchas y decoraciones brillantes, 4×4 por casillero, en escalones), `mix`, `shade`, `castFloor`/`frontFace`/`sideFace`/`getSprite`/`drawSprite` nuevos y ojos que brillan (`emissive`).
- Para probar en la consola: `startGame()`, `genFloor(n)`, `spawn(clave,x,y)` en las casillas de `cellAt(distancia,carril)`, `act('f'|'b'|'tl'|'tr'|'sl'|'sr')`, `setAuto(true)`.

## Estilo: lo que le gusta y lo que no
- **Le gusta:** pixel art grueso con pocos píxeles, bordes nítidos, contorno negro, 3 o 4 tonos en bloques, luz por escalones (sin degradé), aire de fines de los 80 y principios de los 90, tamaños proporcionados por altura real, luz cálida de antorchas sumada encima de la luz de siempre, piedras irregulares con relieve.
- **No le gusta (no repetir):** sombreado suave o "de plastilina" (óvalos y tubos con 8 tonos y tramado); planos angulosos tipo low poly; versiones con muchos más píxeles por monstruo; paquetes de arte ya hechos (prefiere los dibujos propios); luz que cambia el color base de la piedra (tinte frío, filtro sepia); abombado ovalado en el centro de los bloques.

## Juego base (resumen)
Tres aventuras de 5 pisos más el modo Sin fin (`CAMPS`): El Cáliz del Alba (nivel 1), La Mina de Hierronegro (nivel 5) y El Rey bajo el Túmulo (nivel 7). Cada una tiene su plantel de monstruos, rescate en el piso 3, dos finales y escalado por nivel (`scaleFor`). Grupo de 4 héroes, nivel máximo 8, Salón de héroes con hasta 8 grupos. Mercader con vitrina de tesoros y seña; bóvedas con llave, adivinanza o palancas; acertijos con opción "Pensar" (INT).
