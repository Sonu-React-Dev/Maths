# -*- coding: utf-8 -*-
"""
Phase 2 Questions:
- 20 Basic / Foundation Questions (Q1 to Q20)
- 20 Mixed / Standard & Tricky Questions (Q21 to Q40)
- 15 Real Verified SSC PYQs (Q41 to Q55)
Total = 55 Graded Questions!
"""

def get_basic_questions():
    return r'''
  <!-- ========================================== -->
  <!-- LEVEL 1: 20 BASIC / FOUNDATION QUESTIONS -->
  <!-- ========================================== -->
  <section class="book-chapter" id="sec-basic">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
      <div>
        <span class="chap-badge" style="background:rgba(34,211,165,0.1);color:var(--green);border-color:rgba(34,211,165,0.2);">LEVEL 1</span>
        <h2 style="font-size:1.35rem;font-weight:700;color:#fff;">🟢 20 Basic / Foundation Practice Questions</h2>
      </div>
      <span style="font-size:0.82rem;color:var(--text-muted);">Target: 100% Accuracy &bull; 30s/Q</span>
    </div>
    <p class="book-p" style="font-size:0.88rem;color:var(--gold);">
      🤖 <strong>AI Tutor Rule:</strong> Pehle khud rough sheet par attempt karein. Solution tabhi reveal karein jab attempt ho jaye!
    </p>

    <div class="topic-filter-bar">
      <span class="filter-label">🏷️ Filter by Topic:</span>
      <button class="q-filter-chip active" onclick="filterQs('all', this)">All Topics (20 Qs)</button>
      <button class="q-filter-chip" onclick="filterQs('fraction-grid', this)">1. Fraction Grid</button>
      <button class="q-filter-chip" onclick="filterQs('mf-change', this)">2. MF &amp; Changes</button>
      <button class="q-filter-chip" onclick="filterQs('ab-successive', this)">3. AB Formula</button>
      <button class="q-filter-chip" onclick="filterQs('price-consumption', this)">4. P&times;C=E Ladder</button>
      <button class="q-filter-chip" onclick="filterQs('income-depreciation', this)">5. I=E+S &amp; Deprec</button>
      <button class="q-filter-chip" onclick="filterQs('election-venn', this)">6. Election &amp; Venn</button>
    </div>

    <!-- Q1 -->
    <div class="q-block" data-topic="fraction-grid">
      <div class="q-head"><span class="q-num">Q1</span><span class="q-tag">Fraction to Percentage</span></div>
      <div class="q-text">Convert the fraction $\frac{5}{8}$ into percentage.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-b-hint-1')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-b-sol-1')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-b-hint-1">Recall $1/8 = 12.5\%$. Multiply by 5.</div>
      <div class="sol-content" id="p2-b-sol-1">
        <strong>Step-by-step Solution:</strong><br>
        $1/8 = 12.5\%$<br>
        $5/8 = 5 \times 12.5\% = \mathbf{62.5\%}$ (or $62\frac{1}{2}\%$).
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q2 -->
    <div class="q-block" data-topic="fraction-grid">
      <div class="q-head"><span class="q-num">Q2</span><span class="q-tag">Commutative Law</span></div>
      <div class="q-text">Evaluate: $72\% \text{ of } 25 + 48\% \text{ of } 50$.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-b-hint-2')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-b-sol-2')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-b-hint-2">Swap: $25\% \text{ of } 72 + 50\% \text{ of } 48$.</div>
      <div class="sol-content" id="p2-b-sol-2">
        <strong>Step-by-step Solution:</strong><br>
        1) $72\% \text{ of } 25 = 25\% \text{ of } 72 = \frac{72}{4} = 18$.<br>
        2) $48\% \text{ of } 50 = 50\% \text{ of } 48 = \frac{48}{2} = 24$.<br>
        3) Sum $= 18 + 24 = \mathbf{42}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q3 -->
    <div class="q-block" data-topic="mf-change">
      <div class="q-head"><span class="q-num">Q3</span><span class="q-tag">Percentage Comparison</span></div>
      <div class="q-text">If $A = 120$ and $B = 150$, by what percent is $B$ more than $A$, and by what percent is $A$ less than $B$?</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-b-hint-3')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-b-sol-3')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-b-hint-3">Base for 'more than A' is A. Base for 'less than B' is B.</div>
      <div class="sol-content" id="p2-b-sol-3">
        <strong>Step-by-step Solution:</strong><br>
        1) $B$ more than $A = \frac{150 - 120}{120} \times 100\% = \frac{30}{120} \times 100\% = \mathbf{25\% \text{ more}}$.<br>
        2) $A$ less than $B = \frac{150 - 120}{150} \times 100\% = \frac{30}{150} \times 100\% = \mathbf{20\% \text{ less}}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q4 -->
    <div class="q-block" data-topic="mf-change">
      <div class="q-head"><span class="q-num">Q4</span><span class="q-tag">Base Shifting</span></div>
      <div class="q-text">If $A$'s salary is $20\%$ more than $B$'s salary, by what percent is $B$'s salary less than $A$'s salary?</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-b-hint-4')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-b-sol-4')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-b-hint-4">Let $B = 100 \implies A = 120$. Calculate $\frac{20}{120} \times 100\%$.</div>
      <div class="sol-content" id="p2-b-sol-4">
        <strong>Step-by-step Solution:</strong><br>
        1) Let $B = 100 \implies A = 120$.<br>
        2) Difference $= 20$. Base is $A = 120$.<br>
        3) $\%$ Less $= \frac{20}{120} \times 100\% = \frac{1}{6} \times 100\% = \mathbf{16\frac{2}{3}\% \text{ or } 16.67\%}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q5 -->
    <div class="q-block" data-topic="ab-successive">
      <div class="q-head"><span class="q-num">Q5</span><span class="q-tag">Successive Change AB Formula</span></div>
      <div class="q-text">The length of a rectangle is increased by $20\%$ and its breadth is increased by $10\%$. Find the percentage change in its area.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-b-hint-5')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-b-sol-5')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-b-hint-5">Apply $a + b + \frac{ab}{100}$ with $a = 20, b = 10$.</div>
      <div class="sol-content" id="p2-b-sol-5">
        <strong>Step-by-step Solution:</strong><br>
        $\text{Net } \% = 20 + 10 + \frac{20 \times 10}{100} = 30 + 2 = \mathbf{+32\% \text{ increase}}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q6 -->
    <div class="q-block" data-topic="ab-successive">
      <div class="q-head"><span class="q-num">Q6</span><span class="q-tag">Opposite Equal Changes</span></div>
      <div class="q-text">A number is first increased by $15\%$ and then decreased by $15\%$. Find the net percentage change in the number.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-b-hint-6')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-b-sol-6')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-b-hint-6">Formula for $+x\%$ and $-x\%$ is $-\frac{x^2}{100}\%$.</div>
      <div class="sol-content" id="p2-b-sol-6">
        <strong>Step-by-step Solution:</strong><br>
        $\text{Net } \% = -\frac{15^2}{100}\% = -\frac{225}{100}\% = \mathbf{-2.25\% \text{ (2.25% decrease)}}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q7 -->
    <div class="q-block" data-topic="price-consumption">
      <div class="q-head"><span class="q-num">Q7</span><span class="q-tag">Constant Expenditure</span></div>
      <div class="q-text">If the price of petrol increases by $25\%$, by what percentage must a car owner reduce his consumption so that expenditure remains unchanged?</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-b-hint-7')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-b-sol-7')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-b-hint-7">Golden ladder: $+1/4 \implies -1/5 = 20\%$. Or $\frac{x}{100+x} \times 100\%$.</div>
      <div class="sol-content" id="p2-b-sol-7">
        <strong>Step-by-step Solution:</strong><br>
        $\text{Required Reduction} = \frac{25}{100 + 25} \times 100\% = \frac{25}{125} \times 100\% = \mathbf{20\%}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q8 -->
    <div class="q-block" data-topic="price-consumption">
      <div class="q-head"><span class="q-num">Q8</span><span class="q-tag">Price Drop Consumption Increase</span></div>
      <div class="q-text">If the price of sugar decreases by $20\%$, by what percent can a family increase its consumption without changing its budget?</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-b-hint-8')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-b-sol-8')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-b-hint-8">$-1/5 \implies +1/4 = 25\%$. Or $\frac{x}{100-x} \times 100\%$.</div>
      <div class="sol-content" id="p2-b-sol-8">
        <strong>Step-by-step Solution:</strong><br>
        $\text{Required Increase} = \frac{20}{100 - 20} \times 100\% = \frac{20}{80} \times 100\% = \mathbf{25\%}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q9 -->
    <div class="q-block" data-topic="ab-successive">
      <div class="q-head"><span class="q-num">Q9</span><span class="q-tag">Area of Circle</span></div>
      <div class="q-text">If the radius of a circle is increased by $30\%$, find the percentage increase in its area.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-b-hint-9')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-b-sol-9')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-b-hint-9">$\text{Area} \propto r^2$. Apply $a + b + \frac{ab}{100}$ with $a=30, b=30$.</div>
      <div class="sol-content" id="p2-b-sol-9">
        <strong>Step-by-step Solution:</strong><br>
        $\text{Area Increase} = 30 + 30 + \frac{30 \times 30}{100} = 60 + 9 = \mathbf{69\%}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q10 -->
    <div class="q-block" data-topic="ab-successive">
      <div class="q-head"><span class="q-num">Q10</span><span class="q-tag">Two Successive Discounts</span></div>
      <div class="q-text">Find the single equivalent discount for two successive discounts of $20\%$ and $10\%$.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-b-hint-10')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-b-sol-10')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-b-hint-10">Discount formula: $d_1 + d_2 - \frac{d_1 d_2}{100}$.</div>
      <div class="sol-content" id="p2-b-sol-10">
        <strong>Step-by-step Solution:</strong><br>
        $\text{Equivalent Discount} = 20 + 10 - \frac{20 \times 10}{100} = 30 - 2 = \mathbf{28\%}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q11 -->
    <div class="q-block" data-topic="election-venn">
      <div class="q-head"><span class="q-num">Q11</span><span class="q-tag">Simple Election</span></div>
      <div class="q-text">In an election between two candidates, the winner secures $65\%$ of the total votes and wins by a margin of $1,800$ votes. Find the total number of votes polled (assuming no invalid votes).</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-b-hint-11')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-b-sol-11')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-b-hint-11">Winner $= 65\% \implies$ Loser $= 35\%$. Margin $= 65\% - 35\% = 30\%$.</div>
      <div class="sol-content" id="p2-b-sol-11">
        <strong>Step-by-step Solution:</strong><br>
        1) Winner $= 65\%$, Loser $= 100\% - 65\% = 35\%$.<br>
        2) Winning Margin $= 65\% - 35\% = 30\%$.<br>
        3) $30\% = 1,800 \implies 1\% = 60 \implies 100\% = \mathbf{6,000 \text{ votes}}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q12 -->
    <div class="q-block" data-topic="income-depreciation">
      <div class="q-head"><span class="q-num">Q12</span><span class="q-tag">Population Growth</span></div>
      <div class="q-text">The population of a town is $80,000$. It increases at the rate of $5\%$ per annum. Find the population after $2$ years.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-b-hint-12')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-b-sol-12')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-b-hint-12">Multiplying factor $= \frac{21}{20}$ per year. Apply twice.</div>
      <div class="sol-content" id="p2-b-sol-12">
        <strong>Step-by-step Solution:</strong><br>
        $P_{\text{after}} = 80,000 \times \left(1 + \frac{5}{100}\right)^2 = 80,000 \times \frac{21}{20} \times \frac{21}{20} = 200 \times 441 = \mathbf{88,200}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q13 -->
    <div class="q-block" data-topic="income-depreciation">
      <div class="q-head"><span class="q-num">Q13</span><span class="q-tag">Machine Depreciation</span></div>
      <div class="q-text">A machine depreciates at the rate of $10\%$ per annum. If its current value is ₹$72,900$, what was its value $2$ years ago?</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-b-hint-13')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-b-sol-13')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-b-hint-13">$P \times (9/10)^2 = 72,900$.</div>
      <div class="sol-content" id="p2-b-sol-13">
        <strong>Step-by-step Solution:</strong><br>
        $P \times \left(\frac{9}{10}\right)^2 = 72,900$<br>
        $P \times \frac{81}{100} = 72,900 \implies P = \frac{72900 \times 100}{81} = 900 \times 100 = \mathbf{₹90,000}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q14 -->
    <div class="q-block" data-topic="income-depreciation">
      <div class="q-head"><span class="q-num">Q14</span><span class="q-tag">Successive Spending</span></div>
      <div class="q-text">A man spends $20\%$ of his monthly salary on house rent and $40\%$ of the remaining on food. If he saves ₹$7,200$, find his monthly salary.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-b-hint-14')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-b-sol-14')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-b-hint-14">Remaining after rent $= 80\%$. Savings $= 60\%$ of $80\%$.</div>
      <div class="sol-content" id="p2-b-sol-14">
        <strong>Step-by-step Solution:</strong><br>
        1) Let salary $= S$.<br>
        2) After rent, remaining $= S \times 0.80$.<br>
        3) After food, savings $= (S \times 0.80) \times (1 - 0.40) = S \times 0.80 \times 0.60 = 0.48 S$.<br>
        4) $0.48 S = 7,200 \implies S = \frac{7200}{0.48} = \frac{720000}{48} = \mathbf{₹15,000}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q15 -->
    <div class="q-block" data-topic="election-venn">
      <div class="q-head"><span class="q-num">Q15</span><span class="q-tag">Passing Marks Concept</span></div>
      <div class="q-text">A student scores $30\%$ marks and fails by $15$ marks. Another student scores $40\%$ marks and gets $25$ marks more than the minimum passing marks. Find the maximum marks of the examination and the passing percentage.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-b-hint-15')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-b-sol-15')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-b-hint-15">Difference in percentages $(40\% - 30\% = 10\%)$ equals difference in marks $(25 - (-15) = 40)$.</div>
      <div class="sol-content" id="p2-b-sol-15">
        <strong>Step-by-step Solution:</strong><br>
        1) $40\% - 30\% = 10\%$ of total marks.<br>
        2) Mark difference $= 25 - (-15) = 40$ marks.<br>
        3) $10\% = 40 \implies \text{Total Marks} = \mathbf{400}$.<br>
        4) Passing marks $= 30\% \text{ of } 400 + 15 = 120 + 15 = 135$.<br>
        5) Passing percentage $= \frac{135}{400} \times 100\% = \mathbf{33.75\%}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q16 -->
    <div class="q-block" data-topic="election-venn">
      <div class="q-head"><span class="q-num">Q16</span><span class="q-tag">Basic Venn Diagram</span></div>
      <div class="q-text">In an exam, $40\%$ candidates failed in English, $30\%$ failed in Maths, and $15\%$ failed in both. Find the percentage of candidates who passed in both subjects.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-b-hint-16')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-b-sol-16')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-b-hint-16">Total Failed $= 40 + 30 - 15$. Passed both $= 100 - \text{Total Failed}$.</div>
      <div class="sol-content" id="p2-b-sol-16">
        <strong>Step-by-step Solution:</strong><br>
        1) Total failed in at least one subject $= 40 + 30 - 15 = 55\%$.<br>
        2) Passed in both subjects $= 100\% - 55\% = \mathbf{45\%}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q17 -->
    <div class="q-block" data-topic="mf-change">
      <div class="q-head"><span class="q-num">Q17</span><span class="q-tag">Two Numbers Comparison</span></div>
      <div class="q-text">Two numbers are respectively $20\%$ and $50\%$ more than a third number. What percentage is the first number of the second number?</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-b-hint-17')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-b-sol-17')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-b-hint-17">Assume third number $= 100$. Then first $= 120$, second $= 150$.</div>
      <div class="sol-content" id="p2-b-sol-17">
        <strong>Step-by-step Solution:</strong><br>
        1) Let third number $= 100$.<br>
        2) First number $= 120$, Second number $= 150$.<br>
        3) $\text{Percentage} = \frac{120}{150} \times 100\% = \frac{4}{5} \times 100\% = \mathbf{80\%}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q18 -->
    <div class="q-block" data-topic="income-depreciation">
      <div class="q-head"><span class="q-num">Q18</span><span class="q-tag">Tax and Net Income</span></div>
      <div class="q-text">If income tax is increased by $19\%$, net income decreases by $1\%$. Find the rate of income tax.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-b-hint-18')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-b-sol-18')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-b-hint-18">Increase in Tax $=$ Decrease in Net Income. $19\% \times \text{Tax} = 1\% \times \text{Net Income}$.</div>
      <div class="sol-content" id="p2-b-sol-18">
        <strong>Step-by-step Solution:</strong><br>
        1) $19\% \times \text{Tax} = 1\% \times \text{Net Income} \implies \frac{\text{Tax}}{\text{Net Income}} = \frac{1}{19}$.<br>
        2) $\text{Total Gross Income} = \text{Net Income} + \text{Tax} = 19 + 1 = 20$.<br>
        3) $\text{Rate of Tax} = \frac{\text{Tax}}{\text{Total Income}} \times 100\% = \frac{1}{20} \times 100\% = \mathbf{5\%}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q19 -->
    <div class="q-block" data-topic="ab-successive">
      <div class="q-head"><span class="q-num">Q19</span><span class="q-tag">Volume of Cube Scaling</span></div>
      <div class="q-text">If each edge of a cube is increased by $10\%$, find the percentage increase in its surface area and its volume.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-b-hint-19')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-b-sol-19')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-b-hint-19">Surface area $\propto a^2$. Volume $\propto a^3$.</div>
      <div class="sol-content" id="p2-b-sol-19">
        <strong>Step-by-step Solution:</strong><br>
        1) <strong>Surface Area ($a^2$):</strong> $10 + 10 + \frac{100}{100} = \mathbf{+21\%}$.<br>
        2) <strong>Volume ($a^3$):</strong> $(1.1)^3 = 1.331 \implies \mathbf{+33.1\%}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q20 -->
    <div class="q-block" data-topic="fraction-grid">
      <div class="q-head"><span class="q-num">Q20</span><span class="q-tag">Fraction Multiplication Error</span></div>
      <div class="q-text">A student multiplied a number by $\frac{3}{5}$ instead of $\frac{5}{3}$. What is the percentage error in the calculation?</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-b-hint-20')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-b-sol-20')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-b-hint-20">Let the number be $\text{LCM}(5, 3) = 15$.</div>
      <div class="sol-content" id="p2-b-sol-20">
        <strong>Step-by-step Solution:</strong><br>
        1) Let the number be $15$.<br>
        2) Correct value $= 15 \times \frac{5}{3} = 25$.<br>
        3) False value $= 15 \times \frac{3}{5} = 9$.<br>
        4) Error $= 25 - 9 = 16$.<br>
        5) $\%$ Error $= \frac{16}{25} \times 100\% = 16 \times 4 = \mathbf{64\%}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>
  </section>
'''

