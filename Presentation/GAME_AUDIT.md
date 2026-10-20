# TURBO B BOY GAME — TECHNICAL GAME AUDIT
**Prepared for Afro-Asian Forum 2026, Aswan, Egypt**  
**Presentation Team:** Ali Mahrous (علي محروس) & Romana Ahmed (رمانة أحمد)  
**Development Team:** 4 Teenagers (Ali Mahrous, Jomana/Romana Ahmad, Yousef Hussein, Yousef Sheta — ~15 years old)  
**Audit Date:** October 2026  
**Audited Directory:** `m:\Techno\Turpo`

---

## 1. Executive Summary & Purpose

**Turbo B Boy Game** (also branded as **Turbo**) is a 2D top-down traffic safety and road-sign educational arcade game developed by four Egyptian teenagers (~15 years old) from Kafr El Sheikh. 

The game was conceived in response to a real-life incident on Stadium Street in Kafr El Sheikh, where an accident occurred involving a young person unfamiliar with road signage. Rather than delivering dry, textbook-style traffic rules, the team created an interactive, fast-paced vehicle game that reinforces traffic sign knowledge at critical psychological moments (immediately upon collision/game-over and during an integrated interactive quiz).

> **Core Philosophy:** This is an **educational road-sign awareness game**, NOT a driving simulator. It does not train vehicle operation or mechanical driving; it trains teenagers to spot, recognize, and respect international and Egyptian road signs.

---

## 2. Technology Stack & Dependencies

| Layer | Component | Version / Details | Purpose |
| :--- | :--- | :--- | :--- |
| **Language** | Python | 3.12.x / 3.x | Core programming language |
| **Framework** | Pygame | 2.6.1 (SDL 2.28.4) | Hardware surface handling, sound, event loop |
| **Wrapper** | Pygame Zero (`pgzero`) | 1.2+ | Actor system, screen abstraction, game runners |
| **Display Resolution** | 800 × 600 pixels | `pygame.SCALED` | Scalable window with Fullscreen toggle (`F` key) |
| **Packaging / Exe** | PyInstaller | Executable built (`Turpo.exe`, 59.9 MB) | Standalone distribution for Windows PCs without Python |
| **Audio Format** | OGG / WAV / MP3 | Background music and sound effects | Immersive engine, crash, coin, and UI sounds |

---

## 3. Game Screens & Complete Flow Architecture

The game contains **8 distinct screens and modal states**, all verified in the source code:

1. **Start Screen (`start_page.py`):**
   - Features the official game logo (`Actor("icons/logo_game", (400, 270))`).
   - Interactive navigation buttons with warm yellow-gold borders (`#FFD700`, radius 9, width 2): Home, Makers, Quiz, and Car Shop.
   - Prompts: `Press SPACE to Start` and `Press Q or Click Quiz for Traffic Signs Quiz`.
2. **Main Gameplay Screen (`play_page.py`):**
   - 6-lane vertical scrolling highway with parallax scrolling and dynamic alpha-fade transitions between levels.
   - Player vehicle controlled with Left/Right arrow keys.
   - Oncoming randomized traffic obstacles and collectible gold coins.
   - Heads-Up Display (HUD): Score, Level indicator (1–6), High Score, Heart icons (Health), and Coin counter.
   - Controls prompt at the bottom: `P = Pause | F = Fullscreen`.
3. **Pause Screen (`pause_page.py`):**
   - Semi-transparent overlay with golden border.
   - Pause banner (`PAUSED`), resume prompt (`Press P to Resume`).
   - Interactive sound toggle button (`volume` / `mute` icons) with live `ON` / `OFF` indicator.
4. **Game Over & Educational Sign Review (`game_over_page.py`):**
   - Triggered when health reaches 0.
   - Plays `game_over` audio clip.
   - Displays a randomly selected traffic sign from the 20-sign database with full educational text explaining what the sign means and what action the driver must take.
   - Displays final score and total coins earned during the run.
   - Restart prompt: `Press R to Restart`, plus Home and Store navigation buttons.
5. **Traffic Signs Quiz Mode (`questions_page.py`):**
   - Dedicated educational testing screen accessible from the Start menu (`Q` key or Quiz button).
   - Shows sign artwork (130×130 px) and a scenario-based question.
   - 4 multiple-choice options (`A`, `B`, `C`, `D`).
   - Instant visual feedback: Correct turns green (`#00FF00`), Incorrect turns red (`#FF0000`).
   - Rewards: **+1 Gold Coin** deposited directly to player bank for each correct answer.
