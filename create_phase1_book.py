# -*- coding: utf-8 -*-
"""
Generator for Phase 1 Master Book Edition (Phase_1_Number_System.html)
"""

import sys

def get_head_and_styles():
    return r'''<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SSC CGL Maths — Phase 1: Number System (Complete Master Book Edition) | संख्या प्रणाली</title>
  <meta name="description" content="SSC CGL Maths Phase 1: Number System complete textbook edition with 6 comprehensive theory chapters, 10 formula cards, 6 shortcuts, 6 traps, 20 basic questions, 20 mixed questions, 15 PYQs, interactive timed drill and 1-click print export.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
:root {
  --bg: #080B12;
  --surface: #0f1623;
  --surface-elevated: #162035;
  --border: #1e2e47;
  --text: #F0F4F8;
  --text-muted: #7A90A8;
  --primary: #00e5ff;
  --gold: #f6c244;
  --green: #22d3a5;
  --red: #f16a6a;
  --violet: #a78bfa;
  --orange: #fb923c;
  --shadow-cyan: rgba(0,229,255,0.08);
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; scroll-padding-top: 130px; }
body {
  background: var(--bg);
  color: var(--text);
  font-family: 'Poppins', sans-serif;
  line-height: 1.65;
  padding: 16px;
  font-size: 15px;
  max-width: 100vw;
  overflow-x: hidden;
}
.container { max-width: 1180px; margin: 0 auto; }

/* ── STICKY TOPIC NAV BAR ── */
.topic-nav-bar {
  position: sticky; top: 62px; z-index: 180;
  display: flex; align-items: center; gap: 8px;
  background: rgba(15, 22, 35, 0.95);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 8px 14px;
  margin-bottom: 20px;
  backdrop-filter: blur(12px);
  overflow-x: auto;
  white-space: nowrap;
  scrollbar-width: none;
  box-shadow: 0 4px 15px rgba(0,0,0,0.3);
}
.topic-nav-bar::-webkit-scrollbar { display: none; }
.topic-nav-label {
  font-size: 0.72rem; font-weight: 800; color: var(--gold);
  text-transform: uppercase; letter-spacing: 0.8px;
  display: flex; align-items: center; gap: 5px; flex-shrink: 0;
  padding-right: 8px; border-right: 1px solid var(--border);
}
.tnav-chip {
  background: var(--surface-elevated); color: var(--text-muted);
  border: 1px solid var(--border); padding: 5px 12px;
  border-radius: 20px; font-size: 0.75rem; font-weight: 600;
  text-decoration: none; transition: all 0.2s ease;
  display: inline-flex; align-items: center; gap: 5px; flex-shrink: 0;
}
.tnav-chip:hover {
  border-color: var(--primary); color: #fff;
  background: rgba(0, 229, 255, 0.12);
  transform: translateY(-1px);
}
.tnav-chip.active {
  background: linear-gradient(90deg, rgba(246,194,68,0.2), rgba(0,229,255,0.2));
  border-color: var(--primary); color: var(--primary);
  box-shadow: 0 0 10px rgba(0,229,255,0.2);
}

/* ── TOPIC HUB DIRECTORY ── */
.topic-hub-section {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 22px;
  margin-bottom: 24px;
}
.topic-hub-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 14px;
  margin-top: 14px;
}
.topic-hub-card {
  background: var(--surface-elevated);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 16px;
  transition: all 0.25s ease;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.topic-hub-card:hover {
  border-color: var(--primary);
  box-shadow: 0 4px 18px rgba(0,229,255,0.12);
  transform: translateY(-2px);
}
.thc-header {
  display: flex; justify-content: space-between; align-items: flex-start;
  margin-bottom: 8px;
}
.thc-badge {
  font-size: 0.68rem; font-weight: 700; padding: 2px 8px; border-radius: 4px;
  background: rgba(0,229,255,0.12); color: var(--primary); border: 1px solid rgba(0,229,255,0.25);
}
.thc-weight {
  font-size: 0.7rem; color: var(--gold); font-weight: 600;
}
.thc-title {
  font-size: 0.98rem; font-weight: 700; color: #fff; margin-bottom: 6px;
}
.thc-desc {
  font-size: 0.8rem; color: #94a3b8; line-height: 1.5; margin-bottom: 12px; flex-grow: 1;
}
.thc-actions {
  display: flex; gap: 8px; margin-top: 10px;
}
.thc-btn {
  flex: 1; text-align: center; font-size: 0.74rem; font-weight: 600;
  padding: 6px 10px; border-radius: 6px; text-decoration: none;
  transition: all 0.2s;
}
.thc-btn-theory {
  background: rgba(246,194,68,0.12); color: var(--gold); border: 1px solid rgba(246,194,68,0.3);
}
.thc-btn-theory:hover {
  background: var(--gold); color: #080b12;
}
.thc-btn-practice {
  background: rgba(34,211,165,0.12); color: var(--green); border: 1px solid rgba(34,211,165,0.3);
}
.thc-btn-practice:hover {
  background: var(--green); color: #080b12;
}

/* ── TOPIC FILTER BAR IN QUESTIONS ── */
.topic-filter-bar {
  display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 18px;
  background: var(--surface-elevated); padding: 12px 14px;
  border-radius: 12px; border: 1px solid var(--border);
  align-items: center;
}
.filter-label {
  font-size: 0.78rem; font-weight: 700; color: var(--gold); margin-right: 6px;
}
.q-filter-chip {
  background: var(--surface); color: var(--text-muted);
  border: 1px solid var(--border); padding: 5px 12px;
  border-radius: 16px; font-size: 0.74rem; font-weight: 600;
  cursor: pointer; transition: all 0.2s;
}
.q-filter-chip:hover {
  border-color: var(--primary); color: #fff;
}
.q-filter-chip.active {
  background: var(--primary); color: #080b12; border-color: var(--primary);
  font-weight: 700;
}
.topic-anchor-block {
  scroll-margin-top: 130px;
}

/* ── TOPBAR ── */
.topbar {
  position: sticky; top: 0; z-index: 200;
  display: flex; align-items: center; justify-content: space-between;
  background: rgba(9,14,24,0.95);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 10px 18px;
  margin-bottom: 18px;
  backdrop-filter: blur(12px);
  gap: 12px;
}
.brand { display:flex; align-items:center; gap:8px; font-weight:700; font-size:0.95rem; color:var(--primary); text-decoration:none; white-space:nowrap; }
.topbar-actions { display:flex; gap:6px; flex-wrap:wrap; align-items:center; }
.tb-btn {
  background: var(--surface-elevated); color:var(--text-muted);
  border:1px solid var(--border); padding:5px 11px;
  border-radius:8px; font-size:0.76rem; cursor:pointer;
  text-decoration:none; transition:all 0.2s; white-space:nowrap; font-weight:500;
}
.tb-btn:hover { border-color:var(--primary); color:var(--primary); }

/* ── HERO ── */
.phase-hero {
  background: linear-gradient(135deg, rgba(121,40,202,0.15), rgba(0,229,255,0.12));
  border:1px solid var(--border); border-radius:18px;
  padding: 32px 20px; text-align:center; margin-bottom:22px;
  position:relative; overflow:hidden;
}
.phase-badge {
  display:inline-block;
  background:linear-gradient(90deg,#7928ca,#00e5ff);
  color:#fff; font-weight:700; font-size:0.75rem;
  padding:5px 16px; border-radius:50px; margin-bottom:12px;
  letter-spacing:1px; text-transform:uppercase;
}
h1 {
  font-size:2rem; font-weight:800;
  background:linear-gradient(90deg,#fff,#00e5ff);
  -webkit-background-clip:text; -webkit-text-fill-color:transparent;
  margin-bottom:6px;
}
.hero-hindi { color:var(--text-muted); font-size:0.95rem; margin-bottom:12px; }
.hero-stats {
  display:flex; justify-content:center; gap:10px; flex-wrap:wrap; margin-top:14px;
}
.hstat-card {
  background:var(--surface); border:1px solid var(--border);
  border-radius:10px; padding:8px 14px; font-size:0.8rem;
}
.hstat-val { font-weight:800; color:var(--primary); font-size:1.1rem; }

/* ── MASTERY TRACKER ── */
.mastery-tracker {
  background:var(--surface); border:1px solid var(--border);
  border-radius:14px; padding:18px; margin-bottom:22px;
}
.mastery-title { font-weight:700; font-size:1rem; margin-bottom:12px; color:#fff; display:flex; align-items:center; gap:8px; }
.mastery-levels { display:grid; grid-template-columns:repeat(5,1fr); gap:8px; }
.ml-card {
  border-radius:10px; padding:10px 6px; text-align:center;
  border:1px solid var(--border); cursor:pointer; transition:all 0.2s;
  background:var(--surface-elevated);
}
.ml-card:hover { transform:translateY(-2px); }
.ml-card.selected { border-color:var(--primary); box-shadow:0 0 12px var(--shadow-cyan); }
.ml-label { font-size:0.68rem; font-weight:700; color:var(--text-muted); }
.ml-level { font-size:1.1rem; font-weight:800; color:var(--primary); }
.ml-desc { font-size:0.66rem; color:var(--text-muted); margin-top:2px; }
.ml-0 .ml-level { color:#64748b; }
.ml-1 .ml-level { color:#f59e0b; }
.ml-2 .ml-level { color:#22d3ee; }
.ml-3 .ml-level { color:#10b981; }
.ml-4 .ml-level { color:#f6c244; }

/* ── CHAPTER BOOK SECTIONS ── */
.book-chapter {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 24px 26px;
  margin-bottom: 22px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.2);
}
.chap-badge {
  display:inline-block; background:rgba(0,229,255,0.1); color:var(--primary);
  font-size:0.72rem; font-weight:700; padding:3px 10px; border-radius:6px; margin-bottom:8px;
  border:1px solid rgba(0,229,255,0.2);
}
.chap-title {
  font-size:1.3rem; font-weight:700; color:#fff; margin-bottom:14px;
  display:flex; align-items:center; gap:8px; border-bottom:1px solid rgba(255,255,255,0.06);
  padding-bottom:8px;
}
.sec-title {
  font-size:1.2rem; font-weight:700; color:#fff;
  margin-bottom:14px; display:flex; align-items:center; gap:8px;
  padding-bottom:8px; border-bottom:1px solid var(--border);
}
.book-p {
  font-size:0.92rem; color:#cbd5e1; line-height:1.75; margin-bottom:12px;
}
.book-list {
  list-style:none; padding-left:0; margin-bottom:14px;
}
.book-list li {
  font-size:0.9rem; color:#b0c4de; padding:5px 0;
  display:flex; align-items:flex-start; gap:8px;
}
.book-list li::before {
  content:'✦'; color:var(--primary); font-size:0.8rem; flex-shrink:0; margin-top:3px;
}
.concept-callout {
  background: rgba(0,229,255,0.04);
  border-left: 4px solid var(--primary);
  border-radius: 0 10px 10px 0;
  padding: 12px 16px;
  margin: 14px 0;
  font-size: 0.9rem;
  color: #e2f8ff;
}
.table-wrap { overflow-x:auto; margin:14px 0; border-radius:10px; border:1px solid var(--border); }
.book-table {
  width:100%; border-collapse:collapse; font-size:0.86rem; text-align:left;
}
.book-table th {
  background: var(--surface-elevated); color:var(--primary);
  padding:10px 14px; font-weight:600; border-bottom:1px solid var(--border);
}
.book-table td {
  padding:9px 14px; border-bottom:1px solid rgba(255,255,255,0.04); color:#cbd5e1;
}
.book-table tr:hover td { background:rgba(0,229,255,0.02); }

/* ── DAY PLAN ── */
.day-cards { display:flex; flex-direction:column; gap:10px; margin-bottom:22px; }
.day-card {
  background:var(--surface-elevated); border:1px solid var(--border);
  border-radius:12px; padding:14px;
  display:grid; grid-template-columns:120px 1fr;
  gap:12px; align-items:start;
}
.day-label {
  background:linear-gradient(135deg,rgba(121,40,202,0.2),rgba(0,229,255,0.15));
  border:1px solid var(--border); border-radius:8px;
  text-align:center; padding:10px 6px;
}
.day-tag { font-size:0.75rem; font-weight:700; color:var(--primary); }
.day-name { font-size:0.82rem; font-weight:600; color:#fff; margin:2px 0; }
.day-drill { font-size:0.68rem; color:var(--gold); }
.day-topics { list-style:none; padding:0; }
.day-topics li {
  font-size:0.83rem; color:#b0c4de; padding:3px 0;
  border-bottom:1px solid rgba(255,255,255,0.03);
  display:flex; align-items:flex-start; gap:6px;
}
.day-topics li::before { content:'→'; color:var(--primary); flex-shrink:0; margin-top:1px; }

/* ── FORMULA VAULT ── */
.formula-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(330px,1fr)); gap:12px; margin-bottom:22px; }
.formula-card {
  background:var(--surface); border:1px solid rgba(0,229,255,0.12);
  border-radius:12px; overflow:hidden;
}
.fc-header {
  background:rgba(0,229,255,0.06); border-bottom:1px solid rgba(0,229,255,0.12);
  padding:10px 14px; display:flex; align-items:center; justify-content:space-between;
}
.fc-name { font-weight:700; color:var(--primary); font-size:0.88rem; }
.copy-btn {
  background:var(--surface-elevated); color:var(--text-muted);
  border:1px solid var(--border); padding:3px 8px;
  border-radius:6px; font-size:0.7rem; cursor:pointer; transition:all 0.2s;
}
.copy-btn:hover { color:var(--primary); border-color:var(--primary); }
.fc-body { padding:12px 14px; }
.fc-formula {
  background:var(--surface-elevated); border-left:3px solid var(--primary);
  padding:10px 12px; border-radius:6px; margin-bottom:8px;
  font-family:'Fira Code',monospace; font-size:0.86rem; color:#e2f8ff; word-break:break-all;
}
.fc-row { font-size:0.8rem; margin-bottom:6px; color:#b0c4de; }
.fc-row strong { color:#e2e8f0; }
.fc-trap { font-size:0.78rem; color:var(--red); background:rgba(241,106,106,0.07); border-left:3px solid var(--red); padding:6px 10px; border-radius:4px; margin-top:8px; }

/* ── SHORTCUTS & TRAPS ── */
.shortcut-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:12px; margin-bottom:22px; }
.shortcut-card {
  background:rgba(246,194,68,0.05); border:1px solid rgba(246,194,68,0.2);
  border-radius:12px; padding:14px;
}
.sc-title { color:var(--gold); font-weight:700; margin-bottom:8px; font-size:0.88rem; }
.sc-content { font-size:0.83rem; color:#c8d8ec; line-height:1.6; }

.trap-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:12px; margin-bottom:22px; }
.trap-card {
  background:rgba(241,106,106,0.05); border:1px solid rgba(241,106,106,0.2);
  border-radius:12px; padding:14px;
}
.trap-header { display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; }
.trap-title { color:var(--red); font-weight:700; font-size:0.88rem; }
.error-code {
  background:rgba(241,106,106,0.15); color:var(--red);
  font-size:0.7rem; font-weight:800; padding:2px 8px;
  border-radius:4px; letter-spacing:1px;
}
.trap-desc { font-size:0.82rem; color:#c8d8ec; }

/* ── QUESTIONS BLOCKS (ACCORDION CARDS) ── */
.q-block {
  background: var(--surface-elevated);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 16px 18px;
  margin-bottom: 14px;
  transition: border-color 0.2s;
}
.q-block:hover { border-color: rgba(0,229,255,0.3); }
.q-head {
  display: flex; justify-content: space-between; align-items: center;
  margin-bottom: 10px; flex-wrap: wrap; gap: 8px;
}
.q-num {
  font-weight: 700; font-size: 0.85rem; color: var(--primary);
  background: rgba(0,229,255,0.08); padding: 2px 10px; border-radius: 6px;
}
.q-tag {
  font-size: 0.72rem; color: var(--gold);
  background: rgba(246,194,68,0.1); padding: 2px 8px; border-radius: 4px;
}
.q-text {
  font-size: 0.95rem; color: #fff; font-weight: 500;
  line-height: 1.6; margin-bottom: 12px;
}
.q-actions { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 10px; }
.q-btn {
  padding: 6px 14px; border-radius: 6px; font-size: 0.78rem;
  font-weight: 600; cursor: pointer; border: 1px solid;
  transition: all 0.2s;
}
.btn-hint { background: rgba(246,194,68,0.1); color: var(--gold); border-color: rgba(246,194,68,0.3); }
.btn-hint:hover { background: rgba(246,194,68,0.2); }
.btn-sol { background: rgba(34,211,165,0.1); color: var(--green); border-color: rgba(34,211,165,0.3); }
.btn-sol:hover { background: rgba(34,211,165,0.2); }
.hint-content, .sol-content {
  display: none; padding: 12px 14px; border-radius: 8px;
  font-size: 0.88rem; line-height: 1.6; margin-top: 10px;
}
.hint-content { background: rgba(246,194,68,0.06); border-left: 3px solid var(--gold); color: #fde68a; }
.sol-content { background: rgba(34,211,165,0.06); border-left: 3px solid var(--green); color: #a7f3d0; }
.self-rate-row {
  display: flex; gap: 8px; align-items: center; margin-top: 10px;
  padding-top: 8px; border-top: 1px solid rgba(255,255,255,0.04);
  font-size: 0.78rem; color: var(--text-muted); flex-wrap: wrap;
}
.rate-btn {
  background: var(--surface); border: 1px solid var(--border);
  color: var(--text-muted); padding: 3px 8px; border-radius: 4px;
  cursor: pointer; font-size: 0.72rem; transition: all 0.15s;
}
.rate-btn:hover { border-color: var(--primary); color: #fff; }

/* ── PYQ CARDS ── */
.pyq-card {
  background: var(--surface-elevated);
  border: 1px solid rgba(167,139,250,0.2);
  border-radius: 12px;
  padding: 16px 18px;
  margin-bottom: 14px;
}
.pyq-tag {
  display: inline-block; background: rgba(167,139,250,0.15); color: var(--violet);
  font-size: 0.72rem; font-weight: 700; padding: 3px 10px; border-radius: 4px; margin-bottom: 8px;
}
.pyq-q { font-size: 0.95rem; color: #fff; font-weight: 500; margin-bottom: 12px; line-height: 1.6; }
.reveal-sol-btn {
  background: rgba(167,139,250,0.1); color: var(--violet);
  border: 1px solid rgba(167,139,250,0.3); padding: 6px 14px;
  border-radius: 6px; font-size: 0.78rem; cursor: pointer; font-weight: 600;
  transition: all 0.2s;
}
.reveal-sol-btn:hover { background: rgba(167,139,250,0.2); }
.sol-box {
  margin-top: 12px; padding: 12px 14px; border-radius: 8px;
  background: rgba(167,139,250,0.06); border-left: 3px solid var(--violet);
  color: #ddd6fe; font-size: 0.88rem; line-height: 1.6; display: none;
}

/* ── TIMED DRILL ── */
.timed-drill {
  background:var(--surface); border:1px solid var(--border);
  border-radius:14px; padding:20px; margin-bottom:22px;
}
.timer-display {
  font-size:2.8rem; font-weight:800; color:var(--primary);
  font-family:'Fira Code',monospace; text-align:center; margin:12px 0;
  text-shadow:0 0 20px rgba(0,229,255,0.4);
}
.timer-controls { display:flex; gap:10px; justify-content:center; flex-wrap:wrap; margin-bottom:14px; }
.timer-btn {
  padding:8px 20px; border-radius:8px; font-size:0.85rem; font-weight:600;
  cursor:pointer; border:1px solid; transition:all 0.2s;
}
.t-start { background:rgba(34,211,165,0.1); color:var(--green); border-color:rgba(34,211,165,0.4); }
.t-pause { background:rgba(246,194,68,0.1); color:var(--gold); border-color:rgba(246,194,68,0.4); }
.t-reset { background:rgba(241,106,106,0.1); color:var(--red); border-color:rgba(241,106,106,0.4); }
.score-input-row { display:flex; gap:10px; align-items:center; flex-wrap:wrap; justify-content:center; margin-top:12px; }
.score-input {
  background:var(--surface-elevated); border:1px solid var(--border);
  color:var(--text); padding:6px 12px; border-radius:6px;
  font-size:1rem; font-weight:700; width:65px; text-align:center;
}
.score-label { font-size:0.82rem; color:var(--text-muted); }
.score-result {
  margin-top:14px; padding:12px; border-radius:8px; text-align:center; display:none;
  font-size:0.95rem; font-weight:700;
}
.score-pass { background:rgba(34,211,165,0.1); border:1px solid rgba(34,211,165,0.3); color:var(--green); }
.score-fail { background:rgba(241,106,106,0.1); border:1px solid rgba(241,106,106,0.3); color:var(--red); }
.score-ok { background:rgba(246,194,68,0.1); border:1px solid rgba(246,194,68,0.3); color:var(--gold); }

/* ── ACTIVE RECALL ── */
.recall-section {
  background:var(--surface); border:1px solid rgba(246,194,68,0.2);
  border-radius:14px; padding:18px; margin-bottom:22px;
}
.recall-how { display:flex; gap:0; margin-bottom:14px; overflow-x:auto; padding-bottom:6px; }
.recall-step { display:flex; align-items:center; gap:0; flex-shrink:0; }
.rs-box {
  background:rgba(246,194,68,0.08); border:1px solid rgba(246,194,68,0.25);
  border-radius:8px; padding:6px 12px; font-size:0.75rem; color:var(--gold); white-space:nowrap;
}
.rs-arrow { color:var(--gold); margin:0 4px; font-size:0.9rem; }
.recall-qs { display:flex; flex-direction:column; gap:8px; }
.recall-q {
  background:var(--surface-elevated); border:1px solid var(--border);
  border-radius:8px; padding:10px 14px; display:flex; justify-content:space-between; align-items:center; gap:12px;
}
.rq-text { font-size:0.86rem; color:#b0c4de; }
.rq-check { accent-color:var(--gold); width:16px; height:16px; cursor:pointer; flex-shrink:0; }

/* ── ERROR NOTEBOOK ── */
.error-notebook {
  background:var(--surface); border:1px solid rgba(241,106,106,0.2);
  border-radius:14px; padding:18px; margin-bottom:22px;
}
.error-codes-ref { display:flex; flex-wrap:wrap; gap:8px; margin-bottom:14px; }
.ec-pill {
  background:rgba(241,106,106,0.08); border:1px solid rgba(241,106,106,0.2);
  padding:3px 10px; border-radius:6px; font-size:0.75rem; color:#f8a0a0;
}
.ec-pill strong { color:var(--red); }
.error-table { width:100%; border-collapse:collapse; font-size:0.8rem; }
.error-table th { background:rgba(241,106,106,0.08); color:var(--red); padding:8px 10px; border-bottom:1px solid rgba(241,106,106,0.2); text-align:left; }
.error-table td { padding:8px 10px; border-bottom:1px solid rgba(255,255,255,0.04); color:#cbd5e1; }
.error-input { background:var(--surface-elevated); border:1px solid var(--border); color:#fff; padding:4px 8px; border-radius:4px; font-size:0.78rem; width:100%; }

/* ── SIDEBAR DRAWER ── */
.sidebar-backdrop {
  position:fixed; inset:0; background:rgba(0,0,0,0.6);
  z-index:290; opacity:0; pointer-events:none; transition:opacity 0.3s;
  backdrop-filter:blur(4px);
}
.sidebar-backdrop.active { opacity:1; pointer-events:auto; }
.sidebar-drawer {
  position:fixed; top:0; left:0; bottom:0; width:310px; max-width:85vw;
  background:var(--surface); border-right:1px solid var(--border);
  z-index:300; transform:translateX(-100%); transition:transform 0.3s ease;
  display:flex; flex-direction:column; overflow:hidden;
}
.sidebar-drawer.open { transform:translateX(0); }
.sidebar-header {
  padding:14px 18px; border-bottom:1px solid var(--border);
  display:flex; align-items:center; justify-content:space-between;
}
.sb-brand { display:flex; align-items:center; gap:8px; }
.sb-brand-icon { font-size:1.3rem; }
.sb-brand-text { font-weight:700; font-size:0.95rem; color:var(--primary); }
.sb-brand-sub { font-size:0.68rem; color:var(--text-muted); }
.sidebar-close-btn {
  background:none; border:none; color:var(--text-muted); font-size:1.1rem;
  cursor:pointer; padding:4px 8px; border-radius:4px;
}
.sidebar-close-btn:hover { color:#fff; }
.sidebar-content { flex:1; overflow-y:auto; padding:14px; }
.sb-group-title {
  font-size:0.72rem; font-weight:700; color:var(--text-muted);
  text-transform:uppercase; letter-spacing:1px; margin:12px 0 6px 0;
  display:flex; justify-content:space-between;
}
.sb-toc-grid { display:grid; grid-template-columns:1fr; gap:4px; margin-bottom:14px; }
.sb-toc-link {
  display:flex; align-items:center; gap:8px; padding:7px 10px;
  border-radius:6px; color:#cbd5e1; font-size:0.8rem; text-decoration:none;
  transition:all 0.15s;
}
.sb-toc-link:hover { background:var(--surface-elevated); color:var(--primary); }
.sb-phase-item {
  display:flex; align-items:center; justify-content:space-between;
  padding:8px 10px; border-radius:8px; margin-bottom:4px;
  background:var(--surface-elevated); border:1px solid transparent;
  color:#cbd5e1; text-decoration:none; font-size:0.78rem; transition:all 0.15s;
}
.sb-phase-item:hover { border-color:var(--primary); color:var(--primary); }
.sb-phase-item.active { border-color:var(--primary); background:rgba(0,229,255,0.08); color:#fff; }

/* ── PRINT MODAL ── */
.print-modal-overlay {
  display:none; position:fixed; inset:0; background:rgba(0,0,0,0.75);
  z-index:999; align-items:center; justify-content:center; padding:16px;
  backdrop-filter:blur(5px);
}
.print-modal {
  background:var(--surface); border:1px solid var(--border);
  border-radius:16px; max-width:540px; width:100%; padding:24px;
  position:relative; box-shadow:0 8px 32px rgba(0,0,0,0.4);
}
.print-modal h3 { font-size:1.2rem; color:#fff; margin-bottom:8px; }
.print-modal p { font-size:0.85rem; color:#94a3b8; margin-bottom:16px; }
.print-actions { display:flex; gap:10px; justify-content:flex-end; }
.print-btn-primary {
  background:var(--primary); color:#080b12; font-weight:700;
  border:none; padding:8px 18px; border-radius:8px; cursor:pointer; font-size:0.85rem;
}
.print-btn-sec {
  background:var(--surface-elevated); color:#cbd5e1; border:1px solid var(--border);
  padding:8px 16px; border-radius:8px; cursor:pointer; font-size:0.85rem;
}

/* ── PRINT STYLES ── */
@media print {
  body { background:#fff !important; color:#000 !important; font-size:11pt; padding:0; }
  .topbar, .sidebar-drawer, .sidebar-backdrop, .q-actions, .self-rate-row, .reveal-sol-btn,
  .timer-controls, .score-input-row, .print-modal-overlay, .copy-btn { display:none !important; }
  .book-chapter, .day-card, .formula-card, .shortcut-card, .trap-card, .q-block, .pyq-card, .timed-drill, .recall-section, .error-notebook {
    background:#fff !important; color:#000 !important; border:1px solid #ccc !important;
    box-shadow:none !important; page-break-inside:avoid; margin-bottom:12pt;
  }
  .hint-content, .sol-content, .sol-box { display:block !important; color:#000 !important; background:#f8f9fa !important; border-left:2pt solid #000 !important; }
  h1, h2, h3, .chap-title, .sec-title, .q-text, .pyq-q { color:#000 !important; -webkit-text-fill-color:initial !important; }
  .book-p, .fc-row, .book-table td, .book-table th, .rq-text { color:#222 !important; }
}

@media (max-width: 768px) {
  body { padding: 10px; }
  .day-card { grid-template-columns: 1fr; }
  .mastery-levels { grid-template-columns: repeat(3, 1fr); }
  .timer-display { font-size: 2.2rem; }
  h1 { font-size: 1.6rem; }
}
</style>
  <!-- Polyfill & MathJax 3 -->
  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
<div class="container">
'''

print("Head and styles ready.")