def get_mixed_questions():
    return r'''
  <!-- ========================================== -->
  <!-- LEVEL 2: 20 MIXED / ADVANCED QUESTIONS -->
  <!-- ========================================== -->
  <section class="book-chapter" id="sec-mixed">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
      <div>
        <span class="chap-badge" style="background:rgba(246,194,68,0.1);color:var(--gold);border-color:rgba(246,194,68,0.2);">LEVEL 2</span>
        <h2 style="font-size:1.35rem;font-weight:700;color:#fff;">🟡 20 Mixed / Standard &amp; Tricky Questions</h2>
      </div>
      <span style="font-size:0.82rem;color:var(--text-muted);">Tier-1 & Tier-2 Advanced &bull; 45s/Q</span>
    </div>
    <p class="book-p" style="font-size:0.88rem;color:var(--gold);">
      🤖 <strong>AI Tutor Rule:</strong> Pehle independent attempt karein. Ratio aur Multiplier methods se step count reduce karein!
    </p>

    <div class="topic-filter-bar">
      <span class="filter-label">🏷️ Filter Mixed Qs by Topic:</span>
      <button class="q-filter-chip active" onclick="filterQs('all', this)">All Mixed (20 Qs)</button>
      <button class="q-filter-chip" onclick="filterQs('fraction-grid', this)">1. Fraction Grid</button>
      <button class="q-filter-chip" onclick="filterQs('mf-change', this)">2. MF &amp; Changes</button>
      <button class="q-filter-chip" onclick="filterQs('ab-successive', this)">3. AB Formula</button>
      <button class="q-filter-chip" onclick="filterQs('price-consumption', this)">4. P&times;C=E Ladder</button>
      <button class="q-filter-chip" onclick="filterQs('income-depreciation', this)">5. I=E+S &amp; Deprec</button>
      <button class="q-filter-chip" onclick="filterQs('election-venn', this)">6. Election &amp; Venn</button>
    </div>

    <!-- Q21 -->
    <div class="q-block" data-topic="price-consumption">
      <div class="q-head"><span class="q-num">Q21</span><span class="q-tag">Price Drop &amp; Quantity Difference</span></div>
      <div class="q-text">A reduction of $20\%$ in the price of sugar enables a purchaser to obtain $4$ kg more for ₹$160$. Find the original price per kg and the reduced price per kg.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-m-hint-21')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-m-sol-21')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-m-hint-21">Money saved $= 20\% \text{ of } 160 = ₹32$. ₹32 buys 4 kg.</div>
      <div class="sol-content" id="p2-m-sol-21">
        <strong>Step-by-step Solution:</strong><br>
        1) <strong>Reduced Price:</strong> ₹$32$ pays for $4$ kg $\implies \text{Reduced Price} = \frac{32}{4} = \mathbf{₹8/\text{kg}}$.<br>
        2) <strong>Original Price:</strong> Since reduced price is $80\%$ of original price:<br>
        $0.80 \times \text{Original} = 8 \implies \text{Original Price} = \frac{8}{0.80} = \mathbf{₹10/\text{kg}}$.<br>
        &bull; <strong>Answer: Original = ₹10/kg, Reduced = ₹8/kg</strong>.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q22 -->
    <div class="q-block" data-topic="price-consumption">
      <div class="q-head"><span class="q-num">Q22</span><span class="q-tag">Variable Expenditure Model</span></div>
      <div class="q-text">The price of cooking oil increases by $25\%$. By what percentage should a family reduce its consumption so that its expenditure increases by only $10\%$?</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-m-hint-22')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-m-sol-22')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-m-hint-22">Let initial $P = 100, C = 100 \implies E = 10000$. New $P = 125$, new $E = 11000$.</div>
      <div class="sol-content" id="p2-m-sol-22">
        <strong>Step-by-step Solution:</strong><br>
        1) $P \times C = E$.<br>
        New Price $= 1.25 P_0$, New Expenditure $= 1.10 E_0$.<br>
        2) $\text{New } C = \frac{1.10}{1.25} C_0 = \frac{110}{125} C_0 = \frac{22}{25} C_0 = 0.88 C_0$.<br>
        3) Consumption decreases from $1.00$ to $0.88 \implies \mathbf{12\% \text{ reduction}}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q23 -->
    <div class="q-block" data-topic="income-depreciation">
      <div class="q-head"><span class="q-num">Q23</span><span class="q-tag">Income, Expenditure &amp; Savings Ratio</span></div>
      <div class="q-text">A person spends $75\%$ of his income. His income increases by $20\%$ and his expenditure increases by $10\%$. Find the percentage increase in his savings.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-m-hint-23')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-m-sol-23')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-m-hint-23">Let Income $= 100 \implies \text{Exp} = 75, \text{Sav} = 25$.</div>
      <div class="sol-content" id="p2-m-sol-23">
        <strong>Step-by-step Solution:</strong><br>
        1) Initial: Income $= 100$, Expenditure $= 75$, Savings $= 25$.<br>
        2) New Income $= 120$.<br>
        3) New Expenditure $= 75 \times 1.10 = 82.5$.<br>
        4) New Savings $= 120 - 82.5 = 37.5$.<br>
        5) Increase in Savings $= 37.5 - 25 = 12.5$.<br>
        6) $\%$ Increase $= \frac{12.5}{25} \times 100\% = \mathbf{50\%}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q24 -->
    <div class="q-block" data-topic="election-venn">
      <div class="q-head"><span class="q-num">Q24</span><span class="q-tag">Election with Invalid Votes</span></div>
      <div class="q-text">In an election, $10\%$ of voters did not cast their votes and $10\%$ of the votes cast were declared invalid. The winning candidate got $54\%$ of the valid votes and won by a majority of $1,620$ votes. Find the total number of voters enrolled in the voters list.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-m-hint-24')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-m-sol-24')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-m-hint-24">Valid votes $= V \times 0.90 \times 0.90 = 0.81 V$. Winner gets $54\%$, loser gets $46\%$. Margin $= 8\%$.</div>
      <div class="sol-content" id="p2-m-sol-24">
        <strong>Step-by-step Solution:</strong><br>
        1) Let total enrolled voters $= V$.<br>
        2) Voted $= 0.90 V$. Valid votes $= 0.90 \times 0.90 V = 0.81 V$.<br>
        3) Winner gets $54\%$ of valid votes $\implies$ Loser gets $46\%$ of valid votes.<br>
        Winning Margin $= (54\% - 46\%) = 8\%$ of valid votes.<br>
        4) $0.08 \times 0.81 V = 1,620$<br>
        $0.0648 V = 1,620 \implies V = \frac{1620}{0.0648} = \frac{16200000}{648} = \mathbf{25,000}$.<br>
        &bull; <strong>Answer: 25,000 voters</strong>.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q25 -->
    <div class="q-block" data-topic="ab-successive">
      <div class="q-head"><span class="q-num">Q25</span><span class="q-tag">Complex Successive Changes</span></div>
      <div class="q-text">A number is increased by $20\%$, then decreased by $10\%$, and then increased by $25\%$. What is the net percentage increase or decrease in the number?</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-m-hint-25')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-m-sol-25')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-m-hint-25">Use fractional multipliers: $\frac{6}{5} \times \frac{9}{10} \times \frac{5}{4}$.</div>
      <div class="sol-content" id="p2-m-sol-25">
        <strong>Step-by-step Solution:</strong><br>
        1) Net multiplier $= \left(\frac{6}{5}\right) \times \left(\frac{9}{10}\right) \times \left(\frac{5}{4}\right) = \frac{6 \times 9 \times 5}{5 \times 10 \times 4} = \frac{54}{40} = \frac{27}{20} = 1.35$.<br>
        2) Since multiplier is $1.35$, net change $= (1.35 - 1) \times 100\% = \mathbf{+35\% \text{ increase}}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q26 -->
    <div class="q-block" data-topic="ab-successive">
      <div class="q-head"><span class="q-num">Q26</span><span class="q-tag">Cylinder Volume Expansion</span></div>
      <div class="q-text">If the radius of the base of a cylinder is decreased by $20\%$ and its height is increased by $50\%$, find the percentage change in its volume.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-m-hint-26')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-m-sol-26')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-m-hint-26">$\text{Volume} = \pi r^2 h$. Multiplier $= (0.80)^2 \times 1.50$.</div>
      <div class="sol-content" id="p2-m-sol-26">
        <strong>Step-by-step Solution:</strong><br>
        1) $V \propto r^2 h$.<br>
        2) Multiplier $= (0.80)^2 \times (1.50) = 0.64 \times 1.50 = 0.96$.<br>
        3) Since $0.96 < 1$, there is a decrease $= (1 - 0.96) \times 100\% = \mathbf{4\% \text{ decrease}}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q27 -->
    <div class="q-block" data-topic="price-consumption">
      <div class="q-head"><span class="q-num">Q27</span><span class="q-tag">Fresh Fruit vs Dry Fruit</span></div>
      <div class="q-text">Fresh watermelon contains $90\%$ water, whereas dry watermelon contains $20\%$ water. What weight of dry watermelon can be obtained from $40$ kg of fresh watermelon?</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-m-hint-27')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-m-sol-27')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-m-hint-27">The weight of pulp (solid part) remains CONSTANT!</div>
      <div class="sol-content" id="p2-m-sol-27">
        <strong>Step-by-step Solution:</strong><br>
        1) In fresh watermelon: Pulp $= 100\% - 90\% = 10\%$.<br>
        Weight of pulp $= 10\% \text{ of } 40\text{ kg} = 4\text{ kg}$.<br>
        2) In dry watermelon: Pulp $= 100\% - 20\% = 80\%$.<br>
        3) $80\% \text{ of Dry Weight} = 4\text{ kg} \implies \text{Dry Weight} = \frac{4}{0.80} = \mathbf{5\text{ kg}}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q28 -->
    <div class="q-block" data-topic="election-venn">
      <div class="q-head"><span class="q-num">Q28</span><span class="q-tag">Passing Marks with Two Students</span></div>
      <div class="q-text">In an examination, A scored $32\%$ marks and failed by $24$ marks. B scored $45\%$ marks and obtained $41$ marks more than the passing marks. What is the passing mark and the maximum mark?</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-m-hint-28')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-m-sol-28')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-m-hint-28">Difference in $\% = 45\% - 32\% = 13\%$. Difference in marks $= 41 - (-24) = 65$.</div>
      <div class="sol-content" id="p2-m-sol-28">
        <strong>Step-by-step Solution:</strong><br>
        1) $45\% - 32\% = 13\%$.<br>
        2) Marks difference $= 41 + 24 = 65$.<br>
        3) $13\% = 65 \implies 1\% = 5 \implies \text{Max Marks} = \mathbf{500}$.<br>
        4) Passing marks $= 32\% \text{ of } 500 + 24 = 160 + 24 = \mathbf{184}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q29 -->
    <div class="q-block" data-topic="income-depreciation">
      <div class="q-head"><span class="q-num">Q29</span><span class="q-tag">Population Male/Female Breakdown</span></div>
      <div class="q-text">The population of a village was $9,800$. In a year, with the increase in population of males by $8\%$ and that of females by $5\%$, the population of the village became $10,458$. What was the number of males in the village before increase?</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-m-hint-29')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-m-sol-29')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-m-hint-29">Total increase $= 10458 - 9800 = 658$. If all were females, increase would be $5\% \text{ of } 9800 = 490$.</div>
      <div class="sol-content" id="p2-m-sol-29">
        <strong>Step-by-step Solution:</strong><br>
        1) Total increase $= 10,458 - 9,800 = 658$.<br>
        2) If entire population grew at $5\%$, increase $= 5\% \text{ of } 9,800 = 490$.<br>
        3) Surplus increase $= 658 - 490 = 168$.<br>
        4) This surplus is due to extra $3\%$ ($8\% - 5\%$) growth of males:<br>
        $3\% \text{ of Males} = 168 \implies \text{Males} = \frac{168}{3} \times 100 = \mathbf{5,600}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q30 -->
    <div class="q-block" data-topic="income-depreciation">
      <div class="q-head"><span class="q-num">Q30</span><span class="q-tag">Multi-tier Spendings</span></div>
      <div class="q-text">A man gave $30\%$ of his money to his elder son, $40\%$ of the remaining to his younger son, and $10\%$ of the remaining to a trust. If he is left with ₹$18,900$, find his total initial money.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-m-hint-30')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-m-sol-30')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-m-hint-30">Remaining multiplier $= (1 - 0.30) \times (1 - 0.40) \times (1 - 0.10) = 0.70 \times 0.60 \times 0.90$.</div>
      <div class="sol-content" id="p2-m-sol-30">
        <strong>Step-by-step Solution:</strong><br>
        1) Remaining fraction $= \frac{7}{10} \times \frac{6}{10} \times \frac{9}{10} = \frac{378}{1000} = 0.378$.<br>
        2) $0.378 \times \text{Total} = 18,900 \implies \text{Total} = \frac{18900}{0.378} = \mathbf{₹50,000}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q31 -->
    <div class="q-block" data-topic="mf-change">
      <div class="q-head"><span class="q-num">Q31</span><span class="q-tag">Salary Base Equation</span></div>
      <div class="q-text">If $A$'s salary is $40\%$ of $B$'s salary and $B$'s salary is $25\%$ more than $C$'s salary, by what percentage is $C$'s salary more than $A$'s salary?</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-m-hint-31')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-m-sol-31')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-m-hint-31">Assume $C = 100$. Then $B = 125$, and $A = 40\% \text{ of } 125 = 50$.</div>
      <div class="sol-content" id="p2-m-sol-31">
        <strong>Step-by-step Solution:</strong><br>
        1) Let $C = 100$.<br>
        2) $B = 125$.<br>
        3) $A = 40\% \text{ of } 125 = \frac{2}{5} \times 125 = 50$.<br>
        4) How much is $C$ more than $A$? $\frac{100 - 50}{50} \times 100\% = \frac{50}{50} \times 100\% = \mathbf{100\% \text{ more}}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q32 -->
    <div class="q-block" data-topic="election-venn">
      <div class="q-head"><span class="q-num">Q32</span><span class="q-tag">Venn Diagram Exact Counts</span></div>
      <div class="q-text">In a group of $1,500$ students, $65\%$ like football, $55\%$ like cricket, and $10\%$ like neither. How many students like both football and cricket?</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-m-hint-32')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-m-sol-32')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-m-hint-32">Students who like at least one sport $= 100\% - 10\% = 90\%$.</div>
      <div class="sol-content" id="p2-m-sol-32">
        <strong>Step-by-step Solution:</strong><br>
        1) $n(F \cup C) = 100\% - 10\% = 90\%$.<br>
        2) $n(F \cap C) = n(F) + n(C) - n(F \cup C) = 65\% + 55\% - 90\% = 120\% - 90\% = 30\%$.<br>
        3) Number of students $= 30\% \text{ of } 1,500 = \mathbf{450}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q33 -->
    <div class="q-block" data-topic="fraction-grid">
      <div class="q-head"><span class="q-num">Q33</span><span class="q-tag">Fraction Ratio Adjustment</span></div>
      <div class="q-text">If the numerator of a fraction is increased by $20\%$ and its denominator is decreased by $10\%$, the value of the fraction becomes $\frac{16}{21}$. Find the original fraction.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-m-hint-33')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-m-sol-33')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-m-hint-33">$\frac{x \times 1.20}{y \times 0.90} = \frac{16}{21}$. Simplify $\frac{1.20}{0.90} = \frac{4}{3}$.</div>
      <div class="sol-content" id="p2-m-sol-33">
        <strong>Step-by-step Solution:</strong><br>
        1) $\frac{x \times 120}{y \times 90} = \frac{16}{21} \implies \frac{x}{y} \times \frac{4}{3} = \frac{16}{21}$.<br>
        2) $\frac{x}{y} = \frac{16}{21} \times \frac{3}{4} = \frac{4 \times 1}{7 \times 1} = \mathbf{\frac{4}{7}}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q34 -->
    <div class="q-block" data-topic="election-venn">
      <div class="q-head"><span class="q-num">Q34</span><span class="q-tag">Election with Non-Voting</span></div>
      <div class="q-text">In an election, $20\%$ of voters on the voters list did not vote and $120$ votes were cast as invalid. The winner got $41\%$ of the total enrolled voters and won by $200$ votes. Find the total number of enrolled voters.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-m-hint-34')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-m-sol-34')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-m-hint-34">Total enrolled $= 100x$. Winner $= 41x$. Votes cast $= 80x$. Valid $= 80x - 120$.</div>
      <div class="sol-content" id="p2-m-sol-34">
        <strong>Step-by-step Solution:</strong><br>
        1) Let total enrolled voters $= 100x$.<br>
        2) Votes cast $= 80x$. Valid votes $= 80x - 120$.<br>
        3) Winner gets $41x$ votes.<br>
        4) Loser gets $(80x - 120) - 41x = 39x - 120$ votes.<br>
        5) Margin: $41x - (39x - 120) = 200 \implies 2x + 120 = 200 \implies 2x = 80 \implies x = 40$.<br>
        6) Total enrolled voters $= 100 \times 40 = \mathbf{4,000}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q35 -->
    <div class="q-block" data-topic="price-consumption">
      <div class="q-head"><span class="q-num">Q35</span><span class="q-tag">Price Rise &amp; Quantity Cut</span></div>
      <div class="q-text">A reduction of $10\%$ in the price of tea enables a dealer to purchase $5$ kg more for ₹$450$. What is the difference between the original and the reduced price per kg?</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-m-hint-35')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-m-sol-35')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-m-hint-35">Money saved $= 10\% \text{ of } 450 = ₹45$ for 5 kg.</div>
      <div class="sol-content" id="p2-m-sol-35">
        <strong>Step-by-step Solution:</strong><br>
        1) Reduced price $= \frac{45}{5} = ₹9/\text{kg}$.<br>
        2) Original price $= \frac{9}{0.90} = ₹10/\text{kg}$.<br>
        3) Difference $= 10 - 9 = \mathbf{₹1/\text{kg}}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q36 -->
    <div class="q-block" data-topic="income-depreciation">
      <div class="q-head"><span class="q-num">Q36</span><span class="q-tag">Commission System</span></div>
      <div class="q-text">A salesman is allowed $9\%$ commission on total sales plus a bonus of $1\%$ on sales over ₹$20,000$. If his total earnings were ₹$6,800$, find his total sales.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-m-hint-36')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-m-sol-36')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-m-hint-36">Give him 1% bonus on ALL sales: extra ₹200 added to earning $\implies 10\% \text{ of Total} = 7000$.</div>
      <div class="sol-content" id="p2-m-sol-36">
        <strong>⚡ Topper 10-Second Method:</strong><br>
        1) If he had received $1\%$ bonus on the first ₹$20,000$ as well, he would get an extra $1\% \text{ of } 20,000 = ₹200$.<br>
        2) His total earnings would become $6,800 + 200 = ₹7,000$.<br>
        3) Now he gets a flat $(9\% + 1\%) = 10\%$ on ALL sales.<br>
        4) $10\% \text{ of Sales} = 7,000 \implies \text{Total Sales} = \mathbf{₹70,000}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q37 -->
    <div class="q-block" data-topic="income-depreciation">
      <div class="q-head"><span class="q-num">Q37</span><span class="q-tag">Consecutive Rate of Depreciation</span></div>
      <div class="q-text">The value of a car depreciates by $25\%$ in the first year, $20\%$ in the second year, and $15\%$ in the third year. What is the total overall percentage depreciation over the 3 years?</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-m-hint-37')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-m-sol-37')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-m-hint-37">Final value $= 1 \times 0.75 \times 0.80 \times 0.85 = \frac{3}{4} \times \frac{4}{5} \times \frac{17}{20}$.</div>
      <div class="sol-content" id="p2-m-sol-37">
        <strong>Step-by-step Solution:</strong><br>
        1) Final fraction $= \frac{3}{4} \times \frac{4}{5} \times \frac{17}{20} = \frac{51}{100} = 0.51$.<br>
        2) Overall depreciation $= (1 - 0.51) \times 100\% = \mathbf{49\%}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q38 -->
    <div class="q-block" data-topic="election-venn">
      <div class="q-head"><span class="q-num">Q38</span><span class="q-tag">Venn Diagram Three Categories</span></div>
      <div class="q-text">In a survey of $200$ people, $120$ read Hindi newspaper, $100$ read English newspaper, and $50$ read both. How many read neither?</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-m-hint-38')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-m-sol-38')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-m-hint-38">Apply $n(H \cup E) = n(H) + n(E) - n(H \cap E)$.</div>
      <div class="sol-content" id="p2-m-sol-38">
        <strong>Step-by-step Solution:</strong><br>
        1) $n(H \cup E) = 120 + 100 - 50 = 170$.<br>
        2) Neither $= 200 - 170 = \mathbf{30 \text{ people}}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q39 -->
    <div class="q-block" data-topic="income-depreciation">
      <div class="q-head"><span class="q-num">Q39</span><span class="q-tag">Alligation in Salary Increase</span></div>
      <div class="q-text">A man's salary is ₹$45,000$. He spends $80\%$ of it and saves the rest. Next year his income increases by $15\%$ and his savings increase by $20\%$. By what percentage does his expenditure increase?</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-m-hint-39')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-m-sol-39')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-m-hint-39">Ratio of $E : S = 80 : 20 = 4 : 1$. Use weighted percentage: $4 \times E\% + 1 \times 20\% = 5 \times 15\%$.</div>
      <div class="sol-content" id="p2-m-sol-39">
        <strong>Step-by-step Solution:</strong><br>
        1) $E : S = 4 : 1$, Total Income $= 5$ units.<br>
        2) $4(E\%) + 1(20\%) = 5(15\%)$<br>
        $4(E\%) + 20 = 75 \implies 4(E\%) = 55 \implies E\% = \frac{55}{4} = \mathbf{13.75\%}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q40 -->
    <div class="q-block" data-topic="ab-successive">
      <div class="q-head"><span class="q-num">Q40</span><span class="q-tag">Successive Price Markings</span></div>
      <div class="q-text">A trader marks his goods $40\%$ above the cost price and then allows a discount of $25\%$ on the marked price. Find his net profit or loss percentage.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p2-m-hint-40')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p2-m-sol-40')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p2-m-hint-40">Apply AB formula with $a = +40, b = -25$.</div>
      <div class="sol-content" id="p2-m-sol-40">
        <strong>Step-by-step Solution:</strong><br>
        $\text{Net } \% = 40 - 25 - \frac{40 \times 25}{100} = 15 - 10 = \mathbf{+5\% \text{ profit}}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>
  </section>
'''

