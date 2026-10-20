/**
 * TURBO GAME — OFFICIAL COMPETITION PRESENTATION SCRIPT
 * Afro-Asian Forum 2026 | Aswan, Egypt
 * Presenters: Ali Mahrous & Jomana Ahmad
 */

// Total verified signs dataset with verified descriptions
const TRAFFIC_SIGNS_DATA = [
  { id: "1", name: "Road Works Ahead", category: "warning", file: "1.png", desc: "This sign warns that road construction is taking place. Slow down, follow detours or instructions, and watch for workers." },
  { id: "2", name: "STOP Sign", category: "regulatory", file: "2.png", desc: "This sign means you must come to a complete stop. Stop fully, check traffic in all directions, then proceed when safe." },
  { id: "3", name: "Slippery Road", category: "warning", file: "3.png", desc: "This warns that the road surface may be slippery, especially when wet. Reduce speed and avoid sudden braking or sharp turns." },
  { id: "4", name: "Falling Rocks", category: "warning", file: "4.png", desc: "This sign means rocks may fall onto the road from a nearby slope. Drive carefully and do not stop in this area." },
  { id: "5", name: "Pedestrian Crossing", category: "warning", file: "5.png", desc: "This warns that pedestrians may cross the road ahead. Slow down and be ready to stop for pedestrians." },
  { id: "6", name: "No Parking", category: "prohibitory", file: "6.png", desc: "This sign means parking is not allowed in this area. Do not stop or park your vehicle here." },
  { id: "7", name: "No Entry", category: "prohibitory", file: "7.png", desc: "This sign means vehicles are not allowed to enter. Do not drive in this direction." },
  { id: "8", name: "Winding Road Ahead", category: "warning", file: "8.png", desc: "This warns of sharp or continuous curves ahead. Slow down and keep full control of your vehicle." },
  { id: "9", name: "Speed Hump Ahead", category: "warning", file: "9.png", desc: "This sign warns of a speed hump on the road. Reduce speed to pass safely and comfortably." },
  { id: "10", name: "No Overtaking", category: "prohibitory", file: "10.png", desc: "This means passing other vehicles is prohibited. Stay in your lane and do not overtake." },
  { id: "11", name: "No Left Turn", category: "prohibitory", file: "11.png", desc: "This sign means turning left is not allowed. Continue straight or follow the permitted direction." },
  { id: "12", name: "Steep Incline / Descent", category: "warning", file: "12.png", desc: "This warns of a steep uphill or downhill road. Slow down and use the correct gear to control your vehicle." },
  { id: "13", name: "Road Maintenance on Shoulder", category: "warning", file: "13.png", desc: "This indicates workers are present on or near the road. Reduce speed and follow warning signs or signals." },
  { id: "14", name: "Roundabout Ahead", category: "regulatory", file: "14.png", desc: "This warns that a roundabout is coming up. Slow down and give way to traffic already in the roundabout." },
  { id: "15", name: "Uneven / Rough Road", category: "warning", file: "15.png", desc: "This sign means the road surface is uneven or bumpy. Reduce speed to avoid losing control or damaging your vehicle." },
  { id: "16", name: "Priority to Oncoming Traffic", category: "regulatory", file: "16.png", desc: "This means vehicles coming from the opposite direction have priority. Give way and proceed only when the road is clear." },
  { id: "17", name: "School Zone / Children", category: "warning", file: "17.png", desc: "This warns that children may cross the road, often near schools. Slow down and be prepared to stop suddenly." },
  { id: "18", name: "Cyclists Ahead", category: "warning", file: "18.png", desc: "This means bicycles may be crossing or using the road. Watch for cyclists and give them enough space." },
  { id: "19", name: "General Danger / Hazard", category: "warning", file: "19.png", desc: "This sign tells you to reduce your speed. Drive carefully and be alert for hazards ahead." },
  { id: "20", name: "Traffic Signals Ahead", category: "warning", file: "20.png", desc: "This warns that traffic lights are ahead. Prepare to stop and obey the signal lights." }
];

