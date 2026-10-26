# Turbo B Boy Game — Competition Presentation Website
**Event:** Afro-Asian Youth Forum 2026 (منتدى الشباب الأفرو-آسيوي) | Aswan, Egypt  
**Presenters:** Ali Mahrous (علي محروس) & Romana Ahmed (رمانة أحمد)  
**Engineering Team:** 4 Teenagers (Ali Mahrous, Jomana/Romana Ahmad, Yousef Hussein, Yousef Sheta — ~15 years old)  
**Location:** Kafr El Sheikh, Egypt  

---

## 🚀 How to Open and Present Locally

This presentation is built with pure, modern **HTML5, CSS3, and vanilla JavaScript**. It requires no Node.js, npm, webpack, or backend servers.

### Option 1: Direct File Launch (Quickest)
Double-click `index.html` or right-click `index.html` → **Open with** → **Google Chrome / Microsoft Edge / Firefox**.

### Option 2: Local HTTP Server (Recommended for Competition Projectors)
Using Python's built-in lightweight HTTP server ensures seamless font and asset caching:
```bash
# In terminal, navigate to the presentation folder:
cd m:\Techno\Turpo\turbo_b_boy_presentation

# Launch the server:
python -m http.server 8080
```
Then open your browser and navigate to:
**`http://localhost:8080`**

---

## ⌨️ Presentation Keyboard Controls & Shortcuts

| Key | Action |
| :---: | :--- |
| **↓ / Page Down / Space** | Advance to Next Slide |
| **↑ / Page Up** | Return to Previous Slide |
| **Home** | Jump to Slide 1 (Cover) |
| **End** | Jump to Slide 20 (Closing Pitch) |
| **F** | Toggle Fullscreen (Presentation Mode) |
| **M / J** | Open Slide Jump Menu / Table of Contents |
| **ESC** | Close any open modal / Lightbox / Jump menu |
| **Mouse Wheel / Trackpad** | Smooth snap-scrolling between slides |

---

## 📂 Project Structure

```
turbo_b_boy_presentation/
├── index.html                     # Complete 20-slide competition pitch (Simple English + Multilingual Welcome)
├── styles.css                     # Road-inspired glassmorphism design system
├── script.js                      # Navigation, keyboard shortcuts, contact sheet, math simulator
├── PRESENTATION_SPEECH_GUIDE.md   # Slide-by-slide simple English speaker cue card guide
├── GAME_AUDIT.md                  # Full technical audit of the Python/Pygame game
├── README.md                      # This presentation guide
└── assets/
    ├── screenshots/      # 12 Genuine in-game captures rendered directly from Pygame
    │   ├── main-menu.png
    │   ├── gameplay.png
    │   ├── gameplay-snow.png
    │   ├── gameplay-night.png
    │   ├── gameplay-desert.png
    │   ├── traffic-signs.png
    │   ├── traffic-quiz.png
    │   ├── car-shop.png
    │   ├── makers-screen.png
    │   ├── pause-screen.png
    │   └── health-collision.png
    ├── team/             # Verified real photos of the 4 teenagers
    │   ├── ali-mahrous.jpeg
    │   ├── romana-ahmed.png
    │   ├── yousef-hussein.jpg
    │   └── yousef-sheta.jpeg
    ├── traffic-signs/    # All 20 verified in-game road sign graphics (1.png to 20.png)
    ├── game-images/      # Verified roads, cars, skins, and icon assets
    └── logos/            # Official game logo, team logo, and game icon
```

---

## 🖼️ How to Update Team Photographs

All photographs are stored in `assets/team/`:
- `ali-mahrous.jpeg`: Ali Mahrous (Presenter)
- `romana-ahmed.png`: Romana / Jomana Ahmed (Presenter)
- `yousef-hussein.jpg`: Yousef Hussein (Developer)
- `yousef-sheta.jpeg`: Yousef Sheta (Developer)

To replace or update any team photograph, simply save the new image into `assets/team/` under the corresponding filename (or update the `src` attribute in `index.html` lines 68–120).

---

## 🌟 Key Presentation Features for Judges

1. **Exact 20 Signs Interactive Contact Sheet (Slide 8):** Filter by category (Warning, Prohibitory, Regulatory/Info) and click any sign to display its exact in-game safety explanation.
2. **Interactive Progression Math Simulator (Slide 12):** Drag the score slider to demonstrate the real algorithms behind speed caps and spawn interval tightening.
3. **Screenshot Lightbox (Slide 6):** Click on any gameplay thumbnail or main interface view to inspect high-resolution annotated details.
4. **Verified Gameplay Authenticity:** Every claim, number, and image reflects the actual running game code in `Game.py`.

*Best of luck to Ali Mahrous and Romana Ahmed at the Afro-Asian Forum 2026 in Aswan!*