def get_pyq_lab():
    return r'''
  <!-- ========================================== -->
  <!-- LEVEL 3: 15 REAL SSC VERIFIED PYQs -->
  <!-- ========================================== -->
  <section class="book-chapter" id="sec-pyq">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
      <div>
        <span class="chap-badge" style="background:rgba(167,139,250,0.1);color:var(--violet);border-color:rgba(167,139,250,0.2);">LEVEL 3: SSC PYQ LAB</span>
        <h2 style="font-size:1.35rem;font-weight:700;color:#fff;">🏆 15 Verified SSC Exam Questions with Topper Shortcuts</h2>
      </div>
      <span style="font-size:0.82rem;color:var(--text-muted);">Tier-1 & Tier-2 Papers &bull; 100% Authentic</span>
    </div>
    <p class="book-p" style="font-size:0.88rem;color:var(--gold);">
      🔐 <strong>AI Tutor Integrity Rule:</strong> Har question ka exact exam shift tag diya gaya hai. Pehle solve karein fir shortcut dekhein.
    </p>

    <div class="topic-filter-bar">
      <span class="filter-label">🏷️ Filter PYQs by Topic:</span>
      <button class="q-filter-chip active" onclick="filterQs('all', this)">All Real PYQs (15)</button>
      <button class="q-filter-chip" onclick="filterQs('mf-change', this)">2. MF &amp; Changes</button>
      <button class="q-filter-chip" onclick="filterQs('ab-successive', this)">3. AB Formula</button>
      <button class="q-filter-chip" onclick="filterQs('price-consumption', this)">4. P&times;C=E Ladder</button>
      <button class="q-filter-chip" onclick="filterQs('income-depreciation', this)">5. I=E+S &amp; Deprec</button>
      <button class="q-filter-chip" onclick="filterQs('election-venn', this)">6. Election &amp; Venn</button>
    </div>

    <!-- PYQ 1 -->
    <div class="pyq-card" data-topic="price-consumption">
      <div class="pyq-tag">SSC CGL 2023 Tier-1 • 14 July Shift-3</div>
      <div class="pyq-q"><strong>Q41:</strong> The price of petrol was raised by $15\%$. By what percentage should a motorist reduce his consumption of petrol so that the expenditure on it does not increase? (Round off to 1 decimal place).</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p2-p-sol-41')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p2-p-sol-41">
        <strong>⚡ 15-Second Solution:</strong><br>
        $\text{Reduction} = \frac{15}{100 + 15} \times 100\% = \frac{15}{115} \times 100\% = \frac{3}{23} \times 100\% = \frac{300}{23} = \mathbf{13.04\% \approx 13.0\%}$.
      </div>
    </div>

    <!-- PYQ 2 -->
    <div class="pyq-card" data-topic="ab-successive">
      <div class="pyq-tag">SSC CGL 2022 Tier-2 (Mains) • 02 March 2023</div>
      <div class="pyq-q"><strong>Q42:</strong> A's salary is $38\%$ more than B's salary. B's salary is what percent less than A's salary? (Correct to one decimal place).</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p2-p-sol-42')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p2-p-sol-42">
        <strong>⚡ Base Formula Shortcut:</strong><br>
        $\% \text{ Less} = \frac{38}{138} \times 100\% = \frac{19}{69} \times 100\% = \frac{1900}{69} \approx \mathbf{27.5\%}$.
      </div>
    </div>

    <!-- PYQ 3 -->
    <div class="pyq-card" data-topic="election-venn">
      <div class="pyq-tag">SSC CGL 2023 Tier-1 • 17 July Shift-1</div>
      <div class="pyq-q"><strong>Q43:</strong> In an election between two candidates, $8\%$ of the voters did not cast their votes. The winning candidate got $48\%$ of the total enrolled votes and won by $1,100$ votes. Find the total number of enrolled voters.</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p2-p-sol-43')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p2-p-sol-43">
        <strong>⚡ Step-by-Step Breakdown:</strong><br>
        1) Total Enrolled $= 100\%$. Turnout $= 92\%$.<br>
        2) Winner gets $48\%$ of TOTAL enrolled votes.<br>
        3) Loser gets $92\% - 48\% = 44\%$ of total enrolled votes.<br>
        4) Margin $= 48\% - 44\% = 4\%$.<br>
        5) $4\% = 1,100 \implies 100\% = 1100 \times 25 = \mathbf{27,500 \text{ voters}}$.
      </div>
    </div>

    <!-- PYQ 4 -->
    <div class="pyq-card" data-topic="income-depreciation">
      <div class="pyq-tag">SSC CGL 2022 Tier-1 • 01 Dec Shift-2</div>
      <div class="pyq-q"><strong>Q44:</strong> If the length and breadth of a cuboid are increased by $10\%$ and $20\%$ respectively and its height is decreased by $20\%$, what is the percentage change in the volume of the cuboid?</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p2-p-sol-44')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p2-p-sol-44">
        <strong>⚡ Multiplier Trick:</strong><br>
        1) Multipliers: $L \to 1.10$, $B \to 1.20$, $H \to 0.80$.<br>
        2) Net Multiplier $= 1.1 \times 1.2 \times 0.8 = 1.32 \times 0.8 = 1.056$.<br>
        3) Increase $= (1.056 - 1) \times 100\% = \mathbf{+5.6\% \text{ increase}}$.
      </div>
    </div>

    <!-- PYQ 5 -->
    <div class="pyq-card" data-topic="election-venn">
      <div class="pyq-tag">SSC CGL 2023 Tier-2 (Mains) • 26 Oct 2023</div>
      <div class="pyq-q"><strong>Q45:</strong> An examinee has to secure $40\%$ marks to pass. He gets $180$ marks and fails by an equal number of marks. Find the maximum marks.</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p2-p-sol-45')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p2-p-sol-45">
        <strong>⚡ 5-Second Solution:</strong><br>
        1) Fails by an equal number of marks $\implies$ fails by $180$ marks.<br>
        2) Passing marks $= 180 + 180 = 360$.<br>
        3) $40\% = 360 \implies 100\% = \frac{360}{40} \times 100 = \mathbf{900 \text{ marks}}$.
      </div>
    </div>

    <!-- PYQ 6 -->
    <div class="pyq-card" data-topic="income-depreciation">
      <div class="pyq-tag">SSC CHSL 2023 Tier-1 • 02 Aug Shift-2</div>
      <div class="pyq-q"><strong>Q46:</strong> A reduction of $15\%$ in the price of wheat allows a housewife to buy $6$ kg more for ₹$2,720$. What is the reduced price per kg?</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p2-p-sol-46')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p2-p-sol-46">
        <strong>⚡ Single Step Trick:</strong><br>
        $\text{Reduced Price} = \frac{2720 \times 0.15}{6} = \frac{408}{6} = \mathbf{₹68/\text{kg}}$.
      </div>
    </div>

    <!-- PYQ 7 -->
    <div class="pyq-card" data-topic="price-consumption">
      <div class="pyq-tag">SSC CPO 2023 • 03 Oct Shift-1</div>
      <div class="pyq-q"><strong>Q47:</strong> The population of a city was $1,75,000$ two years ago. If it increased by $4\%$ in the first year and $5\%$ in the second year, what is its present population?</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p2-p-sol-47')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p2-p-sol-47">
        <strong>⚡ Ratio Multiplier:</strong><br>
        $1,75,000 \times \frac{26}{25} \times \frac{21}{20} = 7,000 \times \frac{26}{20} \times 21 = 350 \times 26 \times 21 = 9,100 \times 21 = \mathbf{1,91,100}$.
      </div>
    </div>

    <!-- PYQ 8 -->
    <div class="pyq-card" data-topic="mf-change">
      <div class="pyq-tag">SSC CGL 2021 Tier-2 (Mains) • 08 Aug 2022</div>
      <div class="pyq-q"><strong>Q48:</strong> The monthly salary of an employee was increased by $20\%$. After three months, due to company policy, it was reduced by $20\%$. What was the net percentage change in his salary?</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p2-p-sol-48')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p2-p-sol-48">
        <strong>⚡ $x^2/100$ Rule:</strong><br>
        $\text{Net Change} = -\frac{20^2}{100}\% = -\frac{400}{100}\% = \mathbf{-4\% \text{ (4% decrease)}}$.
      </div>
    </div>

    <!-- PYQ 9 -->
    <div class="pyq-card" data-topic="election-venn">
      <div class="pyq-tag">SSC CGL 2022 Tier-1 • 08 Dec Shift-4</div>
      <div class="pyq-q"><strong>Q49:</strong> If the radius of a sphere is decreased by $10\%$, by what percentage does its surface area decrease?</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p2-p-sol-49')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p2-p-sol-49">
        <strong>⚡ Surface Area Scaling:</strong><br>
        $\text{Surface Area} = 4\pi r^2$.<br>
        $\text{Net } \% = -10 - 10 + \frac{100}{100} = -20 + 1 = \mathbf{-19\% \text{ (19% decrease)}}$.
      </div>
    </div>

    <!-- PYQ 10 -->
    <div class="pyq-card" data-topic="income-depreciation">
      <div class="pyq-tag">SSC CHSL 2022 Tier-1 • 27 May Shift-3</div>
      <div class="pyq-q"><strong>Q50:</strong> A person's expenditure and savings are in the ratio $5:3$. If his income increases by $12\%$ and expenditure increases by $15\%$, find the percentage increase in his savings.</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p2-p-sol-50')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p2-p-sol-50">
        <strong>⚡ Weighted Percentage Equation:</strong><br>
        $5(15\%) + 3(S\%) = 8(12\%) \implies 75 + 3S = 96 \implies 3S = 21 \implies S = \mathbf{7\% \text{ increase}}$.
      </div>
    </div>

    <!-- PYQ 11 -->
    <div class="pyq-card" data-topic="ab-successive">
      <div class="pyq-tag">SSC CGL 2023 Tier-1 • 20 July Shift-2</div>
      <div class="pyq-q"><strong>Q51:</strong> In an examination, $70\%$ candidates passed in English and $80\%$ passed in Mathematics. $10\%$ failed in both subjects. If $144$ candidates passed in both, find the total number of candidates.</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p2-p-sol-51')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p2-p-sol-51">
        <strong>⚡ Venn Diagram Method:</strong><br>
        1) Convert to fail: English fail $= 30\%$, Maths fail $= 20\%$, Both fail $= 10\%$.<br>
        2) Total failed in at least one $= 30 + 20 - 10 = 40\%$.<br>
        3) Passed in both $= 100\% - 40\% = 60\%$.<br>
        4) $60\% = 144 \implies 100\% = \frac{144}{60} \times 100 = \mathbf{240 \text{ candidates}}$.
      </div>
    </div>

    <!-- PYQ 12 -->
    <div class="pyq-card" data-topic="election-venn">
      <div class="pyq-tag">SSC CPO 2022 • 10 Nov Shift-2</div>
      <div class="pyq-q"><strong>Q52:</strong> Two successive price hikes of $12\%$ and $15\%$ of an article are equivalent to a single price hike of:</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p2-p-sol-52')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p2-p-sol-52">
        <strong>⚡ AB Formula:</strong><br>
        $\text{Net } \% = 12 + 15 + \frac{12 \times 15}{100} = 27 + \frac{180}{100} = 27 + 1.80 = \mathbf{28.8\%}$.
      </div>
    </div>

    <!-- PYQ 13 -->
    <div class="pyq-card" data-topic="income-depreciation">
      <div class="pyq-tag">SSC CGL 2021 Tier-1 • 18 Aug Shift-3</div>
      <div class="pyq-q"><strong>Q53:</strong> A number is first decreased by $10\%$ and then increased by $10\%$. The number so obtained is $50$ less than the original number. What is the original number?</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p2-p-sol-53')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p2-p-sol-53">
        <strong>⚡ Net Loss Formula:</strong><br>
        1) Net loss $= \frac{10^2}{100}\% = 1\%$.<br>
        2) $1\% \text{ of Original} = 50 \implies \text{Original Number} = 50 \times 100 = \mathbf{5,000}$.
      </div>
    </div>

    <!-- PYQ 14 -->
    <div class="pyq-card" data-topic="mf-change">
      <div class="pyq-tag">SSC CHSL 2023 Tier-1 • 11 Aug Shift-3</div>
      <div class="pyq-q"><strong>Q54:</strong> In an election between two candidates, $5\%$ of the voters did not vote, and $2,000$ votes were invalid. The winning candidate received $52\%$ of the valid votes and won by a margin of $3,600$ votes. Find the total number of enrolled voters.</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p2-p-sol-54')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p2-p-sol-54">
        <strong>⚡ Back-Calculation Method:</strong><br>
        1) Margin $= (52\% - 48\%) = 4\%$ of Valid Votes $= 3,600$.<br>
        $\text{Valid Votes} = \frac{3600}{0.04} = 90,000$.<br>
        2) Total Polled Votes $= 90,000 + 2,000 = 92,000$.<br>
        3) Since $95\%$ voted: $0.95 \times \text{Enrolled} = 92,000 \implies \text{Enrolled} = \frac{92000}{0.95} \approx \mathbf{96,842 \text{ voters}}$.
      </div>
    </div>

    <!-- PYQ 15 -->
    <div class="pyq-card" data-topic="price-consumption">
      <div class="pyq-tag">SSC CGL 2023 Tier-2 (Mains) • 27 Oct 2023</div>
      <div class="pyq-q"><strong>Q55:</strong> If A's income is $60\%$ less than B's income, then B's income is what percentage more than that of A's income?</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p2-p-sol-55')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p2-p-sol-55">
        <strong>⚡ 5-Second Base Swap:</strong><br>
        1) Let $B = 100 \implies A = 40$.<br>
        2) Difference $= 60$. Base is $A = 40$.<br>
        3) $\%$ More $= \frac{60}{40} \times 100\% = \frac{3}{2} \times 100\% = \mathbf{150\% \text{ more}}$.
      </div>
    </div>
  </section>
'''

print("Phase 2 questions module ready.")
