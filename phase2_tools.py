# -*- coding: utf-8 -*-
"""
Phase 2 Timed Drill, Active Recall, Error Notebook, Completion Checklist, Spaced Revision, Sidebar & JavaScript
"""

def get_timed_drill_and_tools():
    return r'''
  <!-- TIMED DRILL -->
  <section class="timed-drill" id="sec-timer">
    <h2 class="sec-title">⏱️ Phase 2 Timed Drill — Stopwatch &amp; Score Calculator</h2>
    <div style="text-align:center;font-size:0.85rem;color:var(--text-muted);margin-bottom:12px;">
      Start timer &rarr; Solve your 25 Percentage questions &rarr; Pause &rarr; Calculate Score
    </div>
    <div class="timer-display" id="timer-display">00:00</div>
    <div class="timer-controls">
      <button class="timer-btn t-start" id="t-start">▶ Start</button>
      <button class="timer-btn t-pause" id="t-pause">⏸ Pause</button>
      <button class="timer-btn t-reset" id="t-reset">↺ Reset</button>
    </div>
    <div class="score-input-row">
      <span class="score-label">Correct:</span>
      <input type="number" class="score-input" id="score-correct" min="0" max="25" placeholder="0">
      <span class="score-label">Total:</span>
      <input type="number" class="score-input" id="score-total" min="1" value="25">
      <button class="tb-btn" style="background:var(--green);color:#080b12;font-weight:700;padding:8px 18px;" id="calc-score">Calculate Score</button>
    </div>
    <div class="score-result" id="score-result"></div>
    <div style="margin-top:14px;font-size:0.78rem;color:var(--text-muted);text-align:center;">
      🎯 <strong>AI Tutor Benchmark:</strong> &ge; 85% accuracy (&ge; 21/25 correct) in under 22 minutes is mandatory for Level 3/4 certification.
    </div>
  </section>

  <!-- ACTIVE RECALL -->
  <section class="recall-section" id="sec-recall">
    <h2 class="sec-title">🧠 Active Recall Session (10 Memory Verification Prompts)</h2>
    <div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:12px;">
      <strong style="color:var(--gold);">Active Recall Protocol:</strong> Screen se nazar hataiye, formula ya rule ko man me recall karein, rough page par likhein, aur verify hone par check karein.
    </div>
    <div class="recall-how">
      <div class="recall-step"><div class="rs-box">1. Hide Notes</div><span class="rs-arrow">&rarr;</span></div>
      <div class="recall-step"><div class="rs-box">2. Mental Recall</div><span class="rs-arrow">&rarr;</span></div>
      <div class="recall-step"><div class="rs-box">3. Write Down</div><span class="rs-arrow">&rarr;</span></div>
      <div class="recall-step"><div class="rs-box">4. Verify</div><span class="rs-arrow">&rarr;</span></div>
      <div class="recall-step"><div class="rs-box">5. Apply to Q</div></div>
    </div>
    <div class="recall-qs">
      <div class="recall-q"><span class="rq-text">1. $1/6, 1/7, 1/8, 1/9, 1/11, 1/12, 1/16$ ke percentage values bina dekhe likhein?</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">2. Commutative rule $A\% \text{ of } B = B\% \text{ of } A$ ka upyog karke $64\% \text{ of } 25$ solve karein?</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">3. "A is $25\%$ more than B" me B, A se kitne percent kam hai aur base kya hai?</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">4. Universal AB formula $a + b + \frac{ab}{100}$ me discount aur decrease ke sign rules kya hain?</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">5. Price $+25\%$ hone par consumption me kitni kami karni hogi (Golden Ladder $1/n \to 1/(n+1)$)?</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">6. Kisi sankhya me pehle $+20\%$ aur fir $-20\%$ karne par net change $-4\%$ kyu hota hai?</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">7. ₹$240$ me $2$ kg adhik sugar (price drop $20\%$) me reduced price nikaalne ka direct formula kya hai?</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">8. $I = E + S$ me alligation / weighted percentage equation kaise banayi jaati hai?</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">9. Election me enrolled voters, polled votes, valid votes, aur winning margin ka hierarchy relation kya hai?</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">10. 2-Set Venn diagram me passed in both nikaalne ka universal formula kya hai?</span><input type="checkbox" class="rq-check"></div>
    </div>
  </section>

  <!-- ERROR NOTEBOOK -->
  <section class="error-notebook" id="sec-errors">
    <h2 class="sec-title">📓 Error Notebook (Mistake Analysis Log)</h2>
    <div style="font-size:0.82rem;color:var(--text-muted);margin-bottom:12px;">
      <strong>AI Tutor Rule:</strong> Har galat question ka ek primary error tag classify karein. Har mistake se seekhe bina aage badhna mana hai!
    </div>
    <div class="error-codes-ref">
      <span class="ec-pill"><strong>[C]</strong> Concept Unclear</span>
      <span class="ec-pill"><strong>[F]</strong> Formula Misused</span>
      <span class="ec-pill"><strong>[K]</strong> Calculation Error</span>
      <span class="ec-pill"><strong>[S]</strong> Silly/Careless</span>
      <span class="ec-pill"><strong>[R]</strong> Reading Mistake</span>
      <span class="ec-pill"><strong>[T]</strong> Too Slow/Time</span>
    </div>
    <table class="error-table">
      <thead>
        <tr>
          <th style="width:50px;">Q#</th>
          <th>What Went Wrong? (Mistake Summary)</th>
          <th style="width:70px;">Tag</th>
          <th>Topper Fix / Correct Rule</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><input type="text" class="error-input" value="Q4"></td>
          <td><input type="text" class="error-input" value="B is less than A me base B ko le liya"></td>
          <td><input type="text" class="error-input" value="[C]" style="color:var(--red);font-weight:700;"></td>
          <td><input type="text" class="error-input" value="'than A' hai to denominator me hamesha A aayega"></td>
        </tr>
        <tr>
          <td><input type="text" class="error-input" placeholder="Q#"></td>
          <td><input type="text" class="error-input" placeholder="Enter error..."></td>
          <td><input type="text" class="error-input" placeholder="[Tag]"></td>
          <td><input type="text" class="error-input" placeholder="Fix..."></td>
        </tr>
        <tr>
          <td><input type="text" class="error-input" placeholder="Q#"></td>
          <td><input type="text" class="error-input" placeholder="Enter error..."></td>
          <td><input type="text" class="error-input" placeholder="[Tag]"></td>
          <td><input type="text" class="error-input" placeholder="Fix..."></td>
        </tr>
      </tbody>
    </table>
  </section>

  <!-- COMPLETION CHECKLIST -->
  <section class="book-chapter" id="sec-checklist" style="margin-bottom:22px;">
    <h2 class="sec-title">✅ Chapter Completion Checklist — AI Tutor Rule Standard</h2>
    <div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:12px;">
      AI Tutor Rule ke mutabiq Phase 2 ko complete tabhi mark karein jab ye 10 shartein poori hon:
    </div>
    <div class="recall-qs">
      <div class="recall-q"><span class="rq-text">1. Concepts understood: 6 Theory Modules thoroughly read</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">2. Formula sheet completed: 10 Formula Vault cards mastered</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">3. Shortcuts learned: 6 Speed Tricks + 6 Exam Traps memorized</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">4. Minimum 20 basic questions: Q1 to Q20 solved with &ge;90% accuracy</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">5. Minimum 20 mixed questions: Q21 to Q40 completed</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">6. Minimum 15 PYQs: Q41 to Q55 solved with Topper Tricks</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">7. One timed drill completed: 25 questions in &le;22 minutes</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">8. Errors classified: All mistakes tagged in Error Notebook</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">9. 24–48 hour re-test passed with &ge;85% score</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">10. Mastery Level set to L3 or L4 in Mastery Tracker</span><input type="checkbox" class="rq-check"></div>
    </div>
  </section>

  <!-- SPACED REVISION -->
  <section class="book-chapter" id="sec-revision" style="margin-bottom:30px;">
    <h2 class="sec-title">🔄 Spaced Revision Tracker (Phase 2)</h2>
    <table class="error-table">
      <thead>
        <tr>
          <th>Revision Stage</th>
          <th>Scheduled Gap</th>
          <th>What to Revise</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>R1 (First Review)</strong></td>
          <td>Day 21 (24h after Phase 2)</td>
          <td>Fraction Grid + Formula Vault + Error Log</td>
          <td><button class="tb-btn" onclick="this.textContent='✓ Completed';this.style.color='var(--green)'">Mark Done</button></td>
        </tr>
        <tr>
          <td><strong>R2 (Second Review)</strong></td>
          <td>Day 27 (7 days later)</td>
          <td>All 15 PYQs + 10 Active Recall Tests</td>
          <td><button class="tb-btn" onclick="this.textContent='✓ Completed';this.style.color='var(--green)'">Mark Done</button></td>
        </tr>
        <tr>
          <td><strong>R3 (Third Review)</strong></td>
          <td>Day 41 (21 days later)</td>
          <td>25-Question Timed Drill (Retest)</td>
          <td><button class="tb-btn" onclick="this.textContent='✓ Completed';this.style.color='var(--green)'">Mark Done</button></td>
        </tr>
      </tbody>
    </table>
  </section>
'''