document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("presentationContainer");
  const slides = Array.from(document.querySelectorAll(".slide-section"));
  const totalSlides = slides.length;
  
  const slideCounter = document.getElementById("slideCounter");
  const progressBar = document.getElementById("globalProgressBar");
  const prevBtn = document.getElementById("prevSlideBtn");
  const nextBtn = document.getElementById("nextSlideBtn");
  const fullscreenBtn = document.getElementById("fullscreenBtn");
  const jumpMenuBtn = document.getElementById("jumpMenuBtn");
  const jumpModal = document.getElementById("jumpMenuModal");
  const lightboxModal = document.getElementById("lightboxModal");
  const signModal = document.getElementById("signDetailModal");

  let currentSlideIndex = 0;

  // Initialize Right Dot Navigation
  const dotNavContainer = document.getElementById("slideDotNav");
  if (dotNavContainer) {
    dotNavContainer.innerHTML = "";
    slides.forEach((slide, idx) => {
      const dot = document.createElement("div");
      dot.className = `dot-nav-item ${idx === 0 ? "active" : ""}`;
      dot.setAttribute("data-slide", idx);
      
      const title = slide.querySelector(".slide-title")?.innerText || slide.getAttribute("data-title") || `Slide ${idx + 1}`;
      
      const tooltip = document.createElement("span");
      tooltip.className = "dot-tooltip";
      tooltip.textContent = `${String(idx + 1).padStart(2, "0")}. ${title.substring(0, 24)}`;
      
      dot.appendChild(tooltip);
      dot.addEventListener("click", () => goToSlide(idx));
      dotNavContainer.appendChild(dot);
    });
  }

  // Populate Jump Menu
  const jumpGrid = document.getElementById("jumpMenuGrid");
  if (jumpGrid) {
    jumpGrid.innerHTML = "";
    slides.forEach((slide, idx) => {
      const itemBtn = document.createElement("button");
      itemBtn.className = "jump-item-btn";
      const title = slide.querySelector(".slide-title")?.innerText || slide.getAttribute("data-title") || `Slide ${idx + 1}`;
      itemBtn.innerHTML = `
        <span class="jump-item-num">${String(idx + 1).padStart(2, "0")}</span>
        <span>${title}</span>
      `;
      itemBtn.addEventListener("click", () => {
        goToSlide(idx);
        closeModal(jumpModal);
      });
      jumpGrid.appendChild(itemBtn);
    });
  }

  // Navigation Functions
  function updateUI(index) {
    currentSlideIndex = index;
    const formatted = `${String(index + 1).padStart(2, "0")} / ${String(totalSlides).padStart(2, "0")}`;
    if (slideCounter) slideCounter.textContent = formatted;
    
    if (progressBar) {
      const percent = ((index + 1) / totalSlides) * 100;
      progressBar.style.width = `${percent}%`;
    }

    // Update Dots
    const dots = document.querySelectorAll(".dot-nav-item");
    dots.forEach((dot, dIdx) => {
      dot.classList.toggle("active", dIdx === index);
    });
  }

  function goToSlide(index) {
    if (index < 0) index = 0;
    if (index >= totalSlides) index = totalSlides - 1;
    slides[index].scrollIntoView({ behavior: "smooth" });
    updateUI(index);
  }

  function nextSlide() {
    if (currentSlideIndex < totalSlides - 1) {
      goToSlide(currentSlideIndex + 1);
    }
  }

  function prevSlide() {
    if (currentSlideIndex > 0) {
      goToSlide(currentSlideIndex - 1);
    }
  }

  // Expose to window for inline onclick handlers in HTML
  window.goToSlide = goToSlide;
  window.nextSlide = nextSlide;
  window.prevSlide = prevSlide;

  // Event Listeners for Nav Buttons
  if (prevBtn) prevBtn.addEventListener("click", prevSlide);
  if (nextBtn) nextBtn.addEventListener("click", nextSlide);
  
  const bottomPrev = document.getElementById("bottomPrevBtn");
  const bottomNext = document.getElementById("bottomNextBtn");
  const bottomTop = document.getElementById("bottomTopBtn");
  if (bottomPrev) bottomPrev.addEventListener("click", prevSlide);
  if (bottomNext) bottomNext.addEventListener("click", nextSlide);
  if (bottomTop) bottomTop.addEventListener("click", () => goToSlide(0));

  const startCtaBtn = document.getElementById("startPresentationBtn");
  if (startCtaBtn) startCtaBtn.addEventListener("click", () => goToSlide(1));

  // Intersection Observer to sync on manual scroll
  const observerOptions = {
    root: container,
    threshold: 0.55
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const slideIndex = slides.indexOf(entry.target);
        if (slideIndex !== -1 && slideIndex !== currentSlideIndex) {
          updateUI(slideIndex);
          // Pause promo video if user navigated away from its slide
          const promoVideo = document.getElementById("promoVideoPlayer");
          if (promoVideo && !entry.target.contains(promoVideo) && !promoVideo.paused) {
            promoVideo.pause();
            const btnText = document.getElementById("videoPlayBtnText");
            if (btnText) btnText.textContent = "▶ PLAY VIDEO";
          }
        }
      }
    });
  }, observerOptions);

  slides.forEach((slide) => observer.observe(slide));

  // Keyboard Navigation
  document.addEventListener("keydown", (e) => {
    // If modal open, handle ESC to close
    if (e.key === "Escape") {
      closeAllModals();
      return;
    }

    // Ignore if user is typing in an input (if any)
    if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") return;

    switch (e.key) {
      case "ArrowDown":
      case "PageDown":
      case " ":
        e.preventDefault();
        nextSlide();
        break;
      case "ArrowUp":
      case "PageUp":
        e.preventDefault();
        prevSlide();
        break;
      case "Home":
        e.preventDefault();
        goToSlide(0);
        break;
      case "End":
        e.preventDefault();
        goToSlide(totalSlides - 1);
        break;
      case "f":
      case "F":
        toggleFullscreen();
        break;
      case "m":
      case "M":
      case "j":
      case "J":
        openModal(jumpModal);
        break;
    }
  });

  // Fullscreen Toggle
  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(() => {});
      if (fullscreenBtn) fullscreenBtn.textContent = "Exit Fullscreen";
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen().catch(() => {});
        if (fullscreenBtn) fullscreenBtn.textContent = "Fullscreen";
      }
    }
  }

  if (fullscreenBtn) fullscreenBtn.addEventListener("click", toggleFullscreen);
  if (jumpMenuBtn) jumpMenuBtn.addEventListener("click", () => openModal(jumpModal));

  // Modal helpers
  function openModal(modal) {
    if (!modal) return;
    modal.classList.add("open");
    modal.style.display = "flex";
  }

  function closeModal(modal) {
    if (!modal) return;
    modal.classList.remove("open");
    modal.style.display = "none";
  }

  function closeAllModals() {
    document.querySelectorAll(".modal-backdrop").forEach(m => closeModal(m));
  }

  document.querySelectorAll(".modal-close-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const modal = btn.closest(".modal-backdrop");
      closeModal(modal);
    });
  });

  document.querySelectorAll(".modal-backdrop").forEach(backdrop => {
    backdrop.addEventListener("click", (e) => {
      if (e.target === backdrop) closeModal(backdrop);
    });
  });

  // Lightbox for Game Screenshots
  window.openScreenshotLightbox = function(src, caption) {
    const imgElem = document.getElementById("lightboxImg");
    const captionElem = document.getElementById("lightboxCaption");
    if (imgElem) imgElem.src = src;
    if (captionElem) captionElem.textContent = caption || "Turbo Game Gameplay Screenshot";
    openModal(lightboxModal);
  };

  // Build 20 Signs Contact Sheet
  const signsGrid = document.getElementById("signsContactGrid");
  const filterPills = document.querySelectorAll(".filter-pill");

  function renderSigns(category = "all") {
    if (!signsGrid) return;
    signsGrid.innerHTML = "";

    const filtered = category === "all" 
      ? TRAFFIC_SIGNS_DATA 
      : TRAFFIC_SIGNS_DATA.filter(s => s.category === category);

    filtered.forEach(sign => {
      const tile = document.createElement("div");
      tile.className = "sign-tile";
      tile.innerHTML = `
        <div class="sign-tile-id">#${sign.id}</div>
        <img class="sign-tile-img" src="assets/traffic-signs/${sign.file}" alt="${sign.name}" loading="lazy">
        <div class="sign-tile-title">${sign.name}</div>
      `;
      tile.addEventListener("click", () => openSignDetails(sign));
      signsGrid.appendChild(tile);
    });
  }

  filterPills.forEach(pill => {
    pill.addEventListener("click", () => {
      filterPills.forEach(p => p.classList.remove("active"));
      pill.classList.add("active");
      const category = pill.getAttribute("data-category");
      renderSigns(category);
    });
  });

  function openSignDetails(sign) {
    const titleElem = document.getElementById("signDetailTitle");
    const imgElem = document.getElementById("signDetailImg");
    const catElem = document.getElementById("signDetailCategory");
    const descElem = document.getElementById("signDetailDesc");

    if (titleElem) titleElem.textContent = `Sign #${sign.id}: ${sign.name}`;
    if (imgElem) imgElem.src = `assets/traffic-signs/${sign.file}`;
    if (catElem) catElem.textContent = sign.category.toUpperCase();
    if (descElem) descElem.textContent = sign.desc;

    openModal(signModal);
  }

  // Initial render of signs
  renderSigns("all");

  // Interactive Progression / Speed Calculator on Slide 12
  const scoreSlider = document.getElementById("calcScoreSlider");
  const calcScoreVal = document.getElementById("calcScoreVal");
  const calcLevelVal = document.getElementById("calcLevelVal");
  const calcSpeedVal = document.getElementById("calcSpeedVal");
  const calcSpawnVal = document.getElementById("calcSpawnVal");

  if (scoreSlider) {
    scoreSlider.addEventListener("input", (e) => {
      const score = parseInt(e.target.value, 10);
      const level = Math.min(Math.floor(score / 30) + 1, 6);
      
      // Speed math from play_page.py
      let speed = 3.0;
      const step10 = Math.floor(score / 10);
      const maxSpds = { 1: 7.0, 2: 7.0, 3: 7.0, 4: 9.0, 5: 12.0, 6: 15.0 };
      const maxSpd = maxSpds[level] || 7.0;
      speed = Math.min(3.0 + step10 * 0.3, maxSpd);

      // Spawn delay math
      const spawnDelay = Math.max(120 - step10 * 10, 40);

      if (calcScoreVal) calcScoreVal.textContent = score;
      if (calcLevelVal) calcLevelVal.textContent = `Level ${level}`;
      if (calcSpeedVal) calcSpeedVal.textContent = `${speed.toFixed(1)} px/f`;
      if (calcSpawnVal) calcSpawnVal.textContent = `${spawnDelay} frames (~${(spawnDelay/60).toFixed(2)}s)`;
    });
  }

  // Promo Video Global Helper Functions
  window.togglePlayPromoVideo = function() {
    const video = document.getElementById("promoVideoPlayer");
    const btnText = document.getElementById("videoPlayBtnText");
    if (!video) return;
    if (video.paused) {
      video.play().then(() => {
        if (btnText) btnText.textContent = "⏸ PAUSE VIDEO";
      }).catch(err => {
        console.warn("Video playback prevented:", err);
      });
    } else {
      video.pause();
      if (btnText) btnText.textContent = "▶ PLAY VIDEO";
    }
  };

  window.toggleFullscreenPromoVideo = function() {
    const video = document.getElementById("promoVideoPlayer");
    if (!video) return;
    if (video.requestFullscreen) {
      video.requestFullscreen();
    } else if (video.webkitRequestFullscreen) {
      video.webkitRequestFullscreen();
    }
  };
});
