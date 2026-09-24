# -*- coding: utf-8 -*-
"""
Phase 2 Theory Chapters, Formula Vault, Shortcuts & Traps
"""

def get_theory_chapters():
    return r'''
  <!-- ========================================== -->
  <!-- 📖 COMPREHENSIVE TEXTBOOK NOTES (BOOK EDITION) -->
  <!-- ========================================== -->
  <section class="book-chapter" id="sec-theory">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:18px;">
      <div>
        <span class="chap-badge">THEORY CHAPTERS</span>
        <h2 style="font-size:1.45rem;font-weight:800;color:#fff;">📖 Exhaustive Textbook Notes: Percentage (प्रतिशतता)</h2>
      </div>
      <span style="font-size:0.82rem;color:var(--text-muted);">6 Detailed Modules &bull; Complete Coverage</span>
    </div>

    <!-- Module 1 -->
    <div style="margin-bottom:28px;">
      <span class="chap-badge">MODULE 1</span>
      <h3 class="chap-title">1. Percentage Basics &amp; Fraction &harr; Percentage Master Table</h3>
      <p class="book-p">
        प्रतिशत (Percentage) का शाब्दिक अर्थ है "प्रति 100" (Per Hundred)। किसी भी संख्या या भिन्न को प्रतिशत में बदलने के लिए $100$ से गुणा किया जाता है, और प्रतिशत को भिन्न में बदलने के लिए $100$ से भाग दिया जाता है।
      </p>

      <div class="table-wrap">
        <table class="book-table">
          <thead>
            <tr>
              <th>Fraction</th>
              <th>Percentage (%)</th>
              <th>Decimal</th>
              <th>Derived Multiples (High SSC Frequency)</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>$1/2$</td><td>$50\%$</td><td>$0.50$</td><td>$3/2 = 150\%$</td></tr>
            <tr><td>$1/3$</td><td>$33\frac{1}{3}\% = 33.33\%$</td><td>$0.333$</td><td>$2/3 = 66.67\%$</td></tr>
            <tr><td>$1/4$</td><td>$25\%$</td><td>$0.25$</td><td>$3/4 = 75\%$</td></tr>
            <tr><td>$1/5$</td><td>$20\%$</td><td>$0.20$</td><td>$2/5 = 40\%, 3/5 = 60\%, 4/5 = 80\%$</td></tr>
            <tr><td>$1/6$</td><td>$16\frac{2}{3}\% = 16.67\%$</td><td>$0.1667$</td><td>$5/6 = 83.33\%$</td></tr>
            <tr><td>$1/7$</td><td>$14\frac{2}{7}\% = 14.28\%$</td><td>$0.1428$</td><td>$2/7 = 28.57\%, 3/7 = 42.86\%, 4/7 = 57.14\%$</td></tr>
            <tr><td>$1/8$</td><td>$12\frac{1}{2}\% = 12.5\%$</td><td>$0.125$</td><td>$3/8 = 37.5\%, 5/8 = 62.5\%, 7/8 = 87.5\%$</td></tr>
            <tr><td>$1/9$</td><td>$11\frac{1}{9}\% = 11.11\%$</td><td>$0.111$</td><td>$2/9 = 22.22\%, 4/9 = 44.44\%, 5/9 = 55.55\%$</td></tr>
            <tr><td>$1/10$</td><td>$10\%$</td><td>$0.10$</td><td>$3/10 = 30\%, 7/10 = 70\%$</td></tr>
            <tr><td>$1/11$</td><td>$9\frac{1}{11}\% = 9.09\%$</td><td>$0.0909$</td><td>$2/11 = 18.18\%, 3/11 = 27.27\%, 4/11 = 36.36\%$</td></tr>
            <tr><td>$1/12$</td><td>$8\frac{1}{3}\% = 8.33\%$</td><td>$0.0833$</td><td>$5/12 = 41.67\%, 7/12 = 58.33\%$</td></tr>
            <tr><td>$1/13$</td><td>$7\frac{9}{13}\% = 7.69\%$</td><td>$0.0769$</td><td>$2/13 = 15.38\%$</td></tr>
            <tr><td>$1/14$</td><td>$7\frac{1}{7}\% = 7.14\%$</td><td>$0.0714$</td><td>$3/14 = 21.43\%$</td></tr>
            <tr><td>$1/15$</td><td>$6\frac{2}{3}\% = 6.67\%$</td><td>$0.0667$</td><td>$4/15 = 26.67\%$</td></tr>
            <tr><td>$1/16$</td><td>$6\frac{1}{4}\% = 6.25\%$</td><td>$0.0625$</td><td>$3/16 = 18.75\%, 5/16 = 31.25\%$</td></tr>
            <tr><td>$1/20$</td><td>$5\%$</td><td>$0.05$</td><td>$1/25 = 4\%, 1/24 = 4.16\%$</td></tr>
          </tbody>
        </table>
      </div>

      <div class="concept-callout">
        <strong>⚡ Commutative Law of Percentages:</strong>
        $$A\% \text{ of } B = B\% \text{ of } A = \frac{A \times B}{100}$$
        <strong>Topper Trick:</strong> यदि प्रश्न में $64\% \text{ of } 25$ पूछा जाए, तो सीधे $25\% \text{ of } 64$ निकालें! $25\% = 1/4$, अतः $\frac{64}{4} = \mathbf{16}$ मात्र 2 सेकंड में!
      </div>
    </div>

    <!-- Module 2 -->
    <div style="margin-bottom:28px;">
      <span class="chap-badge">MODULE 2</span>
      <h3 class="chap-title">2. Percentage Increase, Decrease &amp; Multiplying Factors (MF)</h3>
      <p class="book-p">
        किसी राशि में वृद्धि (Increase) या कमी (Decrease) को परंपरागत तरीके से जोड़ने-घटाने के बजाय <strong>गुणांक (Multiplying Factor)</strong> से एक ही कदम में हल किया जाता है।
      </p>

      <div class="table-wrap">
        <table class="book-table">
          <thead>
            <tr>
              <th>प्रतिशत परिवर्तन (% Change)</th>
              <th>दशमलव गुणांक (Decimal MF)</th>
              <th>भिन्न गुणांक (Fractional MF)</th>
              <th>अनुपात रूप (Initial : Final)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>$+20\%$ वृद्धि</strong></td>
              <td>$\times 1.20$</td>
              <td>$\times \frac{6}{5}$</td>
              <td>$5 : 6$</td>
            </tr>
            <tr>
              <td><strong>$-25\%$ कमी</strong></td>
              <td>$\times 0.75$</td>
              <td>$\times \frac{3}{4}$</td>
              <td>$4 : 3$</td>
            </tr>
            <tr>
              <td><strong>$+16\frac{2}{3}\% (+1/6)$ वृद्धि</strong></td>
              <td>$\approx \times 1.167$</td>
              <td>$\times \frac{7}{6}$</td>
              <td>$6 : 7$</td>
            </tr>
            <tr>
              <td><strong>$-14\frac{2}{7}\% (-1/7)$ कमी</strong></td>
              <td>$\approx \times 0.857$</td>
              <td>$\times \frac{6}{7}$</td>
              <td>$7 : 6$</td>
            </tr>
            <tr>
              <td><strong>$+37.5\% (+3/8)$ वृद्धि</strong></td>
              <td>$\times 1.375$</td>
              <td>$\times \frac{11}{8}$</td>
              <td>$8 : 11$</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="concept-callout">
        <strong>📌 Comparison Rules — Base Identifying Trap:</strong><br>
        1. <strong>"$A$ is what $\%$ of $B$?"</strong> &rarr; $\frac{A}{B} \times 100\%$ (Base is $B$).<br>
        2. <strong>"$A$ is what $\%$ more than $B$?"</strong> &rarr; $\frac{A - B}{B} \times 100\%$ (Base is $B$).<br>
        3. <strong>"$B$ is what $\%$ less than $A$?"</strong> &rarr; $\frac{A - B}{A} \times 100\%$ (Base is $A$).<br>
        <span style="color:var(--gold);">नियम:</span> "Than" (से) या "Of" (का) जिसके साथ लगा हो, वह हमेशा हर (Denominator) में आता है!
      </div>
    </div>

    <!-- Module 3 -->
    <div style="margin-bottom:28px;">
      <span class="chap-badge">MODULE 3</span>
      <h3 class="chap-title">3. Successive Percentage Change &amp; The Universal AB Formula</h3>
      <p class="book-p">
        जब किसी राशि में लगातार दो बार प्रतिशत परिवर्तन होता है, तो कुल शुद्ध परिवर्तन केवल दोनों को जोड़कर नहीं निकलता, बल्कि संयुक्त प्रभाव (compound effect) उत्पन्न होता है।
      </p>

      <div class="concept-callout">
        <strong>🔥 The Universal AB Formula:</strong>
        $$\text{Net } \% = a + b + \frac{a \times b}{100}$$
        <strong>चिह्न नियम (Sign Convention):</strong><br>
        &bull; वृद्धि (Increase) के लिए धनात्मक चिह्न ($+$)<br>
        &bull; कमी (Decrease / Discount) के लिए ऋणात्मक चिह्न ($-$)
      </div>

      <div class="table-wrap">
        <table class="book-table">
          <thead>
            <tr>
              <th>स्थिति (Case)</th>
              <th>परिवर्तन $a$ एवं $b$</th>
              <th>सूत्र (Resulting Formula)</th>
              <th>उदाहरण</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>दोनों में वृद्धि</td>
              <td>$+a\%, +b\%$</td>
              <td>$$a + b + \frac{ab}{100}$$</td>
              <td>$+10\%, +20\% \implies 10 + 20 + \frac{200}{100} = \mathbf{+32\%}$</td>
            </tr>
            <tr>
              <td>एक वृद्धि, एक कमी</td>
              <td>$+a\%, -b\%$</td>
              <td>$$a - b - \frac{ab}{100}$$</td>
              <td>$+20\%, -10\% \implies 20 - 10 - \frac{200}{100} = \mathbf{+8\%}$</td>
            </tr>
            <tr>
              <td>दोनों में कमी (क्रमागत छूट)</td>
              <td>$-a\%, -b\%$</td>
              <td>$$-a - b + \frac{ab}{100} = -\left(a + b - \frac{ab}{100}\right)$$</td>
              <td>$-20\%, -10\% \implies 20 + 10 - \frac{200}{100} = \mathbf{28\% \text{ discount}}$</td>
            </tr>
            <tr>
              <td>समान वृद्धि एवं कमी</td>
              <td>$+x\%, -x\%$</td>
              <td>$$-\frac{x^2}{100}\% \quad (\text{सदैव कमी})$$</td>
              <td>$+20\%, -20\% \implies -\frac{400}{100} = \mathbf{-4\% \text{ loss}}$</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="concept-callout">
        <strong>📐 Geometry Applications:</strong><br>
        &bull; <strong>वृत्त का क्षेत्रफल ($\pi r^2$):</strong> त्रिज्या में $20\%$ वृद्धि $\implies 20 + 20 + \frac{400}{100} = \mathbf{+44\%}$ क्षेत्रफल वृद्धि।<br>
        &bull; <strong>आयत का क्षेत्रफल ($L \times B$):</strong> लंबाई $+10\%$, चौड़ाई $+20\% \implies \text{Area } +32\%$।<br>
        &bull; <strong>गोले का आयतन ($\frac{4}{3}\pi r^3$):</strong> $r$ में $10\%$ वृद्धि $\implies (1.1)^3 = 1.331 \implies \mathbf{+33.1\%}$ आयतन वृद्धि।
      </div>
    </div>

    <!-- Module 4 -->
    <div style="margin-bottom:28px;">
      <span class="chap-badge">MODULE 4</span>
      <h3 class="chap-title">4. Product Constancy Ratio &amp; Price–Consumption–Expenditure ($P \times C = E$)</h3>
      <p class="book-p">
        जब दो राशियों का गुणनफल स्थिर (Constant) रहता है, तो एक राशि में वृद्धि होने पर दूसरी राशि में स्वतः आनुपातिक कमी हो जाती है।
      </p>

      <div class="concept-callout">
        <strong>⚡ The $1/n \to 1/(n+1)$ Golden Ladder:</strong><br>
        यदि $A \times B = \text{Constant}$ हो:<br>
        &bull; यदि $A$ में $\mathbf{+\frac{1}{n}}$ की वृद्धि होती है, तो $B$ में $\mathbf{-\frac{1}{n+1}}$ की कमी करनी होगी।<br>
        &bull; यदि $A$ में $\mathbf{-\frac{1}{n}}$ की कमी होती है, तो $B$ में $\mathbf{+\frac{1}{n-1}}$ की वृद्धि करनी होगी।<br>
        <strong>प्रतिशत रूप:</strong><br>
        मूल्य में $x\%$ वृद्धि होने पर खर्च को अपरिवर्तित रखने के लिए उपभोग में कमी:
        $$\text{Required Decrease in Consumption} = \left(\frac{x}{100 + x}\right) \times 100\%$$
      </div>

      <div class="table-wrap">
        <table class="book-table">
          <thead>
            <tr>
              <th>मूल्य में परिवर्तन (Price Change)</th>
              <th>भिन्न रूप (Fraction)</th>
              <th>उपभोग में आवश्यक परिवर्तन (Consumption Change)</th>
              <th>प्रतिशत में मान</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>$+10\%$ वृद्धि</td><td>$+1/10$</td><td>$-1/11$ कमी</td><td>$9\frac{1}{11}\% = 9.09\%$</td></tr>
            <tr><td>$+20\%$ वृद्धि</td><td>$+1/5$</td><td>$-1/6$ कमी</td><td>$16\frac{2}{3}\% = 16.67\%$</td></tr>
            <tr><td>$+25\%$ वृद्धि</td><td>$+1/4$</td><td>$-1/5$ कमी</td><td>$20\%$</td></tr>
            <tr><td>$+33.33\%$ वृद्धि</td><td>$+1/3$</td><td>$-1/4$ कमी</td><td>$25\%$</td></tr>
            <tr><td>$+50\%$ वृद्धि</td><td>$+1/2$</td><td>$-1/3$ कमी</td><td>$33.33\%$</td></tr>
            <tr><td>$-20\%$ कमी</td><td>$-1/5$</td><td>$+1/4$ वृद्धि</td><td>$25\%$</td></tr>
            <tr><td>$-25\%$ कमी</td><td>$-1/4$</td><td>$+1/3$ वृद्धि</td><td>$33.33\%$</td></tr>
          </tbody>
        </table>
      </div>

      <div class="concept-callout">
        <strong>🔥 Quantitative Price-Drop Model (Kg More for ₹M):</strong><br>
        जब चीनी के मूल्य में $x\%$ की कमी होने पर कोई व्यक्ति ₹$M$ में $K$ किग्रा चीनी अधिक खरीद पाता है:<br>
        &bull; <strong>घटा हुआ मूल्य (Reduced Price / New Price)</strong> $= \frac{M \times x}{100 \times K}$ प्रति किग्रा।<br>
        &bull; <strong>वास्तविक / प्रारंभिक मूल्य (Original Price)</strong> $= \frac{M \times x}{(100 - x) \times K}$ प्रति किग्रा।
      </div>
    </div>

    <!-- Module 5 -->
    <div style="margin-bottom:28px;">
      <span class="chap-badge">MODULE 5</span>
      <h3 class="chap-title">5. Income, Expenditure &amp; Savings ($I = E + S$) &amp; Compound Depreciation</h3>
      <p class="book-p">
        व्यक्ति की आय (Income), व्यय (Expenditure) और बचत (Savings) में मूलभूत संबंध होता है:
        $$\text{Income} = \text{Expenditure} + \text{Savings} \quad (I = E + S)$$
      </p>

      <div class="concept-callout">
        <strong>⚡ Alligation / Weighted Average Method for $I = E + S$:</strong><br>
        यदि किसी व्यक्ति का व्यय $E$ और बचत $S$ का अनुपात $e : s$ है। उसकी आय में $i\%$ वृद्धि होती है और व्यय में $e_p\%$ वृद्धि होती है, तो बचत में $\%$ वृद्धि ($s_p\%$):
        $$I\% \times (E + S) = (E \times e_p\%) + (S \times s_p\%)$$
        यह एक पंक्ति में बिना कोई बड़ा समीकरण बनाए उत्तर दे देता है!
      </div>

      <div class="concept-callout">
        <strong>📉 Population &amp; Depreciation Formula:</strong><br>
        यदि किसी नगर की जनसंख्या या मशीन का वर्तमान मूल्य $P$ है और यह प्रतिवर्ष $r\%$ की दर से बदलता है:<br>
        &bull; $t$ वर्ष बाद मूल्य / जनसंख्या:
        $$P_{\text{after}} = P \left(1 \pm \frac{r}{100}\right)^t$$
        &bull; $t$ वर्ष पूर्व मूल्य / जनसंख्या:
        $$P_{\text{before}} = \frac{P}{\left(1 \pm \frac{r}{100}\right)^t}$$
        (वृद्धि के लिए $+$, अवमूल्यन/कमी के लिए $-$).
      </div>
    </div>

    <!-- Module 6 -->
    <div>
      <span class="chap-badge">MODULE 6</span>
      <h3 class="chap-title">6. Election Problems &amp; Venn Diagram Sets</h3>
      <p class="book-p">
        चुनाव संबंधी प्रश्न SSC CGL Tier-1 और Tier-2 दोनों में अनिवार्य रूप से पूछे जाते हैं। इन प्रश्नों को हल करने के लिए मतदाता सूची की संरचना को समझना आवश्यक है:
      </p>

      <div class="concept-callout">
        <strong>🗳️ Election Hierarchy Breakdown:</strong><br>
        1. <strong>कुल पंजीकृत मतदाता (Total Enrolled Voters)</strong> $= 100\%$<br>
        2. <strong>मतदान (Votes Polled / Turnout):</strong> यदि $10\%$ ने मत नहीं दिया $\implies 90\%$ ने मत दिया।<br>
        3. <strong>वैध मत (Valid Votes):</strong> यदि $10\%$ मत अवैध (invalid) घोषित हुए $\implies 90\% \times 0.90 = 81\%$ वैध मत।<br>
        4. <strong>जीत का अंतर (Winning Margin):</strong>
        $$\text{Winning Margin} = \text{Winner's Votes} - \text{Loser's Votes} = (\%W - \%L) \times \text{Valid Votes}$$
      </div>

      <div class="concept-callout">
        <strong>📊 2-Set Venn Diagram (Examination Problems):</strong><br>
        एक परीक्षा में $A\%$ छात्र गणित में अनुत्तीर्ण हुए, $B\%$ अंग्रेजी में अनुत्तीर्ण हुए, और $C\%$ दोनों में अनुत्तीर्ण हुए:<br>
        &bull; कुल अनुत्तीर्ण छात्र (Failed in at least one):
        $$n(A \cup B) = A + B - C$$
        &bull; दोनों विषयों में उत्तीर्ण छात्र (Passed in both):
        $$\text{Passed Both} = 100\% - (A + B - C)$$
        <span style="color:var(--gold);">महत्वपूर्ण नियम:</span> वेन आरेख में सभी डेटा या तो केवल "अनुत्तीर्ण" (Fail) का रखें, या केवल "उत्तीर्ण" (Pass) का। दोनों को मिलाएँ नहीं!
      </div>
    </div>
  </section>
'''

