# Cripta d20 — historia detallada (hasta la v19)

> Desde la v19 el juego vive en GitHub (`Shengpa/cripta-d20`). La guía principal para trabajar es `CLAUDE.md` y los pendientes son los issues. Este archivo queda como historia detallada de cada versión.

Pegá este documento en un chat nuevo junto con `index.html` y `sw.js` de la v19 (están en `cripta-d20-v19.zip`), y pedile a Claude que siga desde acá. Antes de trabajar, verificar que el `index.html` sea el correcto: tiene que contener `HGT`, `VS=3`, `pixArt`, `blockWall` y `buildLM`.

## Qué es
Juego para celular (Android y iPhone) estilo dungeon crawler retro en primera persona, inspirado en clásicos como Eye of the Beholder. Usa las reglas de la quinta edición (SRD 5.2, licencia CC-BY-4.0). No se llama "Dungeons & Dragons" por ser marca registrada; la atribución al SRD está en la portada. No se copian gráficos, monstruos ni interfaz de juegos comerciales: todo el arte es propio y se genera con código. Las capturas de Eye of the Beholder que Chelo compartió se usan solo como guía de estilo.

Un solo archivo `index.html` con todo el código (HTML, CSS y JavaScript, sin librerías). Solo carga fuentes de Google Fonts: Jacquard 12 (títulos), Pirata One (respaldo) y VT323 (texto).

Se publica como PWA: `index.html`, `manifest.webmanifest`, `sw.js`, cuatro íconos PNG y `social.png` (imagen de la tarjeta del link, 1200×630), todos en la raíz, sin carpetas. Antes estaba en GitHub Pages; ahora se sube a Netlify arrastrando la carpeta en app.netlify.com/drop. Las etiquetas `og:*` y `twitter:*` del `index.html` apuntan a `https://cripta-d20.netlify.app/`: si el sitio queda con otro nombre, hay que cambiar esa dirección.

**Versión de este traspaso: v19** (`VERSION = 'cripta-d20-v19'` en `sw.js`). La última publicada en GitHub Pages era la v16. La v19 incluye todo lo de la v17 y la v18. Se va a publicar en Netlify (`cripta-d20.netlify.app`) para no mostrar el usuario de GitHub. Hay que subir `VERSION` en cada actualización para que los celulares descarguen la nueva.

Interfaz en español rioplatense. Todo el guardado es local: partida (`cripta-save`), grupo armado (`cripta-party`), ajustes y Salón de héroes (`cripta-heroes`).

## Próximo proyecto acordado: juego aparte con vista desde arriba
Chelo quiere una versión con **un solo héroe y vista desde arriba** (estilo pixel art, tipo mazmorra vista en planta con antorchas, cofres, trampas, barras de vida y barra de objetos). La referencia fue una publicidad de un juego para celular ("Top Heroes"), probablemente hecha con IA: se usa solo como guía de estilo, sin copiar arte ni interfaz.
Decisiones tomadas:
- **Juego aparte**, con su propio link y nombre. Cripta d20 queda como está.
- **Combate por turnos en casillas:** cada paso del héroe es un turno y los monstruos responden. Respeta las reglas de la quinta edición.
- Se puede reusar de Cripta d20: reglas, datos de monstruos (`MON`, `HGT`), clases y razas (`CL`, `SP`), conjuros, objetos (`CAT`), aventuras (`CAMPS`), acertijos (`RIDDLES`), guardado local y sonido.
- Hay que hacer nuevo: mapa en planta con tiles, paredes vistas desde arriba, monstruos y héroe redibujados vistos desde arriba en pixel art, movimiento con pad táctil, cámara que sigue al héroe e interfaz de un solo personaje.
- Conviene empezarlo en un chat nuevo y mostrarle primero una muestra (una sala con el héroe y dos o tres monstruos) antes de armar todo.

