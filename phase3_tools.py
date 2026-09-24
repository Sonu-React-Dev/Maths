# -*- coding: utf-8 -*-
"""
Phase 3 Timed Drill, Active Recall, Error Notebook, Completion Checklist, Spaced Revision, Sidebar & JavaScript
"""

def get_timed_drill_and_tools():
    return r'''
  <!-- TIMED DRILL -->
  <section class="timed-drill" id="sec-timer">
    <h2 class="sec-title">⏱️ Phase 3 Timed Drill — Stopwatch &amp; Score Calculator</h2>
    <div style="text-align:center;font-size:0.85rem;color:var(--text-muted);margin-bottom:12px;">
      Start timer &rarr; Solve 25 selected Ratio &amp; Proportion questions &rarr; Pause &rarr; Calculate Score &amp; Accuracy
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
      🎯 <strong>AI Tutor Benchmark:</strong> &ge; 85% accuracy (&ge; 21/25 correct) in under 22 minutes is mandatory for Level 3/4 certification in Ratio &amp; Proportion.
    </div>
  </section>

  <!-- ACTIVE RECALL -->
  <section class="recall-section" id="sec-recall">
    <h2 class="sec-title">🧠 Active Recall Session (10 Memory Verification Prompts)</h2>
    <div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:12px;">
      <strong style="color:var(--gold);">Active Recall Protocol:</strong> Screen se nazar hataiye, formula ya concept ko man me recall karein, rough page par likhein, aur verify hone par checkbox check karein.
    </div>
    <div class="recall-how">
      <div class="recall-step"><div class="rs-box">1. Hide Notes</div><span class="rs-arrow">&rarr;</span></div>
      <div class="recall-step"><div class="rs-box">2. Mental Recall</div><span class="rs-arrow">&rarr;</span></div>
      <div class="recall-step"><div class="rs-box">3. Write Down</div><span class="rs-arrow">&rarr;</span></div>
      <div class="recall-step"><div class="rs-box">4. Verify</div><span class="rs-arrow">&rarr;</span></div>
      <div class="recall-step"><div class="rs-box">5. Apply to Q</div></div>
    </div>
    <div class="recall-qs">
      <div class="recall-q"><span class="rq-text">1. $A:B = 2:3$ aur $B:C = 4:5$ ho to $A:B:C$ combine karne ka N-method / Blank-filling rule bina dekhe explain karein?</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">2. Mean proportional to $a, b$, Third proportional to $a, b$, aur Fourth proportional to $a, b, c$ ke exact formulas likhein?</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">3. Componendo and Dividendo (C&amp;D) rule kya hai: $\frac{a}{b} = \frac{c}{d} \implies \frac{a+b}{a-b} = ?$ aur ye SSC algebra/ratio me kab lagta hai?</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">4. Difference: $\frac{A}{3} = \frac{B}{4} = \frac{C}{5}$ me $A:B:C$ kya hota hai vs $2A = 3B = 4C$ me $A:B:C$ kaise nikalta hai?</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">5. Income, Expenditure &amp; Savings problems me Cross-multiplication method (Ladder) ka sign rule aur calculation setup kya hai?</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">6. Age problems me fundamental invariant kya hota hai, aur do ratios ke difference ko balance kaise karte hain?</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">7. Coin box problems me Ratio of Coins $\times$ Face Value of 1 Coin = Ratio of Total Value ka principle kaise lagate hain?</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">8. What number $x$ must be added/subtracted to $a, b, c, d$ to make them proportional? $x = \frac{|ad - bc|}{(a+d) - (b+c)}$ formula recall karein?</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">9. Error in division: ₹$x$ ko fraction ratio $(1/a : 1/b : 1/c)$ ke badle direct integer ratio $(a : b : c)$ me baantne par gain/loss kaise solve hota hai?</span><input type="checkbox" class="rq-check"></div>
      <div class="recall-q"><span class="rq-text">10. Duplicate ratio ($a^2:b^2$), Sub-duplicate ratio ($\sqrt{a}:\sqrt{b}$), aur Compounded ratio ($ac:bd$) ke standard definitions kya hain?</span><input type="checkbox" class="rq-check"></div>
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
          <td><input type="text" class="error-input" value="Q5"></td>
          <td><input type="text" class="error-input" value="3A = 4B = 5C me direct A:B:C = 3:4:5 likh diya"></td>
          <td><input type="text" class="error-input" value="[C]" style="color:var(--red);font-weight:700;"></td>
          <td><input type="text" class="error-input" value="Equalities me coefficients reciprocal hote hain: 1/3:1/4:1/5 = 20:15:12"></td>
        </tr>
        <tr>
          <td><input type="text" class="error-input" value="Q28"></td>
          <td><input type="text" class="error-input" value="Coin box me ₹1, 50p, 25p ke ratio ko seedhe total rupees ke barabar rakh diya"></td>
          <td><input type="text" class="error-input" value="[F]" style="color:var(--gold);font-weight:700;"></td>
          <td><input type="text" class="error-input" value="Pehle Value Ratio nikalna hoga: Coins * Denomination"></td>
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
      AI Tutor Rule ke mutabiq Phase 3 (Days 21–26) ko complete tabhi mark karein jab ye 10 shartein poori hon:
    </div>
    <div class="recall-qs">
      <div class="recall-q"><span class="rq-text">1. Concepts understood: 6 Theory Modules thoroughly read &amp; digested</span><input type="checkbox" class="rq-check"></div>
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
    <h2 class="sec-title">🔄 Spaced Revision Tracker (Phase 3)</h2>
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
          <td>Day 27 (24h after Phase 3)</td>
          <td>Ratio Combining + Proportion Formulas + Cross-Method</td>
          <td><button class="tb-btn" onclick="this.textContent='✓ Completed';this.style.color='var(--green)'">Mark Done</button></td>
        </tr>
        <tr>
          <td><strong>R2 (Second Review)</strong></td>
          <td>Day 34 (7 days later)</td>
          <td>All 15 PYQs + Coin Problems + 10 Active Recall Tests</td>
          <td><button class="tb-btn" onclick="this.textContent='✓ Completed';this.style.color='var(--green)'">Mark Done</button></td>
        </tr>
        <tr>
          <td><strong>R3 (Third Review)</strong></td>
          <td>Day 48 (21 days later)</td>
          <td>25-Question Timed Drill (Retest under strict timer)</td>
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
    <button class="sidebar-close-btn" id="sidebar-close" aria-label="Close Sidebar">✕</button>
  </div>
  <div class="sidebar-content">
    <div class="sb-group-title"><span>📑 Quick Jump Menu</span></div>
    <div class="sb-toc-grid">
      <a href="#sec-mastery" class="sb-toc-link">📊 Mastery Tracker</a>
      <a href="#sec-plan" class="sb-toc-link">📅 Day-by-Day Plan</a>
      <a href="#sec-theory" class="sb-toc-link">📖 Theory (6 Modules)</a>
      <a href="#sec-formulas" class="sb-toc-link">📐 Formula Vault</a>
      <a href="#sec-shortcuts" class="sb-toc-link">⚡ Shortcuts &amp; Traps</a>
      <a href="#sec-basic" class="sb-toc-link">🟢 20 Basic Questions</a>
      <a href="#sec-mixed" class="sb-toc-link">🟡 20 Mixed Questions</a>
      <a href="#sec-pyq" class="sb-toc-link">🏆 15 SSC PYQs</a>
      <a href="#sec-timer" class="sb-toc-link">⏱️ Timed Drill</a>
      <a href="#sec-recall" class="sb-toc-link">🧠 Active Recall</a>
      <a href="#sec-errors" class="sb-toc-link">📓 Error Notebook</a>
      <a href="#sec-checklist" class="sb-toc-link">✅ Completion Checklist</a>
    </div>

    <div class="sb-group-title"><span>🔢 All Phases</span></div>
    <a href="Day_1_Number_Basics_BODMAS.html" class="sb-phase-item"><span>📖 Day 1 Master Book</span><span>Day 1</span></a>
    <a href="Phase_0_Calculation_Foundation.html" class="sb-phase-item"><span>0. Calculation Foundation</span><span>Days 1–5</span></a>
    <a href="Phase_1_Number_System.html" class="sb-phase-item"><span>1. Number System (Book)</span><span>Days 6–12</span></a>
    <a href="Phase_2_Percentage.html" class="sb-phase-item"><span>2. Percentage (Book)</span><span>Days 13–20</span></a>
    <a href="Phase_3_Ratio_and_Proportion.html" class="sb-phase-item active"><span>3. Ratio &amp; Proportion (Book)</span><span>Days 21–26</span></a>
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
    <h3>🖨️ Print Phase 3 Book Edition / Export to PDF</h3>
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

var mlCards = document.querySelectorAll('.ml-card');
mlCards.forEach(function(card) {
  card.addEventListener('click', function() {
    mlCards.forEach(function(c) { c.classList.remove('selected'); });
    card.classList.add('selected');
    localStorage.setItem('p3_mastery_level', card.getAttribute('data-level'));
  });
});
var savedLevel = localStorage.getItem('p3_mastery_level');
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
    res.innerHTML = '🎉 Outstanding! Score: ' + correct + '/' + total + ' (' + percent + '%) &bull; Ratio &amp; Proportion Benchmark Cleared! Ready for Phase 4: Average!';
  } else if (percent >= 65) {
    res.className = 'score-result score-ok';
    res.innerHTML = '⚠️ Good Progress: Score: ' + correct + '/' + total + ' (' + percent + '%) &bull; Revise Cross-multiplication and Retest in 24 hours!';
  } else {
    res.className = 'score-result score-fail';
    res.innerHTML = '🚨 Score: ' + correct + '/' + total + ' (' + percent + '%) &bull; AI Tutor Rule: Log errors in the notebook and re-attempt all missed questions!';
  }
});
</script>
</body>
</html>
'''

print("Phase 3 tools module ready.")