def get_formula_vault():
    return r'''
  <!-- FORMULA VAULT -->
  <section id="sec-formulas" style="margin-bottom:24px;">
    <h2 class="sec-title">📐 Formula Vault — Phase 2 Completed Formula Sheet (10 Cards)</h2>
    <div class="formula-grid">
      
      <!-- Card 1 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">1. Percentage Comparison</span>
          <button class="copy-btn" onclick="copyFormula('Percentage = (Value / Base) * 100%')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">% More = [(A - B) / B] &times; 100%</div>
          <div class="fc-formula">% Less = [(A - B) / A] &times; 100%</div>
          <div class="fc-row">The value after 'than' or 'of' is ALWAYS in the denominator.</div>
        </div>
      </div>

      <!-- Card 2 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">2. Commutative Rule</span>
          <button class="copy-btn" onclick="copyFormula('A% of B = B% of A')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">A% of B = B% of A = (A &times; B) / 100</div>
          <div class="fc-row">E.g. $84\% \text{ of } 50 = 50\% \text{ of } 84 = 42$.</div>
        </div>
      </div>

      <!-- Card 3 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">3. The AB Successive Formula</span>
          <button class="copy-btn" onclick="copyFormula('Net % = a + b + (ab/100)')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">Net % = a + b + (a &times; b) / 100</div>
          <div class="fc-row">Increase &rarr; $+$, Decrease &rarr; $-$. Two equal opposite changes: $-x^2/100\%$.</div>
        </div>
      </div>

      <!-- Card 4 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">4. Constant Product / Expenditure</span>
          <button class="copy-btn" onclick="copyFormula('Decrease = [x / (100 + x)] * 100%')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">Required % Decrease = [x / (100 + x)] &times; 100%</div>
          <div class="fc-formula">Required % Increase = [x / (100 - x)] &times; 100%</div>
          <div class="fc-row">If $A$ increases by $1/n$, $B$ must decrease by $1/(n+1)$.</div>
        </div>
      </div>

      <!-- Card 5 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">5. Price-Drop Quantity Model</span>
          <button class="copy-btn" onclick="copyFormula('Reduced Price = (M*x)/(100*K); Original Price = (M*x)/((100-x)*K)')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">Reduced Price = (M &times; x) / (100 &times; K)</div>
          <div class="fc-formula">Original Price = (M &times; x) / [(100 - x) &times; K]</div>
          <div class="fc-row">For $x\%$ price drop buying $K$ kg more for ₹$M$.</div>
        </div>
      </div>

      <!-- Card 6 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">6. Income-Expenditure-Savings</span>
          <button class="copy-btn" onclick="copyFormula('Income = Expenditure + Savings; Weighted % change')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">I = E + S</div>
          <div class="fc-formula">%I &times; I = (%E &times; E) + (%S &times; S)</div>
          <div class="fc-row">Solve directly via weighted averages or alligation.</div>
        </div>
      </div>

      <!-- Card 7 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">7. Population Growth &amp; Depreciation</span>
          <button class="copy-btn" onclick="copyFormula('P_after = P*(1 +/- r/100)^t; P_before = P / (1 +/- r/100)^t')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">P(after t years) = P &times; (1 &plusmn; r/100)^t</div>
          <div class="fc-formula">P(before t years) = P / (1 &plusmn; r/100)^t</div>
        </div>
      </div>

      <!-- Card 8 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">8. Successive Multi-Step Spending</span>
          <button class="copy-btn" onclick="copyFormula('Remaining = Initial * (1 - a/100) * (1 - b/100) * ...')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">Remaining = Initial &times; (1 - a/100) &times; (1 - b/100) ...</div>
          <div class="fc-row">Apply when expenditures are of the <em>remaining</em> amount.</div>
        </div>
      </div>

      <!-- Card 9 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">9. Election Winning Margin</span>
          <button class="copy-btn" onclick="copyFormula('Margin = (%Winner - %Loser) * Valid Votes')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">Margin = (%Winner - %Loser) &times; Valid Votes</div>
          <div class="fc-row">Remember: Turnout $\%$ applies first, then Invalid $\%$ is deducted.</div>
        </div>
      </div>

      <!-- Card 10 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">10. 2-Set Venn Diagram Formula</span>
          <button class="copy-btn" onclick="copyFormula('Total Failed = A + B - Both; Passed Both = 100% - Total Failed')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">n(A &cup; B) = n(A) + n(B) - n(A &cap; B)</div>
          <div class="fc-formula">Passed in Both = 100% - n(A &cup; B)</div>
        </div>
      </div>

    </div>
  </section>
'''