## Qué cambió en la v19 (luces y relieve, le gustó)
Dos secciones nuevas al final del script, justo antes de `initDemo();refreshTitle();`, después de la de la v18:
- **Relieve de los bloques (`blockWall`):** reemplaza `stoneTex` solo para las paredes (128 px). Hileras de alto variable y piedras de ancho variable (la textura empalma a lo ancho), esquinas gastadas con radio distinto en cada esquina, bordes que ondulan 1 o 2 píxeles, borde de arriba claro y de abajo oscuro en escalones, juntas hundidas más oscuras debajo y a la izquierda de cada piedra, grietas en algunas piedras y desportillados en los bordes. Usa la misma paleta de 9 tonos por piso. Piso y techo no cambiaron.
- **Luces (`buildLM`):** mapa de luz de 4×4 muestras por casillero, que se arma una vez por piso (`ensure`, `lightRebuild`). Fuentes: cada cara de pared con antorcha (luz cálida, alcance 2,25 casilleros) y las decoraciones que brillan (lava, respiradero, cabeza de demonio, runas, velas, hongos), cada una con su color. La luz se redondea en quintos (escalones, sin degradé) y las paredes la tapan (`los`).
  - `castFloor`: piso y techo suman la luz de antorcha a la de siempre (`mix`, con `GAIN` 0,8 y tope que conserva el tono cálido). Fuera del alcance de las antorchas todo queda un 16 % más oscuro (`AMB`). Hay una franja de sombra al pie de las paredes, en dos escalones.
  - `frontFace` (8 franjas) y `sideFace` (columna por columna) usan `shade`: oscurecen como antes y agregan la luz de antorcha con `soft-light` y un poco de `screen`.
  - `getSprite` / `drawSprite`: los monstruos se oscurecen por escalón según la luz del lugar, se tiñen cálidos cerca de una antorcha, y los píxeles muy brillantes y saturados (ojos, brasas) no se oscurecen (`emissive`).
- Rendimiento medido: unos 7 ms por cuadro.

### Lo que se probó y NO le gustó (no repetir)
- **Paquetes de arte ya hechos** (se probó Tyler Warren RPG Battlers, los 30 gratis, dentro del juego): prefirió los dibujos propios. Son arte pintado, no pixel art, y casi todos tienen estilo de RPG japonés simpático.
- Luz que cambiaba el color base de la piedra (tinte frío general y multiplicar por naranja): las paredes quedaban grises o como un filtro sepia. La versión final suma la luz de antorcha encima de la luz de siempre.
- Versión "con más detalle" de los monstruos (más píxeles por monstruo, lobo de perfil). Prefirió la primera: pocos píxeles, bloques gruesos y el lobo de frente.
- Monstruos "pintados" con óvalos y tubos sombreados en 8 tonos, con texturas y tramado: **demasiado redondeados, como de plastilina**.
- Monstruos con planos de color angulosos ("low poly"): se ven planos.
- Antes (v9 a v14): pasillo con bloques grandes con esqueleto más grande, y monstruos con volumen, luz por píxel y tramado.
- Bloques de pared con abombado ovalado en el centro: se veía raro, se sacó.
- Nivel "pintado a mano" tipo Eye of the Beholder: no se puede generar con código. La alternativa sería arte hecho por personas (ilustrador).

## Qué cambió en la v18: monstruos en pixel art grueso (le gustó)
- **`pixArt(kind)`:** toma el dibujo original de `spriteArt` (rectángulos y elipses) y lo rasteriza en una grilla chica, sin suavizado (40 píxeles por unidad). Cada color se pinta con 4 tonos en bloques según su posición en la mancha (`band`, luz a la izquierda y arriba), con contorno negro de 1 píxel (`edge`). Los detalles de hasta 2 píxeles no cortan las bandas (`gap`).
- **Colores con transparencia** (brillos y auras): se pintan solo encima del cuerpo, salvo en los etéreos (`cube`, `wisp`, `specter`, `banshee`, `shadow`), que no llevan contorno.
- **`HAND`:** goblin, esqueleto, lobo y ogro dibujados a mano píxel a píxel (`handArt`).
- **`OVR`:** dibujos rehechos del fuego fatuo y el cieno gris.
- `makeSprite` usa `HAND` o `pixArt` para los monstruos; el resto sigue igual. El tamaño en pantalla lo fija `HGT` con `spriteTop`.
- Los retratos del grupo quedaron como estaban (el sombreado automático les hacía rayas).

