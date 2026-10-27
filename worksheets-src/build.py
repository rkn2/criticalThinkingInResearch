"""Build the worksheet packets and the binder PDF.

Week 1-6 packets and the binder cover are assembled from the body fragments in
this folder (w01.html ... w06.html, cover.html), reusing the <style> block of
docs/week07-worksheets.html, which is hand-written and is the style source.

    python3 worksheets-src/build.py          # write docs/weekNN-worksheets.html + docs/binder-cover.html
    python3 worksheets-src/build.py --pdf    # also render every packet and join them into docs/worksheets-binder.pdf

--pdf needs Google Chrome and poppler (pdfunite).
"""
import re, sys, pathlib, subprocess, tempfile

here = pathlib.Path(__file__).resolve().parent
repo = here.parent
docs = repo / 'docs'
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

w7 = (docs / 'week07-worksheets.html').read_text()
style = re.search(r'<style>(.*?)</style>', w7, re.S).group(1)

extra = """
  .arc svg { width: 210px; height: auto; display: block; }
  .arc-line { stroke: var(--accent3); stroke-width: 2; }
  .arc-dot { fill: var(--surface); stroke: var(--accent3); stroke-width: 1.5; }
  .arc-dot.done { fill: var(--highlight); }
  .arc-dot.on { fill: var(--accent); stroke: var(--accent); }
  .arc-num { font-size: 9px; fill: var(--text-dim); font-family: 'Roboto', sans-serif; font-weight: 500; }
  .arc-num.on { fill: var(--surface); }
  .arc-lab { font-size: 9.5px; fill: var(--accent); font-family: 'Roboto', sans-serif; font-weight: 700; }

  .cards { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 10px 0; }
  .card { border: 1px solid var(--border); border-radius: 3px; padding: 8px 11px; font-size: 13.5px; }
  .card h3 { font-family: 'Roboto Slab', Georgia, serif; font-size: 14.5px; color: var(--accent); margin-bottom: 3px; }
  .card.wide { grid-column: 1 / span 2; }
  .vs { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 6px 0; }
  .vs > div { border: 1px solid var(--border); border-radius: 3px; padding: 7px 10px; font-size: 13px; }
  .vs .bad { border-left: 3px solid var(--warn); }
  .vs .good { border-left: 3px solid var(--accent); }
  .vs b.t { display: block; font-size: 11px; letter-spacing: 0.06em; text-transform: uppercase; color: var(--text-dim); font-weight: 500; }
  blockquote.q { border-left: 3px solid var(--accent3); padding: 4px 12px; margin: 10px 0; font-style: italic; font-size: 14px; }
  blockquote.q .src { display: block; font-style: normal; font-size: 12px; color: var(--text-dim); margin-top: 3px; }
  .three { counter-reset: t; list-style: none; margin: 4px 0; }
  .three li { counter-increment: t; padding: 2px 0 2px 22px; position: relative; font-size: 13.5px; }
  .three li::before { content: counter(t) "."; position: absolute; left: 0; font-weight: 700; color: var(--accent); }
  .draw { border: 1px solid var(--border); border-radius: 3px; margin: 6px 0 10px; }
  .draw svg { width: 100%; height: auto; display: block; }
  .draw-ell { fill: none; stroke: var(--accent); stroke-width: 1.5; }
  .draw-lab { font-size: 11px; fill: var(--text-dim); font-family: 'Roboto', sans-serif; }
  .circle-opts { margin: 4px 0 8px 12px; letter-spacing: 0.02em; }
  .circle-opts span { margin-right: 28px; }
  img.inline { max-width: 100%; border: 1px solid var(--border); }
  @media (max-width: 640px) {
    .cards, .vs { grid-template-columns: 1fr; }
    .card.wide { grid-column: auto; }
  }
"""

script = """<script>
// Course arc: where this week sits in Phase 1 and the Week 7 pitch.
document.querySelectorAll('.arc').forEach(function (el) {
  var wk = +el.dataset.week;
  var labels = ['A good PhD', 'Why care?', 'The question', 'The hypothesis', 'Scope', 'The story', 'The pitch'];
  var x0 = 12, dx = 31, svg = '<svg viewBox="0 0 210 50" aria-hidden="true">';
  svg += '<line class="arc-line" x1="' + x0 + '" y1="14" x2="' + (x0 + 6 * dx) + '" y2="14"/>';
  for (var i = 0; i < 7; i++) {
    var cls = (i + 1 === wk) ? ' on' : (i + 1 < wk ? ' done' : '');
    svg += '<circle class="arc-dot' + cls + '" cx="' + (x0 + i * dx) + '" cy="14" r="9"/>';
    svg += '<text class="arc-num' + (i + 1 === wk ? ' on' : '') + '" x="' + (x0 + i * dx) + '" y="17.2" text-anchor="middle">' + (i + 1) + '</text>';
  }
  if (wk) svg += '<text class="arc-lab" x="105" y="40" text-anchor="middle">Week ' + wk + ': ' + labels[wk - 1] + '</text>';
  el.innerHTML = svg + '</svg>';
});
</script>"""


def page(title, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;0,500;0,700;1,400&family=Roboto+Slab:wght@400;600;700&display=swap">
<style>{style}{extra}</style>
</head>
<body>
{body}
{script}
</body>
</html>
"""


targets = {'cover.html': 'binder-cover.html'}
targets.update({f.name: f'week{f.stem[1:]}-worksheets.html' for f in sorted(here.glob('w0*.html'))})
targets['s07.html'] = 'week07-session.html'  # Oct 22 run sheet + feedback card
targets['s08.html'] = 'week08-session.html'  # Oct 29 answering questions, student-run
for src, dst in targets.items():
    body = (here / src).read_text()
    title = re.search(r'<!-- title: (.*?) -->', body).group(1)
    (docs / dst).write_text(page(title, body))
    print('wrote', f'docs/{dst}')

if '--pdf' in sys.argv:
    order = ['binder-cover.html'] + [f'week{n:02d}-worksheets.html' for n in range(1, 8)]
    with tempfile.TemporaryDirectory() as tmp:
        pdfs = []
        for name in order:
            out = pathlib.Path(tmp) / name.replace('.html', '.pdf')
            subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
                            '--virtual-time-budget=5000', f'--print-to-pdf={out}',
                            (docs / name).as_uri()], check=True, capture_output=True)
            pdfs.append(str(out))
        subprocess.run(['pdfunite', *pdfs, str(docs / 'worksheets-binder.pdf')], check=True)
    print('wrote docs/worksheets-binder.pdf')