6. **Car Shop / Skin Store (`store.py`):**
   - 3×3 grid displaying 9 distinct player vehicle models.
   - Displays current coin balance.
   - Real-time status tags: `EQUIPPED` (green), `SELECT` (cyan), or `{price} Coins` (gold/gray).
   - Vehicles persist selection into active gameplay (`hero.image = store.selected_skin`).
7. **Game Makers / Credits Screen (`makers_page.py`):**
   - Dedicated team credit page showcasing cards with actual photographs of the four creators.
   - Gold dividers, yellow labels, and closing thank you message: `Thanks for playing!`.
8. **Window Management:**
   - Fullscreen toggle via `F` key.
   - Universal Home reset via `H` key or home button.

---

## 4. Map & Road Environments (Verified: 6 Roads)

The game features **6 distinct themed road environments**, represented as seamless 800×800 px textures scrolling in a dual-tile wrap system with smooth 0.75-second cross-fade transitions (`ROAD_FADE_DURATION = 0.75`):

| Level | Asset Filename | Visual Theme | Road Boundaries & Lanes |
| :---: | :--- | :--- | :--- |
| **1** | `roads/road_egypt_level5.png` | **Egyptian Highway** (Urban highway with Egyptian markings) | 6 Lanes: `[160, 250, 350, 450, 550, 640]` px |
| **2** | `roads/road_forest_level6.png` | **Forest Canopy Route** (Lush greenery borders) | Left boundary: 145 px, Right boundary: 655 px |
| **3** | `roads/road_snow_level3.png` | **Alpine / Snow Route** (Icy shoulders and winter landscape) | Same 6-lane configuration |
| **4** | `roads/road_night_level4.png` | **Night City Expressway** (Dark asphalt, high-contrast markers) | Same 6-lane configuration |
| **5** | `roads/road_normal_level1.png` | **Standard Asphalt Highway** (Classic intercity highway) | Same 6-lane configuration |
| **6** | `roads/road_desert_level2.png` | **Desert / Safari Highway** (Arid golden sand borders) | Same 6-lane configuration |

*Note on road numbering in code:* While the filenames carry legacy numbering (`level5`, `level6`, etc.), the game progression assigns them strictly from Level 1 to 6 in order as the player progresses.

---

## 5. Traffic Sign System (Verified: Exactly 20 Signs)

The project includes exactly **20 verified road signs** stored in `images/signs/1.png` through `20.png`. They are fully wired into two distinct game subsystems: the **Game Over Educational Moment** (`game_over_page.py`) and the **Interactive Traffic Quiz** (`questions.py` and `answers.py`).

