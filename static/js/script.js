/* ============================================================
   CRMS — script.js
   Animations, Interactions, Live UI Logic
   ============================================================ */

"use strict";

/* ============================================================
   1. LIVE CLOCK
   ============================================================ */
function updateClock() {
  const el = document.getElementById('liveClock');
  if (!el) return;
  const now = new Date();
  const h = String(now.getHours()).padStart(2, '0');
  const m = String(now.getMinutes()).padStart(2, '0');
  const s = String(now.getSeconds()).padStart(2, '0');
  el.textContent = `${h}:${m}:${s}`;
}

/* ============================================================
   2. ANIMATED COUNTER
   ============================================================ */
function animateCounter(el, target, duration = 1200) {
  const start = performance.now();
  const startVal = 0;
  function update(ts) {
    const elapsed = ts - start;
    const progress = Math.min(elapsed / duration, 1);
    // Ease out cubic
    const eased = 1 - Math.pow(1 - progress, 3);
    const current = Math.round(startVal + (target - startVal) * eased);
    el.textContent = current;
    if (progress < 1) requestAnimationFrame(update);
    else el.textContent = target;
  }
  requestAnimationFrame(update);
}

function initCounters() {
  const counters = document.querySelectorAll('[data-count]');
  if (!counters.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = parseInt(el.getAttribute('data-count'), 10);
        if (!isNaN(target)) {
          animateCounter(el, target);
        }
        observer.unobserve(el);
      }
    });
  }, { threshold: 0.3 });

  counters.forEach(el => observer.observe(el));
}

/* ============================================================
   3. SCROLL FADE-IN ANIMATIONS
   ============================================================ */
function initScrollAnimations() {
  const els = document.querySelectorAll('.anim-fade-up');
  if (!els.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        // Stagger based on position
        const delay = (entry.target.dataset.delay || 0) * 120;
        setTimeout(() => {
          entry.target.classList.add('visible');
        }, delay);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });

  // Add stagger delays
  els.forEach((el, i) => {
    el.dataset.delay = i;
    observer.observe(el);
  });
}

/* ============================================================
   4. PARTICLE CANVAS (Landing Page)
   ============================================================ */