## Video y publicación en X (hecho)
- Video vertical de 1080×1920 y 33 s, grabado jugando la v18, con música chiptune original compuesta para el video (re menor, final en re mayor). Muestra portada, historia del Cáliz, exploración, combates en tres pisos y el bestiario.
- Texto sugerido para el post, sin nombrar "Dungeons & Dragons".
- Los acortadores de link no ocultan GitHub. La solución fue Netlify.

## Qué cambió en la v17 (respecto de la v16)
- **Tamaños reales de las criaturas:** `HGT` guarda la altura en metros de cada monstruo (o la altura a la que vuela: murciélago, estirge, fuego fatuo, manto oscuro). `monFrac` la pasa a fracción de la pared (2,1 m, con tope de 1,3 para los enormes, que pueden pasar un poco el techo). `drawSprite` mide la altura real de cada dibujo (`spriteTop`) y lo escala para que coincida. Así una rata, un goblin, un humano y un ogro se ven proporcionados. A Chelo le gustó.
- **Vista en alta resolución:** el lienzo mide 720×480 (`VS=3`), pero todo se sigue dibujando en coordenadas de 240×160 con `setTransform`. El piso y el techo se calculan en 240×160 en un lienzo aparte (`fcv`) y se escalan. `getSprite` y `drawSprite` usan el tamaño propio de cada dibujo, así que un sprite puede tener cualquier resolución.
- Las etiquetas de estado y el punto al que apuntan los conjuros usan la altura real del monstruo.

## v16: estilo 90 (le gustó)
Está en dos secciones al final del script, justo antes de `initDemo()`, que reemplazan funciones de dibujo definidas más arriba:
- **Paredes:** bloques tallados grandes con bisel (nuevo `stoneTex` con rampas de 9 tonos), luz por escalones por casillero (`light`), sin sombreado suave (`getAO` vacío) y contorno negro en cada cara de pared (`frontFace`, `sideFace`). El piso y el techo usan la misma luz por escalones (`castFloor`).
- **Paletas** (`PALS`): ocre, azul pizarra, verde musgo, azul verdoso y rojo ladrillo. A los dibujos de monstruos se les agrega contorno y líneas internas (`makeSprite`), y hay un marco de piedra tipo mármol en la vista y en las tarjetas del grupo (`marble`).
- **Decoraciones por ambiente:** `DEC` define 5 por estilo de piso, dibujadas con `deco90`, más antorchas; aparecen en cerca del 40 % de las paredes.
  - Catacumbas: nicho, osario, velas, lápida, telarañas.
  - Castillo: tapiz, cuadro, escudo con espadas, estandarte, cadenas.
  - Musgo: enredaderas, telaraña con araña, raíces, hongos.
  - Salas anegadas: desagüe, algas, caño que gotea, algas colgantes, cadenas.
  - Fragua: lava, horno, herramientas, cabeza de demonio, runas.
- Los botones, el cuadro de mensajes y la brújula todavía tienen el estilo madera anterior.

## v15: vitrina del mercader, bóvedas y acertijos
- **Vitrina de tesoros:** el mercader muestra 3 objetos (raro, muy raro y a veces legendario) de `CAT` con `tr:1`, elegidos con `trPick`. Se puede dejar una **seña** del 20 % para que guarde uno (`flags.res`), que se devuelve al terminar la aventura. Hay 29 tesoros (espada vorpalina, vengadora sagrada, túnica del archimago, manuales +2, cinturones de gigante, etc.) y dos casilleros nuevos: Cabeza y Cinturón. Los efectos están en `getAttack`, `attackRoll`, `acFor`, `effStats`, `spellDC`, `spAtkB`, `saveHalf`, `hurtMember`, `thiefB` y `perception`.
- **Bóvedas** (`addVault`): sala sin otra salida con un cofre de bóveda. Hay tres tipos de puerta: `4` con llave, `5` rostro con adivinanza y `6` reja de palancas.
- **Desafíos:** adivinanzas (`RIDDLES`), palancas con pistas lógicas de solución única (`leverPuzzle`) y tres cofres donde una placa dice cuántas inscripciones mienten (`triadPuzzle`). En cada desafío se puede "Pensar" con INT (`think`). Las ventanas usan `pzShow` / `pzClose` con la fase `puzzle`.
- Hay dos cofres comunes por piso.

