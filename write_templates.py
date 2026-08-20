
import os

BASE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(BASE, 'templates')
S = os.path.join(BASE, 'static')

def w(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Written: {path}")

# ============================================================
# CSS
# ============================================================
css = r"""
/* =========================================================
   VOID TERMINAL — CRMS Design System
   Theme: Obsidian Black + Electric Cyan + Amber Gold
   ========================================================= */

@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&family=Syne:wght@700;800&display=swap');

/* ── CSS Variables ── */
:root {
  --void: #05050a;
  --abyss: #08080f;
  --surface: #0e0e1a;
  --surface-2: #141422;
  --surface-3: #1c1c2e;
  --border: rgba(99, 215, 255, 0.12);
  --border-bright: rgba(99, 215, 255, 0.28);
  --cyan: #3de8ff;
  --cyan-dim: #1db8d8;
  --cyan-glow: rgba(61, 232, 255, 0.18);
  --cyan-glow-strong: rgba(61, 232, 255, 0.35);
  --amber: #ffb800;
  --amber-dim: #cc9200;
  --amber-glow: rgba(255, 184, 0, 0.2);
  --rose: #ff4466;
  --rose-glow: rgba(255, 68, 102, 0.2);
  --emerald: #00e5a0;
  --emerald-glow: rgba(0, 229, 160, 0.2);
  --violet: #a855f7;
  --text-primary: #e8eaf6;
  --text-secondary: #8b93b8;
  --text-muted: #525878;
  --font-main: 'Space Grotesk', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --font-display: 'Syne', sans-serif;
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-xl: 24px;
  --sidebar-w: 240px;
  --header-h: 60px;
  --transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: 16px; scroll-behavior: smooth; }
body {
  font-family: var(--font-main);
  background: var(--void);
  color: var(--text-primary);
  min-height: 100vh;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}
a { color: inherit; text-decoration: none; }
button { cursor: pointer; font-family: inherit; }
input, textarea, select { font-family: inherit; }

::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--abyss); }
::-webkit-scrollbar-thumb { background: var(--border-bright); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--cyan-dim); }

/* =========================================================  LANDING  ========================================================= */
.landing-root { min-height: 100vh; background: var(--void); position: relative; overflow: hidden; }

.grid-canvas {
  position: fixed; inset: 0; z-index: 0;
  background-image: linear-gradient(rgba(61,232,255,0.04) 1px, transparent 1px), linear-gradient(90deg,rgba(61,232,255,0.04) 1px, transparent 1px);
  background-size: 48px 48px;
  animation: gridDrift 20s linear infinite;
}
@keyframes gridDrift { 0%{transform:translate(0,0)} 100%{transform:translate(48px,48px)} }

.scanlines {
  position: fixed; inset: 0; z-index: 0; pointer-events: none;
  background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.1) 2px, rgba(0,0,0,0.1) 4px);
}

.orb { position: fixed; border-radius: 50%; filter: blur(100px); opacity: 0.15; pointer-events: none; z-index: 0; animation: orbFloat 12s ease-in-out infinite alternate; }
.orb-1 { width: 600px; height: 600px; background: var(--cyan); top: -200px; left: -200px; animation-duration: 14s; }
.orb-2 { width: 500px; height: 500px; background: var(--amber); bottom: -150px; right: -150px; animation-duration: 18s; }
.orb-3 { width: 400px; height: 400px; background: var(--violet); top: 40%; left: 50%; animation-duration: 22s; }
@keyframes orbFloat { 0%{transform:translate(0,0) scale(1)} 100%{transform:translate(40px,40px) scale(1.08)} }

@keyframes blinkPulse { 0%,100%{opacity:1} 50%{opacity:0.2} }

.l-nav {
  position: fixed; top:0; left:0; right:0; z-index:100;
  display:flex; align-items:center; justify-content:space-between;
  padding: 0 3rem; height: 70px;
  background: rgba(5,5,10,0.75); backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
}
.l-nav-logo { display:flex; align-items:center; gap:12px; }
.logo-mark {
  width:38px; height:38px;
  background: linear-gradient(135deg, var(--cyan), var(--cyan-dim));
  border-radius: 8px; display:flex; align-items:center; justify-content:center;
  font-family: var(--font-mono); font-size:0.75rem; font-weight:700; color:var(--void);
  box-shadow: 0 0 20px var(--cyan-glow-strong);
}
.logo-text { font-family:var(--font-display); font-size:1rem; font-weight:700; color:var(--text-primary); }
.logo-text span { color:var(--cyan); }
.l-nav-right { display:flex; align-items:center; gap:1rem; }
.l-nav-link { font-size:0.85rem; color:var(--text-secondary); transition:var(--transition); padding:6px 12px; border-radius:var(--radius-sm); }
.l-nav-link:hover { color:var(--cyan); background:var(--cyan-glow); }
.l-nav-cta {
  font-size:0.85rem; font-weight:600; padding:8px 20px; border-radius:var(--radius-sm);
  background:transparent; border:1px solid var(--border-bright); color:var(--cyan); transition:var(--transition);
}
.l-nav-cta:hover { background:var(--cyan-glow); box-shadow:0 0 20px var(--cyan-glow-strong); }

.l-hero {
  position:relative; z-index:1; min-height:100vh;
  display:flex; flex-direction:column; align-items:center; justify-content:center;
  text-align:center; padding:100px 2rem 4rem;
}
.hero-eyebrow {
  display:inline-flex; align-items:center; gap:8px;
  font-family:var(--font-mono); font-size:0.72rem; color:var(--cyan);
  letter-spacing:2px; text-transform:uppercase;
  border:1px solid var(--border-bright); background:rgba(61,232,255,0.06);
  padding:6px 16px; border-radius:100px; margin-bottom:2rem;
}
.hero-eyebrow-dot { width:6px; height:6px; background:var(--cyan); border-radius:50%; animation:blinkPulse 1.5s ease-in-out infinite; }

.l-hero-title {
  font-family:var(--font-display); font-size:clamp(3rem,7vw,5.5rem); font-weight:800;
  line-height:1.05; color:var(--text-primary); margin-bottom:1.5rem; letter-spacing:-1px;
}
.l-hero-title .t-cyan { background:linear-gradient(90deg,var(--cyan),#68e7ff); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; }
.l-hero-title .t-amber { background:linear-gradient(90deg,var(--amber),#ffd060); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; }

.l-hero-sub { font-size:1.05rem; color:var(--text-secondary); max-width:560px; line-height:1.7; margin-bottom:3rem; }

.hero-ctas { display:flex; gap:1rem; justify-content:center; flex-wrap:wrap; }

.btn-portal {
  display:inline-flex; align-items:center; gap:10px; padding:14px 32px;
  font-size:0.95rem; font-weight:600; border-radius:var(--radius-md);
  background:linear-gradient(135deg,var(--cyan),var(--cyan-dim)); color:var(--void); border:none;
  box-shadow:0 0 40px rgba(61,232,255,0.3),0 4px 20px rgba(0,0,0,0.5);
  transition:var(--transition); position:relative; overflow:hidden;
}
.btn-portal:hover { transform:translateY(-2px); box-shadow:0 0 60px rgba(61,232,255,0.4),0 8px 30px rgba(0,0,0,0.5); }

.btn-portal-ghost {
  display:inline-flex; align-items:center; gap:10px; padding:14px 32px;
  font-size:0.95rem; font-weight:600; border-radius:var(--radius-md);
  background:transparent; color:var(--amber); border:1px solid rgba(255,184,0,0.35); transition:var(--transition);
}
.btn-portal-ghost:hover { background:var(--amber-glow); border-color:var(--amber); box-shadow:0 0 30px var(--amber-glow); transform:translateY(-2px); }

.hero-stats {
  display:flex; gap:2px; justify-content:center; margin-top:4rem;
  background:rgba(255,255,255,0.03); border:1px solid var(--border); border-radius:var(--radius-lg);
  padding:6px; flex-wrap:wrap;
}
.hero-stat { flex:1; min-width:120px; display:flex; flex-direction:column; align-items:center; padding:1.2rem 1.5rem; border-radius:var(--radius-md); transition:var(--transition); }
.hero-stat:hover { background:rgba(61,232,255,0.06); }
.hero-stat-val { font-family:var(--font-mono); font-size:1.8rem; font-weight:700; color:var(--cyan); line-height:1; margin-bottom:4px; }
.hero-stat-label { font-size:0.72rem; color:var(--text-muted); text-transform:uppercase; letter-spacing:1px; }

.l-section { position:relative; z-index:1; padding:6rem 2rem; max-width:1200px; margin:0 auto; }
.section-tag { display:inline-flex; align-items:center; gap:8px; font-family:var(--font-mono); font-size:0.7rem; color:var(--amber); letter-spacing:2px; text-transform:uppercase; margin-bottom:1rem; }
.section-tag::before { content:''; width:24px; height:1px; background:var(--amber); }
.section-title { font-family:var(--font-display); font-size:clamp(1.8rem,3vw,2.6rem); font-weight:800; color:var(--text-primary); margin-bottom:0.75rem; letter-spacing:-0.5px; }
.section-sub { color:var(--text-secondary); font-size:1rem; max-width:500px; line-height:1.65; margin-bottom:3rem; }

.features-grid {
  display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
  gap:1.5px; background:var(--border); border:1px solid var(--border); border-radius:var(--radius-lg); overflow:hidden;
}
.feat-card { background:var(--surface); padding:2.5rem; transition:var(--transition); position:relative; overflow:hidden; }
.feat-card::before { content:''; position:absolute; top:0; left:0; width:100%; height:1px; background:linear-gradient(90deg,transparent,var(--cyan),transparent); opacity:0; transition:var(--transition); }
.feat-card:hover { background:var(--surface-2); }
.feat-card:hover::before { opacity:1; }
.feat-icon { width:48px; height:48px; border-radius:var(--radius-md); display:flex; align-items:center; justify-content:center; margin-bottom:1.5rem; font-size:1.5rem; }
.feat-icon-cyan { background:rgba(61,232,255,0.12); border:1px solid rgba(61,232,255,0.2); }
.feat-icon-amber { background:rgba(255,184,0,0.12); border:1px solid rgba(255,184,0,0.2); }
.feat-icon-emerald { background:rgba(0,229,160,0.12); border:1px solid rgba(0,229,160,0.2); }
.feat-title { font-size:1.1rem; font-weight:700; color:var(--text-primary); margin-bottom:0.75rem; }
.feat-desc { font-size:0.875rem; color:var(--text-secondary); line-height:1.65; }

.access-section { position:relative; z-index:1; padding:4rem 2rem 8rem; text-align:center; }
.access-cards { display:flex; gap:1.5rem; justify-content:center; flex-wrap:wrap; margin-top:3rem; max-width:800px; margin-left:auto; margin-right:auto; }
.access-card {
  flex:1; min-width:280px; max-width:360px;
  background:var(--surface); border:1px solid var(--border); border-radius:var(--radius-xl);
  padding:2.5rem 2rem; display:flex; flex-direction:column; align-items:center; gap:1.25rem;
  transition:var(--transition); position:relative; overflow:hidden; cursor:pointer;
}
.access-card::after { content:''; position:absolute; inset:0; border-radius:var(--radius-xl); opacity:0; transition:var(--transition); }
.access-card-citizen::after { background:radial-gradient(ellipse at top,rgba(61,232,255,0.08),transparent 70%); }
.access-card-police::after { background:radial-gradient(ellipse at top,rgba(255,184,0,0.08),transparent 70%); }
.access-card:hover { transform:translateY(-6px); }
.access-card-citizen:hover { border-color:rgba(61,232,255,0.4); box-shadow:0 20px 60px rgba(61,232,255,0.12); }
.access-card-police:hover { border-color:rgba(255,184,0,0.4); box-shadow:0 20px 60px rgba(255,184,0,0.12); }
.access-card:hover::after { opacity:1; }
.access-icon { width:72px; height:72px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:2rem; position:relative; z-index:1; }
.access-icon-citizen { background:rgba(61,232,255,0.1); border:2px solid rgba(61,232,255,0.25); box-shadow:0 0 30px rgba(61,232,255,0.15); }
.access-icon-police { background:rgba(255,184,0,0.1); border:2px solid rgba(255,184,0,0.25); box-shadow:0 0 30px rgba(255,184,0,0.15); }
.access-card-title { font-family:var(--font-display); font-size:1.4rem; font-weight:800; color:var(--text-primary); position:relative; z-index:1; }
.access-card-desc { font-size:0.875rem; color:var(--text-secondary); line-height:1.6; text-align:center; position:relative; z-index:1; }
.access-card-badge { font-family:var(--font-mono); font-size:0.7rem; letter-spacing:1.5px; text-transform:uppercase; padding:4px 14px; border-radius:100px; position:relative; z-index:1; }
.badge-citizen { background:rgba(61,232,255,0.1); color:var(--cyan); border:1px solid rgba(61,232,255,0.25); }
.badge-police { background:rgba(255,184,0,0.1); color:var(--amber); border:1px solid rgba(255,184,0,0.25); }
.access-btn { display:inline-flex; align-items:center; gap:8px; padding:11px 28px; border-radius:var(--radius-md); font-size:0.9rem; font-weight:600; border:none; transition:var(--transition); position:relative; z-index:1; width:100%; justify-content:center; }
.access-btn-citizen { background:linear-gradient(135deg,var(--cyan),var(--cyan-dim)); color:var(--void); box-shadow:0 0 30px rgba(61,232,255,0.2); }
.access-btn-citizen:hover { box-shadow:0 0 50px rgba(61,232,255,0.4); transform:translateY(-1px); }
.access-btn-police { background:linear-gradient(135deg,var(--amber),var(--amber-dim)); color:var(--void); box-shadow:0 0 30px rgba(255,184,0,0.2); }
.access-btn-police:hover { box-shadow:0 0 50px rgba(255,184,0,0.4); transform:translateY(-1px); }

.l-footer { position:relative; z-index:1; border-top:1px solid var(--border); padding:2rem 3rem; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:1rem; }
.l-footer-left { font-family:var(--font-mono); font-size:0.78rem; color:var(--text-muted); }
.l-footer-left span { color:var(--cyan); }
.l-footer-right { font-size:0.78rem; color:var(--text-muted); }

/* =========================================================  LOGIN  ========================================================= */
.login-root { min-height:100vh; background:var(--void); display:flex; align-items:stretch; position:relative; }

.login-panel-left {
  width:45%; min-height:100vh; background:var(--surface); border-right:1px solid var(--border);
  display:flex; flex-direction:column; justify-content:center; align-items:flex-start;
  padding:4rem; position:relative; overflow:hidden;
}
.login-panel-left::before {
  content:''; position:absolute; inset:0;
  background-image:linear-gradient(rgba(61,232,255,0.03) 1px,transparent 1px),linear-gradient(90deg,rgba(61,232,255,0.03) 1px,transparent 1px);
  background-size:32px 32px;
}
.login-panel-left::after {
  content:''; position:absolute; bottom:-200px; left:-100px; width:500px; height:500px;
  background:var(--cyan); border-radius:50%; filter:blur(120px); opacity:0.07;
}

.lpl-content { position:relative; z-index:1; }
.lpl-eyebrow { font-family:var(--font-mono); font-size:0.72rem; color:var(--cyan); letter-spacing:2px; text-transform:uppercase; margin-bottom:2rem; display:flex; align-items:center; gap:10px; }
.lpl-eyebrow::before { content:''; width:24px; height:1px; background:var(--cyan); }
.lpl-title { font-family:var(--font-display); font-size:2.8rem; font-weight:800; line-height:1.1; color:var(--text-primary); margin-bottom:1rem; letter-spacing:-0.5px; }
.lpl-title .accent { color:var(--cyan); }
.lpl-desc { font-size:0.9rem; color:var(--text-secondary); line-height:1.7; margin-bottom:2.5rem; max-width:380px; }
.lpl-features { display:flex; flex-direction:column; gap:12px; margin-bottom:2.5rem; }
.lpl-feature { display:flex; align-items:center; gap:12px; font-size:0.875rem; color:var(--text-secondary); }
.lpl-feature-dot { width:8px; height:8px; border-radius:50%; background:var(--cyan); box-shadow:0 0 10px var(--cyan); flex-shrink:0; }
.lpl-back { display:inline-flex; align-items:center; gap:8px; font-size:0.8rem; color:var(--text-muted); transition:var(--transition); padding:8px 0; font-family:var(--font-mono); }
.lpl-back:hover { color:var(--cyan); }

.login-panel-right {
  flex:1; display:flex; align-items:center; justify-content:center; padding:3rem 2rem; position:relative;
}
.login-panel-right::before {
  content:''; position:absolute; top:-100px; right:-100px; width:400px; height:400px;
  background:var(--amber); border-radius:50%; filter:blur(120px); opacity:0.05;
}

.login-box { width:100%; max-width:440px; position:relative; z-index:1; }
.login-box-header { margin-bottom:2rem; }
.login-box-title { font-family:var(--font-display); font-size:1.8rem; font-weight:800; color:var(--text-primary); margin-bottom:0.4rem; }
.login-box-sub { font-size:0.875rem; color:var(--text-secondary); }

.role-toggle { display:flex; gap:8px; padding:6px; background:var(--surface-3); border-radius:var(--radius-md); margin-bottom:2rem; border:1px solid var(--border); }
.role-tab {
  flex:1; padding:10px 16px; border-radius:var(--radius-sm); font-size:0.875rem; font-weight:600;
  cursor:pointer; transition:var(--transition); color:var(--text-muted);
  display:flex; align-items:center; justify-content:center; gap:8px; border:1px solid transparent; user-select:none;
}
.role-tab.active-citizen { background:rgba(61,232,255,0.12); color:var(--cyan); border-color:rgba(61,232,255,0.3); box-shadow:0 0 20px rgba(61,232,255,0.1); }
.role-tab.active-police { background:rgba(255,184,0,0.12); color:var(--amber); border-color:rgba(255,184,0,0.3); box-shadow:0 0 20px rgba(255,184,0,0.1); }

.form-field { margin-bottom:1.25rem; }
.form-field label { display:block; font-size:0.78rem; font-weight:600; color:var(--text-secondary); letter-spacing:0.5px; text-transform:uppercase; margin-bottom:8px; font-family:var(--font-mono); }
.form-field label .req { color:var(--rose); }
.input-wrap { position:relative; }
.input-icon { position:absolute; left:14px; top:50%; transform:translateY(-50%); color:var(--text-muted); width:16px; height:16px; pointer-events:none; }

.void-input { width:100%; background:var(--surface-2); border:1px solid var(--border); border-radius:var(--radius-md); padding:12px 14px 12px 40px; color:var(--text-primary); font-size:0.9rem; transition:var(--transition); outline:none; }
.void-input::placeholder { color:var(--text-muted); }
.void-input:focus { border-color:var(--cyan-dim); box-shadow:0 0 0 3px rgba(61,232,255,0.1); background:var(--surface-3); }
.void-input.police-focus:focus { border-color:var(--amber-dim); box-shadow:0 0 0 3px rgba(255,184,0,0.1); }
.form-hint-text { font-size:0.75rem; color:var(--text-muted); margin-top:6px; font-family:var(--font-mono); }

.submit-btn { width:100%; padding:14px; border-radius:var(--radius-md); font-size:0.95rem; font-weight:700; border:none; cursor:pointer; transition:var(--transition); display:flex; align-items:center; justify-content:center; gap:10px; margin-top:1.5rem; }
.submit-btn-citizen { background:linear-gradient(135deg,var(--cyan),var(--cyan-dim)); color:var(--void); box-shadow:0 0 30px rgba(61,232,255,0.2); }
.submit-btn-citizen:hover { box-shadow:0 0 50px rgba(61,232,255,0.35); transform:translateY(-1px); }
.submit-btn-police { background:linear-gradient(135deg,var(--amber),var(--amber-dim)); color:var(--void); box-shadow:0 0 30px rgba(255,184,0,0.2); }
.submit-btn-police:hover { box-shadow:0 0 50px rgba(255,184,0,0.35); transform:translateY(-1px); }

.demo-section { margin-top:2rem; border-top:1px solid var(--border); padding-top:1.5rem; }
.demo-section-label { font-family:var(--font-mono); font-size:0.7rem; color:var(--text-muted); letter-spacing:1.5px; text-transform:uppercase; margin-bottom:1rem; }
.demo-grid { display:grid; grid-template-columns:1fr 1fr; gap:8px; }
.demo-card { background:var(--surface-2); border:1px solid var(--border); border-radius:var(--radius-md); padding:10px 12px; cursor:pointer; transition:var(--transition); display:flex; align-items:center; gap:10px; }
.demo-card:hover { border-color:var(--border-bright); background:var(--surface-3); }
.demo-card.demo-police:hover { border-color:rgba(255,184,0,0.3); }
.demo-avatar { width:32px; height:32px; border-radius:50%; background:var(--surface-3); border:1px solid var(--border-bright); font-family:var(--font-mono); font-size:0.65rem; font-weight:700; color:var(--cyan); display:flex; align-items:center; justify-content:center; flex-shrink:0; }
.demo-avatar-police { color:var(--amber); border-color:rgba(255,184,0,0.3); }
.demo-name { font-size:0.8rem; font-weight:600; color:var(--text-primary); line-height:1.2; }
.demo-id { font-family:var(--font-mono); font-size:0.68rem; color:var(--text-muted); }
.auth-footer-link { margin-top:1.5rem; text-align:center; font-size:0.83rem; color:var(--text-muted); }
.auth-footer-link a { color:var(--cyan); transition:var(--transition); }
.auth-footer-link a:hover { opacity:0.8; }

/* =========================================================  REGISTER  ========================================================= */
.register-root { min-height:100vh; background:var(--void); display:flex; align-items:center; justify-content:center; padding:2rem; position:relative; }
.register-root::before { content:''; position:fixed; inset:0; background-image:linear-gradient(rgba(61,232,255,0.03) 1px,transparent 1px),linear-gradient(90deg,rgba(61,232,255,0.03) 1px,transparent 1px); background-size:40px 40px; pointer-events:none; }
.register-card { width:100%; max-width:620px; background:var(--surface); border:1px solid var(--border); border-radius:var(--radius-xl); overflow:hidden; position:relative; z-index:1; box-shadow:0 40px 120px rgba(0,0,0,0.6); }
.register-top { padding:2.5rem; border-bottom:1px solid var(--border); background:var(--surface-2); position:relative; overflow:hidden; }
.register-top::after { content:''; position:absolute; top:0; left:0; right:0; height:2px; background:linear-gradient(90deg,var(--cyan),transparent); }
.register-top-logo { display:flex; align-items:center; gap:12px; margin-bottom:1.5rem; }
.register-title { font-family:var(--font-display); font-size:1.5rem; font-weight:800; color:var(--text-primary); margin-bottom:0.3rem; }
.register-sub { font-size:0.85rem; color:var(--text-secondary); }
.register-body { padding:2.5rem; }
.form-grid-2 { display:grid; grid-template-columns:1fr 1fr; gap:1rem; }
.form-grid-2 .full { grid-column:1/-1; }
.register-input { width:100%; background:var(--surface-3); border:1px solid var(--border); border-radius:var(--radius-md); padding:11px 14px; color:var(--text-primary); font-size:0.875rem; transition:var(--transition); outline:none; }
.register-input::placeholder { color:var(--text-muted); }
.register-input:focus { border-color:var(--cyan-dim); box-shadow:0 0 0 3px rgba(61,232,255,0.08); }
.register-input option { background:var(--surface-3); }
.register-label { display:block; font-family:var(--font-mono); font-size:0.72rem; font-weight:600; color:var(--text-secondary); letter-spacing:0.8px; text-transform:uppercase; margin-bottom:7px; }
.register-btn { width:100%; padding:14px; background:linear-gradient(135deg,var(--cyan),var(--cyan-dim)); color:var(--void); border:none; border-radius:var(--radius-md); font-size:0.95rem; font-weight:700; cursor:pointer; transition:var(--transition); display:flex; align-items:center; justify-content:center; gap:10px; margin-top:1.5rem; box-shadow:0 0 30px rgba(61,232,255,0.2); }
.register-btn:hover { box-shadow:0 0 50px rgba(61,232,255,0.35); transform:translateY(-1px); }

/* =========================================================  APP SHELL  ========================================================= */
.app-shell { display:flex; height:100vh; overflow:hidden; background:var(--abyss); }

.sidebar { width:var(--sidebar-w); min-width:var(--sidebar-w); height:100vh; background:var(--surface); border-right:1px solid var(--border); display:flex; flex-direction:column; overflow:hidden; position:relative; z-index:10; }
.sidebar::after { content:''; position:absolute; top:0; right:0; width:1px; height:100%; background:linear-gradient(180deg,var(--cyan),transparent 60%); opacity:0.4; }

.sidebar-brand { padding:1.25rem; border-bottom:1px solid var(--border); display:flex; align-items:center; gap:10px; flex-shrink:0; }
.sidebar-logo-mark { width:34px; height:34px; background:linear-gradient(135deg,var(--cyan),var(--cyan-dim)); border-radius:7px; display:flex; align-items:center; justify-content:center; font-family:var(--font-mono); font-size:0.7rem; font-weight:700; color:var(--void); flex-shrink:0; box-shadow:0 0 15px var(--cyan-glow); }
.sidebar-brand-text { flex:1; }
.sidebar-brand-name { font-family:var(--font-display); font-size:0.9rem; font-weight:800; color:var(--text-primary); line-height:1.2; }
.sidebar-brand-tagline { font-family:var(--font-mono); font-size:0.6rem; color:var(--text-muted); letter-spacing:1px; text-transform:uppercase; }

.sidebar-nav { flex:1; padding:1rem 0.75rem; overflow-y:auto; }
.nav-group-label { font-family:var(--font-mono); font-size:0.6rem; color:var(--text-muted); letter-spacing:2px; text-transform:uppercase; padding:1rem 0.75rem 0.5rem; }
.nav-item { display:flex; align-items:center; gap:10px; padding:10px 12px; border-radius:var(--radius-sm); color:var(--text-secondary); font-size:0.875rem; font-weight:500; transition:var(--transition); margin-bottom:2px; position:relative; }
.nav-item svg { width:17px; height:17px; stroke-width:2; flex-shrink:0; }
.nav-item:hover { background:var(--surface-2); color:var(--text-primary); }
.nav-item.active { background:rgba(61,232,255,0.1); color:var(--cyan); border:1px solid rgba(61,232,255,0.2); }
.nav-item.active::before { content:''; position:absolute; left:0; top:50%; transform:translateY(-50%); width:3px; height:60%; background:var(--cyan); border-radius:0 2px 2px 0; box-shadow:0 0 8px var(--cyan); }
.nav-item-danger { color:var(--rose) !important; }
.nav-item-danger:hover { background:rgba(255,68,102,0.08) !important; }

.sidebar-footer { border-top:1px solid var(--border); padding:1rem; flex-shrink:0; }
.user-chip { display:flex; align-items:center; gap:10px; padding:10px; border-radius:var(--radius-md); background:var(--surface-2); border:1px solid var(--border); }
.user-chip-avatar { width:34px; height:34px; border-radius:50%; background:var(--surface-3); border:1px solid var(--border-bright); font-family:var(--font-mono); font-size:0.75rem; font-weight:700; color:var(--cyan); display:flex; align-items:center; justify-content:center; flex-shrink:0; }
.user-chip-avatar.police-avatar { color:var(--amber); border-color:rgba(255,184,0,0.3); }
.user-chip-info { flex:1; overflow:hidden; }
.user-chip-name { font-size:0.8rem; font-weight:600; color:var(--text-primary); white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
.user-chip-role { font-family:var(--font-mono); font-size:0.62rem; color:var(--text-muted); text-transform:uppercase; letter-spacing:1px; }

.role-tag { display:inline-block; font-family:var(--font-mono); font-size:0.6rem; padding:2px 8px; border-radius:100px; letter-spacing:1px; text-transform:uppercase; }
.role-tag-citizen { background:rgba(61,232,255,0.1); color:var(--cyan); border:1px solid rgba(61,232,255,0.25); }
.role-tag-police { background:rgba(255,184,0,0.1); color:var(--amber); border:1px solid rgba(255,184,0,0.25); }

.main-area { flex:1; display:flex; flex-direction:column; overflow:hidden; }
.top-bar { height:var(--header-h); flex-shrink:0; background:rgba(8,8,15,0.8); backdrop-filter:blur(20px); border-bottom:1px solid var(--border); display:flex; align-items:center; justify-content:space-between; padding:0 1.5rem; }
.top-bar-left { display:flex; flex-direction:column; }
.top-bar-title { font-size:0.95rem; font-weight:700; color:var(--text-primary); }
.top-bar-meta { font-family:var(--font-mono); font-size:0.65rem; color:var(--text-muted); display:flex; align-items:center; gap:8px; }
.top-bar-right { display:flex; align-items:center; gap:1rem; }

.db-status { display:flex; align-items:center; gap:6px; font-family:var(--font-mono); font-size:0.7rem; color:var(--emerald); background:rgba(0,229,160,0.08); border:1px solid rgba(0,229,160,0.2); padding:5px 12px; border-radius:100px; }
.db-status-dot { width:6px; height:6px; background:var(--emerald); border-radius:50%; animation:blinkPulse 2s ease-in-out infinite; box-shadow:0 0 8px var(--emerald); }
.btn-logout { font-family:var(--font-mono); font-size:0.72rem; padding:6px 14px; border-radius:var(--radius-sm); background:transparent; border:1px solid var(--border); color:var(--text-secondary); cursor:pointer; transition:var(--transition); text-transform:uppercase; display:inline-block; }
.btn-logout:hover { border-color:var(--rose); color:var(--rose); background:rgba(255,68,102,0.08); }

.content-body { flex:1; overflow-y:auto; padding:2rem; scroll-behavior:smooth; }

.flash-wrap { margin-bottom:1.5rem; }
.flash-msg { display:flex; align-items:center; justify-content:space-between; padding:12px 16px; border-radius:var(--radius-md); font-size:0.875rem; margin-bottom:8px; gap:1rem; }
.flash-success { background:rgba(0,229,160,0.1); border:1px solid rgba(0,229,160,0.25); color:var(--emerald); }
.flash-danger,.flash-error { background:rgba(255,68,102,0.1); border:1px solid rgba(255,68,102,0.25); color:var(--rose); }
.flash-info,.flash-warning { background:rgba(255,184,0,0.1); border:1px solid rgba(255,184,0,0.25); color:var(--amber); }
.flash-close { background:none; border:none; font-size:1.2rem; cursor:pointer; color:inherit; opacity:0.6; transition:var(--transition); flex-shrink:0; }
.flash-close:hover { opacity:1; }

/* =========================================================  DASHBOARD  ========================================================= */
.dash-wrap { display:flex; flex-direction:column; gap:1.5rem; }

.welcome-banner { border-radius:var(--radius-lg); padding:1.75rem 2rem; display:flex; align-items:center; justify-content:space-between; gap:1rem; border:1px solid; position:relative; overflow:hidden; }
.welcome-banner::before { content:''; position:absolute; inset:0; background-image:linear-gradient(rgba(255,255,255,0.02) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,0.02) 1px,transparent 1px); background-size:24px 24px; }
.wb-citizen { background:linear-gradient(135deg,rgba(61,232,255,0.06),rgba(61,232,255,0.02)); border-color:rgba(61,232,255,0.2); }
.wb-police { background:linear-gradient(135deg,rgba(255,184,0,0.06),rgba(255,184,0,0.02)); border-color:rgba(255,184,0,0.2); }
.wb-left { position:relative; z-index:1; }
.wb-eyebrow { font-family:var(--font-mono); font-size:0.7rem; color:var(--text-muted); letter-spacing:1.5px; text-transform:uppercase; margin-bottom:6px; }
.wb-name { font-family:var(--font-display); font-size:1.6rem; font-weight:800; color:var(--text-primary); margin-bottom:4px; }
.wb-meta { font-size:0.83rem; color:var(--text-secondary); }
.wb-right { display:flex; gap:0.75rem; flex-wrap:wrap; position:relative; z-index:1; }

.action-btn { display:inline-flex; align-items:center; gap:8px; padding:10px 20px; border-radius:var(--radius-md); font-size:0.85rem; font-weight:600; transition:var(--transition); border:none; cursor:pointer; }
.action-btn svg { width:16px; height:16px; }
.action-btn-primary { background:linear-gradient(135deg,var(--cyan),var(--cyan-dim)); color:var(--void); box-shadow:0 0 20px rgba(61,232,255,0.2); }
.action-btn-primary:hover { box-shadow:0 0 35px rgba(61,232,255,0.3); transform:translateY(-1px); }
.action-btn-ghost { background:transparent; border:1px solid var(--border-bright); color:var(--text-secondary); }
.action-btn-ghost:hover { border-color:var(--cyan-dim); color:var(--cyan); background:var(--cyan-glow); }
.action-btn-amber { background:linear-gradient(135deg,var(--amber),var(--amber-dim)); color:var(--void); }
.action-btn-amber:hover { transform:translateY(-1px); box-shadow:0 0 30px var(--amber-glow); }

.metrics-row { display:grid; grid-template-columns:repeat(auto-fit,minmax(170px,1fr)); gap:1rem; }
.metric-card { background:var(--surface); border:1px solid var(--border); border-radius:var(--radius-lg); padding:1.5rem; position:relative; overflow:hidden; transition:var(--transition); }
.metric-card:hover { transform:translateY(-2px); border-color:var(--border-bright); }
.metric-card-accent { position:absolute; top:0; right:0; width:80px; height:80px; border-radius:50%; filter:blur(30px); opacity:0.4; }
.mc-cyan { border-left:2px solid var(--cyan); }
.mc-cyan .metric-card-accent { background:var(--cyan); }
.mc-amber { border-left:2px solid var(--amber); }
.mc-amber .metric-card-accent { background:var(--amber); }
.mc-rose { border-left:2px solid var(--rose); }
.mc-rose .metric-card-accent { background:var(--rose); }
.mc-emerald { border-left:2px solid var(--emerald); }
.mc-emerald .metric-card-accent { background:var(--emerald); }
.metric-label { font-family:var(--font-mono); font-size:0.68rem; color:var(--text-muted); text-transform:uppercase; letter-spacing:1.5px; margin-bottom:0.75rem; }
.metric-value { font-family:var(--font-display); font-size:2.2rem; font-weight:800; line-height:1; margin-bottom:6px; }
.mv-cyan { color:var(--cyan); }
.mv-amber { color:var(--amber); }
.mv-rose { color:var(--rose); }
.mv-emerald { color:var(--emerald); }
.metric-desc { font-size:0.72rem; color:var(--text-muted); }

.panel { background:var(--surface); border:1px solid var(--border); border-radius:var(--radius-lg); overflow:hidden; }
.panel-header { display:flex; align-items:center; justify-content:space-between; padding:1.25rem 1.5rem; border-bottom:1px solid var(--border); gap:1rem; flex-wrap:wrap; }
.panel-title { display:flex; align-items:center; gap:10px; font-size:0.9rem; font-weight:700; color:var(--text-primary); }
.panel-title svg { width:18px; height:18px; color:var(--cyan); stroke-width:2; }
.panel-body { padding:1.5rem; }

.filter-row { display:flex; align-items:center; gap:0.75rem; flex-wrap:wrap; }
.search-wrap { position:relative; flex:1; min-width:200px; }
.search-icon { position:absolute; left:12px; top:50%; transform:translateY(-50%); width:15px; height:15px; color:var(--text-muted); pointer-events:none; }
.search-input { width:100%; background:var(--surface-2); border:1px solid var(--border); border-radius:var(--radius-sm); padding:9px 12px 9px 36px; color:var(--text-primary); font-size:0.82rem; outline:none; transition:var(--transition); }
.search-input::placeholder { color:var(--text-muted); }
.search-input:focus { border-color:var(--cyan-dim); }
.filter-select { background:var(--surface-2); border:1px solid var(--border); border-radius:var(--radius-sm); padding:9px 12px; color:var(--text-secondary); font-size:0.82rem; outline:none; transition:var(--transition); cursor:pointer; }
.filter-select option { background:var(--surface-3); }

.table-wrap { overflow-x:auto; }
.data-table { width:100%; border-collapse:collapse; font-size:0.84rem; }
.data-table thead tr { border-bottom:1px solid var(--border); }
.data-table th { padding:10px 12px; text-align:left; font-family:var(--font-mono); font-size:0.65rem; color:var(--text-muted); text-transform:uppercase; letter-spacing:1.5px; font-weight:500; white-space:nowrap; }
.data-table tbody tr { border-bottom:1px solid rgba(255,255,255,0.04); transition:var(--transition); }
.data-table tbody tr:hover { background:rgba(255,255,255,0.02); }
.data-table td { padding:12px 12px; color:var(--text-secondary); vertical-align:middle; }
.td-primary { font-family:var(--font-mono); font-size:0.8rem; color:var(--cyan) !important; font-weight:600; }
.td-strong { font-weight:600; color:var(--text-primary) !important; }
.td-muted { font-size:0.75rem; color:var(--text-muted) !important; margin-top:2px; }

.vbadge { display:inline-flex; align-items:center; gap:5px; font-family:var(--font-mono); font-size:0.68rem; font-weight:600; padding:3px 10px; border-radius:100px; text-transform:uppercase; letter-spacing:0.5px; white-space:nowrap; }
.vbadge-dot { width:5px; height:5px; border-radius:50%; animation:blinkPulse 2s ease-in-out infinite; }
.vb-cyan { background:rgba(61,232,255,0.1); color:var(--cyan); border:1px solid rgba(61,232,255,0.25); }
.vb-cyan .vbadge-dot { background:var(--cyan); }
.vb-amber { background:rgba(255,184,0,0.1); color:var(--amber); border:1px solid rgba(255,184,0,0.25); }
.vb-amber .vbadge-dot { background:var(--amber); }
.vb-rose { background:rgba(255,68,102,0.1); color:var(--rose); border:1px solid rgba(255,68,102,0.25); }
.vb-rose .vbadge-dot { background:var(--rose); }
.vb-emerald { background:rgba(0,229,160,0.1); color:var(--emerald); border:1px solid rgba(0,229,160,0.25); }
.vb-emerald .vbadge-dot { background:var(--emerald); }
.vb-violet { background:rgba(168,85,247,0.1); color:var(--violet); border:1px solid rgba(168,85,247,0.25); }
.vb-violet .vbadge-dot { background:var(--violet); }
.vb-gray { background:rgba(255,255,255,0.06); color:var(--text-muted); border:1px solid var(--border); }
.vb-gray .vbadge-dot { background:var(--text-muted); }

.btn { display:inline-flex; align-items:center; gap:8px; padding:8px 18px; border-radius:var(--radius-sm); font-size:0.84rem; font-weight:600; border:1px solid transparent; cursor:pointer; transition:var(--transition); white-space:nowrap; font-family:var(--font-main); }
.btn svg { width:15px; height:15px; }
.btn-xs { padding:5px 12px; font-size:0.75rem; }
.btn-sm { padding:7px 14px; font-size:0.8rem; }
.btn-cyan { background:linear-gradient(135deg,var(--cyan),var(--cyan-dim)); color:var(--void); border:none; box-shadow:0 0 20px rgba(61,232,255,0.2); }
.btn-cyan:hover { box-shadow:0 0 35px rgba(61,232,255,0.3); transform:translateY(-1px); }
.btn-amber { background:linear-gradient(135deg,var(--amber),var(--amber-dim)); color:var(--void); border:none; }
.btn-amber:hover { transform:translateY(-1px); box-shadow:0 0 25px var(--amber-glow); }
.btn-rose { background:rgba(255,68,102,0.12); color:var(--rose); border-color:rgba(255,68,102,0.3); }
.btn-rose:hover { background:rgba(255,68,102,0.2); }
.btn-ghost { background:transparent; color:var(--text-secondary); border-color:var(--border); }
.btn-ghost:hover { border-color:var(--border-bright); color:var(--text-primary); }
/* backward compat aliases */
.btn-primary { background:linear-gradient(135deg,var(--cyan),var(--cyan-dim)); color:var(--void); border:none; }
.btn-danger { background:rgba(255,68,102,0.12); color:var(--rose); border-color:rgba(255,68,102,0.3); }
.btn-outline { background:transparent; color:var(--text-secondary); border-color:var(--border); }
.btn-outline:hover { border-color:var(--border-bright); color:var(--text-primary); }

.empty-state { text-align:center; padding:3rem; color:var(--text-muted); }
.empty-state svg { width:48px; height:48px; margin-bottom:1rem; opacity:0.3; }
.empty-state h4 { font-size:1rem; font-weight:600; color:var(--text-secondary); margin-bottom:0.5rem; }
.empty-state p { font-size:0.83rem; max-width:320px; margin:0 auto; }

.mono { font-family:var(--font-mono); }
.mono-text { font-family:var(--font-mono); }

/* =========================================================  FORMS  ========================================================= */
.page-wrap { max-width:820px; margin:0 auto; }

.notice-banner { display:flex; gap:1rem; align-items:flex-start; padding:1.25rem 1.5rem; border-radius:var(--radius-md); background:rgba(61,232,255,0.05); border:1px solid rgba(61,232,255,0.15); margin-bottom:1.5rem; font-size:0.84rem; color:var(--text-secondary); line-height:1.6; }
.notice-icon { font-size:1.25rem; flex-shrink:0; }

.fir-banner { display:flex; align-items:center; justify-content:space-between; background:var(--surface); border:1px solid var(--border); border-left:3px solid var(--cyan); border-radius:var(--radius-md); padding:1.25rem 1.5rem; margin-bottom:1.5rem; gap:1rem; }
.fir-banner-label { font-family:var(--font-mono); font-size:0.65rem; text-transform:uppercase; letter-spacing:1.5px; color:var(--text-muted); margin-bottom:4px; }
.fir-banner-num { font-family:var(--font-mono); font-size:1.2rem; font-weight:700; color:var(--cyan); }
.fir-banner-sub { font-size:0.82rem; color:var(--text-secondary); margin-top:3px; }

.field-group { margin-bottom:1.1rem; }
.field-label { display:block; font-family:var(--font-mono); font-size:0.72rem; font-weight:600; color:var(--text-secondary); letter-spacing:0.8px; text-transform:uppercase; margin-bottom:7px; }
.field-label .req { color:var(--rose); }
.field-input,.field-select,.field-textarea { width:100%; background:var(--surface-2); border:1px solid var(--border); border-radius:var(--radius-md); padding:11px 14px; color:var(--text-primary); font-size:0.875rem; outline:none; transition:var(--transition); font-family:var(--font-main); }
.field-input::placeholder,.field-textarea::placeholder { color:var(--text-muted); }
.field-input:focus,.field-select:focus,.field-textarea:focus { border-color:var(--cyan-dim); box-shadow:0 0 0 3px rgba(61,232,255,0.08); background:var(--surface-3); }
.field-select option { background:var(--surface-3); }
.field-textarea { resize:vertical; }
.field-hint { font-size:0.72rem; color:var(--text-muted); margin-top:5px; font-family:var(--font-mono); }

/* backward compat form classes */
.form-control { width:100%; background:var(--surface-2); border:1px solid var(--border); border-radius:var(--radius-md); padding:11px 14px; color:var(--text-primary); font-size:0.875rem; outline:none; transition:var(--transition); font-family:var(--font-main); }
.form-control::placeholder { color:var(--text-muted); }
.form-control:focus { border-color:var(--cyan-dim); box-shadow:0 0 0 3px rgba(61,232,255,0.08); background:var(--surface-3); }
.form-control option { background:var(--surface-3); }
.form-label { display:block; font-family:var(--font-mono); font-size:0.72rem; font-weight:600; color:var(--text-secondary); letter-spacing:0.8px; text-transform:uppercase; margin-bottom:7px; }
.form-hint { font-size:0.72rem; color:var(--text-muted); margin-top:5px; font-family:var(--font-mono); }
.required { color:var(--rose); }
.form-group { margin-bottom:1.1rem; }
.form-grid { display:grid; grid-template-columns:1fr 1fr; gap:1rem; }
.form-grid .full-width { grid-column:1/-1; }

.form-2col { display:grid; grid-template-columns:1fr 1fr; gap:1rem; }
.form-2col .full-col { grid-column:1/-1; }

.form-actions { display:flex; justify-content:flex-end; gap:0.75rem; margin-top:1.5rem; padding-top:1.25rem; border-top:1px solid var(--border); }

.attribution-box { background:rgba(61,232,255,0.04); border:1px solid rgba(61,232,255,0.12); border-radius:var(--radius-md); padding:0.875rem 1.125rem; font-size:0.8rem; color:var(--text-secondary); margin-top:0.75rem; font-family:var(--font-mono); }
.attribution-box strong { color:var(--cyan); }

/* compat: old classes used in police_fir, fir_details */
.card-panel { background:var(--surface); border:1px solid var(--border); border-radius:var(--radius-lg); overflow:hidden; margin-bottom:1.5rem; }
.card-panel-header { display:flex; align-items:center; justify-content:space-between; padding:1.25rem 1.5rem; border-bottom:1px solid var(--border); gap:1rem; flex-wrap:wrap; }
.card-panel-body { padding:1.5rem; }
.card-title { display:flex; align-items:center; gap:10px; font-size:0.9rem; font-weight:700; color:var(--text-primary); }
.card-title svg { width:18px; height:18px; color:var(--cyan); stroke-width:2; }

/* Info grid */
.info-grid { display:grid; grid-template-columns:1fr 1fr; gap:1.25rem; }
.info-item-label { font-family:var(--font-mono); font-size:0.65rem; color:var(--text-muted); text-transform:uppercase; letter-spacing:1.5px; margin-bottom:4px; }
.info-item-val { font-size:0.875rem; font-weight:600; color:var(--text-primary); }

/* Timeline */
.timeline { display:flex; flex-direction:column; gap:0; }
.timeline-item { display:flex; gap:1rem; padding-bottom:1.25rem; position:relative; }
.timeline-item:not(:last-child)::before { content:''; position:absolute; left:15px; top:28px; bottom:0; width:1px; background:var(--border); }
.timeline-dot { width:30px; height:30px; border-radius:50%; background:var(--surface-3); border:1px solid var(--border); display:flex; align-items:center; justify-content:center; font-size:0.75rem; flex-shrink:0; z-index:1; }
.td-cyan { border-color:rgba(61,232,255,0.4); color:var(--cyan); background:rgba(61,232,255,0.08); }
.td-amber { border-color:rgba(255,184,0,0.4); color:var(--amber); background:rgba(255,184,0,0.08); }
.td-rose { border-color:rgba(255,68,102,0.4); color:var(--rose); background:rgba(255,68,102,0.08); }
.td-emerald { border-color:rgba(0,229,160,0.4); color:var(--emerald); background:rgba(0,229,160,0.08); }
.timeline-content { flex:1; }
.timeline-title { font-size:0.85rem; font-weight:600; color:var(--text-primary); margin-bottom:2px; }
.timeline-date { font-family:var(--font-mono); font-size:0.7rem; color:var(--text-muted); margin-bottom:4px; }
.timeline-notes { font-size:0.78rem; color:var(--text-secondary); line-height:1.5; }

/* dashboard compat */
.dashboard-wrapper { display:flex; flex-direction:column; gap:1.5rem; }
.dash-welcome { border-radius:var(--radius-lg); padding:1.75rem 2rem; border:1px solid; position:relative; overflow:hidden; margin-bottom:0; }
.dash-welcome::before { content:''; position:absolute; inset:0; background-image:linear-gradient(rgba(255,255,255,0.02) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,0.02) 1px,transparent 1px); background-size:24px 24px; }
.dash-welcome-police { background:linear-gradient(135deg,rgba(255,184,0,0.06),rgba(255,184,0,0.02)); border-color:rgba(255,184,0,0.2); }
.dash-welcome-user { background:linear-gradient(135deg,rgba(61,232,255,0.06),rgba(61,232,255,0.02)); border-color:rgba(61,232,255,0.2); }
.dash-welcome-inner { display:flex; align-items:center; justify-content:space-between; gap:1rem; flex-wrap:wrap; position:relative; z-index:1; }
.dash-welcome-text .welcome-greeting { font-family:var(--font-mono); font-size:0.7rem; color:var(--text-muted); letter-spacing:1.5px; text-transform:uppercase; margin-bottom:6px; }
.dash-welcome-text h2 { font-family:var(--font-display); font-size:1.6rem; font-weight:800; color:var(--text-primary); margin-bottom:4px; }
.dash-welcome-text p,.station-meta { font-size:0.83rem; color:var(--text-secondary); }
.dash-welcome-actions { display:flex; gap:0.75rem; flex-wrap:wrap; }
.dash-action-btn { display:inline-flex; align-items:center; gap:8px; padding:10px 20px; border-radius:var(--radius-md); font-size:0.85rem; font-weight:600; transition:var(--transition); border:none; cursor:pointer; }
.dash-action-btn svg { width:16px; height:16px; }
.dash-action-btn-white { background:transparent; border:1px solid var(--border-bright); color:var(--text-secondary); }
.dash-action-btn-white:hover { border-color:var(--cyan-dim); color:var(--cyan); background:var(--cyan-glow); }
.dash-action-btn-solid { background:linear-gradient(135deg,var(--cyan),var(--cyan-dim)); color:var(--void); box-shadow:0 0 20px rgba(61,232,255,0.2); }
.dash-action-btn-solid:hover { box-shadow:0 0 35px rgba(61,232,255,0.3); transform:translateY(-1px); }

.metrics-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(170px,1fr)); gap:1rem; }
.metric-card { background:var(--surface); border:1px solid var(--border); border-radius:var(--radius-lg); padding:1.5rem; position:relative; overflow:hidden; transition:var(--transition); }
.metric-card:hover { transform:translateY(-2px); border-color:var(--border-bright); }
.metric-card-top { display:flex; align-items:center; justify-content:space-between; margin-bottom:0.75rem; }
.metric-icon { font-size:1.25rem; }
.metric-label { font-family:var(--font-mono); font-size:0.68rem; color:var(--text-muted); text-transform:uppercase; letter-spacing:1.5px; }
.metric-value { font-family:var(--font-display); font-size:2.2rem; font-weight:800; line-height:1; margin-bottom:6px; color:var(--cyan); }
.metric-desc { font-size:0.72rem; color:var(--text-muted); }
.card-primary .metric-value { color:var(--cyan); }
.card-warning .metric-value { color:var(--amber); }
.card-success .metric-value { color:var(--emerald); }
.card-danger .metric-value { color:var(--rose); }

/* badge compat */
.badge { display:inline-flex; align-items:center; gap:5px; font-family:var(--font-mono); font-size:0.68rem; font-weight:600; padding:3px 10px; border-radius:100px; text-transform:uppercase; letter-spacing:0.5px; white-space:nowrap; }
.badge-pulse { width:5px; height:5px; border-radius:50%; animation:blinkPulse 2s ease-in-out infinite; background:currentColor; display:inline-block; }
.badge-registered { background:rgba(61,232,255,0.1); color:var(--cyan); border:1px solid rgba(61,232,255,0.25); }
.badge-investigating { background:rgba(255,184,0,0.1); color:var(--amber); border:1px solid rgba(255,184,0,0.25); }
.badge-completed { background:rgba(0,229,160,0.1); color:var(--emerald); border:1px solid rgba(0,229,160,0.25); }
.badge-court { background:rgba(168,85,247,0.1); color:var(--violet); border:1px solid rgba(168,85,247,0.25); }
.badge-closed { background:rgba(255,255,255,0.06); color:var(--text-muted); border:1px solid var(--border); }
.badge-secondary { background:rgba(255,255,255,0.06); color:var(--text-muted); border:1px solid var(--border); }
.badge-chargesheet { background:rgba(255,68,102,0.1); color:var(--rose); border:1px solid rgba(255,68,102,0.25); }

/* filter bar compat */
.filter-bar { display:flex; align-items:center; gap:0.75rem; flex-wrap:wrap; }
.search-box { position:relative; flex:1; min-width:200px; }
.search-box .search-icon { position:absolute; left:12px; top:50%; transform:translateY(-50%); width:15px; height:15px; color:var(--text-muted); pointer-events:none; }
.search-box input { width:100%; background:var(--surface-2); border:1px solid var(--border); border-radius:var(--radius-sm); padding:9px 12px 9px 36px; color:var(--text-primary); font-size:0.82rem; outline:none; transition:var(--transition); }
.search-box input::placeholder { color:var(--text-muted); }
.search-box input:focus { border-color:var(--cyan-dim); }
#statusFilterSelect { background:var(--surface-2); border:1px solid var(--border); border-radius:var(--radius-sm); padding:9px 12px; color:var(--text-secondary); font-size:0.82rem; outline:none; transition:var(--transition); cursor:pointer; }
#statusFilterSelect option { background:var(--surface-3); }

/* table-responsive compat */
.table-responsive { overflow-x:auto; }

/* misc compat */
.criminals-container { }
.fir-detail-grid { display:grid; grid-template-columns:2fr 1fr; gap:1.5rem; }
.evidence-item { display:flex; align-items:center; justify-content:space-between; padding:0.875rem 1rem; border-bottom:1px solid var(--border); gap:1rem; flex-wrap:wrap; }
.evidence-item:last-child { border-bottom:none; }
.evidence-type { font-weight:600; font-size:0.85rem; color:var(--text-primary); }
.evidence-meta { font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono); margin-top:2px; }

/* alerts */
.alert { display:flex; align-items:center; justify-content:space-between; padding:12px 16px; border-radius:var(--radius-md); font-size:0.875rem; margin-bottom:8px; gap:1rem; }
.alert-success { background:rgba(0,229,160,0.1); border:1px solid rgba(0,229,160,0.25); color:var(--emerald); }
.alert-danger,.alert-error { background:rgba(255,68,102,0.1); border:1px solid rgba(255,68,102,0.25); color:var(--rose); }
.alert-info,.alert-warning { background:rgba(255,184,0,0.1); border:1px solid rgba(255,184,0,0.25); color:var(--amber); }

.flash-container { margin-bottom:1.5rem; }

/* icon-color compat */
.icon-blue { color:var(--cyan); }
.icon-amber { color:var(--amber); }
.icon-crimson { color:var(--rose); }
.icon-emerald { color:var(--emerald); }

/* navy compat */
--navy-blue: var(--cyan);
--navy-subtle: rgba(61,232,255,0.05);
--bg-primary: var(--text-primary);
--bg-surface: var(--surface);
--bg-surface-2: var(--surface-2);
--bg-subtle: var(--surface-3);
--text-accent: var(--cyan);
--border-color: var(--border);
--crimson: var(--rose);

@keyframes fadeUp { from{opacity:0;transform:translateY(20px)} to{opacity:1;transform:translateY(0)} }
@keyframes fadeIn { from{opacity:0} to{opacity:1} }
.anim-fade-up { animation:fadeUp 0.5s ease forwards; }
.anim-fade-up:nth-child(1){animation-delay:0.05s}
.anim-fade-up:nth-child(2){animation-delay:0.1s}
.anim-fade-up:nth-child(3){animation-delay:0.15s}
.anim-fade-up:nth-child(4){animation-delay:0.2s}

@media(max-width:768px){
  .login-panel-left{display:none}
  .l-nav{padding:0 1.25rem}
  .l-nav-link{display:none}
  .l-hero-title{font-size:2.5rem}
  .info-grid{grid-template-columns:1fr}
  .form-2col,.form-grid,.form-grid-2{grid-template-columns:1fr}
  .content-body{padding:1rem}
  .register-card{border-radius:0}
  .register-root{padding:0}
  .fir-detail-grid{grid-template-columns:1fr}
  .top-bar-meta{display:none}
}
@media(max-width:480px){
  .metrics-row,.metrics-grid{grid-template-columns:1fr 1fr}
  .access-cards{flex-direction:column;align-items:center}
}
"""

# ============================================================
# LANDING.HTML
# ============================================================
landing = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRMS &#8212; Crime Record Management System | Official Portal</title>
    <meta name="description" content="CRMS: A secure law enforcement portal for filing FIRs, tracking investigations, and managing criminal records.">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
<div class="landing-root">
    <div class="grid-canvas"></div>
    <div class="scanlines"></div>
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>

    <nav class="l-nav">
        <div class="l-nav-logo">
            <div class="logo-mark">CR</div>
            <div class="logo-text">CRMS <span>Portal</span></div>
        </div>
        <div class="l-nav-right">
            <a href="#features" class="l-nav-link">System</a>
            <a href="#access" class="l-nav-link">Access</a>
            <a href="{{ url_for('auth.login') }}" class="l-nav-cta">Login</a>
        </div>
    </nav>

    <section class="l-hero">
        <div class="hero-eyebrow">
            <span class="hero-eyebrow-dot"></span>
            DBMS Project &nbsp;&bull;&nbsp; Law Enforcement Intelligence Platform
        </div>
        <h1 class="l-hero-title">
            <span class="t-cyan">Crime Record</span><br>
            <span class="t-amber">Management System</span>
        </h1>
        <p class="l-hero-sub">
            A fully normalized, MySQL-backed portal for citizens to file FIRs and track cases &mdash;
            and officers to manage investigations with real-time evidence logging.
        </p>
        <div class="hero-ctas">
            <a href="{{ url_for('auth.login') }}" class="btn-portal">
                <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"/></svg>
                Access Portal
            </a>
            <a href="{{ url_for('auth.register') }}" class="btn-portal-ghost">
                <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"/></svg>
                Register Citizen
            </a>
        </div>
        <div class="hero-stats">
            <div class="hero-stat"><div class="hero-stat-val" data-count="10">10</div><div class="hero-stat-label">DB Tables</div></div>
            <div class="hero-stat"><div class="hero-stat-val">3NF</div><div class="hero-stat-label">Normalized</div></div>
            <div class="hero-stat"><div class="hero-stat-val" data-count="25">25+</div><div class="hero-stat-label">SQL Queries</div></div>
            <div class="hero-stat"><div class="hero-stat-val">2</div><div class="hero-stat-label">Role Tiers</div></div>
        </div>
    </section>

    <div id="features">
        <div class="l-section">
            <div class="section-tag">Core Capabilities</div>
            <h2 class="section-title">Built for Justice &amp; Accountability</h2>
            <p class="section-sub">Fully operational CRUD-driven system backed by a relational database with foreign keys, joins, and triggers.</p>
            <div class="features-grid">
                <div class="feat-card anim-fade-up">
                    <div class="feat-icon feat-icon-cyan">&#128221;</div>
                    <div class="feat-title">FIR Filing &amp; Tracking</div>
                    <p class="feat-desc">Citizens register First Information Reports online. Each FIR auto-generates a unique ID and moves through a full status pipeline &mdash; Registered &rarr; Investigation &rarr; Chargesheet &rarr; Court &rarr; Closed.</p>
                </div>
                <div class="feat-card anim-fade-up">
                    <div class="feat-icon feat-icon-amber">&#128269;</div>
                    <div class="feat-title">Investigation Command Console</div>
                    <p class="feat-desc">Officers manage assigned cases, log evidence with chain-of-custody tracking, update investigation status histories, and generate chargesheets with relational integrity enforced at every step.</p>
                </div>
                <div class="feat-card anim-fade-up">
                    <div class="feat-icon feat-icon-emerald">&#128451;</div>
                    <div class="feat-title">Criminal Intelligence Registry</div>
                    <p class="feat-desc">Searchable criminal directory with threat classifications, living status, arrest records, and linked FIR counts. Demonstrates complex multi-table JOINs and aggregate SQL queries across the full schema.</p>
                </div>
            </div>
        </div>
    </div>

    <div id="access">
        <div class="access-section">
            <div class="section-tag">Choose Your Role</div>
            <h2 class="section-title">Select Access Level</h2>
            <p class="section-sub" style="max-width:480px;margin:0 auto 0;">The portal offers two separate authenticated environments with role-based dashboards and permissions.</p>
            <div class="access-cards">
                <div class="access-card access-card-citizen">
                    <div class="access-icon access-icon-citizen">&#128100;</div>
                    <div class="access-card-badge badge-citizen">Citizen Access</div>
                    <div class="access-card-title">Public Portal</div>
                    <p class="access-card-desc">File FIRs, track case status in real time, view criminal records, and receive investigation updates. Login with your registered email.</p>
                    <a href="{{ url_for('auth.login') }}" class="access-btn access-btn-citizen">
                        <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14"/></svg>
                        Citizen Login
                    </a>
                </div>
                <div class="access-card access-card-police">
                    <div class="access-icon access-icon-police">&#128110;</div>
                    <div class="access-card-badge badge-police">Officer Access</div>
                    <div class="access-card-title">Command Center</div>
                    <p class="access-card-desc">Manage assigned FIR investigations, log evidence with custody chain, update case statuses, and oversee station-wide complaint registry.</p>
                    <a href="{{ url_for('auth.login') }}" class="access-btn access-btn-police">
                        <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
                        Officer Login
                    </a>
                </div>
            </div>
        </div>
    </div>

    <footer class="l-footer">
        <div class="l-footer-left"><span>CRMS</span> &mdash; Crime Record Management System &copy; 2026</div>
        <div class="l-footer-right">MySQL &nbsp;+&nbsp; Flask &nbsp;+&nbsp; Python &nbsp;&bull;&nbsp; DBMS Project</div>
    </footer>
</div>
<script src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>"""

# ============================================================
# BASE.HTML
# ============================================================
base = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}CRMS{% endblock %} | Law Enforcement Portal</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
{% if session.get('role') %}
<div class="app-shell">
    <!-- Sidebar -->
    <aside class="sidebar">
        <div class="sidebar-brand">
            <div class="sidebar-logo-mark">CR</div>
            <div class="sidebar-brand-text">
                <div class="sidebar-brand-name">CRMS</div>
                <div class="sidebar-brand-tagline">Record System</div>
            </div>
        </div>

        <nav class="sidebar-nav">
            {% if session.get('role') == 'user' %}
                <div class="nav-group-label">Citizen Services</div>
                <a href="{{ url_for('user.dashboard') }}" class="nav-item {% if request.endpoint == 'user.dashboard' %}active{% endif %}">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
                    Dashboard
                </a>
                <a href="{{ url_for('user.file_fir') }}" class="nav-item {% if request.endpoint == 'user.file_fir' %}active{% endif %}">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                    File New FIR
                </a>
                <a href="{{ url_for('fir.criminals_list') }}" class="nav-item {% if request.endpoint == 'fir.criminals_list' %}active{% endif %}">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
                    Criminal Records
                </a>
            {% elif session.get('role') == 'police' %}
                <div class="nav-group-label">Police Management</div>
                <a href="{{ url_for('police.dashboard') }}" class="nav-item {% if request.endpoint == 'police.dashboard' %}active{% endif %}">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
                    Officer Dashboard
                </a>
                <a href="{{ url_for('fir.criminals_list') }}" class="nav-item {% if request.endpoint == 'fir.criminals_list' %}active{% endif %}">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
                    Criminal Directory
                </a>
            {% endif %}
            <div class="nav-group-label">Session</div>
            <a href="{{ url_for('auth.logout') }}" class="nav-item nav-item-danger">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"/></svg>
                Sign Out
            </a>
        </nav>

        <div class="sidebar-footer">
            <div class="user-chip">
                <div class="user-chip-avatar {% if session.get('role') == 'police' %}police-avatar{% endif %}">
                    {{ session.get('name', 'U')[0] }}
                </div>
                <div class="user-chip-info">
                    <div class="user-chip-name">{{ session.get('name') }}</div>
                    <div class="user-chip-role">
                        {% if session.get('role') == 'police' %}Officer{% else %}Citizen{% endif %}
                    </div>
                </div>
            </div>
        </div>
    </aside>

    <!-- Main Area -->
    <div class="main-area">
        <header class="top-bar">
            <div class="top-bar-left">
                <div class="top-bar-title">{% block header_title %}CRMS Portal{% endblock %}</div>
                <div class="top-bar-meta">
                    <span>DB: crimemanagementsystem</span>
                    <span>&bull;</span>
                    <span>MySQL Active</span>
                </div>
            </div>
            <div class="top-bar-right">
                <div class="db-status">
                    <span class="db-status-dot"></span>
                    Live Sync
                </div>
                <a href="{{ url_for('auth.logout') }}" class="btn-logout">Logout</a>
            </div>
        </header>

        <main class="content-body">
            {% with messages = get_flashed_messages(with_categories=true) %}
                {% if messages %}
                    <div class="flash-container">
                        {% for category, message in messages %}
                            <div class="alert alert-{{ category }}">
                                <span>{{ message }}</span>
                                <button type="button" style="background:none;border:none;cursor:pointer;font-size:1.2rem;color:inherit;" onclick="this.parentElement.remove();">&times;</button>
                            </div>
                        {% endfor %}
                    </div>
                {% endif %}
            {% endwith %}

            {% block content %}
                {% if error_title %}
                    <div class="card-panel" style="max-width:600px;margin:3rem auto;text-align:center;">
                        <div class="card-panel-body">
                            <h3 style="color:var(--rose);margin-bottom:0.5rem;">{{ error_title }}</h3>
                            <p style="color:var(--text-secondary);margin-bottom:1.5rem;">{{ error_msg }}</p>
                            <a href="{{ url_for('auth.login') }}" class="btn btn-cyan">Return to Portal</a>
                        </div>
                    </div>
                {% endif %}
            {% endblock %}
        </main>
    </div>
</div>
{% else %}
    <!-- Auth / Unauthenticated Layout -->
    <main>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <div style="max-width:480px;margin:1rem auto 0;padding:0 1rem;">
                    {% for category, message in messages %}
                        <div class="alert alert-{{ category }}">
                            <span>{{ message }}</span>
                            <button type="button" style="background:none;border:none;cursor:pointer;font-size:1.2rem;color:inherit;" onclick="this.parentElement.remove();">&times;</button>
                        </div>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}
        {% block auth_content %}{% endblock %}
    </main>
{% endif %}
<script src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>"""

# ============================================================
# LOGIN.HTML
# ============================================================
login = """{% extends 'base.html' %}
{% block title %}Login &mdash; CRMS Portal{% endblock %}

{% block auth_content %}
<div class="login-root">
    <!-- Left panel -->
    <div class="login-panel-left">
        <div class="lpl-content">
            <div class="lpl-eyebrow">Secure Access</div>
            <h1 class="lpl-title">
                Crime Record<br><span class="accent">Management</span><br>System
            </h1>
            <p class="lpl-desc">
                Official law enforcement portal for filing FIRs, tracking investigations, and managing criminal records in real time.
            </p>
            <div class="lpl-features">
                <div class="lpl-feature"><span class="lpl-feature-dot"></span>Role-based access control (Citizen / Officer)</div>
                <div class="lpl-feature"><span class="lpl-feature-dot"></span>Real-time FIR status tracking pipeline</div>
                <div class="lpl-feature"><span class="lpl-feature-dot"></span>Evidence chain-of-custody management</div>
                <div class="lpl-feature"><span class="lpl-feature-dot"></span>Criminal intelligence registry with threat levels</div>
            </div>
            <a href="{{ url_for('auth.landing') }}" class="lpl-back">
                <svg width="14" height="14" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/></svg>
                Back to Landing
            </a>
        </div>
    </div>

    <!-- Right panel -->
    <div class="login-panel-right">
        <div class="login-box">
            <div class="login-box-header">
                <div class="login-box-title">Access Portal</div>
                <div class="login-box-sub">Select your role and sign in to continue.</div>
            </div>

            <!-- Role Toggle -->
            <div class="role-toggle" id="roleToggle">
                <div class="role-tab active-citizen" data-role="user" id="tabCitizen">
                    <svg width="15" height="15" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
                    Citizen
                </div>
                <div class="role-tab" data-role="police" id="tabPolice">
                    <svg width="15" height="15" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
                    Police Officer
                </div>
            </div>

            <form action="{{ url_for('auth.login') }}" method="POST">
                <input type="hidden" name="role" id="roleInput" value="user">

                <div class="form-field">
                    <label id="emailLabel">Email / Badge ID <span class="req">*</span></label>
                    <div class="input-wrap">
                        <svg class="input-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                        <input type="text" name="email" id="emailInput" class="void-input" placeholder="e.g. walter@gmail.com" required autofocus>
                    </div>
                </div>

                <div class="form-field">
                    <label>Password <span class="req">*</span></label>
                    <div class="input-wrap">
                        <svg class="input-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg>
                        <input type="password" name="password" id="passwordInput" class="void-input" placeholder="Enter your password" required>
                    </div>
                    <div class="form-hint-text">Demo passwords are pre-set in mock data.</div>
                </div>

                <button type="submit" class="submit-btn submit-btn-citizen" id="submitBtn">
                    <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14"/></svg>
                    <span id="submitText">Sign In as Citizen</span>
                </button>
            </form>

            <!-- Demo Citizens -->
            <div class="demo-section" id="userDemoSection">
                <div class="demo-section-label">Quick Demo — Citizens (click to autofill)</div>
                <div class="demo-grid">
                    <div class="demo-card demo-badge-btn" data-email="walter@gmail.com" data-pass="heisenberg@123">
                        <div class="demo-avatar">WW</div>
                        <div><div class="demo-name">Walter White</div><div class="demo-id">walter@gmail.com</div></div>
                    </div>
                    <div class="demo-card demo-badge-btn" data-email="bruce@gmail.com" data-pass="batman@123">
                        <div class="demo-avatar">BW</div>
                        <div><div class="demo-name">Bruce Wayne</div><div class="demo-id">bruce@gmail.com</div></div>
                    </div>
                    <div class="demo-card demo-badge-btn" data-email="tony@gmail.com" data-pass="ironman@123">
                        <div class="demo-avatar">TS</div>
                        <div><div class="demo-name">Tony Stark</div><div class="demo-id">tony@gmail.com</div></div>
                    </div>
                    <div class="demo-card demo-badge-btn" data-email="burt@gmail.com" data-pass="noob@123">
                        <div class="demo-avatar">BB</div>
                        <div><div class="demo-name">Burt Bargain</div><div class="demo-id">burt@gmail.com</div></div>
                    </div>
                </div>
            </div>

            <!-- Demo Officers -->
            <div class="demo-section" id="policeDemoSection" style="display:none;">
                <div class="demo-section-label">Quick Demo &mdash; Officers (click to autofill)</div>
                <div class="demo-grid">
                    <div class="demo-card demo-police demo-badge-btn" data-email="HS002" data-pass="HS002">
                        <div class="demo-avatar demo-avatar-police">HS</div>
                        <div><div class="demo-name">Hank Schrader</div><div class="demo-id">Badge: HS002</div></div>
                    </div>
                    <div class="demo-card demo-police demo-badge-btn" data-email="JG003" data-pass="JG003">
                        <div class="demo-avatar demo-avatar-police">JG</div>
                        <div><div class="demo-name">Jim Gordon</div><div class="demo-id">Badge: JG003</div></div>
                    </div>
                    <div class="demo-card demo-police demo-badge-btn" data-email="raven001" data-pass="raven001">
                        <div class="demo-avatar demo-avatar-police">FC</div>
                        <div><div class="demo-name">Frank Castle</div><div class="demo-id">Badge: raven001</div></div>
                    </div>
                    <div class="demo-card demo-police demo-badge-btn" data-email="SH005" data-pass="SH005">
                        <div class="demo-avatar demo-avatar-police">SH</div>
                        <div><div class="demo-name">Sherlock Holmes</div><div class="demo-id">Badge: SH005</div></div>
                    </div>
                </div>
            </div>

            <div class="auth-footer-link">
                No citizen account? <a href="{{ url_for('auth.register') }}">Register here</a>
            </div>
        </div>
    </div>
</div>
{% endblock %}"""

# ============================================================
# REGISTER.HTML
# ============================================================
register = """{% extends 'base.html' %}
{% block title %}Register &mdash; CRMS Portal{% endblock %}

{% block auth_content %}
<div class="register-root">
    <div class="register-card">
        <div class="register-top">
            <div class="register-top-logo">
                <div class="logo-mark">CR</div>
                <div class="logo-text">CRMS <span style="color:var(--cyan);">Portal</span></div>
            </div>
            <div class="register-title">Citizen Registration</div>
            <div class="register-sub">Create a verified citizen account to file and track FIRs online.</div>
        </div>
        <div class="register-body">
            <form action="{{ url_for('auth.register') }}" method="POST">
                <div class="form-grid-2">
                    <div class="full">
                        <label class="register-label">Full Name <span style="color:var(--rose);">*</span></label>
                        <input type="text" name="name" class="register-input" placeholder="e.g. Walter White" required>
                    </div>
                    <div>
                        <label class="register-label">Email Address <span style="color:var(--rose);">*</span></label>
                        <input type="email" name="email" class="register-input" placeholder="walter@example.com" required>
                    </div>
                    <div>
                        <label class="register-label">Phone Number</label>
                        <input type="text" name="phone" class="register-input" placeholder="9811221145">
                    </div>
                    <div>
                        <label class="register-label">Date of Birth</label>
                        <input type="date" name="dob" class="register-input">
                    </div>
                    <div>
                        <label class="register-label">Gender</label>
                        <select name="gender" class="register-input">
                            <option value="Male">Male</option>
                            <option value="Female">Female</option>
                            <option value="Other">Other</option>
                        </select>
                    </div>
                    <div class="full">
                        <label class="register-label">Residential Address</label>
                        <textarea name="residential_address" class="register-input" rows="2" placeholder="Street Address, City, Postal Code"></textarea>
                    </div>
                    <div class="full">
                        <label class="register-label">Password <span style="color:var(--rose);">*</span></label>
                        <input type="password" name="password" class="register-input" placeholder="Create a secure password" required>
                    </div>
                </div>
                <button type="submit" class="register-btn">
                    <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                    Create Citizen Account
                </button>
            </form>
            <div class="auth-footer-link" style="margin-top:1.25rem;">
                Already registered? <a href="{{ url_for('auth.login') }}">Sign In</a>
            </div>
        </div>
    </div>
</div>
{% endblock %}"""

# ============================================================
# JAVASCRIPT
# ============================================================
js = r"""// CRMS Void Terminal — script.js

(function () {
  'use strict';

  /* ---- Role selector on login page ---- */
  var toggle = document.getElementById('roleToggle');
  if (toggle) {
    var tabs = toggle.querySelectorAll('.role-tab');
    var roleInput = document.getElementById('roleInput');
    var emailInput = document.getElementById('emailInput');
    var emailLabel = document.getElementById('emailLabel');
    var submitBtn = document.getElementById('submitBtn');
    var submitText = document.getElementById('submitText');
    var userDemo = document.getElementById('userDemoSection');
    var policeDemo = document.getElementById('policeDemoSection');

    tabs.forEach(function (tab) {
      tab.addEventListener('click', function () {
        tabs.forEach(function (t) {
          t.classList.remove('active-citizen', 'active-police');
        });

        var role = tab.getAttribute('data-role');
        roleInput.value = role;

        if (role === 'police') {
          tab.classList.add('active-police');
          if (emailLabel) emailLabel.textContent = 'Badge Number *';
          if (emailInput) { emailInput.placeholder = 'e.g. HS002'; emailInput.value = ''; }
          if (submitBtn) { submitBtn.classList.remove('submit-btn-citizen'); submitBtn.classList.add('submit-btn-police'); }
          if (submitText) submitText.textContent = 'Sign In as Officer';
          if (userDemo) userDemo.style.display = 'none';
          if (policeDemo) policeDemo.style.display = 'block';
          /* police focus */
          var voids = document.querySelectorAll('.void-input');
          voids.forEach(function(v){ v.classList.add('police-focus'); });
        } else {
          tab.classList.add('active-citizen');
          if (emailLabel) emailLabel.textContent = 'Email Address *';
          if (emailInput) { emailInput.placeholder = 'e.g. walter@gmail.com'; emailInput.value = ''; }
          if (submitBtn) { submitBtn.classList.remove('submit-btn-police'); submitBtn.classList.add('submit-btn-citizen'); }
          if (submitText) submitText.textContent = 'Sign In as Citizen';
          if (userDemo) userDemo.style.display = 'block';
          if (policeDemo) policeDemo.style.display = 'none';
          var voids = document.querySelectorAll('.void-input');
          voids.forEach(function(v){ v.classList.remove('police-focus'); });
        }
      });
    });
  }

  /* ---- Demo card autofill ---- */
  document.querySelectorAll('.demo-badge-btn').forEach(function (card) {
    card.addEventListener('click', function () {
      var email = card.getAttribute('data-email');
      var pass = card.getAttribute('data-pass');
      var emailEl = document.getElementById('emailInput') || document.querySelector('[name="email"]');
      var passEl = document.getElementById('passwordInput') || document.querySelector('[name="password"]');
      if (emailEl) emailEl.value = email;
      if (passEl) passEl.value = pass;
    });
  });

  /* ---- Table search filter ---- */
  var searchInput = document.getElementById('tableSearchInput');
  if (searchInput) {
    searchInput.addEventListener('input', function () {
      var q = this.value.toLowerCase();
      var tables = document.querySelectorAll('.data-table tbody');
      tables.forEach(function (tbody) {
        var rows = tbody.querySelectorAll('tr');
        rows.forEach(function (row) {
          var text = row.textContent.toLowerCase();
          row.style.display = text.includes(q) ? '' : 'none';
        });
      });
    });
  }

  /* ---- Status filter ---- */
  var statusFilter = document.getElementById('statusFilterSelect');
  if (statusFilter) {
    statusFilter.addEventListener('change', function () {
      var val = this.value.toLowerCase();
      var tables = document.querySelectorAll('.data-table tbody');
      tables.forEach(function (tbody) {
        var rows = tbody.querySelectorAll('tr');
        rows.forEach(function (row) {
          if (!val) { row.style.display = ''; return; }
          var text = row.textContent.toLowerCase();
          row.style.display = text.includes(val) ? '' : 'none';
        });
      });
    });
  }

  /* ---- Greeting on user dashboard ---- */
  var greetEl = document.getElementById('timeGreeting');
  if (greetEl) {
    var h = new Date().getHours();
    var greeting = h < 12 ? 'Good Morning' : h < 17 ? 'Good Afternoon' : 'Good Evening';
    greetEl.textContent = greeting;
  }

  /* ---- Counter animation ---- */
  function animateCount(el, target, suffix) {
    suffix = suffix || '';
    var start = 0;
    var dur = 1200;
    var step = target / (dur / 16);
    var interval = setInterval(function () {
      start += step;
      if (start >= target) { start = target; clearInterval(interval); }
      el.textContent = Math.floor(start) + suffix;
    }, 16);
  }

  document.querySelectorAll('[data-count]').forEach(function (el) {
    var target = parseInt(el.getAttribute('data-count'), 10);
    var suffix = el.textContent.includes('%') ? '%' : '';
    animateCount(el, target, suffix);
  });

  /* ---- Intersection observer for anim-fade-up ---- */
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    document.querySelectorAll('.anim-fade-up').forEach(function (el) {
      el.style.opacity = '0';
      el.style.transform = 'translateY(20px)';
      el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
      io.observe(el);
    });
  }

  /* ---- Flash auto-dismiss ---- */
  document.querySelectorAll('.alert, .flash-msg').forEach(function (msg) {
    setTimeout(function () {
      msg.style.transition = 'opacity 0.4s ease';
      msg.style.opacity = '0';
      setTimeout(function () { msg.remove(); }, 400);
    }, 5000);
  });

})();
"""

# Write all files
w(os.path.join(S, 'css', 'style.css'), css)
w(os.path.join(T, 'landing.html'), landing)
w(os.path.join(T, 'base.html'), base)
w(os.path.join(T, 'login.html'), login)
w(os.path.join(T, 'register.html'), register)
w(os.path.join(S, 'js', 'script.js'), js)

print("\nAll files written successfully!")