def get_sidebar_modal_and_js():
    return r'''
</div><!-- /container -->

<!-- SIDEBAR BACKDROP & DRAWER -->
<div class="sidebar-backdrop" id="sidebar-backdrop"></div>
<aside class="sidebar-drawer" id="sidebar-drawer">
  <div class="sidebar-header">
    <div class="sb-brand">
      <span class="sb-brand-icon">⚡</span>
      <div>
        <div class="sb-brand-text">SSC CGL Hub</div>
        <div class="sb-brand-sub">120-Day Master Prep</div>
      </div>
    </div>
    <button class="sidebar-close-btn" id="sidebar-close" aria-la  <div class="sidebar-content">
    <div class="sb-group-title"><span>🎯 Topic-Wise Theory &amp; Practice</span></div>
    <div class="sb-toc-grid">
      <a href="#topic-1-fraction-grid" class="sb-toc-link">1. Fraction Grid</a>
      <a href="#topic-2-mf-change" class="sb-toc-link">2. MF &amp; Changes</a>
      <a href="#topic-3-ab-successive" class="sb-toc-link">3. AB Formula</a>
      <a href="#topic-4-price-consumption" class="sb-toc-link">4. P&times;C=E Ladder</a>
      <a href="#topic-5-income-depreciation" class="sb-toc-link">5. I=E+S &amp; Deprec</a>
      <a href="#topic-6-election-venn" class="sb-toc-link">6. Election &amp; Venn</a>
    </div>

    <div class="sb-group-title"><span>📑 Course Sections</span></div>
    <div class="sb-toc-grid">
      <a href="#sec-topics" class="sb-toc-link">📑 Topic Directory</a>
      <a href="#sec-mastery" class="sb-toc-link">📊 Mastery Tracker</a>
      <a href="#sec-plan" class="sb-toc-link">📅 Day-by-Day Plan</a>
      <a href="#sec-theory" class="sb-toc-link">📖 Theory (6 Modules)</a>
      <a href="#sec-formulas" class="sb-toc-link">📐 Formula Vault</a>
      <a href="#sec-basic" class="sb-toc-link">🟢 20 Basic Qs</a>
      <a href="#sec-mixed" class="sb-toc-link">🟡 20 Mixed Qs</a>
      <a href="#sec-pyq" class="sb-toc-link">🏆 15 SSC PYQs</a>
      <a href="#sec-timer" class="sb-toc-link">⏱️ Timed Drill</a>
      <a href="#sec-recall" class="sb-toc-link">🧠 Active Recall</a>
      <a href="#sec-errors" class="sb-toc-link">📓 Error Notebook</a>
      <a href="#sec-checklist" class="sb-toc-link">✅ Completion Checklist</a>
      <a href="#sec-revision" class="sb-toc-link">🔄 Revision Tracker</a>
    </div>

    <div class="sb-group-title"><span>🔢 All Phases</span></div>
    <a href="Day_1_Number_Basics_BODMAS.html" class="sb-phase-item"><span>📖 Day 1 Master Book</span><span>Day 1</span></a>
    <a href="Phase_0_Calculation_Foundation.html" class="sb-phase-item"><span>0. Calculation Foundation</span><span>Days 1–5</span></a>
    <a href="Phase_1_Number_System.html" class="sb-phase-item"><span>1. Number System (Book)</span><span>Days 6–12</span></a>
    <a href="Phase_2_Percentage.html" class="sb-phase-item active"><span>2. Percentage (Book)</span><span>Days 13–20</span></a>
    <a href="Phase_3_Ratio_and_Proportion.html" class="sb-phase-item"><span>3. Ratio &amp; Proportion</span><span>Days 21–26</span></a>
    <a href="Phase_4_Average.html" class="sb-phase-item"><span>4. Average</span><span>Days 27–31</span></a>
    <a href="Phase_5_Profit_Loss_Discount.html" class="sb-phase-item"><span>5. Profit, Loss &amp; Discount</span><span>Days 32–39</span></a>
    <a href="Phase_6_Simple_and_Compound_Interest.html" class="sb-phase-item"><span>6. Simple &amp; CI</span><span>Days 40–44</span></a>
    <a href="Phase_7_Partnership_and_Mixtures.html" class="sb-phase-item"><span>7. Partnership &amp; Mixture</span><span>Days 45–51</span></a>
    <a href="Phase_8_Time_and_Work.html" class="sb-phase-item"><span>8. Time &amp; Work</span><span>Days 52–59</span></a>
    <a href="Phase_9_Time_Speed_Distance.html" class="sb-phase-item"><span>9. Time, Speed &amp; Distance</span><span>Days 60–67</span></a>
    <a href="Phase_10_Algebra.html" class="sb-phase-item"><span>10. Algebra</span><span>Days 68–72</span></a>
    <a href="Phase_11_Geometry.html" class="sb-phase-item"><span>11. Geometry</span><span>Days 73–78</span></a>
    <a href="Phase_12_Mensuration.html" class="sb-phase-item"><span>12. Mensuration 2D &amp; 3D</span><span>Days 79–83</span></a>
    <a href="Phase_13_Trigonometry.html" class="sb-phase-item"><span>13. Trigonometry + H&amp;D</span><span>Days 84–87</span></a>
    <a href="Phase_14_DI_and_Statistics.html" class="sb-phase-item"><span>14. DI &amp; Statistics</span><span>Day 88</span></a>
    <a href="Phase_15_Revision_and_Mocks.html" class="sb-phase-item"><span>15. Revision &amp; Mocks</span><span>Days 89–120</span></a>
  </div>
</aside>

<!-- 1-CLICK PRINT MODAL -->
<div class="print-modal-overlay" id="print-modal">
  <div class="print-modal">
    <h3>🖨️ Print Phase 2 Book Edition / Export to PDF</h3>
    <p>
      Is action se poori book formatting clean document me convert ho jayegi. Sabhi hidden hints aur step-by-step solutions print view me automatically open ho jayenge taaki aap poori kitaba print ya PDF save kar sakein!
    </p>
    <div class="print-actions">
      <button class="print-btn-sec" onclick="closePrintModal()">Cancel</button>
      <button class="print-btn-primary" onclick="window.print()">Print / Save PDF</button>
    </div>
  </div>
</div>

<!-- SCRIPTS -->
<script>
function toggleEl(id) {
  var el = document.getElementById(id);
  if (!el) return;
  el.style.display = (el.style.display === 'block') ? 'none' : 'block';
}

function copyFormula(text) {
  navigator.clipboard.writeText(text).then(function() {
    alert('Formula copied to clipboard: ' + text);
  });
}

function openPrintModal() { document.getElementById('print-modal').style.display = 'flex'; }
function closePrintModal() { document.getElementById('print-modal').style.display = 'none'; }

/* Topic Filter function */
function filterQs(topic, btn) {
  if (btn) {
    var container = btn.parentElement;
    if (container) {
      container.querySelectorAll('.q-filter-chip').forEach(function(c) { c.classList.remove('active'); });
      btn.classList.add('active');
    }
  } else {
    // If called programmatically from topic hub, sync active chip
    document.querySelectorAll('.topic-filter-bar').forEach(function(bar) {
      bar.querySelectorAll('.q-filter-chip').forEach(function(c) {
        if (c.getAttribute('onclick') && c.getAttribute('onclick').indexOf("'" + topic + "'") !== -1) {
          bar.querySelectorAll('.q-filter-chip').forEach(function(b) { b.classList.remove('active'); });
          c.classList.add('active');
        }
      });
    });
  }
  
  var cards = document.querySelectorAll('.q-block, .pyq-card');
  cards.forEach(function(card) {
    if (topic === 'all' || card.getAttribute('data-topic') === topic) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
}

var sbDrawer = document.getElementById('sidebar-drawer');
var sbBackdrop = document.getElementById('sidebar-backdrop');
var sbToggle = document.getElementById('sidebar-toggle-btn');
var sbClose = document.getElementById('sidebar-close');

if (sbToggle) {
  sbToggle.addEventListener('click', function() {
    sbDrawer.classList.add('open');
    sbBackdrop.classList.add('active');
  });
}
if (sbClose) {
  sbClose.addEventListener('click', function() {
    sbDrawer.classList.remove('open');
    sbBackdrop.classList.remove('active');
  });
}
if (sbBackdrop) {
  sbBackdrop.addEventListener('click', function() {
    sbDrawer.classList.remove('open');
    sbBackdrop.classList.remove('active');
  });
}

// Auto close sidebar when clicking a link inside it
document.querySelectorAll('.sb-toc-link').forEach(function(link) {
  link.addEventListener('click', function() {
    if (sbDrawer) sbDrawer.classList.remove('open');
    if (sbBackdrop) sbBackdrop.classList.remove('active');
  });
});

var mlCards = document.querySelectorAll('.ml-card');
mlCards.forEach(function(card) {
  card.addEventListener('click', function() {
    mlCards.forEach(function(c) { c.classList.remove('selected'); });
    card.classList.add('selected');
    localStorage.setItem('p2_mastery_level', card.getAttribute('data-level'));
  });
});
var savedLevel = localStorage.getItem('p2_mastery_level');
if (savedLevel !== null) {
  var sel = document.querySelector('.ml-card[data-level="' + savedLevel + '"]');
  if (sel) sel.classList.add('selected');
}

var timerDisplay = document.getElementById('timer-display');
var timerInterval = null;
var secondsElapsed = 0;

function formatTime(s) {
  var m = Math.floor(s / 60);
  var sec = s % 60;
  return (m < 10 ? '0' + m : m) + ':' + (sec < 10 ? '0' + sec : sec);
}

document.getElementById('t-start').addEventListener('click', function() {
  if (timerInterval) return;
  timerInterval = setInterval(function() {
    secondsElapsed++;
    timerDisplay.textContent = formatTime(secondsElapsed);
  }, 1000);
});

document.getElementById('t-pause').addEventListener('click', function() {
  clearInterval(timerInterval);
  timerInterval = null;
});

document.getElementById('t-reset').addEventListener('click', function() {
  clearInterval(timerInterval);
  timerInterval = null;
  secondsElapsed = 0;
  timerDisplay.textContent = '00:00';
});

document.getElementById('calc-score').addEventListener('click', function() {
  var correct = parseInt(document.getElementById('score-correct').value) || 0;
  var total = parseInt(document.getElementById('score-total').value) || 25;
  var percent = Math.round((correct / total) * 100);
  var res = document.getElementById('score-result');
  res.style.display = 'block';
  
  if (percent >= 85) {
    res.className = 'score-result score-pass';
    res.innerHTML = '🎉 Outstanding! Score: ' + correct + '/' + total + ' (' + percent + '%) &bull; Percentage Mastery Benchmark Cleared! Ready for Profit &amp; Loss!';
  } else if (percent >= 65) {
    res.className = 'score-result score-ok';
    res.innerHTML = '⚠️ Good Progress: Score: ' + correct + '/' + total + ' (' + percent + '%) &bull; Revise Fraction Grid and Retest in 24 hours!';
  } else {
    res.className = 'score-result score-fail';
    res.innerHTML = '🚨 Score: ' + correct + '/' + total + ' (' + percent + '%) &bull; AI Tutor Rule: Log errors in the notebook and re-attempt all missed questions!';
  }
});

// ScrollSpy to highlight active topic chips in .topic-nav-bar
window.addEventListener('scroll', function() {
  var scrollPos = window.scrollY + 140;
  var chips = document.querySelectorAll('.tnav-chip');
  chips.forEach(function(chip) {
    var targetId = chip.getAttribute('href');
    if (!targetId || targetId.charAt(0) !== '#') return;
    var target = document.querySelector(targetId);
    if (!target) return;
    var top = target.offsetTop;
    var height = target.offsetHeight;
    if (scrollPos >= top && scrollPos < top + height) {
      chips.forEach(function(c) { c.classList.remove('active'); });
      chip.classList.add('active');
    }
  });
</script>
</body>
</html>
'''

print("Phase 2 tools module ready.")