function initParticleCanvas() {
  const canvas = document.getElementById('particle-canvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  let W, H, particles = [];

  function resize() {
    W = canvas.width  = window.innerWidth;
    H = canvas.height = window.innerHeight;
  }

  function Particle() {
    this.x = Math.random() * W;
    this.y = Math.random() * H;
    this.vx = (Math.random() - 0.5) * 0.3;
    this.vy = (Math.random() - 0.5) * 0.3;
    this.r  = Math.random() * 1.5 + 0.5;
    this.alpha = Math.random() * 0.5 + 0.1;
  }

  function initParticles() {
    particles = [];
    const count = Math.floor(W * H / 8000);
    for (let i = 0; i < Math.min(count, 120); i++) {
      particles.push(new Particle());
    }
  }

  function drawConnections() {
    const maxDist = 120;
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < maxDist) {
          const alpha = (1 - dist / maxDist) * 0.12;
          ctx.beginPath();
          ctx.strokeStyle = `rgba(59, 130, 246, ${alpha})`;
          ctx.lineWidth = 0.8;
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.stroke();
        }
      }
    }
  }

  function animate() {
    ctx.clearRect(0, 0, W, H);
    particles.forEach(p => {
      p.x += p.vx;
      p.y += p.vy;
      if (p.x < 0) p.x = W;
      if (p.x > W) p.x = 0;
      if (p.y < 0) p.y = H;
      if (p.y > H) p.y = 0;

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(147, 197, 253, ${p.alpha})`;
      ctx.fill();
    });
    drawConnections();
    requestAnimationFrame(animate);
  }

  resize();
  initParticles();
  animate();
  window.addEventListener('resize', () => { resize(); initParticles(); });
}

/* ============================================================
   5. TYPEWRITER EFFECT
   ============================================================ */
function initTypewriter() {
  const el = document.getElementById('typewriter');
  if (!el) return;

  const text = el.getAttribute('data-text') || el.textContent;
  el.textContent = '';
  el.setAttribute('aria-label', text);

  let i = 0;
  const cursor = document.createElement('span');
  cursor.className = 'typewriter-cursor';
  cursor.textContent = '|';
  cursor.style.cssText = 'color: var(--blue-400); animation: blink 1s step-end infinite;';
  el.parentNode.insertBefore(cursor, el.nextSibling);

  // Add blink keyframes
  if (!document.getElementById('twStyle')) {
    const s = document.createElement('style');
    s.id = 'twStyle';
    s.textContent = '@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }';
    document.head.appendChild(s);
  }

  function type() {
    if (i < text.length) {
      el.textContent += text[i++];
      setTimeout(type, 60 + Math.random() * 40);
    } else {
      setTimeout(() => cursor.remove(), 2000);
    }
  }

  setTimeout(type, 500);
}

/* ============================================================
   6. LOGIN ROLE TOGGLE
   ============================================================ */
function initRoleToggle() {
  const tabCitizen = document.getElementById('tabCitizen');
  const tabPolice  = document.getElementById('tabPolice');
  const roleInput  = document.getElementById('roleInput');
  const submitBtn  = document.getElementById('submitBtn');
  const submitText = document.getElementById('submitText');
  const emailInput = document.getElementById('emailInput');
  const emailLabel = document.getElementById('emailLabel');
  const userDemo   = document.getElementById('userDemoSection');
  const policeDemo = document.getElementById('policeDemoSection');

  if (!tabCitizen || !tabPolice) return;

  function setRole(role) {
    if (role === 'user') {
      tabCitizen.className = 'role-tab active-citizen';
      tabPolice.className  = 'role-tab';
      roleInput.value = 'user';
      submitText.textContent = 'Sign In as Citizen';
      submitBtn.className = 'submit-btn submit-btn-citizen';
      emailLabel.textContent = 'Email Address *';
      emailInput.placeholder = 'e.g. walter@gmail.com';
      if (userDemo)   userDemo.style.display = '';
      if (policeDemo) policeDemo.style.display = 'none';
    } else {
      tabCitizen.className = 'role-tab';
      tabPolice.className  = 'role-tab active-police';
      roleInput.value = 'police';
      submitText.textContent = 'Sign In as Officer';
      submitBtn.className = 'submit-btn submit-btn-police';
      emailLabel.textContent = 'Badge ID / Email *';
      emailInput.placeholder = 'e.g. HS002 or officer@police.gov';
      if (userDemo)   userDemo.style.display = 'none';
      if (policeDemo) policeDemo.style.display = '';
    }
  }

  tabCitizen.addEventListener('click', () => setRole('user'));
  tabPolice.addEventListener('click',  () => setRole('police'));
}

/* ============================================================
   7. DEMO BADGE AUTOFILL
   ============================================================ */
function initDemoCards() {
  document.querySelectorAll('.demo-badge-btn').forEach(card => {
    card.addEventListener('click', () => {
      const email    = card.getAttribute('data-email');
      const password = card.getAttribute('data-pass');
      const emailEl  = document.getElementById('emailInput');
      const passEl   = document.getElementById('passwordInput');
      if (emailEl) emailEl.value = email;
      if (passEl)  passEl.value  = password;

      // Flash feedback
      card.style.borderColor = 'rgba(59,130,246,0.5)';
      card.style.background  = 'rgba(59,130,246,0.08)';
      setTimeout(() => {
        card.style.borderColor = '';
        card.style.background  = '';
      }, 800);
    });
  });
}

/* ============================================================
   8. TABLE SEARCH & FILTER
   ============================================================ */
function initTableSearch() {
  const searchInput  = document.getElementById('tableSearchInput');
  const filterSelect = document.getElementById('statusFilterSelect');
  const tableBody    = document.querySelector('.data-table tbody');

  if (!tableBody) return;

  function filterTable() {
    const query  = searchInput  ? searchInput.value.toLowerCase().trim()  : '';
    const status = filterSelect ? filterSelect.value.toLowerCase().trim() : '';
    const rows   = tableBody.querySelectorAll('tr');

    rows.forEach(row => {
      const text = row.textContent.toLowerCase();
      const matchesQuery  = !query  || text.includes(query);
      const matchesStatus = !status || text.includes(status);
      row.style.display = matchesQuery && matchesStatus ? '' : 'none';
    });
  }

  if (searchInput)  searchInput.addEventListener('input',  filterTable);
  if (filterSelect) filterSelect.addEventListener('change', filterTable);
}

/* ============================================================
   9. TIME-BASED GREETING
   ============================================================ */
function initTimeGreeting() {
  const el = document.getElementById('timeGreeting');
  if (!el) return;
  const h = new Date().getHours();
  let greet = 'Welcome Back';
  if (h < 12)       greet = 'Good Morning';
  else if (h < 17)  greet = 'Good Afternoon';
  else if (h < 21)  greet = 'Good Evening';
  else               greet = 'Good Night';
  el.textContent = greet + ' — ' + el.textContent;
}

/* ============================================================
   10. FLASH MESSAGE AUTO-DISMISS
   ============================================================ */
function initFlashMessages() {
  document.querySelectorAll('.alert').forEach(alert => {
    setTimeout(() => {
      alert.style.transition = 'opacity 0.4s, transform 0.4s';
      alert.style.opacity = '0';
      alert.style.transform = 'translateY(-6px)';
      setTimeout(() => alert.remove(), 400);
    }, 5000);
  });
}

/* ============================================================
   11. SMOOTH NAV ACTIVE STATE (for landing page scroll)
   ============================================================ */
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const id = a.getAttribute('href').slice(1);
      const target = document.getElementById(id);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
}

/* ============================================================
   INIT — Run everything on DOM ready
   ============================================================ */
document.addEventListener('DOMContentLoaded', () => {
  initParticleCanvas();
  initTypewriter();
  initCounters();
  initScrollAnimations();
  initRoleToggle();
  initDemoCards();
  initTableSearch();
  initTimeGreeting();
  initFlashMessages();
  initSmoothScroll();

  // Live Clock
  updateClock();
  setInterval(updateClock, 1000);
});