def get_shortcuts_and_traps():
    return r'''
  <!-- SHORTCUTS & TRAPS -->
  <section style="margin-bottom:24px;">
    <h2 class="sec-title">⚡ Speed Shortcuts &amp; Classic SSC Exam Traps</h2>
    
    <div class="shortcut-grid">
      <div class="shortcut-card">
        <div class="sc-title">⚡ 1. Commutative Swap Shortcut</div>
        <div class="sc-content">
          $16\%\text{ of } 25$ nikaalne ke bajaye $25\%\text{ of } 16$ karein $\implies \frac{16}{4} = \mathbf{4}$! Jab bhi $25, 50, 75, 20$ dikhe, turant swap karein.
        </div>
      </div>

      <div class="shortcut-card">
        <div class="sc-title">⚡ 2. 1/n to 1/(n+1) Mental Ladder</div>
        <div class="sc-content">
          Price $+25\% (+1/4) \implies$ Consumption $-1/5 = \mathbf{20\%}$ bina kisi pen chalaye! Price $-20\% (-1/5) \implies$ Consumption $+1/4 = \mathbf{25\%}$!
        </div>
      </div>

      <div class="shortcut-card">
        <div class="sc-title">⚡ 3. Effective Rate for Circle &amp; Square</div>
        <div class="sc-content">
          Radius $+x\% \implies \text{Area } + (2x + x^2/100)\%$. E.g. $r +15\% \implies 30 + 2.25 = \mathbf{+32.25\%}$!
        </div>
      </div>

      <div class="shortcut-card">
        <div class="sc-title">⚡ 4. Direct Ratio Invariance in $I = E + S$</div>
        <div class="sc-content">
          Agar $E : S = 4 : 1$, to Income $= 5$ unit. $I$ badha $10\% (+50), E$ badha $12\% (+48) \implies S$ badha $+2$ unit $\implies \frac{2}{1} \times 100 = \mathbf{+2\%}$!
        </div>
      </div>

      <div class="shortcut-card">
        <div class="sc-title">⚡ 5. Reduced Price in One Step</div>
        <div class="sc-content">
          ₹$240$ me $2$ kg adhik jab price $20\%$ gira: Reduced Price $= \frac{240 \times 0.20}{2} = \frac{48}{2} = \mathbf{₹24/\text{kg}}$!
        </div>
      </div>

      <div class="shortcut-card">
        <div class="sc-title">⚡ 6. Fraction Multiplier for Successive Discounts</div>
        <div class="sc-content">
          $20\%$ aur $12.5\%$ discount: $\text{SP} = \text{MP} \times \frac{4}{5} \times \frac{7}{8} = \text{MP} \times \frac{7}{10} \implies \mathbf{30\% \text{ total discount}}$!
        </div>
      </div>
    </div>

    <div class="trap-grid" style="margin-top:14px;">
      <div class="trap-card">
        <div class="trap-header">
          <span class="trap-title">🚨 Trap 1: Base Confusion in "A is x% more than B"</span>
          <span class="error-code">[C] CONCEPT</span>
        </div>
        <div class="trap-desc">
          Agar $A, B$ se $25\%$ adhik hai, to $B, A$ se $25\%$ kam nahi hota! $B, A$ se $\frac{25}{125} \times 100 = 20\%$ kam hota hai.
        </div>
      </div>

      <div class="trap-card">
        <div class="trap-header">
          <span class="trap-title">🚨 Trap 2: Direct Addition of Successive Changes</span>
          <span class="error-code">[F] FORMULA</span>
        </div>
        <div class="trap-desc">
          $+10\%$ aur $+20\%$ milkar $+30\%$ nahi banta! Formula $10 + 20 + \frac{200}{100} = +32\%$ hota hai.
        </div>
      </div>

      <div class="trap-card">
        <div class="trap-header">
          <span class="trap-title">🚨 Trap 3: "Of the Total" vs "Of the Remaining"</span>
          <span class="error-code">[R] READING</span>
        </div>
        <div class="trap-desc">
          "Spends 20% on rent and 30% on food" $= 50\%$ total. Par "20% on rent and 30% of the REMAINING on food" $= 20 + 30\% \times 80 = 44\%$!
        </div>
      </div>

      <div class="trap-card">
        <div class="trap-header">
          <span class="trap-title">🚨 Trap 4: Margin on Total Votes vs Valid Votes</span>
          <span class="error-code">[R] READING</span>
        </div>
        <div class="trap-desc">
          Winner ko $60\%$ mila valid votes ka, to margin $= (60 - 40)\% = 20\%$ of VALID votes hota hai, total enrolled votes ka nahi!
        </div>
      </div>

      <div class="trap-card">
        <div class="trap-header">
          <span class="trap-title">🚨 Trap 5: Mixing Pass and Fail in Venn Diagrams</span>
          <span class="error-code">[K] CALCULATION</span>
        </div>
        <div class="trap-desc">
          Agar $40\%$ fail math me aur $70\%$ pass english me diya ho, to pehle english fail $= 30\%$ banayein. Dono ka type same hona aniwarya hai.
        </div>
      </div>

      <div class="trap-card">
        <div class="trap-header">
          <span class="trap-title">🚨 Trap 6: Equal Increase &amp; Decrease Net Loss</span>
          <span class="error-code">[C] CONCEPT</span>
        </div>
        <div class="trap-desc">
          Kisi sankhya me $+x\%$ aur fir $-x\%$ karne par sankhya wahi nahi rehti, balki hamesha $\frac{x^2}{100}\%$ ki kami hoti hai!
        </div>
      </div>
    </div>
  </section>
'''

print("Phase 2 theory module ready.")
