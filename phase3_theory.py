# -*- coding: utf-8 -*-
"""
Phase 3 Theory Chapters, Formula Vault, Shortcuts & Traps
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
        <h2 style="font-size:1.45rem;font-weight:800;color:#fff;">📖 Exhaustive Textbook Notes: Ratio &amp; Proportion (अनुपात एवं समानुपात)</h2>
      </div>
      <span style="font-size:0.82rem;color:var(--text-muted);">6 Detailed Modules &bull; Complete Coverage</span>
    </div>

    <!-- Module 1 -->
    <div style="margin-bottom:28px;">
      <span class="chap-badge">MODULE 1</span>
      <h3 class="chap-title">1. Ratio Fundamentals, Simplification &amp; Combining Methods</h3>
      <p class="book-p">
        <strong>अनुपात (Ratio)</strong> दो या दो से अधिक सजातीय (same unit) राशियों की भाग द्वारा तुलना है। अनुपात $a : b = \frac{a}{b}$ की कोई इकाई (dimension) नहीं होती।
      </p>

      <div class="concept-callout">
        <strong>⚡ Rules for Ratio Operations:</strong><br>
        1. अनुपात के दोनों पदों में किसी भी गैर-शून्य संख्या से गुणा या भाग करने पर अनुपात अपरिवर्तित रहता है: $\frac{a}{b} = \frac{ka}{kb}$।<br>
        2. <strong>भिन्नों के अनुपात का सरलीकरण:</strong> यदि अनुपात $\frac{a}{p} : \frac{b}{q} : \frac{c}{r}$ दिया हो, तो तीनों पदों को हरों के ल.स. (LCM of denominators) से गुणा करके पूर्णांक अनुपात में बदलें।<br>
        उदाहरण: $\frac{1}{2} : \frac{2}{3} : \frac{3}{4} \implies \text{LCM}(2, 3, 4) = 12 \implies (12 \times \frac{1}{2}) : (12 \times \frac{2}{3}) : (12 \times \frac{3}{4}) = \mathbf{6 : 8 : 9}$।
      </div>

      <div class="table-wrap">
        <table class="book-table">
          <thead>
            <tr>
              <th>जोड़ने की विधि (Combining Method)</th>
              <th>दी गई स्थितियाँ (Given Data)</th>
              <th>संयुक्त अनुपात (Combined Ratio $A:B:C$)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>1. Bridging Term Equalization</strong></td>
              <td>$A : B = 2 : 3$,<br>$B : C = 4 : 5$</td>
              <td>उभयनिष्ठ पद $B$ को समान करें ($\text{LCM}(3, 4) = 12$):<br>
              $A : B = (2 \times 4) : (3 \times 4) = 8 : 12$<br>
              $B : C = (4 \times 3) : (5 \times 3) = 12 : 15$<br>
              &bull; $\mathbf{A : B : C = 8 : 12 : 15}$
              </td>
            </tr>
            <tr>
              <td><strong>2. Inverted-N Technique</strong></td>
              <td>$A : B = a : b$,<br>$B : C = c : d$</td>
              <td>
                $$\begin{matrix} a & b \\ & \downarrow \\ c & d \end{matrix} \implies A = a \times c, \quad B = b \times c, \quad C = b \times d$$
                &bull; $\mathbf{A : B : C = (ac) : (bc) : (bd)}$
              </td>
            </tr>
            <tr>
              <td><strong>3. 4-Term Combining ($A:B:C:D$)</strong></td>
              <td>$A:B = 1:2$, $B:C = 3:4$, $C:D = 5:6$</td>
              <td>
                खाली स्थानों को निकटतम अंक से भरें:<br>
                $A: 1 \times 3 \times 5 = 15$<br>
                $B: 2 \times 3 \times 5 = 30$<br>
                $C: 2 \times 4 \times 5 = 40$<br>
                $D: 2 \times 4 \times 6 = 48$<br>
                &bull; $\mathbf{A : B : C : D = 15 : 30 : 40 : 48}$
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Module 2 -->
    <div style="margin-bottom:28px;">
      <span class="chap-badge">MODULE 2</span>
      <h3 class="chap-title">2. Proportions &amp; Componendo &amp; Dividendo (C&amp;D)</h3>
      <p class="book-p">
        जब दो अनुपात आपस में बराबर हों, तो वे <strong>समानुपात (Proportion)</strong> में कहलाते हैं।
        $$a : b :: c : d \iff \frac{a}{b} = \frac{c}{d}$$
      </p>

      <div class="concept-callout">
        <strong>📌 Fundamental Property:</strong>
        $$\text{Product of Extremes} = \text{Product of Means} \implies a \times d = b \times c$$
        जहाँ $a$ और $d$ बाह्य पद (extremes) हैं तथा $b$ और $c$ मध्य पद (means) हैं।
      </div>

      <div class="table-wrap">
        <table class="book-table">
          <thead>
            <tr>
              <th>नियम का नाम (Rule Name)</th>
              <th>मूल समानुपात ($\frac{a}{b} = \frac{c}{d}$)</th>
              <th>परिणामी स्वरूप (Resulting Form)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Invertendo (व्युत्क्रमानुपात)</strong></td>
              <td>$\frac{a}{b} = \frac{c}{d}$</td>
              <td>$$\frac{b}{a} = \frac{d}{c}$$</td>
            </tr>
            <tr>
              <td><strong>Alternando (एकांतरानुपात)</strong></td>
              <td>$\frac{a}{b} = \frac{c}{d}$</td>
              <td>$$\frac{a}{c} = \frac{b}{d}$$</td>
            </tr>
            <tr>
              <td><strong>Componendo (योगानुपात)</strong></td>
              <td>$\frac{a}{b} = \frac{c}{d}$</td>
              <td>$$\frac{a + b}{b} = \frac{c + d}{d}$$</td>
            </tr>
            <tr>
              <td><strong>Dividendo (अंतरानुपात)</strong></td>
              <td>$\frac{a}{b} = \frac{c}{d}$</td>
              <td>$$\frac{a - b}{b} = \frac{c - d}{d}$$</td>
            </tr>
            <tr>
              <td><strong>Componendo &amp; Dividendo (C&amp;D)</strong></td>
              <td>$\frac{a}{b} = \frac{c}{d}$</td>
              <td>$$\mathbf{\frac{a + b}{a - b} = \frac{c + d}{c - d}}$$</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="concept-callout">
        <strong>⚡ C&amp;D Application in SSC Algebra / Surds:</strong><br>
        यदि $\frac{\sqrt{x + 5} + \sqrt{x - 5}}{\sqrt{x + 5} - \sqrt{x - 5}} = \frac{3}{1}$ दिया हो:<br>
        C&amp;D लगाने पर: $\frac{2\sqrt{x + 5}}{2\sqrt{x - 5}} = \frac{3 + 1}{3 - 1} = \frac{4}{2} = 2 \implies \sqrt{\frac{x+5}{x-5}} = 2 \implies \frac{x+5}{x-5} = 4 \implies x+5 = 4x - 20 \implies 3x = 25 \implies \mathbf{x = 25/3}$!
      </div>
    </div>

    <!-- Module 3 -->
    <div style="margin-bottom:28px;">
      <span class="chap-badge">MODULE 3</span>
      <h3 class="chap-title">3. Types of Ratios (Duplicate, Triplicate, Compound &amp; Inverse)</h3>
      <p class="book-p">
        SSC परीक्षाओं में प्रत्यक्ष शब्दावली आधारित प्रश्न पूछे जाते हैं। प्रत्येक प्रकार का स्पष्ट गणितीय अर्थ यहाँ दिया गया है:
      </p>

      <div class="table-wrap">
        <table class="book-table">
          <thead>
            <tr>
              <th>अनुपात का प्रकार (Type)</th>
              <th>मूल अनुपात $a : b$</th>
              <th>परिभाषा एवं सूत्र (Definition &amp; Formula)</th>
              <th>उदाहरण ($4 : 9$)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Duplicate Ratio (वर्गानुपात)</strong></td>
              <td>$a : b$</td>
              <td>$$a^2 : b^2$$</td>
              <td>$4^2 : 9^2 = \mathbf{16 : 81}$</td>
            </tr>
            <tr>
              <td><strong>Sub-duplicate Ratio (वर्गमूलानुपात)</strong></td>
              <td>$a : b$</td>
              <td>$$\sqrt{a} : \sqrt{b}$$</td>
              <td>$\sqrt{4} : \sqrt{9} = \mathbf{2 : 3}$</td>
            </tr>
            <tr>
              <td><strong>Triplicate Ratio (घनानुपात)</strong></td>
              <td>$a : b$</td>
              <td>$$a^3 : b^3$$</td>
              <td>$4^3 : 9^3 = \mathbf{64 : 729}$</td>
            </tr>
            <tr>
              <td><strong>Sub-triplicate Ratio (घनमूलानुपात)</strong></td>
              <td>$a : b$</td>
              <td>$$\sqrt[3]{a} : \sqrt[3]{b}$$</td>
              <td>$8 : 27 \implies \sqrt[3]{8} : \sqrt[3]{27} = \mathbf{2 : 3}$</td>
            </tr>
            <tr>
              <td><strong>Compound Ratio (मिश्रित अनुपात)</strong></td>
              <td>$a:b, c:d, e:f$</td>
              <td>$$(a \times c \times e) : (b \times d \times f)$$</td>
              <td>$2:3, 4:5, 6:7 \implies (2 \cdot 4 \cdot 6) : (3 \cdot 5 \cdot 7) = \mathbf{16 : 35}$</td>
            </tr>
            <tr>
              <td><strong>Inverse / Reciprocal Ratio (व्युत्क्रमानुपात)</strong></td>
              <td>$a : b : c$</td>
              <td>$$\frac{1}{a} : \frac{1}{b} : \frac{1}{c} = bc : ac : ab$$</td>
              <td>$2 : 3 : 5 \implies (3 \cdot 5) : (2 \cdot 5) : (2 \cdot 3) = \mathbf{15 : 10 : 6}$</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Module 4 -->
    <div style="margin-bottom:28px;">
      <span class="chap-badge">MODULE 4</span>
      <h3 class="chap-title">4. Mean, Third &amp; Fourth Proportional &amp; The Number $x$ Model</h3>
      <p class="book-p">
        समानुपाती पदों (Proportionals) की गणना SSC CGL Tier-1 और Tier-2 के सबसे पसंदीदा 100% गारंटीड प्रश्नों में से एक है।
      </p>

      <div class="table-wrap">
        <table class="book-table">
          <thead>
            <tr>
              <th>समानुपाती पद (Term)</th>
              <th>दी गई संख्याएँ (Given Values)</th>
              <th>समानुपात समीकरण</th>
              <th>हल सूत्र (Formula)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Mean Proportional (मध्यानुपाती)</strong></td>
              <td>$a$ एवं $b$</td>
              <td>$a : x :: x : b \implies x^2 = ab$</td>
              <td>$$\mathbf{x = \sqrt{ab}}$$</td>
            </tr>
            <tr>
              <td><strong>Third Proportional (तृतीयानुपाती)</strong></td>
              <td>$a$ एवं $b$</td>
              <td>$a : b :: b : x \implies ax = b^2$</td>
              <td>$$\mathbf{x = \frac{b^2}{a}}$$</td>
            </tr>
            <tr>
              <td><strong>Fourth Proportional (चतुर्थानुपाती)</strong></td>
              <td>$a, b,$ एवं $c$</td>
              <td>$a : b :: c : x \implies ax = bc$</td>
              <td>$$\mathbf{x = \frac{bc}{a}}$$</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="concept-callout">
        <strong>🔥 The Universal Number $x$ Added / Subtracted Model:</strong><br>
        संख्याओं $a, b, c, d$ में से क्या संख्या $x$ घटाई या जोड़ी जाए ताकि प्राप्त संख्याएँ समानुपाती हो जाएँ?
        $$\frac{a - x}{b - x} = \frac{c - x}{d - x}$$
        <strong>⚡ 10-Second Topper Direct Formula:</strong>
        $$\mathbf{x = \frac{ad - bc}{(a + d) - (b + c)}}$$
        (चिह्न निरपेक्ष मान लें यदि धनात्मक संख्या पूछी जाए)।
      </div>
    </div>

    <!-- Module 5 -->
    <div style="margin-bottom:28px;">
      <span class="chap-badge">MODULE 5</span>
      <h3 class="chap-title">5. Cross-Multiplication Method &amp; Age Invariance Problems</h3>
      <p class="book-p">
        जब दो व्यक्तियों की प्रारंभिक अनुपात, व्यय या समय के बाद का अनुपात, और निश्चित अंतर दिया हो, तो <strong>वज्र-गुणन विधि (Cross-Multiplication Method)</strong> बिना किसी $x$ और $y$ के 15 सेकंड में उत्तर निकालती है।
      </p>

      <div class="concept-callout">
        <strong>⚡ Cross-Multiplication Layout for $I = E + S$:</strong><br>
        मान लीजिए $A$ और $B$ की आय का अनुपात $a : b$ है और व्यय का अनुपात $c : d$ है, तथा बचत क्रमशः $S_1$ और $S_2$ है:<br>
        $$\begin{matrix} \text{Income:} & a & & b \\ & & \searrow \hspace{-0.7em} \swarrow & \\ \text{Expenditure:} & c & & d \\ & & \searrow \hspace{-0.7em} \swarrow & \\ \text{Savings:} & S_1 & & S_2 \end{matrix}$$
        $$\mathbf{\text{Upper Cross Difference: } |ad - bc| \text{ units} = |c S_2 - d S_1| \text{ rupees}}$$
        एक यूनिट का मान सीधे निकल जाता है!
      </div>

      <div class="concept-callout">
        <strong>⏳ Age Invariance Principle:</strong><br>
        दो व्यक्तियों की आयु का अंतर समय के साथ कभी नहीं बदलता! $5$ वर्ष पहले, वर्तमान में, और $10$ वर्ष बाद—अंतर सदैव समान रहता है।<br>
        <strong>नियम:</strong> दोनों अनुपातों के अंतर को समान (Equalize the gap) करके सीधे यूनिट मान ज्ञात करें।
      </div>
    </div>

    <!-- Module 6 -->
    <div>
      <span class="chap-badge">MODULE 6</span>
      <h3 class="chap-title">6. Coin Box Problems &amp; Distribution Mistakes</h3>
      <p class="book-p">
        सिक्कों के प्रश्नों में केवल एक मूल सिद्धांत होता है:
        $$\text{Total Monetary Value (कुल मूल्य)} = \text{Number of Coins (सिक्कों की संख्या)} \times \text{Face Value (सिक्के का मान)}$$
      </p>

      <div class="table-wrap">
        <table class="book-table">
          <thead>
            <tr>
              <th>सिक्के का प्रकार (Denomination)</th>
              <th>रुपये में मान (Value in ₹)</th>
              <th>सिक्कों की संख्या का अनुपात</th>
              <th>कुल मूल्य का अनुपात</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>₹1 का सिक्का</td><td>₹$1.00 = 1$</td><td>$x$</td><td>$1 \times x$</td></tr>
            <tr><td>50 पैसे का सिक्का</td><td>₹$0.50 = \frac{1}{2}$</td><td>$y$</td><td>$\frac{1}{2} \times y$</td></tr>
            <tr><td>25 पैसे का सिक्का</td><td>₹$0.25 = \frac{1}{4}$</td><td>$z$</td><td>$\frac{1}{4} \times z$</td></tr>
            <tr><td>10 पैसे का सिक्का</td><td>₹$0.10 = \frac{1}{10}$</td><td>$w$</td><td>$\frac{1}{10} \times w$</td></tr>
          </tbody>
        </table>
      </div>

      <div class="concept-callout">
        <strong>⚠️ Distribution Error Model (गलत अनुपात में वितरण):</strong><br>
        ₹$X$ की राशि को $A, B, C$ में $\frac{1}{2} : \frac{1}{3} : \frac{1}{4}$ के अनुपात में बाँटने के बजाय गलती से $2 : 3 : 4$ में बाँट दिया गया:<br>
        &bull; सही अनुपात $= \text{LCM}(2,3,4) = 12 \implies 6 : 4 : 3$ (कुल 13 यूनिट)।<br>
        &bull; गलत अनुपात $= 2 : 3 : 4$ (कुल 9 यूनिट)।<br>
        &bull; दोनों स्थितियों में कुल राशि समान रखने के लिए 13 और 9 का ल.स. 117 मानकर आसानी से अंतर निकालें!
      </div>
    </div>
  </section>
'''

def get_formula_vault():
    return r'''
  <!-- FORMULA VAULT -->
  <section id="sec-formulas" style="margin-bottom:24px;">
    <h2 class="sec-title">📐 Formula Vault — Phase 3 Completed Formula Sheet (10 Cards)</h2>
    <div class="formula-grid">
      
      <!-- Card 1 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">1. Extremes &amp; Means Product</span>
          <button class="copy-btn" onclick="copyFormula('a : b :: c : d => a * d = b * c')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">a &times; d = b &times; c</div>
          <div class="fc-row">In any proportion, Product of Extremes = Product of Means.</div>
        </div>
      </div>

      <!-- Card 2 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">2. Mean Proportional</span>
          <button class="copy-btn" onclick="copyFormula('Mean Proportional = sqrt(a * b)')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">Mean Proportional = &radic;(a &times; b)</div>
          <div class="fc-row">Between two positive numbers $a$ and $b$.</div>
        </div>
      </div>

      <!-- Card 3 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">3. Third Proportional</span>
          <button class="copy-btn" onclick="copyFormula('Third Proportional = b^2 / a')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">Third Proportional = b&sup2; / a</div>
          <div class="fc-row">To numbers $a$ and $b$ where $a : b :: b : x$.</div>
        </div>
      </div>

      <!-- Card 4 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">4. Fourth Proportional</span>
          <button class="copy-btn" onclick="copyFormula('Fourth Proportional = (b * c) / a')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">Fourth Proportional = (b &times; c) / a</div>
          <div class="fc-row">To three numbers $a, b, c$ where $a : b :: c : x$.</div>
        </div>
      </div>

      <!-- Card 5 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">5. Number x Added / Subtracted</span>
          <button class="copy-btn" onclick="copyFormula('x = (ad - bc) / ((a + d) - (b + c))')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">x = (a&times;d - b&times;c) / [(a + d) - (b + c)]</div>
          <div class="fc-row">Number $x$ to make $a, b, c, d$ proportional.</div>
        </div>
      </div>

      <!-- Card 6 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">6. Componendo &amp; Dividendo</span>
          <button class="copy-btn" onclick="copyFormula('If a/b = c/d, then (a+b)/(a-b) = (c+d)/(c-d)')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">(a + b) / (a - b) = (c + d) / (c - d)</div>
          <div class="fc-row">Invaluable for square-root surds and algebraic fractions.</div>
        </div>
      </div>

      <!-- Card 7 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">7. Duplicate &amp; Triplicate Ratios</span>
          <button class="copy-btn" onclick="copyFormula('Duplicate = a^2 : b^2; Triplicate = a^3 : b^3')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">Duplicate = a&sup2; : b&sup2;; Sub-dup = &radic;a : &radic;b</div>
          <div class="fc-formula">Triplicate = a&sup3; : b&sup3;; Sub-trip = &sup3;&radic;a : &sup3;&radic;b</div>
        </div>
      </div>

      <!-- Card 8 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">8. Inverse Ratio of Three Terms</span>
          <button class="copy-btn" onclick="copyFormula('Inverse of a:b:c = bc : ac : ab')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">Inverse(a : b : c) = bc : ac : ab</div>
          <div class="fc-row">Cover each term and multiply the other two!</div>
        </div>
      </div>

      <!-- Card 9 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">9. Cross-Multiplication Method</span>
          <button class="copy-btn" onclick="copyFormula('|ad - bc| units = |c*S2 - d*S1|')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">|a&times;d - b&times;c| units = |c&times;S&sub2; - d&times;S&sub1;|</div>
          <div class="fc-row">For Income-Expenditure-Savings and shifted ratios.</div>
        </div>
      </div>

      <!-- Card 10 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">10. Coin Box Value Equation</span>
          <button class="copy-btn" onclick="copyFormula('Total Value = Sum(Coins * Denomination)')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">Value = N(&#8377;1)&times;1 + N(50p)&times;0.5 + N(25p)&times;0.25</div>
          <div class="fc-row">Always convert to a single monetary unit (Rupees or Paise).</div>
        </div>
      </div>

    </div>
  </section>
'''

def get_shortcuts_and_traps():
    return r'''
  <!-- SHORTCUTS & TRAPS -->
  <section class="book-chapter" id="sec-shortcuts" style="margin-bottom:24px;">
    <h2 class="sec-title">⚡ Speed Shortcuts &amp; Classic SSC Exam Traps</h2>
    
    <div class="shortcut-grid">
      <div class="shortcut-card">
        <div class="sc-title">⚡ 1. Finger-Cover Inverse Trick</div>
        <div class="sc-content">
          $2A = 3B = 4C$ me $A:B:C$ nikaalne ke liye: $A$ ko chhipao aur $3 \times 4 = 12$ likho; $B$ ko chhipao $2 \times 4 = 8$; $C$ ko chhipao $2 \times 3 = 6$! Ratio $= 12:8:6 = \mathbf{6:4:3}$!
        </div>
      </div>

      <div class="shortcut-card">
        <div class="sc-title">⚡ 2. 10-Second Subtracted Number $x$</div>
        <div class="sc-content">
          $a, b, c, d$ me se kya ghatayein? Seedhe $x = \frac{ad - bc}{(a+d)-(b+c)}$ lagayein. Lambe $(a-x)(d-x)=(b-x)(c-x)$ quadratic se 1 minute bachta hai!
        </div>
      </div>

      <div class="shortcut-card">
        <div class="sc-title">⚡ 3. Constant Age Difference Trick</div>
        <div class="sc-content">
          Do logon ki aayu ka antar hamesha constant rehta hai. Ratio 1 me gap 2 unit hai aur Ratio 2 me gap 1 unit, to Ratio 2 ko 2 se guna karke gap barabar karein, fir unit change dekhein!
        </div>
      </div>

      <div class="shortcut-card">
        <div class="sc-title">⚡ 4. Rapid Mean Proportional</div>
        <div class="sc-content">
          $\text{Mean Proportional of } (3 + \sqrt{2}) \text{ and } (12 - \sqrt{32})$: $12 - \sqrt{32} = 4(3 - \sqrt{2})$. Product $= 4(9 - 2) = 28 \implies \sqrt{28} = \mathbf{2\sqrt{7}}$!
        </div>
      </div>

      <div class="shortcut-card">
        <div class="sc-title">⚡ 5. Cross-Multiplication for Income</div>
        <div class="sc-content">
          Income ratio $5:3$, Expenditure $9:5$, Savings ₹$2600$ and ₹$1800$. Cross 1: $5 \times 5 - 3 \times 9 = |25 - 27| = 2$ units. Cross 2: $9 \times 1800 - 5 \times 2600 = 16200 - 13000 = 3200$. $2 \text{ units} = 3200 \implies 1 \text{ unit} = 1600$!
        </div>
      </div>

      <div class="shortcut-card">
        <div class="sc-title">⚡ 6. Coin Value Multiplier</div>
        <div class="sc-content">
          ₹1, 50p, 25p ke coins ka ratio $2:3:5$ hai. Value ratio $= (2 \times 1) : (3 \times 0.5) : (5 \times 0.25) = 2 : 1.5 : 1.25 = 8 : 6 : 5$.
        </div>
      </div>
    </div>

    <div class="trap-grid" style="margin-top:14px;">
      <div class="trap-card">
        <div class="trap-header">
          <span class="trap-title">🚨 Trap 1: Swapping Third &amp; Fourth Proportional</span>
          <span class="error-code">[F] FORMULA</span>
        </div>
        <div class="trap-desc">
          Third Proportional do sankhyaon $(a, b)$ ka hota hai ($b^2/a$), jabki Fourth Proportional teen sankhyaon $(a, b, c)$ ka hota hai ($bc/a$).
        </div>
      </div>

      <div class="trap-card">
        <div class="trap-header">
          <span class="trap-title">🚨 Trap 2: Direct Addition of Ratios</span>
          <span class="error-code">[C] CONCEPT</span>
        </div>
        <div class="trap-desc">
          Agar $A:B = 2:3$ aur $B:C = 4:5$, to $A+B+C = 2+3+5$ nahi ho sakta! Pehle $B$ ko barabar karke $8:12:15$ banana aniwarya hai.
        </div>
      </div>

      <div class="trap-card">
        <div class="trap-header">
          <span class="trap-title">🚨 Trap 3: Coin Count vs Monetary Value</span>
          <span class="error-code">[R] READING</span>
        </div>
        <div class="trap-desc">
          Prashna me ₹$420$ "Total Value" di hai ya "Total Number of Coins"? Ratio coins ka hai ya rupees ka? Dhyan se na padhne par poora sawal galat ho jata hai.
        </div>
      </div>

      <div class="trap-card">
        <div class="trap-header">
          <span class="trap-title">🚨 Trap 4: Sub-duplicate vs Duplicate</span>
          <span class="error-code">[F] FORMULA</span>
        </div>
        <div class="trap-desc">
          Duplicate ka arth square ($a^2:b^2$) hota hai, aur Sub-duplicate ka arth square root ($\sqrt{a}:\sqrt{b}$) hota hai. 'Sub' shabd ka dhyan rakhein!
        </div>
      </div>

      <div class="trap-card">
        <div class="trap-header">
          <span class="trap-title">🚨 Trap 5: Unequal Units in Age Problem</span>
          <span class="error-code">[K] CALCULATION</span>
        </div>
        <div class="trap-desc">
          Aayuu ke prashno me aane wale varsh dono ke liye barabar judte hain. Agar ratio ka unit change dono taraf barabar nahi dikh raha, to pehle gap barabar karein!
        </div>
      </div>

      <div class="trap-card">
        <div class="trap-header">
          <span class="trap-title">🚨 Trap 6: Reciprocal Ratio of 3 Terms</span>
          <span class="error-code">[C] CONCEPT</span>
        </div>
        <div class="trap-desc">
          $a:b:c$ ka inverse $c:b:a$ NAHI hota! Inverse $\frac{1}{a} : \frac{1}{b} : \frac{1}{c} = bc : ac : ab$ hota hai.
        </div>
      </div>
    </div>
  </section>
'''

print("Phase 3 theory ready.")
