# -*- coding: utf-8 -*-
"""
Phase 1 Theory Chapters, Formula Vault, Shortcuts & Traps
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
        <h2 style="font-size:1.45rem;font-weight:800;color:#fff;">📖 Exhaustive Textbook Notes: Number System</h2>
      </div>
      <span style="font-size:0.82rem;color:var(--text-muted);">6 Detailed Modules &bull; Complete Coverage</span>
    </div>

    <!-- Chapter 1 -->
    <div class="topic-anchor-block" id="topic-1-classification" data-topic="1" style="margin-bottom:28px;">
      <div class="topic-breadcrumb">
        <a href="#sec-topics">Topics Hub</a> &gt; <span>Topic 1</span> &gt; <strong>Classification, Primes &amp; Decimals</strong>
      </div>
      <span class="chap-badge">MODULE 1</span>
      <h3 class="chap-title">1. Classification of Numbers, Primes & Decimal Expansions</h3>
      <p class="book-p">
        संख्या प्रणाली (Number System) गणित का आधार स्तंभ है। SSC CGL में हर साल Tier-1 में 2 से 3 प्रश्न और Tier-2 में 3 से 4 प्रश्न इसी अध्याय से पूछे जाते हैं।
      </p>
      
      <div class="table-wrap">
        <table class="book-table">
          <thead>
            <tr>
              <th>संख्या का प्रकार (Type)</th>
              <th>संकेत (Symbol)</th>
              <th>परिभाषा एवं उदाहरण (Definition & Examples)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Natural Numbers (प्राकृत संख्याएँ)</strong></td>
              <td>$\mathbb{N}$</td>
              <td>गिनती की संख्याएँ: $\{1, 2, 3, 4, 5, \dots\}$. सबसे छोटी प्राकृत संख्या 1 है।</td>
            </tr>
            <tr>
              <td><strong>Whole Numbers (पूर्ण संख्याएँ)</strong></td>
              <td>$\mathbb{W}$</td>
              <td>$\{0, 1, 2, 3, 4, \dots\}$. जब शून्य को प्राकृत संख्याओं में जोड़ दिया जाए।</td>
            </tr>
            <tr>
              <td><strong>Integers (पूर्णांक)</strong></td>
              <td>$\mathbb{Z}$</td>
              <td>$\{\dots, -3, -2, -1, 0, 1, 2, 3, \dots\}$. ऋणात्मक, शून्य और धनात्मक पूर्ण मान।</td>
            </tr>
            <tr>
              <td><strong>Rational Numbers (परिमेय संख्याएँ)</strong></td>
              <td>$\mathbb{Q}$</td>
              <td>वे संख्याएँ जिन्हें $p/q$ के रूप में व्यक्त किया जा सके, जहाँ $p, q \in \mathbb{Z}$ और $q \ne 0$। दशमलव रूप या तो सांत (terminating जैसे $0.75$) या असांत आवर्ती (non-terminating recurring जैसे $0.333\dots = 1/3$) होता है।</td>
            </tr>
            <tr>
              <td><strong>Irrational Numbers (अपरिमेय संख्याएँ)</strong></td>
              <td>$\mathbb{Q}'$</td>
              <td>वे संख्याएँ जिन्हें $p/q$ रूप में नहीं लिखा जा सकता। दशमलव रूप असांत अनावर्ती (non-terminating non-recurring) होता है। जैसे $\sqrt{2}, \sqrt{3}, \pi, e$। (ध्यान दें: $\frac{22}{7}$ परिमेय है, पर $\pi$ अपरिमेय है!)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="concept-callout">
        <strong>🔥 Prime Numbers (अभाज्य संख्याएँ) — Key Facts for SSC:</strong>
        <ul class="book-list" style="margin-top:8px;">
          <li>वह संख्या जिसके केवल और केवल दो अलग-अलग गुणनखंड हों (1 और स्वयं वह संख्या)।</li>
          <li><strong>1 न तो अभाज्य है और न ही भाज्य (1 is neither prime nor composite).</strong></li>
          <li><strong>2 एकमात्र सम अभाज्य संख्या है (2 is the only even prime number).</strong> सबसे छोटी विषम अभाज्य संख्या 3 है।</li>
          <li><strong>1 से 50 तक कुल 15 अभाज्य संख्याएँ होती हैं:</strong> $2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47$।</li>
          <li><strong>51 से 100 तक कुल 10 अभाज्य संख्याएँ होती हैं:</strong> $53, 59, 61, 67, 71, 73, 79, 83, 89, 97$।</li>
          <li><strong>1 से 100 तक कुल 25 अभाज्य संख्याएँ होती हैं।</strong> (1 से 200 तक कुल 46 अभाज्य संख्याएँ होती हैं)।</li>
          <li><strong>Prime Testing Algorithm:</strong> यदि किसी संख्या $N$ की जाँच करनी हो कि वह अभाज्य है या नहीं, तो $\sqrt{N}$ से छोटे या बराबर के सभी अभाज्य संख्याओं से $N$ को भाग देकर देखें। यदि किसी से भी भाग नहीं जाता, तो $N$ अभाज्य है। उदाहरण: 173 के लिए $14^2 = 196 > 173$। 13 तक के अभाज्य $\{2, 3, 5, 7, 11, 13\}$ में से कोई भी 173 को विभाजित नहीं करता, अतः 173 एक अभाज्य संख्या है।</li>
          <li><strong>Recurring Decimals to Fractions:</strong>
            $$0.\bar{a} = \frac{a}{9}, \quad 0.\overline{ab} = \frac{ab}{99}, \quad 0.a\bar{b} = \frac{ab - a}{90}, \quad 0.ab\bar{c} = \frac{abc - ab}{900}$$
          </li>
        </ul>
      </div>

      <!-- Topic Navigation Footer -->
      <div class="topic-nav-footer">
        <span class="tnav-step-info">Topic 1 of 6: Classification &amp; Primes</span>
        <div class="tnav-footer-btns">
          <button class="tnav-fbtn practice" onclick="filterQs('1', event); document.getElementById('sec-basic').scrollIntoView({behavior:'smooth'});">🎯 Practice Topic Qs</button>
          <a href="#topic-2-divisibility" class="tnav-fbtn next">Next: Divisibility Rules &rarr;</a>
        </div>
      </div>
    </div>

    <!-- Chapter 2 -->
    <div class="topic-anchor-block" id="topic-2-divisibility" data-topic="2" style="margin-bottom:28px;">
      <div class="topic-breadcrumb">
        <a href="#sec-topics">Topics Hub</a> &gt; <span>Topic 2</span> &gt; <strong>Divisibility Rules (2 to 99)</strong>
      </div>
      <span class="chap-badge">MODULE 2</span>
      <h3 class="chap-title">2. The Master Divisibility Engine (2 to 11 & High-Yield Composites 72, 88, 99)</h3>
      <p class="book-p">
        Divisibility Rules SSC CGL के सबसे महत्वपूर्ण टूल्स में से एक हैं। बड़े-बड़े 8 या 9 अंकों के समीकरणों को बिना पूरा भाग दिए 15 सेकंड में हल किया जा सकता है।
      </p>

      <div class="table-wrap">
        <table class="book-table">
          <thead>
            <tr>
              <th>भाजक (Divisor)</th>
              <th>विभाज्यता नियम (Condition)</th>
              <th>स्मार्ट ट्रिक / उदाहरण (Topper Insight)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>2, 4, 8, 16 ($2^k$)</strong></td>
              <td>$2^1 \to$ अंतिम 1 अंक; $2^2 (4) \to$ अंतिम 2 अंक; $2^3 (8) \to$ अंतिम 3 अंक; $2^4 (16) \to$ अंतिम 4 अंक।</td>
              <td><strong>8 की स्पीड ट्रिक:</strong> यदि सैकड़े (hundreds) का अंक सम (even) हो, तो केवल अंतिम 2 अंकों को 8 से भाग देकर देखें! यदि सैकड़े का अंक विषम (odd) हो, तो अंतिम 2 अंकों में 4 जोड़कर 8 से भाग दें।</td>
            </tr>
            <tr>
              <td><strong>3 एवं 9</strong></td>
              <td>दी गई संख्या के सभी अंकों का योग (Sum of digits) 3 या 9 से कटना चाहिए।</td>
              <td><strong>Casting Out 9s:</strong> योग करते समय 9 या 9 बनाने वाले जोड़ों (जैसे $4+5, 3+6, 2+7$) को तुरंत काट दें। केवल बचे हुए अंकों का योग देखें।</td>
            </tr>
            <tr>
              <td><strong>5, 25, 125 ($5^k$)</strong></td>
              <td>$5^1 \to$ अंतिम अंक 0 या 5; $5^2 (25) \to$ अंतिम 2 अंक ($00, 25, 50, 75$); $5^3 (125) \to$ अंतिम 3 अंक।</td>
              <td>अंतिम अंकों को देखकर तुरंत निष्कर्ष निकालें।</td>
            </tr>
            <tr>
              <td><strong>11</strong></td>
              <td>$(\text{विषम स्थानों के अंकों का योग}) - (\text{सम स्थानों के अंकों का योग}) = 0$ या 11 का गुणज।</td>
              <td>दाहिनी ओर से $d_1 - d_2 + d_3 - d_4 + \dots$ का मान निकालें। यह मान $0, \pm 11, \pm 22$ होना चाहिए।</td>
            </tr>
            <tr>
              <td><strong>7, 11, 13 (संयुक्त नियम)</strong></td>
              <td>दाहिनी ओर से 3-3 अंकों के जोड़े (triplets) बनाएँ। एकांतर (alternate) जोड़ों का अंतर 7, 11 या 13 से कटना चाहिए।</td>
              <td>उदा: संख्या $654321$ &rarr; $321 - 654 = -333$। चूँकि $-333$ न तो 7 से कटता है न 11 से न 13 से, अतः यह संख्या इनसे नहीं कटेगी।</td>
            </tr>
            <tr>
              <td><strong>72 ($8 \times 9$)</strong></td>
              <td>संख्या 8 और 9 दोनों से विभाजित होनी चाहिए ($\text{HCF}(8, 9) = 1$)।</td>
              <td><strong>पैटर्न:</strong> $785x3678y$ में पहले 8 के नियम से $y$ का मान निकालें, फिर 9 के नियम (डिजिट सम) से $x$ निकालें।</td>
            </tr>
            <tr>
              <td><strong>88 ($8 \times 11$)</strong></td>
              <td>संख्या 8 और 11 दोनों से विभाजित होनी चाहिए।</td>
              <td>पहले अंतिम 3 अंकों से 8 का परीक्षण कर अज्ञात चर निकालें, फिर 11 का एकांतर अंतर लगाएँ।</td>
            </tr>
            <tr>
              <td><strong>99 ($9 \times 11$)</strong></td>
              <td>संख्या 9 और 11 दोनों से विभाजित होनी चाहिए।</td>
              <td>अंकों का योग 9 से कटना चाहिए और एकांतर अंतर 0 या 11 होना चाहिए।</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Topic Navigation Footer -->
      <div class="topic-nav-footer">
        <a href="#topic-1-classification" class="tnav-fbtn prev">&larr; Prev: Classification</a>
        <button class="tnav-fbtn practice" onclick="filterQs('2', event); document.getElementById('sec-basic').scrollIntoView({behavior:'smooth'});">🎯 Practice Topic Qs</button>
        <a href="#topic-3-lcm-hcf" class="tnav-fbtn next">Next: LCM &amp; HCF &rarr;</a>
      </div>
    </div>

    <!-- Chapter 3 -->
    <div class="topic-anchor-block" id="topic-3-lcm-hcf" data-topic="3" style="margin-bottom:28px;">
      <div class="topic-breadcrumb">
        <a href="#sec-topics">Topics Hub</a> &gt; <span>Topic 3</span> &gt; <strong>LCM &amp; HCF Mastery</strong>
      </div>
      <span class="chap-badge">MODULE 3</span>
      <h3 class="chap-title">3. HCF & LCM Mastery, Fraction Rules & The 4 Classical Remainder Models</h3>
      <p class="book-p">
        <strong>महत्तम समापवर्तक (HCF - Highest Common Factor)</strong> वह सबसे बड़ी संख्या है जो दी गई सभी संख्याओं को पूर्णतः विभाजित करती है।
        <strong>लघुत्तम समापवर्त्य (LCM - Least Common Multiple)</strong> वह सबसे छोटी संख्या है जो दी गई सभी संख्याओं से पूर्णतः विभाजित होती है।
      </p>

      <div class="concept-callout">
        <strong>📌 Core Formulas:</strong><br>
        1. <strong>केवल दो संख्याओं $A$ और $B$ के लिए:</strong>
        $$A \times B = \text{HCF}(A, B) \times \text{LCM}(A, B)$$
        <span style="color:var(--red);">⚠️ चेतावनी: यह नियम 3 या अधिक संख्याओं के लिए सीधे लागू नहीं होता!</span><br>
        2. <strong>भिन्नों का HCF एवं LCM:</strong>
        $$\text{HCF}\left(\frac{a}{b}, \frac{c}{d}, \frac{e}{f}\right) = \frac{\text{HCF}(a, c, e)}{\text{LCM}(b, d, f)}, \qquad \text{LCM}\left(\frac{a}{b}, \frac{c}{d}, \frac{e}{f}\right) = \frac{\text{LCM}(a, c, e)}{\text{HCF}(b, d, f)}$$
        3. <strong>अनुपात एवं HCF संबंध:</strong> यदि दो संख्याओं का अनुपात $a : b$ हो (जहाँ $a, b$ सह-अभाज्य हैं) और उनका HCF $= H$ हो, तो:<br>
        &bull; संख्याएँ $= aH$ और $bH$<br>
        &bull; $\text{LCM} = a \times b \times H$<br>
        &bull; संख्याओं का योग $= (a + b)H$<br>
        &bull; संख्याओं का गुणनफल $= a \times b \times H^2$
      </div>

      <div class="table-wrap">
        <table class="book-table">
          <thead>
            <tr>
              <th>मॉडल (Remainder Model)</th>
              <th>प्रश्नों की भाषा (Question Phrasing)</th>
              <th>हल करने का अचूक सूत्र (Solution Formula)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Model 1: समान शेषफल (LCM)</strong></td>
              <td>वह सबसे छोटी संख्या जिसे $x, y, z$ से भाग देने पर प्रत्येक दशा में शेषफल $r$ बचे।</td>
              <td>$$N = k \times \text{LCM}(x, y, z) + r \quad (k = 1, 2, 3\dots)$$</td>
            </tr>
            <tr>
              <td><strong>Model 2: नियत अंतर शेषफल (LCM)</strong></td>
              <td>वह सबसे छोटी संख्या जिसे $x, y, z$ से भाग देने पर क्रमशः $r_1, r_2, r_3$ शेष बचे, जहाँ $(x - r_1) = (y - r_2) = (z - r_3) = d$ (समान अंतर)।</td>
              <td>$$N = k \times \text{LCM}(x, y, z) - d$$</td>
            </tr>
            <tr>
              <td><strong>Model 3: अज्ञात समान शेषफल (HCF)</strong></td>
              <td>वह सबसे बड़ी संख्या जिससे $x, y, z$ को भाग देने पर प्रत्येक स्थिति में समान शेषफल बचे (परंतु शेषफल अज्ञात हो)।</td>
              <td>$$H = \text{HCF}(|x - y|, |y - z|, |z - x|)$$</td>
            </tr>
            <tr>
              <td><strong>Model 4: ज्ञात भिन्न शेषफल (HCF)</strong></td>
              <td>वह सबसे बड़ी संख्या जिससे $x, y, z$ को भाग देने पर क्रमशः $a, b, c$ शेष बचे।</td>
              <td>$$H = \text{HCF}(x - a, y - b, z - c)$$</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Topic Navigation Footer -->
      <div class="topic-nav-footer">
        <a href="#topic-2-divisibility" class="tnav-fbtn prev">&larr; Prev: Divisibility</a>
        <button class="tnav-fbtn practice" onclick="filterQs('3', event); document.getElementById('sec-basic').scrollIntoView({behavior:'smooth'});">🎯 Practice Topic Qs</button>
        <a href="#topic-4-remainders" class="tnav-fbtn next">Next: Remainder Theorems &rarr;</a>
      </div>
    </div>

    <!-- Chapter 4 -->
    <div class="topic-anchor-block" id="topic-4-remainders" data-topic="4" style="margin-bottom:28px;">
      <div class="topic-breadcrumb">
        <a href="#sec-topics">Topics Hub</a> &gt; <span>Topic 4</span> &gt; <strong>Remainder Theorems &amp; Power Remainder</strong>
      </div>
      <span class="chap-badge">MODULE 4</span>
      <h3 class="chap-title">4. Remainder Theorems, Negative Remainders & Algebraic Remainder Patterns</h3>
      <p class="book-p">
        शेषफल प्रमेय SSC CGL के सबसे पसंदीदा विषयों में से एक है। <strong>Remainder कभी भी ऋणात्मक नहीं हो सकता और हमेशा $0 \le R < \text{Divisor}$ होता है।</strong>
      </p>

      <div class="concept-callout">
        <strong>⚡ Negative Remainder Concept:</strong><br>
        यदि $67$ को $68$ से भाग दें, तो सामान्य शेषफल $67$ है। लेकिन गणितीय सुविधा के लिए हम इसे $-1$ ($67 - 68 = -1$) लिख सकते हैं।<br>
        यदि गणना के अंत में शेषफल $-r$ आता है, तो वास्तविक धनात्मक शेषफल $= \text{Divisor} - r$ होगा।<br>
        उदाहरण: $\frac{67^{67} + 67}{68} \implies (-1)^{67} + (-1) = -1 - 1 = -2$। वास्तविक शेषफल $= 68 - 2 = \mathbf{66}$।
      </div>

      <div class="table-wrap">
        <table class="book-table">
          <thead>
            <tr>
              <th>प्रमेय / स्वरूप (Theorem / Pattern)</th>
              <th>सूत्र (Formula)</th>
              <th>शर्तें एवं अनुप्रयोग (Condition & Example)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Binomial Theorem Pattern 1</strong></td>
              <td>$$\frac{(ax + 1)^n}{a} \implies \text{Remainder} = 1^n = 1$$</td>
              <td>किसी भी घात $n$ के लिए मान्य। जैसे $\frac{9^{19}}{8} = \frac{(8+1)^{19}}{8} \implies R = 1$।</td>
            </tr>
            <tr>
              <td><strong>Binomial Theorem Pattern 2</strong></td>
              <td>$$\frac{(ax - 1)^n}{a} \implies \begin{cases} +1 & \text{यदि } n \text{ सम (even) है} \\ a - 1 & \text{यदि } n \text{ विषम (odd) है} \end{cases}$$</td>
              <td>जैसे $\frac{17^{200}}{18} \implies (-1)^{200} = 1$। परंतु $\frac{17^{199}}{18} \implies (-1)^{199} = -1 \to 18 - 1 = 17$।</td>
            </tr>
            <tr>
              <td><strong>Fermat's Little Theorem</strong></td>
              <td>$$\frac{a^{p-1}}{p} \implies \text{Remainder} = 1$$</td>
              <td>जहाँ $p$ एक अभाज्य संख्या (Prime) है और $\text{HCF}(a, p) = 1$। उदाहरण: $\frac{2^{100}}{101} \implies R = 1$ (चूँकि 101 अभाज्य है)।</td>
            </tr>
            <tr>
              <td><strong>Wilson's Theorem</strong></td>
              <td>$$\frac{(p-1)!}{p} \implies \text{Remainder} = p - 1 \equiv -1$$</td>
              <td>जहाँ $p$ अभाज्य है। उदाहरण: $\frac{28!}{29} \implies R = 28$। तथा $\frac{(p-2)!}{p} \implies R = 1$।</td>
            </tr>
            <tr>
              <td><strong>Algebraic Identity Remainder</strong></td>
              <td>
                &bull; $(x^n - a^n)$ हमेशा $(x - a)$ से पूर्णतः विभाज्य होता है (सभी $n$ के लिए)।<br>
                &bull; $(x^n - a^n)$ संख्या $(x + a)$ से विभाज्य होता है यदि $n$ <strong>सम (even)</strong> हो।<br>
                &bull; $(x^n + a^n)$ संख्या $(x + a)$ से विभाज्य होता है यदि $n$ <strong>विषम (odd)</strong> हो।
              </td>
              <td>जैसे $(23^{10} - 1024) = 23^{10} - 2^{10}$ सम घात है, अतः यह $(23-2)=21$ और $(23+2)=25$ दोनों से विभाजित होगी।</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Topic Navigation Footer -->
      <div class="topic-nav-footer">
        <a href="#topic-3-lcm-hcf" class="tnav-fbtn prev">&larr; Prev: LCM &amp; HCF</a>
        <button class="tnav-fbtn practice" onclick="filterQs('4', event); document.getElementById('sec-basic').scrollIntoView({behavior:'smooth'});">🎯 Practice Topic Qs</button>
        <a href="#topic-5-unit-digit" class="tnav-fbtn next">Next: Unit Digit &amp; Cyclicity &rarr;</a>
      </div>
    </div>

    <!-- Chapter 5 -->
    <div class="topic-anchor-block" id="topic-5-unit-digit" data-topic="5" style="margin-bottom:28px;">
      <div class="topic-breadcrumb">
        <a href="#sec-topics">Topics Hub</a> &gt; <span>Topic 5</span> &gt; <strong>Unit Digit &amp; Cyclicity of Powers</strong>
      </div>
      <span class="chap-badge">MODULE 5</span>
      <h3 class="chap-title">5. Unit Digit (इकाई अंक) & Cyclicity of Powers</h3>
      <p class="book-p">
        किसी भी गुणनफल या घात वाले व्यंजक का अंतिम अंक (Unit Digit) निकालने के लिए हमें केवल आधार के इकाई अंक और घात की चक्रीयता (Cyclicity) से मतलब होता है।
      </p>

      <div class="table-wrap">
        <table class="book-table">
          <thead>
            <tr>
              <th>चक्रीयता वर्ग (Class)</th>
              <th>अंक (Digits)</th>
              <th>चक्रीयता (Cyclicity)</th>
              <th>नियम एवं उदाहरण (Rule & Example)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Class 1: अपरिवर्तनीय</strong></td>
              <td>$\{0, 1, 5, 6\}$</td>
              <td><strong>1</strong> (सदैव समान)</td>
              <td>किसी भी धनात्मक पूर्णांक घात पर इकाई अंक कभी नहीं बदलता। $0^n \to 0, 1^n \to 1, 5^n \to 5, 6^n \to 6$। जैसे $756^{987}$ का इकाई अंक $6$ ही होगा।</td>
            </tr>
            <tr>
              <td><strong>Class 2: दोहरी चक्रीयता</strong></td>
              <td>$\{4, 9\}$</td>
              <td><strong>2</strong> (सम / विषम)</td>
              <td>
                &bull; $4^{\text{विषम}} = 4, \quad 4^{\text{सम}} = 6$<br>
                &bull; $9^{\text{विषम}} = 9, \quad 9^{\text{सम}} = 1$
              </td>
            </tr>
            <tr>
              <td><strong>Class 3: चतुर्थ चक्रीयता</strong></td>
              <td>$\{2, 3, 7, 8\}$</td>
              <td><strong>4</strong> (4 से भाग नियम)</td>
              <td>
                दी गई घात को 4 से भाग दें और शेषफल $r$ प्राप्त करें:<br>
                &bull; यदि $r = 1, 2, 3 \implies$ इकाई अंक $\text{Base}^r$ का इकाई अंक होगा।<br>
                &bull; <strong>यदि $r = 0$ (पूर्ण विभाज्य) $\implies$ घात को 4 मानें ($\text{Base}^4$)!</strong><br>
                उदा: $7^{95} \to 95 \div 4 \implies r = 3 \to 7^3 = 343 \to$ इकाई अंक $\mathbf{3}$।
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="concept-callout">
        <strong>⚡ Factorial Unit Digits:</strong><br>
        $1! = 1, \quad 2! = 2, \quad 3! = 6, \quad 4! = 24 \to 4, \quad 5! = 120 \to 0$।<br>
        $5!$ या उससे बड़े किसी भी फैक्टोरियल में कम से कम एक 2 और एक 5 अवश्य होता है, अतः <strong>$n \ge 5$ के लिए $n!$ का इकाई अंक सदैव 0 होता है!</strong>
      </div>

      <!-- Topic Navigation Footer -->
      <div class="topic-nav-footer">
        <a href="#topic-4-remainders" class="tnav-fbtn prev">&larr; Prev: Remainder Theorems</a>
        <button class="tnav-fbtn practice" onclick="filterQs('5', event); document.getElementById('sec-basic').scrollIntoView({behavior:'smooth'});">🎯 Practice Topic Qs</button>
        <a href="#topic-6-factors" class="tnav-fbtn next">Next: Factors Engine &rarr;</a>
      </div>
    </div>

    <!-- Chapter 6 -->
    <div class="topic-anchor-block" id="topic-6-factors" data-topic="6" style="margin-bottom:28px;">
      <div class="topic-breadcrumb">
        <a href="#sec-topics">Topics Hub</a> &gt; <span>Topic 6</span> &gt; <strong>Factors, Divisors &amp; Trailing Zeros</strong>
      </div>
      <span class="chap-badge">MODULE 6</span>
      <h3 class="chap-title">6. Factors (गुणनखंड), Sum of Factors & Trailing Zeros (शून्यकों की संख्या)</h3>
      <p class="book-p">
        जब किसी संख्या $N$ का अभाज्य गुणनखंडन (Prime Factorization) $N = 2^a \cdot p_2^b \cdot p_3^c \dots$ किया जाता है:
      </p>

      <div class="table-wrap">
        <table class="book-table">
          <thead>
            <tr>
              <th>विशेषता (Feature)</th>
              <th>गणितीय सूत्र (Mathematical Formula)</th>
              <th>उदाहरण: $360 = 2^3 \times 3^2 \times 5^1$</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>कुल गुणनखंड (Total Factors)</strong></td>
              <td>$$(a+1)(b+1)(c+1)\dots$$</td>
              <td>$(3+1)(2+1)(1+1) = 4 \times 3 \times 2 = \mathbf{24}$</td>
            </tr>
            <tr>
              <td><strong>विषम गुणनखंड (Odd Factors)</strong></td>
              <td>$$(b+1)(c+1)\dots \quad (2 \text{ की घात को 0 मान लें})$$</td>
              <td>$(2+1)(1+1) = 3 \times 2 = \mathbf{6}$</td>
            </tr>
            <tr>
              <td><strong>सम गुणनखंड (Even Factors)</strong></td>
              <td>$$a(b+1)(c+1)\dots = \text{Total} - \text{Odd}$$</td>
              <td>$3 \times (2+1)(1+1) = 3 \times 6 = \mathbf{18}$ (या $24 - 6 = 18$)</td>
            </tr>
            <tr>
              <td><strong>अभाज्य गुणनखंड (Prime Factors)</strong></td>
              <td>$$a + b + c + \dots$$</td>
              <td>$3 + 2 + 1 = \mathbf{6}$ (विशिष्ट अभाज्य संख्याएँ $= 3$ यथा $2, 3, 5$)</td>
            </tr>
            <tr>
              <td><strong>गुणनखंडों का योग (Sum of Factors)</strong></td>
              <td>$$\left(\frac{2^{a+1}-1}{2-1}\right) \times \left(\frac{p_2^{b+1}-1}{p_2-1}\right) \times \dots$$</td>
              <td>$\frac{2^4-1}{1} \times \frac{3^3-1}{2} \times \frac{5^2-1}{4} = 15 \times 13 \times 6 = \mathbf{1170}$</td>
            </tr>
            <tr>
              <td><strong>गुणनखंडों का गुणनफल (Product of Factors)</strong></td>
              <td>$$N^{\frac{\text{Total Factors}}{2}}$$</td>
              <td>$360^{24/2} = 360^{12}$</td>
            </tr>
            <tr>
              <td><strong>पूर्ण वर्ग गुणनखंड (Perfect Square Factors)</strong></td>
              <td>$$\left(\lfloor a/2 \rfloor + 1\right)\left(\lfloor b/2 \rfloor + 1\right)\dots$$</td>
              <td>$(\lfloor 3/2 \rfloor + 1)(\lfloor 2/2 \rfloor + 1)(\lfloor 1/2 \rfloor + 1) = 2 \times 2 \times 1 = \mathbf{4}$</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="concept-callout">
        <strong>🔥 Trailing Zeros in $N!$ (Legendre's Formula):</strong><br>
        किसी भी फैक्टोरियल में शून्य (0) का निर्माण $2 \times 5 = 10$ के जोड़े से होता है। $N!$ में 2 की संख्या हमेशा 5 से अधिक होती है, अतः <strong>शून्यों की संख्या 5 की घात पर निर्भर करती है:</strong>
        $$\text{Trailing Zeros} = \left\lfloor \frac{N}{5} \right\rfloor + \left\lfloor \frac{N}{25} \right\rfloor + \left\lfloor \frac{N}{125} \right\rfloor + \dots$$
        उदाहरण: $100!$ में शून्यों की संख्या $= \lfloor 100/5 \rfloor + \lfloor 100/25 \rfloor = 20 + 4 = \mathbf{24}$।
      </div>

      <!-- Topic Navigation Footer -->
      <div class="topic-nav-footer">
        <a href="#topic-5-unit-digit" class="tnav-fbtn prev">&larr; Prev: Unit Digit</a>
        <button class="tnav-fbtn practice" onclick="filterQs('6', event); document.getElementById('sec-basic').scrollIntoView({behavior:'smooth'});">🎯 Practice Topic Qs</button>
        <a href="#sec-shortcuts" class="tnav-fbtn next">Next: Speed Shortcuts &rarr;</a>
      </div>
    </div>
  </section>
'''

def get_formula_vault():
    return r'''
  <!-- FORMULA VAULT -->
  <section id="sec-formulas" style="margin-bottom:24px;">
    <h2 class="sec-title">📐 Formula Vault — Phase 1 Completed Formula Sheet (10 Cards)</h2>
    <div class="formula-grid">
      
      <!-- Card 1 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">1. Fundamental HCF & LCM Product</span>
          <button class="copy-btn" onclick="copyFormula('HCF * LCM = A * B (Valid ONLY for 2 numbers)')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">HCF(A, B) &times; LCM(A, B) = A &times; B</div>
          <div class="fc-row"><strong>Ratio Form:</strong> If $A:B = a:b$ and HCF is $H$, then $A=aH, B=bH$, LCM $= a \cdot b \cdot H$.</div>
          <div class="fc-trap">⚠️ Do NOT apply $HCF \times LCM = A \times B \times C$ to three numbers!</div>
        </div>
      </div>

      <!-- Card 2 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">2. HCF & LCM of Fractions</span>
          <button class="copy-btn" onclick="copyFormula('HCF = HCF(Num)/LCM(Den); LCM = LCM(Num)/HCF(Den)')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">HCF = HCF(Numerators) / LCM(Denominators)</div>
          <div class="fc-formula">LCM = LCM(Numerators) / HCF(Denominators)</div>
          <div class="fc-row"><strong>Rule:</strong> Always reduce fractions to their simplest form first!</div>
        </div>
      </div>

      <!-- Card 3 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">3. LCM Remainder Models</span>
          <button class="copy-btn" onclick="copyFormula('Model 1: k*LCM + r; Model 2: k*LCM - d')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">Same Remainder r: N = k &times; LCM(x, y, z) + r</div>
          <div class="fc-formula">Diff Remainders: N = k &times; LCM(x, y, z) - d</div>
          <div class="fc-row">where $d = (x - r_1) = (y - r_2) = (z - r_3)$ is constant.</div>
        </div>
      </div>

      <!-- Card 4 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">4. HCF Remainder Models</span>
          <button class="copy-btn" onclick="copyFormula('HCF(|x-y|, |y-z|, |z-x|)')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">Unknown same remainder: H = HCF(|x-y|, |y-z|, |z-x|)</div>
          <div class="fc-formula">Given remainders a,b,c: H = HCF(x-a, y-b, z-c)</div>
        </div>
      </div>

      <!-- Card 5 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">5. Binomial Remainder Forms</span>
          <button class="copy-btn" onclick="copyFormula('(ax+1)^n / a => Rem 1; (ax-1)^n / a => (-1)^n')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">(ax + 1)^n / a &implies; Remainder = 1</div>
          <div class="fc-formula">(ax - 1)^n / a &implies; Rem = (-1)^n [1 if even, a-1 if odd]</div>
        </div>
      </div>

      <!-- Card 6 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">6. Fermat's & Wilson's Theorems</span>
          <button class="copy-btn" onclick="copyFormula('Fermat: a^(p-1) mod p = 1; Wilson: (p-1)! mod p = p-1')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">Fermat: a^(p-1) &equiv; 1 (mod p) [p is prime, gcd(a,p)=1]</div>
          <div class="fc-formula">Wilson: (p-1)! &equiv; -1 &equiv; p-1 (mod p)</div>
        </div>
      </div>

      <!-- Card 7 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">7. Factor Counts Engine</span>
          <button class="copy-btn" onclick="copyFormula('Total = (a+1)(b+1)(c+1); Odd = (b+1)(c+1); Even = a(b+1)(c+1)')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">Total Factors = (a+1)(b+1)(c+1)</div>
          <div class="fc-formula">Odd = (b+1)(c+1); Even = a(b+1)(c+1)</div>
          <div class="fc-row">For prime factorization $N = 2^a p_2^b p_3^c$.</div>
        </div>
      </div>

      <!-- Card 8 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">8. Sum & Product of Factors</span>
          <button class="copy-btn" onclick="copyFormula('Sum = [(2^(a+1)-1)/(2-1)] * ... ; Product = N^(Total/2)')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">Sum = [(2^(a+1)-1)/1] &times; [(p2^(b+1)-1)/(p2-1)] &times; ...</div>
          <div class="fc-formula">Product of Factors = N^(Total Factors / 2)</div>
        </div>
      </div>

      <!-- Card 9 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">9. Trailing Zeros (Legendre's Formula)</span>
          <button class="copy-btn" onclick="copyFormula('Zeros in N! = floor(N/5) + floor(N/25) + floor(N/125) + ...')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">Zeros in N! = &lfloor;N/5&rfloor; + &lfloor;N/25&rfloor; + &lfloor;N/125&rfloor; + ...</div>
          <div class="fc-row">Number of zeros is governed by the power of 5 in the prime breakdown.</div>
        </div>
      </div>

      <!-- Card 10 -->
      <div class="formula-card">
        <div class="fc-header">
          <span class="fc-name">10. Recurring Decimal Conversion</span>
          <button class="copy-btn" onclick="copyFormula('0.ab... = (Full number - non-recurring) / (99..00..)')">📋 Copy</button>
        </div>
        <div class="fc-body">
          <div class="fc-formula">0.a(bar b) = (ab - a) / 90</div>
          <div class="fc-formula">0.ab(bar cd) = (abcd - ab) / 9900</div>
          <div class="fc-row">Put as many 9s as recurring digits, followed by as many 0s as non-recurring digits.</div>
        </div>
      </div>

    </div>
  </section>
'''

def get_shortcuts_and_traps():
    return r'''
  <!-- SHORTCUTS & TRAPS -->
  <section id="sec-shortcuts" style="margin-bottom:24px;">
    <h2 class="sec-title">⚡ Speed Shortcuts &amp; Classic SSC Exam Traps</h2>
    
    <div class="shortcut-grid">
      <div class="shortcut-card">
        <div class="sc-title">⚡ 1. Divisibility by 8 — Hundreds Digit Trick</div>
        <div class="sc-content">
          Last 3 digits me agar सैकड़े का अंक सम (0, 2, 4, 6, 8) हो, तो केवल अंतिम 2 अंक 8 से कटने चाहिए! अगर सैकड़े का अंक विषम (1, 3, 5, 7, 9) हो, तो अंतिम 2 अंकों में 4 जोड़ें और 8 से चेक करें। 10 सेकंड बचते हैं!
        </div>
      </div>

      <div class="shortcut-card">
        <div class="sc-title">⚡ 2. 72 and 88 Missing Digits Strategy</div>
        <div class="sc-content">
          $785x3678y$ div by 72: हमेशा पहले 8 का नियम ($78y$) लगाकर $y$ निकालें। फिर 9 का डिजिटल सम (casting out 9s) लगाकर तुरंत $x$ निकालें। कभी भी पहले 9 से मत शुरू करें!
        </div>
      </div>

      <div class="shortcut-card">
        <div class="sc-title">⚡ 3. Negative Remainder for Rapid Powers</div>
        <div class="sc-content">
          जब भाज्य भाजक से 1 कम हो ($67 \div 68$), तो शेष $-1$ लें। $(-1)^{\text{odd}} = -1 \implies 68 - 1 = 67$; $(-1)^{\text{even}} = +1$। कोई द्विपद विस्तार लिखने की जरूरत नहीं।
        </div>
      </div>

      <div class="shortcut-card">
        <div class="sc-title">⚡ 4. Divisible by 12 Factors Shortcut</div>
        <div class="sc-content">
          1080 के 12 से विभाज्य गुणनखंड चाहिए? 1080 में से 12 बाहर निकालें: $1080 = 12 \times 90$। अब केवल 90 के कुल गुणनखंड निकालें: $90 = 2^1 \times 3^2 \times 5^1 \implies 2 \times 3 \times 2 = 12$!
        </div>
      </div>

      <div class="shortcut-card">
        <div class="sc-title">⚡ 5. Power Mod 4 Last Two Digits Rule</div>
        <div class="sc-content">
          बड़ी घात जैसे $7^{987654321}$ का इकाई अंक निकालना हो, तो पूरी घात को 4 से भाग न दें! 4 की विभाज्यता के लिए केवल अंतिम 2 अंक ($21$) को 4 से भाग दें: $21 \div 4 \implies r=1 \implies 7^1 = 7$!
        </div>
      </div>

      <div class="shortcut-card">
        <div class="sc-title">⚡ 6. Trailing Zeros in Odd Products</div>
        <div class="sc-content">
          $1 \times 3 \times 5 \times 7 \times \dots \times 99$ में एक भी 2 नहीं होता, अतः शून्यों की संख्या 0 होती है! जब तक 2 नहीं मिलेगा, 5 कभी 0 नहीं बना सकता।
        </div>
      </div>
    </div>

    <div class="trap-grid" style="margin-top:14px;">
      <div class="trap-card">
        <div class="trap-header">
          <span class="trap-title">🚨 Trap 1: 1 is NOT a Prime Number</span>
          <span class="error-code">[C] CONCEPT</span>
        </div>
        <div class="trap-desc">
          विद्यार्थी अक्सर 1 को अभाज्य मान लेते हैं। 1 का केवल एक ही गुणनखंड (1) होता है, जबकि Prime की परिभाषा के लिए ठीक 2 अलग-अलग गुणनखंड होने चाहिए।
        </div>
      </div>

      <div class="trap-card">
        <div class="trap-header">
          <span class="trap-title">🚨 Trap 2: HCF &times; LCM for 3 Numbers</span>
          <span class="error-code">[F] FORMULA</span>
        </div>
        <div class="trap-desc">
          $HCF \times LCM = A \times B$ केवल 2 संख्याओं के लिए सत्य है। 3 संख्याओं में $HCF \times LCM \ne A \times B \times C$!
        </div>
      </div>

      <div class="trap-card">
        <div class="trap-header">
          <span class="trap-title">🚨 Trap 3: Unit Digit When Remainder is 0</span>
          <span class="error-code">[S] SILLY</span>
        </div>
        <div class="trap-desc">
          $2^{48}$ में $48 \div 4 \implies r = 0$। छात्र घात 0 मानकर उत्तर 1 लिख देते हैं! नियम: जब $r=0$ हो, तो घात 4 लेनी है: $2^4 = 16 \implies 6$!
        </div>
      </div>

      <div class="trap-card">
        <div class="trap-header">
          <span class="trap-title">🚨 Trap 4: Negative Remainder Unconverted</span>
          <span class="error-code">[R] READING</span>
        </div>
        <div class="trap-desc">
          Negative remainder $-2$ मिलने पर विकल्प में $-2$ नहीं होता। वास्तविक शेषफल हमेशा $\text{Divisor} - 2$ होता है।
        </div>
      </div>

      <div class="trap-card">
        <div class="trap-header">
          <span class="trap-title">🚨 Trap 5: Forgetting to Reduce Fractions First</span>
          <span class="error-code">[K] CALCULATION</span>
        </div>
        <div class="trap-desc">
          भिन्नों का HCF/LCM निकालते समय अगर भिन्न सरलतम रूप (lowest terms) में नहीं हैं, तो गलत उत्तर आएगा। जैसे $4/6$ को पहले $2/3$ बनाना अनिवार्य है!
        </div>
      </div>

      <div class="trap-card">
        <div class="trap-header">
          <span class="trap-title">🚨 Trap 6: Swapping Divisible By vs Divided By</span>
          <span class="error-code">[R] READING</span>
        </div>
        <div class="trap-desc">
          "Divided by X, Y, Z" &implies; LCM निकालना है। "Divides X, Y, Z" &implies; HCF निकालना है। भाषा की गलती से पूरा सवाल उल्टा हो जाता है!
        </div>
      </div>
    </div>
  </section>
'''

print("Theory, formula vault, and shortcuts ready.")
