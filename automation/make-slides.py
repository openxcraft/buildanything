#!/usr/bin/env python3
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

ROOT = Path(__file__).resolve().parents[1]
out = ROOT / 'formats/universal-build-workflow-slides.pptx'
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
slides = [
    ('Universal Build Workflow', 'From Idea to Full Execution Readiness'),
    ('The map', '1 Capture → 2 Questions → 3 Blueprint → 4 Elements → 5 Readiness → 6 Execution mode → 7 Actual execution'),
    ('Questions create clarity', 'Use the 12 dimensions × 10 question forms matrix. Every unknown becomes an assumption or an owned open question.'),
    ('Build the clear picture', 'One-page Blueprint: problem, user, outcome, outputs, scope, constraints, success criteria, risks, assumptions.'),
    ('Make assembly possible', 'Decompose outputs into 1–3 day elements. Every element needs a decision, owner, definition of done, and interface contract.'),
    ('START HERE', 'Write the one-sentence idea, create the public source repository, and ask one independent reviewer to run the 60-second comprehension test.'),
]
for title, body in slides:
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    fill = slide.background.fill
    fill.solid(); fill.fore_color.rgb = RGBColor(248, 250, 252)
    tf = slide.shapes.add_textbox(Inches(.7), Inches(.6), Inches(12), Inches(1)).text_frame
    p = tf.paragraphs[0]; p.text = title; p.font.size = Pt(34); p.font.bold = True; p.font.name = 'Aptos'; p.font.color.rgb = RGBColor(15, 23, 42)
    bf = slide.shapes.add_textbox(Inches(.9), Inches(2.1), Inches(11.5), Inches(3.2)).text_frame
    p = bf.paragraphs[0]; p.text = body; p.font.size = Pt(25); p.font.name = 'Aptos'; p.font.color.rgb = RGBColor(30, 41, 59); p.alignment = PP_ALIGN.CENTER
prs.core_properties.title = 'Universal Build Workflow'
prs.core_properties.subject = 'From Idea to Full Execution Readiness'
prs.save(out)
print(out)