| Sign ID | Graphic File | International / Egyptian Sign Name | Sign Category | In-Game Verified Educational Explanation |
| :---: | :---: | :--- | :--- | :--- |
| **1** | `1.png` | **Road Works Ahead** | Warning | "This sign warns that road construction is taking place. Slow down, follow detours, and watch for workers." |
| **2** | `2.png` | **STOP Sign** | Regulatory / Mandatory | "This sign means you must come to a complete stop. Stop fully, check traffic in all directions, then proceed when safe." |
| **3** | `3.png` | **Slippery Road** | Warning | "This warns that the road surface may be slippery, especially when wet. Reduce speed and avoid sudden braking." |
| **4** | `4.png` | **Falling Rocks** | Warning | "This sign means rocks may fall onto the road from a nearby slope. Drive carefully and do not stop in this area." |
| **5** | `5.png` | **Pedestrian Crossing** | Warning | "This warns that pedestrians may cross the road ahead. Slow down and be ready to stop for pedestrians." |
| **6** | `6.png` | **No Parking** | Prohibitory | "This sign means parking is not allowed in this area. Do not stop or park your vehicle here." |
| **7** | `7.png` | **No Entry** | Prohibitory | "This sign means vehicles are not allowed to enter. Do not drive in this direction." |
| **8** | `8.png` | **Winding Road / Double Bend** | Warning | "This warns of sharp or continuous curves ahead. Slow down and keep full control of your vehicle." |
| **9** | `9.png` | **Speed Hump Ahead** | Warning | "This sign warns of a speed hump on the road. Reduce speed to pass safely and comfortably." |
| **10** | `10.png` | **No Overtaking** | Prohibitory | "This means passing other vehicles is prohibited. Stay in your lane and do not overtake." |
| **11** | `11.png` | **No Left Turn** | Prohibitory | "This sign means turning left is not allowed. Continue straight or follow the permitted direction." |
| **12** | `12.png` | **Steep Hill Downwards** | Warning | "This warns of a steep uphill or downhill road. Slow down and use the correct gear to control your vehicle." |
| **13** | `13.png` | **Road Workers on Shoulder** | Warning | "This indicates workers are present on or near the road. Reduce speed and follow warning signs or signals." |
| **14** | `14.png` | **Roundabout Ahead** | Mandatory / Information | "This warns that a roundabout is coming up. Slow down and give way to traffic already in the roundabout." |
| **15** | `15.png` | **Uneven / Rough Road** | Warning | "This sign means the road surface is uneven or bumpy. Reduce speed to avoid losing control or damaging your vehicle." |
| **16** | `16.png` | **Priority to Oncoming Traffic** | Priority / Regulatory | "This means vehicles coming from the opposite direction have priority. Give way and proceed only when clear." |
| **17** | `17.png` | **Children Crossing (School Zone)** | Warning | "This warns that children may cross the road, often near schools. Slow down and be prepared to stop suddenly." |
| **18** | `18.png` | **Cyclists Ahead** | Warning | "This means bicycles may be crossing or using the road. Watch for cyclists and give them enough space." |
| **19** | `19.png` | **General Danger / Hazard** | Warning | "This sign tells you to reduce your speed. Drive carefully and be alert for hazards ahead." |
| **20** | `20.png` | **Traffic Signals Ahead** | Warning | "This warns that traffic lights are ahead. Prepare to stop and obey the signal lights." |

---

## 6. Numerical Game Mechanics (Verified Values)

All values below were extracted directly from the executable game code (`play_page.py`, `store.py`, `Game.py`):

### A. Health & Damage Mechanics
- **Starting Health:** Exactly **3 Hearts** (`health = 3`).
- **Heart UI:** Displayed in the bottom-left corner at `(40 + i * 40, 570)` with scale `1.5`.
- **Damage Trigger:** Collision between the hero's collision box and any oncoming enemy car (`car.colliderect(hero)`).
- **Health Deduction:** Exactly **-1 Heart** per collision.
- **Invulnerability Period ("Safe Mode"):** Upon collision, player enters safe mode for **60 frames** (~1.0 second at 60 FPS). During safe mode, the car sprite flashes (`timer % 6 < 3`) and cannot take damage.
- **Health Recovery:** **None** during a standard run (no repair kits currently implemented).
- **Failure Condition:** When `health <= 0`, game transitions immediately to `game_over_page.py`.

### B. Speed & Difficulty Scaling
- **Initial Game Speed:** `speed = 3.0` pixels per frame.
- **Hero Steering Speed:** `6.0` pixels per frame horizontally.
- **Enemy Vehicle Speed:** `speed * 0.5` relative downward velocity.
- **Speed Increment Rule:** Every 10 score points (`score % 10 == 0`), speed increases by **+0.3** pixels per frame until reaching the level speed cap.
- **Level Speed Caps:**
  - Level 1: Cap = **7.0**
  - Level 2: Cap = **7.0**
  - Level 3: Cap = **7.0**
  - Level 4: Cap = **9.0**
  - Level 5: Cap = **12.0**
  - Level 6: Cap = **15.0** (Top speed)
- **Enemy Spawn Frequency:** Initial delay = **120 frames** (~2.0 seconds). Every 10 score points, delay decreases by **10 frames** down to a minimum cap of **40 frames** (~0.67 seconds between obstacles).

### C. Scoring System
- **Score Rate:** 1 point awarded every **30 frames** (~0.5 seconds of survival time).
- **Level Up Calculation:** `level = min((score // 30) + 1, 6)`.
  - Level 1: 0–29 points
  - Level 2: 30–59 points
  - Level 3: 60–89 points
  - Level 4: 90–119 points
  - Level 5: 120–149 points
  - Level 6: 150+ points
- **High Score:** Persists during the application session (`high_score = max(high_score, play_page.score)`).

### D. Coin Economy & Vehicle Store
- **Coin Spawning in Game:** One coin spawns every **140 frames** (~2.33 seconds) in an unobstructed lane.
- **Coin Collection:** Touching a coin awards **+1 Coin** and plays `sounds.coin_collect.play()`.
- **Quiz Reward:** Answering any traffic sign question correctly awards **+1 Coin**.
- **The Car Store (9 Vehicles Verified):**

