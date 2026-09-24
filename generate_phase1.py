# -*- coding: utf-8 -*-
"""
Complete Phase 1: Number System Master Book Generator
Adheres 100% to AI Tutor Rule.md:
- Detailed book-like theory (6 chapters)
- Formula Vault (10 cards)
- Speed Shortcuts (6) & Traps (6)
- 20 Basic Questions (Q1 to Q20)
- 20 Mixed Questions (Q21 to Q40)
- 15 Verified SSC PYQs (Q41 to Q55)
- Timed Drill Stopwatch & Score Calculator
- Active Recall, Mistake Log, Checklist, Print Modal
"""

import sys

def get_topbar_and_hero():
    return r'''
  <!-- TOPBAR -->
  <nav class="topbar">
    <a href="index.html" class="brand">
      <span>⚡</span>
      <span>SSC CGL Maths Prep</span>
    </a>
    <div class="topbar-actions">
      <button class="tb-btn" id="sidebar-toggle-btn">☰ All Phases</button>
      <a href="#sec-theory" class="tb-btn">📖 Theory (6 Ch)</a>
      <a href="#sec-plan" class="tb-btn">📅 Plan</a>
      <a href="#sec-formulas" class="tb-btn">📐 Formulas</a>
      <a href="#sec-basic" class="tb-btn">🟢 20 Basic Qs</a>
      <a href="#sec-mixed" class="tb-btn">🟡 20 Mixed Qs</a>
      <a href="#sec-pyq" class="tb-btn">🏆 15 PYQs</a>
      <a href="#sec-timer" class="tb-btn">⏱️ Drill</a>
      <button class="tb-btn" onclick="openPrintModal()">🖨️ Print Book</button>
    </div>
  </nav>

  <!-- HERO -->
  <header class="phase-hero">
    <span class="phase-badge">Phase 1 • Days 6–12 • Complete Book Edition</span>
    <h1>Phase 1: Number System (संख्या प्रणाली)</h1>
    <p class="hero-hindi">Complete Exhaustive Study Book — To the Point, Conceptual & Practical</p>
    <div class="hero-stats">
      <div class="hstat-card"><div class="hstat-val">6</div><div>Book Chapters</div></div>
      <div class="hstat-card"><div class="hstat-val">10</div><div>Formula Cards</div></div>
      <div class="hstat-card"><div class="hstat-val">20</div><div>Basic Foundation Qs</div></div>
      <div class="hstat-card"><div class="hstat-val">20</div><div>Mixed / Tricky Qs</div></div>
      <div class="hstat-card"><div class="hstat-val">15</div><div>Verified SSC PYQs</div></div>
      <div class="hstat-card"><div class="hstat-val">55</div><div>Total Graded Qs</div></div>
    </div>
  </header>

  <!-- MASTERY TRACKER -->
  <div class="mastery-tracker" id="sec-mastery">
    <div class="mastery-title">📊 My Current Mastery Level — Click to Update</div>
    <div class="mastery-levels">
      <div class="ml-card ml-0" data-level="0">
        <div class="ml-label">L0</div><div class="ml-level">◉</div><div class="ml-desc">Not Started</div>
      </div>
      <div class="ml-card ml-1" data-level="1">
        <div class="ml-label">L1</div><div class="ml-level">○◉</div><div class="ml-desc">Concept Learned</div>
      </div>
      <div class="ml-card ml-2" data-level="2">
        <div class="ml-label">L2</div><div class="ml-level">○○◉</div><div class="ml-desc">Basic Solving (70%+)</div>
      </div>
      <div class="ml-card ml-3" data-level="3">
        <div class="ml-label">L3</div><div class="ml-level">○○○◉</div><div class="ml-desc">Exam Ready (80%+)</div>
      </div>
      <div class="ml-card ml-4" data-level="4">
        <div class="ml-label">L4</div><div class="ml-level">⭐</div><div class="ml-desc">Mastered (90%+)</div>
      </div>
    </div>
    <div style="margin-top:10px;font-size:0.78rem;color:var(--text-muted);">
      ⚠️ <strong>AI Tutor Rule:</strong> Phase ko complete tabhi mark karo jab mastery drill me &ge;80% accuracy aaye — calendar ke anusar nahi!
    </div>
  </div>

  <!-- AI TUTOR PROTOCOL BANNER -->
  <div style="background:rgba(0,229,255,0.04);border:1px solid rgba(0,229,255,0.15);border-radius:12px;padding:12px 16px;margin-bottom:20px;font-size:0.82rem;color:#7a90a8;">
    <strong style="color:var(--primary);">⏱️ AI Tutor Standard Lesson Protocol:</strong>
    &nbsp;Concept (5–10m) &rarr; Logic/Intuition (5m) &rarr; Formula (5m) &rarr; Shortcuts + Traps (5–10m) &rarr; Foundation Practice (20 Qs) &rarr; Mixed Practice (20 Qs) &rarr; Real PYQ Lab (15 Qs) &rarr; Error Log &rarr; Active Recall.
    <br><strong style="color:var(--gold);">Rule:</strong> Question ko pehle rough sheet par solve karein &mdash; turant solution mat dekhein!
  </div>
'''

