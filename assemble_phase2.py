# -*- coding: utf-8 -*-
"""
Assembler script to generate Phase_2_Percentage.html
"""

import os
from create_phase2_book import get_head_and_styles, get_topbar_and_hero, get_day_plan
from phase2_theory import get_theory_chapters, get_formula_vault, get_shortcuts_and_traps
from phase2_questions import get_basic_questions, get_mixed_questions, get_pyq_lab
from phase2_tools import get_timed_drill_and_tools, get_sidebar_modal_and_js

def build():
    html_parts = [
        get_head_and_styles(),
        get_topbar_and_hero(),
        get_day_plan(),
        get_theory_chapters(),
        get_formula_vault(),
        get_shortcuts_and_traps(),
        get_basic_questions(),
        get_mixed_questions(),
        get_pyq_lab(),
        get_timed_drill_and_tools(),
        get_sidebar_modal_and_js()
    ]
    
    full_html = "".join(html_parts)
    out_file = "/Users/appple/Desktop/Khushboo/Maths/Phase_2_Percentage.html"
    
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(full_html)
    
    print(f"Successfully generated {out_file}")
    print(f"File size: {os.path.getsize(out_file)} bytes")
    print(f"Lines count: {len(full_html.splitlines())}")

if __name__ == "__main__":
    build()