## Juego base (hasta v14)
- Tres aventuras de 5 pisos más el modo Sin fin (`CAMPS`). Cada una tiene rescate en el piso 3, dos finales y escalado por nivel (`scaleFor`):
  - El Cáliz del Alba: nivel 1, `tier` 0.
  - La Mina de Hierronegro: nivel 5, `tier` 3.
  - El Rey bajo el Túmulo: nivel 7, `tier` 5.
- **Salón de héroes:** hasta 8 grupos guardados, que se pueden llevar a la próxima aventura.
- Nivel máximo 8. Los caídos solo vuelven con un Pergamino de Revivificar o con el conjuro Revivificar.
- Cada aventura tiene su plantel de monstruos (`MON`); el mimic aparece en todas.
- Pendiente opcional: poderes especiales de los monstruos nuevos (parálisis del chuul, óxido que arruina armaduras, etc.).

## Pendientes
- Juego aparte con vista desde arriba (ver arriba), en un chat nuevo.
- Publicar la v19 en Netlify y el post en X.
- Botones, mensajes y brújula al estilo piedra, si le gusta.
- Botón "Mandar opinión" en la portada.
- Destellos de luz de los conjuros (una Descarga de Fuego que ilumine el pasillo) y luz propia del grupo al caminar: ideas ofrecidas, no pedidas todavía.
- Poderes especiales de los monstruos nuevos (parálisis del chuul, óxido que arruina armaduras, etc.), opcional.
- Play Store (consultado, no empezado): PWABuilder, cuenta de USD 25, prueba cerrada con 12 testers durante 14 días y `assetlinks.json` en `.well-known`.

## Cómo está armado el código (funciones clave)
- **Datos:** `MON`, `CL`, `SP`, `BG`, `SPL`, `CAT`, `DIFF`, `CAMPS`, `RIDDLES`, `SYMS`, `HGT`.
- **Flujo:** `startGame`, `continueGame`, `genFloor`, `genMap`, `addVault`, `descend`, `openShop` / `renderShop`, `finalChoice`, `ending`, `toTitle`.
- **Combate:** `memberAttack`, `attackRoll`, `castSpell`, `useAbility`, `monAttack`, `hurtMember`, `killMon`, `levelUp`.
- **Dibujo:** `drawView`, `castFloor`, `buildTextures`, `stoneTex`, `deco90`, `doorTex`, `riddleTex`, `gateTex`, `spriteArt` / `makeSprite` / `pixArt` / `handArt` / `getSprite` / `drawSprite`, `blockWall` (paredes con relieve), `buildLM` / `mix` / `shade` (luces), `drawMap` y `drawPortrait` (retratos de 32×32).

## Cómo probarlo sin teléfono
Hay un Chromium en `/opt/pw-browsers/chromium-1194/chrome-linux/chrome` que se usa con Playwright de Python. Las fuentes se bajan de `raw.githubusercontent.com/google/fonts` y se inyectan interceptando `fonts.googleapis.com` y `fonts.gstatic.com`.

Para ver monstruos lado a lado:
1. Llamar a `startGame()`.
2. Generar un piso.
3. Ubicar al grupo en una sala.
4. Usar `spawn(clave, x, y)` en las casillas que da `cellAt(distancia, carril)`.
5. Reemplazar `update` por una función vacía para que no se muevan.
6. Sacar la captura de `#view`.