def get_day_plan():
    return r'''
  <!-- DAY PLAN -->
  <h2 class="sec-title" id="sec-plan">📅 Days 6–12 (7 Days) — Day-by-Day Master Syllabus Plan</h2>
  <div class="day-cards">
    <div class="day-card">
      <div class="day-label">
        <div class="day-tag">Day 6</div>
        <div class="day-name">Classification & Divisibility (2, 3, 5, 10)</div>
        <div class="day-drill">📝 20 Foundation Drills</div>
      </div>
      <div>
        <div style="font-weight:700;color:#fff;font-size:0.92rem;margin-bottom:6px;">Classification of Numbers, Prime Testing & Basic Divisibility</div>
        <ul class="day-topics">
          <li><strong>Real Numbers Hierarchy:</strong> Natural ($\mathbb{N} = 1,2,3..$), Whole ($\mathbb{W} = 0,1,2..$), Integers ($\mathbb{Z}$), Rational ($p/q$, terminating or recurring), Irrational ($\sqrt{2}, \pi$, non-terminating non-recurring).</li>
          <li><strong>Prime Numbers (अभाज्य संख्याएँ):</strong> Exactly 2 factors (1 and itself). 2 is the ONLY even prime. 1 to 50 = 15 primes; 51 to 100 = 10 primes; <strong>1 to 100 = 25 primes total</strong>.</li>
          <li><strong>Prime Testing Algorithm:</strong> For integer $N$, find $k = \lceil \sqrt{N} \rceil$. Test divisibility of $N$ by all primes $\le k$. If none divides $N$, $N$ is prime!</li>
          <li><strong>Coprimes:</strong> Two numbers $a$ and $b$ whose $\text{HCF}(a, b) = 1$. E.g. $(8, 9), (15, 28)$.</li>
        </ul>
      </div>
    </div>

    <div class="day-card">
      <div class="day-label">
        <div class="day-tag">Day 7</div>
        <div class="day-name">Divisibility (4, 8, 9, 11, 72, 88, 99)</div>
        <div class="day-drill">📝 25 SSC Pattern Qs</div>
      </div>
      <div>
        <div style="font-weight:700;color:#fff;font-size:0.92rem;margin-bottom:6px;">Power-of-2 Divisibility, Alternating Sums & High-Yield Composites</div>
        <ul class="day-topics">
          <li><strong>Powers of 2 and 5 ($2^k$ and $5^k$):</strong> By 4 ($2^2$): last 2 digits; By 8 ($2^3$): last 3 digits; By 16 ($2^4$): last 4 digits.</li>
          <li><strong>Divisibility by 9:</strong> Sum of all digits divisible by 9. Digital sum casting out 9s.</li>
          <li><strong>Divisibility by 11:</strong> $(\sum \text{odd places}) - (\sum \text{even places}) = 0$ or multiple of 11.</li>
          <li><strong>High-Frequency SSC Composites:</strong> 72 ($8 \times 9$), 88 ($8 \times 11$), 99 ($9 \times 11$). Always solve for the last digit using 8 first, then the remaining digit using 9 or 11!</li>
        </ul>
      </div>
    </div>

    <div class="day-card">
      <div class="day-label">
        <div class="day-tag">Day 8</div>
        <div class="day-name">HCF & LCM Mastery & Remainder Models</div>
        <div class="day-drill">📝 25 Word Problems</div>
      </div>
      <div>
        <div style="font-weight:700;color:#fff;font-size:0.92rem;margin-bottom:6px;">Factorization, Fractions & The 4 Classical Remainder Models</div>
        <ul class="day-topics">
          <li><strong>Fundamental Rule:</strong> For two numbers $A$ and $B$: $A \times B = \text{HCF} \times \text{LCM}$. (Never apply to 3 numbers!).</li>
          <li><strong>Fractions:</strong> $\text{HCF} = \frac{\text{HCF}(Num)}{\text{LCM}(Den)}$, $\text{LCM} = \frac{\text{LCM}(Num)}{\text{HCF}(Den)}$.</li>
          <li><strong>Classical Remainder Models:</strong> LCM constant remainder ($k \cdot L + r$), LCM constant difference ($k \cdot L - d$), HCF difference model ($\text{HCF}(|x-y|, |y-z|, |z-x|)$).</li>
        </ul>
      </div>
    </div>

    <div class="day-card">
      <div class="day-label">
        <div class="day-tag">Day 9</div>
        <div class="day-name">Remainder Theorems & Power Remainder</div>
        <div class="day-drill">📝 25 Pattern Drills</div>
      </div>
      <div>
        <div style="font-weight:700;color:#fff;font-size:0.92rem;margin-bottom:6px;">Negative Remainder, Binomial Expansions & Fermat/Wilson Theorems</div>
        <ul class="day-topics">
          <li><strong>Negative Remainder Concept:</strong> If remainder is $-r$, true positive remainder $= \text{Divisor} - r$.</li>
          <li><strong>Binomial Form:</strong> $\frac{(ax+1)^n}{a} \implies \text{Rem } 1$; $\frac{(ax-1)^n}{a} \implies +1$ (if $n$ even), $-1 \implies a-1$ (if $n$ odd).</li>
          <li><strong>Fermat's Little Theorem:</strong> $\frac{a^{p-1}}{p} \implies \text{Rem } 1$ where $p$ is prime and $\gcd(a, p) = 1$.</li>
          <li><strong>Wilson's Theorem:</strong> $\frac{(p-1)!}{p} \implies \text{Rem } (p-1) \equiv -1$.</li>
        </ul>
      </div>
    </div>

    <div class="day-card">
      <div class="day-label">
        <div class="day-tag">Day 10</div>
        <div class="day-name">Unit Digit & Cyclicity of Powers</div>
        <div class="day-drill">📝 20 Speed Drills</div>
      </div>
      <div>
        <div style="font-weight:700;color:#fff;font-size:0.92rem;margin-bottom:6px;">The 3 Cyclicity Classes, Exponent Mod 4 & Factorials</div>
        <ul class="day-topics">
          <li><strong>Class 1 (Cyclicity 1):</strong> $\{0, 1, 5, 6\}$ &mdash; unit digit never changes with any positive power.</li>
          <li><strong>Class 2 (Cyclicity 2):</strong> $\{4, 9\}$ &mdash; $4^{\text{odd}}=4, 4^{\text{even}}=6$; $9^{\text{odd}}=9, 9^{\text{even}}=1$.</li>
          <li><strong>Class 3 (Cyclicity 4):</strong> $\{2, 3, 7, 8\}$ &mdash; divide power by 4. If remainder is $r \in \{1, 2, 3\}$, use power $r$. If remainder is 0, use power 4!</li>
          <li><strong>Factorial Unit Digits:</strong> $5! = 120$ ends in 0. Hence for any $n \ge 5$, unit digit of $n!$ is ALWAYS 0!</li>
        </ul>
      </div>
    </div>

    <div class="day-card">
      <div class="day-label">
        <div class="day-tag">Day 11</div>
        <div class="day-name">Factors, Sum of Factors & Trailing Zeros</div>
        <div class="day-drill">📝 25 Formula Drills</div>
      </div>
      <div>
        <div style="font-weight:700;color:#fff;font-size:0.92rem;margin-bottom:6px;">Total/Even/Odd Factors, Divisors Sum & Legendre's Formula</div>
        <ul class="day-topics">
          <li><strong>Factor Counts for $N = 2^a p_2^b p_3^c$:</strong> Total $= (a+1)(b+1)(c+1)$; Odd $= (b+1)(c+1)$; Even $= a(b+1)(c+1)$.</li>
          <li><strong>Sum of Factors:</strong> $\frac{2^{a+1}-1}{2-1} \cdot \frac{p_2^{b+1}-1}{p_2-1} \cdot \frac{p_3^{c+1}-1}{p_3-1}$.</li>
          <li><strong>Trailing Zeros in $N!$:</strong> $\lfloor N/5 \rfloor + \lfloor N/25 \rfloor + \lfloor N/125 \rfloor + \dots$</li>
        </ul>
      </div>
    </div>

    <div class="day-card">
      <div class="day-label">
        <div class="day-tag">Day 12</div>
        <div class="day-name">Mixed PYQ Lab & Phase 1 Mastery Test</div>
        <div class="day-drill">⏱️ 25 Questions Timed Drill</div>
      </div>
      <div>
        <div style="font-weight:700;color:#fff;font-size:0.92rem;margin-bottom:6px;">Tier-1 & Tier-2 Comprehensive Mixed Testing & Speed Optimization</div>
        <ul class="day-topics">
          <li><strong>Multi-concept integration:</strong> Divisibility combined with algebraic identities, remainder theorem with factorial expansions, factor count of large composites.</li>
          <li><strong>Target:</strong> 25 Questions in 22 minutes with $\ge 80\%$ accuracy (20+ correct).</li>
        </ul>
      </div>
    </div>
  </div>
'''

print("Topbar, hero, and day plan ready.")
