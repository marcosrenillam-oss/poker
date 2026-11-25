#!/usr/bin/env python3
"""Wraps index.html (the artifact source) into app/index.html, a full page
that can be installed on a phone's home screen (manifest, icons, offline)."""
from pathlib import Path
root = Path(__file__).resolve().parent.parent
body = (root / "index.html").read_text(encoding="utf-8")
head = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="tapete-app" content="1">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Tapete">
<meta name="format-detection" content="telephone=no">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icon-180.png">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font-size:14px}img{max-width:100%}[hidden]{display:none!important}</style>
"""
# Move the page's own <title>/<meta>/<link>/<style> into <head>; the rest goes in <body>.
split = body.index('<div id="root">')
out = head + body[:split] + "</head>\n<body>\n" + body[split:] + "\n</body>\n</html>\n"
(root / "app" / "index.html").write_text(out, encoding="utf-8")
print("app/index.html written")
