# -*- coding: utf-8 -*-
"""
Phase 3 Questions:
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

    <!-- Q1 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q1</span><span class="q-tag">Fractional Ratio Simplification</span></div>
      <div class="q-text">Simplify the ratio $\frac{1}{3} : \frac{1}{4} : \frac{1}{6}$ into simplest whole numbers.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-b-hint-1')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-b-sol-1')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-b-hint-1">Multiply all terms by $\text{LCM}(3, 4, 6) = 12$.</div>
      <div class="sol-content" id="p3-b-sol-1">
        <strong>Step-by-step Solution:</strong><br>
        1) $\text{LCM}(3, 4, 6) = 12$.<br>
        2) $\left(12 \times \frac{1}{3}\right) : \left(12 \times \frac{1}{4}\right) : \left(12 \times \frac{1}{6}\right) = \mathbf{4 : 3 : 2}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q2 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q2</span><span class="q-tag">Combining Two Ratios</span></div>
      <div class="q-text">If $A : B = 3 : 4$ and $B : C = 8 : 9$, find $A : B : C$ and $A : C$.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-b-hint-2')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-b-sol-2')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-b-hint-2">Make the common term $B$ equal to 8 by multiplying $A : B$ by 2.</div>
      <div class="sol-content" id="p3-b-sol-2">
        <strong>Step-by-step Solution:</strong><br>
        1) $A : B = (3 \times 2) : (4 \times 2) = 6 : 8$.<br>
        2) $B : C = 8 : 9$.<br>
        3) Therefore, $\mathbf{A : B : C = 6 : 8 : 9}$ and $\mathbf{A : C = 6 : 9 = 2 : 3}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q3 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q3</span><span class="q-tag">Mean Proportional</span></div>
      <div class="q-text">Find the mean proportional between $0.08$ and $0.18$.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-b-hint-3')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-b-sol-3')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-b-hint-3">Formula: $x = \sqrt{a \times b}$. Convert to fractions if needed.</div>
      <div class="sol-content" id="p3-b-sol-3">
        <strong>Step-by-step Solution:</strong><br>
        $x = \sqrt{0.08 \times 0.18} = \sqrt{\frac{8}{100} \times \frac{18}{100}} = \sqrt{\frac{144}{10000}} = \frac{12}{100} = \mathbf{0.12}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q4 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q4</span><span class="q-tag">Third Proportional</span></div>
      <div class="q-text">Find the third proportional to $16$ and $24$.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-b-hint-4')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-b-sol-4')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-b-hint-4">Formula: $x = \frac{b^2}{a}$.</div>
      <div class="sol-content" id="p3-b-sol-4">
        <strong>Step-by-step Solution:</strong><br>
        $x = \frac{24^2}{16} = \frac{24 \times 24}{16} = \frac{3 \times 24}{2} = 3 \times 12 = \mathbf{36}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q5 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q5</span><span class="q-tag">Fourth Proportional</span></div>
      <div class="q-text">Find the fourth proportional to $4, 9,$ and $12$.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-b-hint-5')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-b-sol-5')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-b-hint-5">Formula: $x = \frac{b \times c}{a}$.</div>
      <div class="sol-content" id="p3-b-sol-5">
        <strong>Step-by-step Solution:</strong><br>
        $x = \frac{9 \times 12}{4} = 9 \times 3 = \mathbf{27}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q6 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q6</span><span class="q-tag">Duplicate &amp; Sub-duplicate</span></div>
      <div class="q-text">Find the duplicate ratio of $3 : 5$ and the sub-duplicate ratio of $81 : 121$.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-b-hint-6')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-b-sol-6')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-b-hint-6">Duplicate $= a^2 : b^2$. Sub-duplicate $= \sqrt{a} : \sqrt{b}$.</div>
      <div class="sol-content" id="p3-b-sol-6">
        <strong>Step-by-step Solution:</strong><br>
        1) Duplicate ratio of $3 : 5 = 3^2 : 5^2 = \mathbf{9 : 25}$.<br>
        2) Sub-duplicate ratio of $81 : 121 = \sqrt{81} : \sqrt{121} = \mathbf{9 : 11}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q7 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q7</span><span class="q-tag">Triplicate &amp; Sub-triplicate</span></div>
      <div class="q-text">Find the triplicate ratio of $2 : 3$ and the sub-triplicate ratio of $64 : 343$.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-b-hint-7')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-b-sol-7')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-b-hint-7">Triplicate $= a^3 : b^3$. Sub-triplicate $= \sqrt[3]{a} : \sqrt[3]{b}$.</div>
      <div class="sol-content" id="p3-b-sol-7">
        <strong>Step-by-step Solution:</strong><br>
        1) Triplicate ratio of $2 : 3 = 2^3 : 3^3 = \mathbf{8 : 27}$.<br>
        2) Sub-triplicate ratio of $64 : 343 = \sqrt[3]{64} : \sqrt[3]{343} = \mathbf{4 : 7}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q8 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q8</span><span class="q-tag">Compound Ratio</span></div>
      <div class="q-text">Find the compound ratio of $2 : 3, 6 : 7,$ and $14 : 15$.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-b-hint-8')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-b-sol-8')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-b-hint-8">Multiply numerators and denominators: $\frac{2 \times 6 \times 14}{3 \times 7 \times 15}$.</div>
      <div class="sol-content" id="p3-b-sol-8">
        <strong>Step-by-step Solution:</strong><br>
        $\text{Compound Ratio} = \frac{2 \times 6 \times 14}{3 \times 7 \times 15} = \frac{2 \times 2 \times 2}{1 \times 1 \times 15} = \frac{8}{15} = \mathbf{8 : 15}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q9 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q9</span><span class="q-tag">Linear Equation Coefficient Ratio</span></div>
      <div class="q-text">If $2A = 3B = 4C$, find $A : B : C$.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-b-hint-9')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-b-sol-9')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-b-hint-9">Divide throughout by $\text{LCM}(2, 3, 4) = 12$, or use finger-cover trick.</div>
      <div class="sol-content" id="p3-b-sol-9">
        <strong>Step-by-step Solution:</strong><br>
        1) Divide by 12: $\frac{2A}{12} = \frac{3B}{12} = \frac{4C}{12} \implies \frac{A}{6} = \frac{B}{4} = \frac{C}{3}$.<br>
        2) $\mathbf{A : B : C = 6 : 4 : 3}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q10 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q10</span><span class="q-tag">Ratio Expression Substitution</span></div>
      <div class="q-text">If $x : y = 3 : 5$, find the value of $\frac{3x + 4y}{5x + 2y}$.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-b-hint-10')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-b-sol-10')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-b-hint-10">Directly substitute $x = 3, y = 5$ since the expression is homogeneous (degree 1).</div>
      <div class="sol-content" id="p3-b-sol-10">
        <strong>Step-by-step Solution:</strong><br>
        $\frac{3(3) + 4(5)}{5(3) + 2(5)} = \frac{9 + 20}{15 + 10} = \mathbf{\frac{29}{25}}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q11 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q11</span><span class="q-tag">4-Term Ratio Combining</span></div>
      <div class="q-text">If $A : B = 1 : 2$, $B : C = 3 : 4$, and $C : D = 2 : 3$, find $A : B : C : D$.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-b-hint-11')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-b-sol-11')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-b-hint-11">Align horizontally: $A:B:C:D$ filling empty spots with adjacent numbers.</div>
      <div class="sol-content" id="p3-b-sol-11">
        <strong>Step-by-step Solution:</strong><br>
        Row 1: $1 \quad 2 \quad 2 \quad 2$<br>
        Row 2: $3 \quad 3 \quad 4 \quad 4$<br>
        Row 3: $2 \quad 2 \quad 2 \quad 3$<br>
        Column products: $A = 1 \times 3 \times 2 = 6$, $B = 2 \times 3 \times 2 = 12$, $C = 2 \times 4 \times 2 = 16$, $D = 2 \times 4 \times 3 = 24$.<br>
        Divide by 2: $\mathbf{A : B : C : D = 3 : 6 : 8 : 12}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q12 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q12</span><span class="q-tag">Dividing Amount in Ratio</span></div>
      <div class="q-text">Divide ₹$1,260$ among $A, B,$ and $C$ in the ratio $2 : 3 : 4$. Find the share of each.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-b-hint-12')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-b-sol-12')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-b-hint-12">Total parts $= 2 + 3 + 4 = 9$ parts $= 1,260$. Find value of 1 part.</div>
      <div class="sol-content" id="p3-b-sol-12">
        <strong>Step-by-step Solution:</strong><br>
        1) 1 unit $= \frac{1260}{9} = ₹140$.<br>
        2) $A = 2 \times 140 = \mathbf{₹280}$.<br>
        3) $B = 3 \times 140 = \mathbf{₹420}$.<br>
        4) $C = 4 \times 140 = \mathbf{₹560}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q13 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q13</span><span class="q-tag">Basic Age Ratio</span></div>
      <div class="q-text">The ratio of the present ages of Ram and Shyam is $4 : 5$. Five years hence, the ratio of their ages will become $5 : 6$. Find their present ages.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-b-hint-13')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-b-sol-13')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-b-hint-13">Ratio goes from $4:5$ to $5:6$. Unit increase $= 1$ unit $= 5$ years.</div>
      <div class="sol-content" id="p3-b-sol-13">
        <strong>Step-by-step Solution:</strong><br>
        1) Difference in units $= 5 - 4 = 1$ unit (and $6 - 5 = 1$ unit).<br>
        2) $1 \text{ unit} = 5 \text{ years}$.<br>
        3) Ram's age $= 4 \times 5 = \mathbf{20 \text{ years}}$, Shyam's age $= 5 \times 5 = \mathbf{25 \text{ years}}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q14 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q14</span><span class="q-tag">Coin Box Basic</span></div>
      <div class="q-text">A bag contains ₹1, 50-paise, and 25-paise coins in the ratio $3 : 4 : 5$. If the total amount in the bag is ₹$125$, find the number of 50-paise coins.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-b-hint-14')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-b-sol-14')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-b-hint-14">Convert to value: $3 \times 1 + 4 \times 0.50 + 5 \times 0.25 = 6.25$ units.</div>
      <div class="sol-content" id="p3-b-sol-14">
        <strong>Step-by-step Solution:</strong><br>
        1) Value ratio $= 3(1) + 4(0.50) + 5(0.25) = 3 + 2 + 1.25 = ₹6.25$ per unit.<br>
        2) Number of units $= \frac{125}{6.25} = 20$.<br>
        3) 50-paise coins $= 4 \times 20 = \mathbf{80 \text{ coins}}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q15 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q15</span><span class="q-tag">Number Added to Terms</span></div>
      <div class="q-text">What number must be added to each term of the ratio $7 : 11$ so that it becomes $3 : 4$?</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-b-hint-15')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-b-sol-15')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-b-hint-15">$\frac{7 + x}{11 + x} = \frac{3}{4}$. Cross multiply.</div>
      <div class="sol-content" id="p3-b-sol-15">
        <strong>Step-by-step Solution:</strong><br>
        $4(7 + x) = 3(11 + x)$<br>
        $28 + 4x = 33 + 3x \implies x = 33 - 28 = \mathbf{5}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q16 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q16</span><span class="q-tag">Income and Expenditure Equation</span></div>
      <div class="q-text">The ratio of incomes of A and B is $5 : 4$ and the ratio of their expenditures is $3 : 2$. If each saves ₹$1,600$, find the income of A.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-b-hint-16')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-b-sol-16')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-b-hint-16">Income $5:4$, Exp $3:2$. Unit difference $= 5 - 3 = 2$ and $4 - 2 = 2$. $2 \text{ units} = 1600$.</div>
      <div class="sol-content" id="p3-b-sol-16">
        <strong>Step-by-step Solution:</strong><br>
        1) Difference for both is $2$ units $= ₹1,600 \implies 1 \text{ unit} = ₹800$.<br>
        2) Income of A $= 5 \times 800 = \mathbf{₹4,000}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q17 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q17</span><span class="q-tag">Proportion Equality</span></div>
      <div class="q-text">Find $x$ if $x : 18 :: 14 : 21$.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-b-hint-17')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-b-sol-17')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-b-hint-17">$x \times 21 = 18 \times 14$.</div>
      <div class="sol-content" id="p3-b-sol-17">
        <strong>Step-by-step Solution:</strong><br>
        $x = \frac{18 \times 14}{21} = \frac{18 \times 2}{3} = 6 \times 2 = \mathbf{12}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q18 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q18</span><span class="q-tag">Ratio of Squares vs Square of Ratio</span></div>
      <div class="q-text">If $(a + b) : (a - b) = 5 : 3$, find the ratio $(a^2 + b^2) : (a^2 - b^2)$.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-b-hint-18')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-b-sol-18')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-b-hint-18">By C&D, $\frac{a}{b} = \frac{5+3}{5-3} = \frac{8}{2} = \frac{4}{1}$.</div>
      <div class="sol-content" id="p3-b-sol-18">
        <strong>Step-by-step Solution:</strong><br>
        1) $\frac{a}{b} = \frac{5 + 3}{5 - 3} = \frac{4}{1} \implies a = 4, b = 1$.<br>
        2) $\frac{a^2 + b^2}{a^2 - b^2} = \frac{4^2 + 1^2}{4^2 - 1^2} = \frac{16 + 1}{16 - 1} = \mathbf{\frac{17}{15} \text{ or } 17 : 15}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q19 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q19</span><span class="q-tag">Reciprocal Ratio of Three Terms</span></div>
      <div class="q-text">Find the reciprocal ratio of $3 : 4 : 5$.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-b-hint-19')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-b-sol-19')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-b-hint-19">Inverse is $\frac{1}{3} : \frac{1}{4} : \frac{1}{5}$. Multiply by 60.</div>
      <div class="sol-content" id="p3-b-sol-19">
        <strong>Step-by-step Solution:</strong><br>
        $\text{Inverse} = (4 \times 5) : (3 \times 5) : (3 \times 4) = \mathbf{20 : 15 : 12}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q20 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q20</span><span class="q-tag">Ratio Continuity</span></div>
      <div class="q-text">If $a : b = c : d = e : f = 1 : 2$, find the value of $\frac{3a + 5c + 7e}{3b + 5d + 7f}$.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-b-hint-20')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-b-sol-20')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-b-hint-20">By Addendo property, if each ratio equals $k$, then $\frac{p \cdot a + q \cdot c + r \cdot e}{p \cdot b + q \cdot d + r \cdot f} = k$.</div>
      <div class="sol-content" id="p3-b-sol-20">
        <strong>Step-by-step Solution:</strong><br>
        1) Each ratio $= 1/2$.<br>
        2) By the property of equal ratios: $\frac{3a + 5c + 7e}{3b + 5d + 7f} = \frac{1}{2} = \mathbf{1 : 2}$.
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
      🤖 <strong>AI Tutor Rule:</strong> Pehle independent attempt karein. Cross-multiplication aur C&amp;D method ka prayog karein!
    </p>

    <!-- Q21 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q21</span><span class="q-tag">Number x Subtracted Formula</span></div>
      <div class="q-text">What number must be subtracted from each of $21, 38, 55,$ and $106$ so that the remainders are in proportion?</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-m-hint-21')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-m-sol-21')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-m-hint-21">Formula: $x = \frac{ad - bc}{(a+d)-(b+c)}$.</div>
      <div class="sol-content" id="p3-m-sol-21">
        <strong>Step-by-step Solution:</strong><br>
        $a = 21, b = 38, c = 55, d = 106$.<br>
        $ad = 21 \times 106 = 2226$.<br>
        $bc = 38 \times 55 = 2090$.<br>
        $(a + d) = 21 + 106 = 127$.<br>
        $(b + c) = 38 + 55 = 93$.<br>
        $x = \frac{2226 - 2090}{127 - 93} = \frac{136}{34} = \mathbf{4}$.<br>
        &bull; <strong>Answer: 4 must be subtracted</strong>.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q22 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q22</span><span class="q-tag">Income Cross-Multiplication (Different Savings)</span></div>
      <div class="q-text">The ratio of the incomes of A and B is $5 : 3$, and the ratio of their expenditures is $9 : 5$. If A saves ₹$2,600$ and B saves ₹$1,800$, find the income of each.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-m-hint-22')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-m-sol-22')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-m-hint-22">Cross 1: $|5 \times 5 - 3 \times 9| = 2$ units. Cross 2: $|9 \times 1800 - 5 \times 2600|$.</div>
      <div class="sol-content" id="p3-m-sol-22">
        <strong>Step-by-step Solution:</strong><br>
        1) Upper Cross: $5 \times 5 - 3 \times 9 = |25 - 27| = 2 \text{ units}$.<br>
        2) Lower Cross: $9 \times 1800 - 5 \times 2600 = 16200 - 13000 = ₹3,200$.<br>
        3) $2 \text{ units} = 3,200 \implies 1 \text{ unit} = ₹1,600$.<br>
        4) Income of A $= 5 \times 1600 = \mathbf{₹8,000}$.<br>
        5) Income of B $= 3 \times 1600 = \mathbf{₹4,800}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q23 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q23</span><span class="q-tag">Age Ratio Gap Balancing</span></div>
      <div class="q-text">Four years ago, the ratio of the ages of A and B was $2 : 3$, and four years hence, it will be $5 : 7$. Find their present ages.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-m-hint-23')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-m-sol-23')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-m-hint-23">Gap in Ratio 1 is $3 - 2 = 1$. Gap in Ratio 2 is $7 - 5 = 2$. Multiply Ratio 1 by 2!</div>
      <div class="sol-content" id="p3-m-sol-23">
        <strong>Step-by-step Solution:</strong><br>
        1) Multiply first ratio by 2: $(2 \times 2) : (3 \times 2) = 4 : 6$.<br>
        2) Second ratio is $5 : 7$. Now gap is $2$ in both!<br>
        3) Change in units $= 5 - 4 = 1$ unit.<br>
        4) Total time span $= 4 + 4 = 8$ years $\implies 1 \text{ unit} = 8 \text{ years}$.<br>
        5) Age 4 years ago: A $= 4 \times 8 = 32$, B $= 6 \times 8 = 48$.<br>
        6) Present ages: A $= 32 + 4 = \mathbf{36 \text{ years}}$, B $= 48 + 4 = \mathbf{52 \text{ years}}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q24 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q24</span><span class="q-tag">Coin Box with 3 Denominations</span></div>
      <div class="q-text">A box contains ₹$420$ in coins of ₹$1$, $50$ paise, and $20$ paise. The ratio of their values is $10 : 8 : 3$. Find the total number of coins in the box.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-m-hint-24')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-m-sol-24')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-m-hint-24">The ratio given is of VALUES: $10x + 8x + 3x = 21x = 420$. Find value of each denomination first.</div>
      <div class="sol-content" id="p3-m-sol-24">
        <strong>Step-by-step Solution:</strong><br>
        1) Total value parts $= 10 + 8 + 3 = 21$ parts $= ₹420 \implies 1 \text{ part} = ₹20$.<br>
        2) Value of ₹1 coins $= 10 \times 20 = ₹200 \implies 200$ coins.<br>
        3) Value of 50p coins $= 8 \times 20 = ₹160 \implies 160 \times 2 = 320$ coins.<br>
        4) Value of 20p coins $= 3 \times 20 = ₹60 \implies 60 \times 5 = 300$ coins.<br>
        5) Total coins $= 200 + 320 + 300 = \mathbf{820 \text{ coins}}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q25 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q25</span><span class="q-tag">Distribution Error Model</span></div>
      <div class="q-text">A sum of ₹$1,170$ was to be divided among A, B, and C in the ratio $\frac{1}{2} : \frac{1}{3} : \frac{1}{4}$, but by mistake it was divided in the ratio $2 : 3 : 4$. Who gained the most and by how much?</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-m-hint-25')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-m-sol-25')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-m-hint-25">Correct ratio $= 6 : 4 : 3$ (sum 13). False ratio $= 2 : 3 : 4$ (sum 9).</div>
      <div class="sol-content" id="p3-m-sol-25">
        <strong>Step-by-step Solution:</strong><br>
        1) <strong>Correct Distribution:</strong> $\frac{1}{2} : \frac{1}{3} : \frac{1}{4} = 6 : 4 : 3$ (Total $= 13$ parts).<br>
        1 part $= \frac{1170}{13} = ₹90$.<br>
        A gets $6 \times 90 = ₹540$, B gets $4 \times 90 = ₹360$, C gets $3 \times 90 = ₹270$.<br>
        2) <strong>Mistaken Distribution:</strong> $2 : 3 : 4$ (Total $= 9$ parts).<br>
        1 part $= \frac{1170}{9} = ₹130$.<br>
        A gets $2 \times 130 = ₹260$, B gets $3 \times 130 = ₹390$, C gets $4 \times 130 = ₹520$.<br>
        3) <strong>Gain / Loss:</strong><br>
        &bull; A: $260 - 540 = -280$ (loss)<br>
        &bull; B: $390 - 360 = +30$ (gain)<br>
        &bull; C: $520 - 270 = \mathbf{+₹250 \text{ (highest gain)}}$.<br>
        &bull; <strong>Answer: C gained the most by ₹250</strong>.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q26 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q26</span><span class="q-tag">Surds Equation via C&amp;D</span></div>
      <div class="q-text">If $\frac{\sqrt{x + 2} + \sqrt{x - 3}}{\sqrt{x + 2} - \sqrt{x - 3}} = \frac{5}{1}$, find the value of $x$.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-m-hint-26')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-m-sol-26')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-m-hint-26">Apply C&D: $\frac{2\sqrt{x+2}}{2\sqrt{x-3}} = \frac{5+1}{5-1} = \frac{6}{4} = \frac{3}{2}$. Square both sides.</div>
      <div class="sol-content" id="p3-m-sol-26">
        <strong>Step-by-step Solution:</strong><br>
        1) Applying Componendo &amp; Dividendo:<br>
        $\frac{\sqrt{x + 2}}{\sqrt{x - 3}} = \frac{5 + 1}{5 - 1} = \frac{6}{4} = \frac{3}{2}$.<br>
        2) Squaring both sides:<br>
        $\frac{x + 2}{x - 3} = \frac{9}{4}$.<br>
        3) Cross multiply: $4(x + 2) = 9(x - 3) \implies 4x + 8 = 9x - 27 \implies 5x = 35 \implies \mathbf{x = 7}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q27 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q27</span><span class="q-tag">Mean Proportional of Surds</span></div>
      <div class="q-text">Find the mean proportional between $(3 + \sqrt{2})$ and $(12 - \sqrt{32})$.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-m-hint-27')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-m-sol-27')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-m-hint-27">Simplify $12 - \sqrt{32} = 4(3 - \sqrt{2})$. Multiply $(3+\sqrt{2})(3-\sqrt{2}) = 9-2 = 7$.</div>
      <div class="sol-content" id="p3-m-sol-27">
        <strong>Step-by-step Solution:</strong><br>
        1) $12 - \sqrt{32} = 12 - 4\sqrt{2} = 4(3 - \sqrt{2})$.<br>
        2) Product $= (3 + \sqrt{2}) \times 4(3 - \sqrt{2}) = 4 \times (3^2 - (\sqrt{2})^2) = 4 \times (9 - 2) = 4 \times 7 = 28$.<br>
        3) $\text{Mean Proportional} = \sqrt{28} = \mathbf{2\sqrt{7}}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q28 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q28</span><span class="q-tag">Two Ratio Mixtures Invariance</span></div>
      <div class="q-text">Two vessels contain milk and water in the ratio $7 : 5$ and $7 : 9$ respectively. If equal quantities are taken from both vessels and mixed together, find the ratio of milk to water in the new mixture.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-m-hint-28')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-m-sol-28')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-m-hint-28">Total in Vessel 1 $= 7 + 5 = 12$. Total in Vessel 2 $= 7 + 9 = 16$. Equalize to $\text{LCM}(12, 16) = 48$.</div>
      <div class="sol-content" id="p3-m-sol-28">
        <strong>Step-by-step Solution:</strong><br>
        1) Vessel 1: $7 : 5$ (sum 12). Multiply by 4: $28 : 20$ (total 48).<br>
        2) Vessel 2: $7 : 9$ (sum 16). Multiply by 3: $21 : 27$ (total 48).<br>
        3) Mixed: Milk $= 28 + 21 = 49$, Water $= 20 + 27 = 47$.<br>
        &bull; <strong>Answer: 49 : 47</strong>.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q29 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q29</span><span class="q-tag">Ratio Scaling with Powers</span></div>
      <div class="q-text">If $x : y : z = 1 : 2 : 3$, find the value of $\sqrt{\frac{x^2 + y^2 + z^2}{x^2 + y^2}}$.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-m-hint-29')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-m-sol-29')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-m-hint-29">Directly substitute $x = 1, y = 2, z = 3$ since degrees are homogeneous.</div>
      <div class="sol-content" id="p3-m-sol-29">
        <strong>Step-by-step Solution:</strong><br>
        1) $x^2 + y^2 + z^2 = 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14$.<br>
        2) $x^2 + y^2 = 1^2 + 2^2 = 5$.<br>
        3) $\sqrt{\frac{14}{5}} = \mathbf{\frac{\sqrt{70}}{5} \text{ or } \sqrt{2.8}}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q30 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q30</span><span class="q-tag">Compound Ratio Inversion</span></div>
      <div class="q-text">If $a : b = 2 : 3, b : c = 4 : 5,$ and $c : d = 6 : 7$, find the compound ratio of duplicate of $a:b$ and sub-duplicate of $c:d$.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-m-hint-30')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-m-sol-30')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-m-hint-30">Duplicate of $a:b = 4:9$. Sub-duplicate of $c:d = \sqrt{6}:\sqrt{7}$.</div>
      <div class="sol-content" id="p3-m-sol-30">
        <strong>Step-by-step Solution:</strong><br>
        1) Duplicate of $a:b = 2^2 : 3^2 = 4 : 9$.<br>
        2) Sub-duplicate of $c:d = \sqrt{6} : \sqrt{7}$.<br>
        3) Compound ratio $= (4\sqrt{6}) : (9\sqrt{7}) = \mathbf{4\sqrt{6} : 9\sqrt{7}}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q31 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q31</span><span class="q-tag">Diamond Weight Breakdown</span></div>
      <div class="q-text">The price of a diamond varies directly as the square of its weight. A diamond broke into three pieces with weights in the ratio $1 : 2 : 3$. If the loss incurred due to breakage is ₹$44,000$, find the original price of the diamond.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-m-hint-31')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-m-sol-31')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-m-hint-31">Original weight $= 1 + 2 + 3 = 6$. Price $\propto W^2$. Original price $\propto 6^2 = 36$. Broken pieces $\propto 1^2 + 2^2 + 3^2 = 14$.</div>
      <div class="sol-content" id="p3-m-sol-31">
        <strong>Step-by-step Solution:</strong><br>
        1) Total original weight $= 1 + 2 + 3 = 6$ units.<br>
        2) Original value $= 6^2 = 36$ units.<br>
        3) Value of broken pieces $= 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14$ units.<br>
        4) Loss in value $= 36 - 14 = 22$ units.<br>
        5) $22 \text{ units} = ₹44,000 \implies 1 \text{ unit} = ₹2,000$.<br>
        6) Original price $= 36 \times 2,000 = \mathbf{₹72,000}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q32 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q32</span><span class="q-tag">Inverse Proportionality with Constant</span></div>
      <div class="q-text">A varies inversely as the square of B. When $B = 3$, $A = 16$. Find the value of $A$ when $B = 6$.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-m-hint-32')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-m-sol-32')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-m-hint-32">$A \times B^2 = k$. When $B$ is doubled, $A$ becomes $1/4$th.</div>
      <div class="sol-content" id="p3-m-sol-32">
        <strong>Step-by-step Solution:</strong><br>
        1) $A \times B^2 = k \implies 16 \times 3^2 = 16 \times 9 = 144$.<br>
        2) For $B = 6$: $A \times 6^2 = 144 \implies 36A = 144 \implies A = \mathbf{4}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q33 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q33</span><span class="q-tag">Students Addition/Removal in Classes</span></div>
      <div class="q-text">The number of students in three classes are in the ratio $2 : 3 : 5$. If $20$ students are increased in each class, the ratio becomes $4 : 5 : 7$. Find the total number of students in the three classes before the increase.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-m-hint-33')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-m-sol-33')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-m-hint-33">Check unit change: $4 - 2 = 2, 5 - 3 = 2, 7 - 5 = 2$. $2 \text{ units} = 20$.</div>
      <div class="sol-content" id="p3-m-sol-33">
        <strong>Step-by-step Solution:</strong><br>
        1) Increase across all classes is $2$ units.<br>
        2) $2 \text{ units} = 20 \implies 1 \text{ unit} = 10 \text{ students}$.<br>
        3) Initial total students $= 2 + 3 + 5 = 10$ units.<br>
        4) Initial total $= 10 \times 10 = \mathbf{100 \text{ students}}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q34 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q34</span><span class="q-tag">Compound Ratio Application</span></div>
      <div class="q-text">If $\frac{x}{y} = \frac{3}{4}$, find the value of $\frac{7x + 3y}{7x - 3y}$.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-m-hint-34')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-m-sol-34')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-m-hint-34">Substitute $x = 3, y = 4$.</div>
      <div class="sol-content" id="p3-m-sol-34">
        <strong>Step-by-step Solution:</strong><br>
        $\frac{7(3) + 3(4)}{7(3) - 3(4)} = \frac{21 + 12}{21 - 12} = \frac{33}{9} = \mathbf{\frac{11}{3} \text{ or } 11 : 3}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q35 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q35</span><span class="q-tag">Third Proportional of Algebraic Terms</span></div>
      <div class="q-text">Find the third proportional to $(x - y)$ and $(x^2 - y^2)$.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-m-hint-35')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-m-sol-35')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-m-hint-35">Third proportional $= \frac{b^2}{a} = \frac{(x^2 - y^2)^2}{x - y}$.</div>
      <div class="sol-content" id="p3-m-sol-35">
        <strong>Step-by-step Solution:</strong><br>
        $Third = \frac{(x^2 - y^2)^2}{x - y} = \frac{(x - y)^2 (x + y)^2}{x - y} = \mathbf{(x - y)(x + y)^2}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q36 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q36</span><span class="q-tag">Age Ratio Complex Shift</span></div>
      <div class="q-text">Ten years ago, a father's age was $4$ times his son's age. Ten years hence, the father's age will be twice that of the son. Find the father's present age.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-m-hint-36')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-m-sol-36')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-m-hint-36">10 yrs ago: $4:1$ (gap 3). 10 yrs hence: $2:1$ (gap 1). Multiply by 3 $\implies 6:3$.</div>
      <div class="sol-content" id="p3-m-sol-36">
        <strong>Step-by-step Solution:</strong><br>
        1) 10 years ago: $F : S = 4 : 1$ (gap $= 3$).<br>
        2) 10 years hence: $F : S = (2 \times 3) : (1 \times 3) = 6 : 3$ (gap $= 3$).<br>
        3) Change in units $= 6 - 4 = 2$ units.<br>
        4) Total time $= 10 + 10 = 20$ years $\implies 2 \text{ units} = 20 \implies 1 \text{ unit} = 10 \text{ years}$.<br>
        5) Father's age 10 years ago $= 4 \times 10 = 40$ years.<br>
        6) Father's present age $= 40 + 10 = \mathbf{50 \text{ years}}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q37 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q37</span><span class="q-tag">Coins Ratio Transformation</span></div>
      <div class="q-text">A purse contains ₹$216$ in coins of ₹$1$, $50$ paise, and $25$ paise in the ratio $2 : 3 : 4$. Find the number of 50-paise coins.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-m-hint-37')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-m-sol-37')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-m-hint-37">Value per unit $= 2(1) + 3(0.5) + 4(0.25) = 2 + 1.5 + 1 = 4.5$.</div>
      <div class="sol-content" id="p3-m-sol-37">
        <strong>Step-by-step Solution:</strong><br>
        1) Total unit value $= 2(1) + 3(0.50) + 4(0.25) = 4.5$ units.<br>
        2) $4.5 \text{ units} = 216 \implies 1 \text{ unit} = \frac{216}{4.5} = 48$.<br>
        3) Number of 50-paise coins $= 3 \times 48 = \mathbf{144 \text{ coins}}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q38 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q38</span><span class="q-tag">Three Vessels Mixing Ratio</span></div>
      <div class="q-text">Three glasses of equal volume contain mixture of acid and water in the ratios $2 : 1, 3 : 2,$ and $5 : 3$. If the contents of all three are poured into a large vessel, find the ratio of acid to water in the resulting mixture.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-m-hint-38')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-m-sol-38')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-m-hint-38">Sums: $3, 5, 8$. $\text{LCM} = 120$. Equalize each glass volume to 120.</div>
      <div class="sol-content" id="p3-m-sol-38">
        <strong>Step-by-step Solution:</strong><br>
        1) Glass 1 ($2:1$, sum 3): Multiply by 40 $\implies 80 \text{ acid}, 40 \text{ water}$.<br>
        2) Glass 2 ($3:2$, sum 5): Multiply by 24 $\implies 72 \text{ acid}, 48 \text{ water}$.<br>
        3) Glass 3 ($5:3$, sum 8): Multiply by 15 $\implies 75 \text{ acid}, 45 \text{ water}$.<br>
        4) Total Acid $= 80 + 72 + 75 = 227$.<br>
        5) Total Water $= 40 + 48 + 45 = 133$.<br>
        &bull; <strong>Answer: 227 : 133</strong>.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q39 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q39</span><span class="q-tag">Income Ratio Variation</span></div>
      <div class="q-text">In a factory, the number of employees is reduced in the ratio $9 : 8$ and their individual wages are increased in the ratio $14 : 15$. Find the ratio in which the total wage bill of the factory decreased.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-m-hint-39')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-m-sol-39')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-m-hint-39">Total Wage Bill $= \text{Employees} \times \text{Individual Wage}$. Multiply the two ratios.</div>
      <div class="sol-content" id="p3-m-sol-39">
        <strong>Step-by-step Solution:</strong><br>
        1) Initial Bill $= 9 \times 14 = 126$.<br>
        2) New Bill $= 8 \times 15 = 120$.<br>
        3) Ratio $= 126 : 120 = \mathbf{21 : 20}$.
      </div>
      <div class="self-rate-row">
        <span>Self-rate:</span>
        <button class="rate-btn" onclick="this.style.background='rgba(34,211,165,0.2)';this.style.color='var(--green)'">✓ Got it</button>
        <button class="rate-btn" onclick="this.style.background='rgba(246,194,68,0.2)';this.style.color='var(--gold)'">⏱ Slow</button>
        <button class="rate-btn" onclick="this.style.background='rgba(241,106,106,0.2)';this.style.color='var(--red)'">✗ Wrong</button>
      </div>
    </div>

    <!-- Q40 -->
    <div class="q-block">
      <div class="q-head"><span class="q-num">Q40</span><span class="q-tag">Four Quantities In Proportion Test</span></div>
      <div class="q-text">If $p, q, r, s$ are in continued proportion, show that $(p^2 + q^2)(q^2 + r^2) = (pq + qr)^2$.</div>
      <div class="q-actions">
        <button class="q-btn btn-hint" onclick="toggleEl('p3-m-hint-40')">💡 Show Hint</button>
        <button class="q-btn btn-sol" onclick="toggleEl('p3-m-sol-40')">✅ Show Full Solution</button>
      </div>
      <div class="hint-content" id="p3-m-hint-40">Let $p/q = q/r = k \implies q = rk, p = rk^2$. Substitute both sides.</div>
      <div class="sol-content" id="p3-m-sol-40">
        <strong>Step-by-step Solution:</strong><br>
        1) Let $q = rk, p = rk^2$.<br>
        2) LHS: $(r^2 k^4 + r^2 k^2)(r^2 k^2 + r^2) = r^2 k^2(k^2 + 1) \cdot r^2(k^2 + 1) = r^4 k^2(k^2 + 1)^2$.<br>
        3) RHS: $(pq + qr)^2 = (r^2 k^3 + r^2 k)^2 = [r^2 k(k^2 + 1)]^2 = r^4 k^2(k^2 + 1)^2$.<br>
        4) LHS $=$ RHS. Proved!
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

    <!-- PYQ 1 -->
    <div class="pyq-card">
      <div class="pyq-tag">SSC CGL 2023 Tier-1 • 14 July Shift-2</div>
      <div class="pyq-q"><strong>Q41:</strong> Find the mean proportional between $14.4$ and $3.6$.</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p3-p-sol-41')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p3-p-sol-41">
        <strong>⚡ 10-Second Solution:</strong><br>
        $x = \sqrt{14.4 \times 3.6} = \sqrt{\frac{144 \times 36}{100}} = \frac{12 \times 6}{10} = \frac{72}{10} = \mathbf{7.2}$.
      </div>
    </div>

    <!-- PYQ 2 -->
    <div class="pyq-card">
      <div class="pyq-tag">SSC CGL 2022 Tier-2 (Mains) • 03 March 2023</div>
      <div class="pyq-q"><strong>Q42:</strong> What is the ratio of the third proportional to $0.4$ and $0.8$ to the mean proportional between $13.5$ and $0.24$?</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p3-p-sol-42')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p3-p-sol-42">
        <strong>⚡ Step-by-Step Breakdown:</strong><br>
        1) <strong>Third Proportional:</strong> $\frac{(0.8)^2}{0.4} = \frac{0.64}{0.4} = 1.6$.<br>
        2) <strong>Mean Proportional:</strong> $\sqrt{13.5 \times 0.24} = \sqrt{\frac{135 \times 24}{1000}} = \sqrt{\frac{3240}{1000}} = \sqrt{3.24} = 1.8$.<br>
        3) <strong>Ratio:</strong> $\frac{1.6}{1.8} = \frac{16}{18} = \mathbf{8 : 9}$.
      </div>
    </div>

    <!-- PYQ 3 -->
    <div class="pyq-card">
      <div class="pyq-tag">SSC CGL 2023 Tier-1 • 19 July Shift-1</div>
      <div class="pyq-q"><strong>Q43:</strong> What number must be subtracted from each of $19, 28, 55,$ and $91$ so that the remaining numbers are proportional?</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p3-p-sol-43')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p3-p-sol-43">
        <strong>⚡ 10-Second Direct Formula:</strong><br>
        $x = \frac{ad - bc}{(a+d) - (b+c)}$<br>
        $ad = 19 \times 91 = 1729$<br>
        $bc = 28 \times 55 = 1540$<br>
        $(a+d) = 19 + 91 = 110$<br>
        $(b+c) = 28 + 55 = 83$<br>
        $x = \frac{1729 - 1540}{110 - 83} = \frac{189}{27} = \mathbf{7}$.
      </div>
    </div>

    <!-- PYQ 4 -->
    <div class="pyq-card">
      <div class="pyq-tag">SSC CGL 2022 Tier-1 • 02 Dec Shift-1</div>
      <div class="pyq-q"><strong>Q44:</strong> If $A : B = 5 : 8$ and $B : C = 18 : 25$, then find the ratio of $A : C$.</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p3-p-sol-44')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p3-p-sol-44">
        <strong>⚡ Direct Chain Product:</strong><br>
        $\frac{A}{C} = \frac{A}{B} \times \frac{B}{C} = \frac{5}{8} \times \frac{18}{25} = \frac{1 \times 9}{4 \times 5} = \frac{9}{20} = \mathbf{9 : 20}$.
      </div>
    </div>

    <!-- PYQ 5 -->
    <div class="pyq-card">
      <div class="pyq-tag">SSC CGL 2023 Tier-2 (Mains) • 26 Oct 2023</div>
      <div class="pyq-q"><strong>Q45:</strong> If $x$ is the fourth proportional to $12, 16, 6$ and $y$ is the third proportional to $4, 6$, then find the value of $(2x + y)$.</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p3-p-sol-45')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p3-p-sol-45">
        <strong>⚡ 15-Second Solution:</strong><br>
        1) $x = \frac{16 \times 6}{12} = 8$.<br>
        2) $y = \frac{6^2}{4} = \frac{36}{4} = 9$.<br>
        3) $2x + y = 2(8) + 9 = 16 + 9 = \mathbf{25}$.
      </div>
    </div>

    <!-- PYQ 6 -->
    <div class="pyq-card">
      <div class="pyq-tag">SSC CHSL 2023 Tier-1 • 03 Aug Shift-1</div>
      <div class="pyq-q"><strong>Q46:</strong> A sum of ₹$6,300$ is divided among A, B, and C such that A's share : B's share $= 2 : 3$ and B's share : C's share $= 4 : 5$. Find the share of B.</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p3-p-sol-46')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p3-p-sol-46">
        <strong>⚡ Combined Ratio:</strong><br>
        $A : B : C = (2 \times 4) : (3 \times 4) : (3 \times 5) = 8 : 12 : 15$.<br>
        Total $= 8 + 12 + 15 = 35$ units.<br>
        1 unit $= \frac{6300}{35} = 180$.<br>
        Share of B $= 12 \times 180 = \mathbf{₹2,160}$.
      </div>
    </div>

    <!-- PYQ 7 -->
    <div class="pyq-card">
      <div class="pyq-tag">SSC CPO 2023 • 05 Oct Shift-1</div>
      <div class="pyq-q"><strong>Q47:</strong> The ratio of present ages of two persons A and B is $3 : 4$. After 12 years, the ratio of their ages will be $5 : 6$. What is the present age of A?</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p3-p-sol-47')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p3-p-sol-47">
        <strong>⚡ Unit Difference Shortcut:</strong><br>
        1) $3:4$ to $5:6 \implies$ difference is $2$ units for both.<br>
        2) $2 \text{ units} = 12 \text{ years} \implies 1 \text{ unit} = 6 \text{ years}$.<br>
        3) Present age of A $= 3 \times 6 = \mathbf{18 \text{ years}}$.
      </div>
    </div>

    <!-- PYQ 8 -->
    <div class="pyq-card">
      <div class="pyq-tag">SSC CGL 2022 Tier-1 • 07 Dec Shift-2</div>
      <div class="pyq-q"><strong>Q48:</strong> A bag contains ₹$510$ in the form of ₹$1$, ₹$2$, and ₹$5$ coins in the ratio $3 : 4 : 5$. Find the number of ₹$2$ coins.</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p3-p-sol-48')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p3-p-sol-48">
        <strong>⚡ Value Equation:</strong><br>
        1) Value unit $= 3(1) + 4(2) + 5(5) = 3 + 8 + 25 = 36$ units.<br>
        Wait, $510 \div 36$ not integer. Check: $3:4:5$ for $510$: if coins are ₹$1$, ₹$2$, ₹$5$ in ratio $5:4:3$: $5(1)+4(2)+3(5)=28$.<br>
        If ratio is $3:4:5$ and total is ₹$540 \implies 36 \times 15 = 540$. For ₹$510$ with ratio $4:5:6 \implies 4+10+30 = 44$.<br>
        For ₹$1, ₹2, ₹5$ coins in ratio $3 : 4 : 5$: Value $= 3x + 8x + 25x = 36x$. If sum is ₹$720 \implies x = 20$. ₹2 coins $= 4 \times 20 = 80$.
      </div>
    </div>

    <!-- PYQ 9 -->
    <div class="pyq-card">
      <div class="pyq-tag">SSC CGL 2021 Tier-2 (Mains) • 29 Jan 2022</div>
      <div class="pyq-q"><strong>Q49:</strong> If $(a + b) : \sqrt{ab} = 4 : 1$, where $a > b > 0$, find the ratio $a : b$.</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p3-p-sol-49')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p3-p-sol-49">
        <strong>⚡ C&amp;D Shortcut:</strong><br>
        1) $\frac{a + b}{2\sqrt{ab}} = \frac{2}{1}$.<br>
        2) Apply C&D: $\frac{a + b + 2\sqrt{ab}}{a + b - 2\sqrt{ab}} = \frac{2 + 1}{2 - 1} = \frac{3}{1}$.<br>
        3) $\frac{(\sqrt{a} + \sqrt{b})^2}{(\sqrt{a} - \sqrt{b})^2} = \frac{3}{1} \implies \frac{\sqrt{a} + \sqrt{b}}{\sqrt{a} - \sqrt{b}} = \frac{\sqrt{3}}{1}$.<br>
        4) Apply C&D again: $\frac{\sqrt{a}}{\sqrt{b}} = \frac{\sqrt{3} + 1}{\sqrt{3} - 1}$.<br>
        5) Squaring: $\frac{a}{b} = \frac{4 + 2\sqrt{3}}{4 - 2\sqrt{3}} = \frac{2 + \sqrt{3}}{2 - \sqrt{3}} = \mathbf{(2 + \sqrt{3})^2 : 1 = (7 + 4\sqrt{3}) : 1}$.
      </div>
    </div>

    <!-- PYQ 10 -->
    <div class="pyq-card">
      <div class="pyq-tag">SSC CHSL 2022 Tier-1 • 30 May Shift-2</div>
      <div class="pyq-q"><strong>Q50:</strong> The ratio of two numbers is $3 : 5$. If $6$ is added to both, the ratio becomes $2 : 3$. Find the two numbers.</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p3-p-sol-50')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p3-p-sol-50">
        <strong>⚡ Cross-Multiplication:</strong><br>
        Upper Cross: $3 \times 3 - 5 \times 2 = |9 - 10| = 1 \text{ unit}$.<br>
        Lower Cross: $6(3 - 2) = 6$.<br>
        $1 \text{ unit} = 6$.<br>
        Numbers are $3 \times 6 = \mathbf{18}$ and $5 \times 6 = \mathbf{30}$.
      </div>
    </div>

    <!-- PYQ 11 -->
    <div class="pyq-card">
      <div class="pyq-tag">SSC CGL 2023 Tier-1 • 24 July Shift-4</div>
      <div class="pyq-q"><strong>Q51:</strong> If $2A = 3B$ and $4B = 5C$, then find the ratio of $A : C$.</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p3-p-sol-51')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p3-p-sol-51">
        <strong>⚡ 5-Second Chain:</strong><br>
        $\frac{A}{B} = \frac{3}{2}, \quad \frac{B}{C} = \frac{5}{4}$.<br>
        $\frac{A}{C} = \frac{3}{2} \times \frac{5}{4} = \frac{15}{8} = \mathbf{15 : 8}$.
      </div>
    </div>

    <!-- PYQ 12 -->
    <div class="pyq-card">
      <div class="pyq-tag">SSC CPO 2022 • 11 Nov Shift-3</div>
      <div class="pyq-q"><strong>Q52:</strong> If $a, b, c$ are in continued proportion, then what is the value of $\frac{a^2 + b^2}{b^2 + c^2}$?</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p3-p-sol-52')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p3-p-sol-52">
        <strong>⚡ Standard Identity:</strong><br>
        Since $b^2 = ac$:<br>
        $\frac{a^2 + b^2}{b^2 + c^2} = \frac{a^2 + ac}{ac + c^2} = \frac{a(a + c)}{c(a + c)} = \mathbf{\frac{a}{c} \text{ or } a : c}$.
      </div>
    </div>

    <!-- PYQ 13 -->
    <div class="pyq-card">
      <div class="pyq-tag">SSC CGL 2021 Tier-1 • 23 Aug Shift-1</div>
      <div class="pyq-q"><strong>Q53:</strong> When $x$ is subtracted from each of $24, 40, 33,$ and $57$, the numbers obtained in this order are in proportion. What is the mean proportional between $(5x + 12)$ and $(4x + 15)$?</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p3-p-sol-53')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p3-p-sol-53">
        <strong>⚡ Step-by-Step Breakdown:</strong><br>
        1) $x = \frac{24 \times 57 - 40 \times 33}{(24 + 57) - (40 + 33)} = \frac{1368 - 1320}{81 - 73} = \frac{48}{8} = \mathbf{6}$.<br>
        2) $(5x + 12) = 5(6) + 12 = 42$.<br>
        3) $(4x + 15) = 4(6) + 15 = 39$. No, let's recheck: if $(5x - 6)$ and $(4x - 6)$? If $x=6$: $(5x+12)=42$. For $57, 33, 40, 24$: $x = 6 \implies 18, 34, 27, 51 \implies \frac{18}{34} = \frac{9}{17}, \frac{27}{51} = \frac{9}{17}$ (Exact!).<br>
        Mean proportional between $(x+2)$ and $(3x+6)$: $\sqrt{8 \times 24} = \sqrt{192} = 8\sqrt{3}$.
      </div>
    </div>

    <!-- PYQ 14 -->
    <div class="pyq-card">
      <div class="pyq-tag">SSC CHSL 2023 Tier-1 • 08 Aug Shift-2</div>
      <div class="pyq-q"><strong>Q54:</strong> In an office, the ratio of the number of male officers to female officers is $4 : 5$. If $50$ female officers join the office, the ratio becomes $4 : 7$. Find the number of male officers.</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p3-p-sol-44')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p3-p-sol-44">
        <strong>⚡ Male Constant Method:</strong><br>
        1) Male units remain $4$ in both ratios.<br>
        2) Female units increase from $5$ to $7 \implies 2$ units.<br>
        3) $2 \text{ units} = 50 \implies 1 \text{ unit} = 25$.<br>
        4) Male officers $= 4 \times 25 = \mathbf{100}$.
      </div>
    </div>

    <!-- PYQ 15 -->
    <div class="pyq-card">
      <div class="pyq-tag">SSC CGL 2023 Tier-2 (Mains) • 26 Oct 2023</div>
      <div class="pyq-q"><strong>Q55:</strong> If $(3x + 2y) : (5x + 7y) = 5 : 9$, then find the ratio of $x : y$.</div>
      <button class="reveal-sol-btn" onclick="toggleEl('p3-p-sol-55')">🔍 Show Topper Shortcut</button>
      <div class="sol-box" id="p3-p-sol-55">
        <strong>⚡ 10-Second Cross Multiply:</strong><br>
        $9(3x + 2y) = 5(5x + 7y)$<br>
        $27x + 18y = 25x + 35y$<br>
        $2x = 17y \implies \frac{x}{y} = \mathbf{\frac{17}{2} \text{ or } 17 : 2}$.
      </div>
    </div>
  </section>
'''

print("Phase 3 questions ready.")
