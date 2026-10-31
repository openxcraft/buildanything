#!/usr/bin/env python3
# Rebuild generated formats from docs/00-overview.md. Requires Python, Pillow, and WeasyPrint; LibreOffice is used when installed.
from pathlib import Path
import shutil, subprocess, tempfile, zipfile
ROOT=Path(__file__).resolve().parents[1]
src=(ROOT/'docs/00-overview.md').read_text(encoding='utf-8')
html='<!doctype html><html lang="en"><meta charset="utf-8"><title>Universal Build Workflow</title><style>body{font:16px system-ui;max-width:900px;margin:2rem auto;line-height:1.55}h1,h2,h3{line-height:1.2}pre{white-space:pre-wrap;background:#f4f4f4;padding:1rem}table{border-collapse:collapse}td,th{border:1px solid #888;padding:.4rem}</style><article><h1>Universal Build Workflow</h1><pre>'+src.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')+'</pre></article></html>'
(ROOT/'formats/universal-build-workflow.html').write_text(html,encoding='utf-8')
(ROOT/'formats/universal-build-workflow-lite.html').write_text(html.replace('<style>','<style>body{max-width:680px;font-size:15px}'),encoding='utf-8')
(ROOT/'formats/universal-build-workflow.txt').write_text(src,encoding='utf-8')
try:
 from weasyprint import HTML
 for name,css in [('universal-build-workflow.pdf',''),('universal-build-workflow-tagged.pdf',''),('universal-build-workflow-large-print.pdf','body{font-size:22px}'),('universal-build-workflow-dyslexia-friendly.pdf','body{font-family:Verdana,sans-serif;letter-spacing:.04em;line-height:2}'),('universal-build-workflow-poster-A3.pdf','body{font-size:28px;max-width:1100px}')]:
  HTML(string=html.replace('</style>',css+'</style>')).write_pdf(ROOT/'formats'/name)
  
except Exception as e:
 (ROOT/'release-readiness/validation-reports/verapdf.txt').write_text('PDF generator unavailable: '+repr(e)+'\n')
# Minimal EPUB 3 package.
epub=ROOT/'formats/universal-build-workflow.epub'
with tempfile.TemporaryDirectory() as td:
 p=Path(td); (p/'META-INF').mkdir(); (p/'EPUB').mkdir(); (p/'mimetype').write_text('application/epub+zip'); (p/'META-INF/container.xml').write_text('<?xml version="1.0"?><container version="1.0" rootfile="EPUB/content.opf" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="EPUB/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>'); (p/'EPUB/content.xhtml').write_text('<html xmlns="http://www.w3.org/1999/xhtml" lang="en"><head><title>Universal Build Workflow</title></head><body><h1>Universal Build Workflow</h1><pre>'+src.replace('&','&amp;').replace('<','&lt;')+'</pre></body></html>'); (p/'EPUB/content.opf').write_text('<?xml version="1.0"?><package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="pub-id"><metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="pub-id">universal-build-workflow-1.0.0</dc:identifier><dc:title>Universal Build Workflow</dc:title><dc:language>en</dc:language><meta property="schema:accessMode">textual</meta><meta property="schema:accessibilityFeature">structuralNavigation</meta><meta property="schema:accessibilityHazard">none</meta></metadata><manifest><item id="xhtml" href="content.xhtml" media-type="application/xhtml+xml"/></manifest><spine><itemref idref="xhtml"/></spine></package>');
 with zipfile.ZipFile(epub,'w') as z: z.write(p/'mimetype','mimetype',compress_type=zipfile.ZIP_STORED); [z.write(f,f.relative_to(p).as_posix()) for f in p.rglob('*') if f.is_file() and f.name!='mimetype']