| Vehicle Name | Asset Key | Verified Price | Description / Role |
| :--- | :--- | :---: | :--- |
| **Red Racer** | `cars/car_red` | **0 Coins** | Starting vehicle (equipped by default) |
| **Beach Buggy** | `skins/beachbugyy` | **5 Coins** | Off-road coastal buggy |
| **Super Ferrari** | `skins/ferrari` | **10 Coins** | Exotic Italian supercar |
| **Formula 1** | `skins/formula1` | **15 Coins** | Open-wheel high-downforce racer |
| **Tough Pickup** | `skins/pickup` | **20 Coins** | Heavy-duty utility truck |
| **Speed Moto** | `skins/motocycle` | **25 Coins** | Two-wheeled agile motorbike |
| **Glassy Car** | `skins/glassycar` | **30 Coins** | Futuristic transparent concept vehicle |
| **Diamond Car** | `skins/diamound` | **40 Coins** | Luxury crystalline show car |
| **Golden Car** | `skins/golden_car` | **50 Coins** | Ultimate prestige prize car |

---

## 7. Controls & User Experience

| Key / Control | Screen / Mode | Functionality |
| :---: | :---: | :--- |
| **SPACE** | Start Screen | Launches gameplay session |
| **Left Arrow (←)** | In-Game | Steers vehicle left (clamped to road shoulder at x=145) |
| **Right Arrow (→)** | In-Game | Steers vehicle right (clamped to road shoulder at x=655) |
| **P / ESC** | In-Game | Toggles Pause modal overlay & pauses/unpauses music |
| **F** | Universal | Toggles Fullscreen display mode (`pygame.display.toggle_fullscreen()`) |
| **H** | Universal | Resets session and returns to Home / Start Screen |
| **Q** | Start Screen | Toggles Traffic Signs Quiz mode |
| **R** | Game Over | Restarts gameplay session immediately |
| **Mouse Left Click** | Menus / Store / Quiz | Selects options, buys cars, toggles volume, answers quiz |

---

## 8. Implemented Features vs. Planned / Future Features

### Implemented Features (Verified in Codebase):
- 6 dynamically transitioning road environments with smooth alpha cross-fading.
- Exact 20 traffic signs with complete English educational descriptions.
- Game Over sign review mechanic to capture attention after failure.
- Interactive 4-choice traffic quiz mode rewarding coins.
- 9 purchasable vehicles in the Car Shop with active persistence in gameplay.
- 3-heart health system with collision detection, invulnerability safe frames, and sound effects.
- Progressive speed scaling and obstacle spawn tightening across 6 levels.
- Full audio system with game music, game over fanfare, coin chimes, and mute toggle.
- Standalone Windows packaging (`Turpo.exe`) built via PyInstaller.

### Planned Features (Explicitly Documented in Q&A / Roadmap):
- **Mobile Edition (Android / Google Play):** Touch screen controls, APK build for budget smartphones.
- **Expanded Sign Library:** Expansion from 20 signs to 50+ signs covering more rural and international codes.
- **5-Second Rapid In-Game Quiz:** Timed challenge appearing during gameplay rather than only in a standalone menu.
- **Two-Player Split-Screen / Multiplayer Mode:** Allowing friends in youth clubs to compete side-by-side.
- **Institutional Driver-School Portal:** Custom curriculum modules for driving schools and secondary school road-safety programs.

---

## 9. Limitations & Code Uncertainties

1. **Persistent Storage:** Coins, owned vehicles, and high scores reset when closing the game application because file-based saving (e.g., JSON or SQLite) is not currently implemented in `Game.py`.
2. **Pygame Scaled Behavior:** The game runs at a fixed 800×600 resolution and scales up with black letterboxing when toggled to fullscreen on widescreen monitors.
3. **Presenter Names in Code vs. Presentation:**
   - In code: `Jomana Ahmad.png` (`Jomana Ahmad`).
   - In presentation prompt and Arabic Q&A: Romana Ahmed (رمانة أحمد) / Jomana Ahmad. Both names refer to the same presenter; the presentation respects Romana / Jomana Ahmed with her genuine photograph from `images/makers/Jomana Ahmad.png`.

---

*End of Technical Game Audit. Approved for use in Afro-Asian Forum 2026 Presentation.*
