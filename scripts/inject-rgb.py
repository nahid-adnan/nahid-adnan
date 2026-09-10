import re, sys

RGB_CSS = """
        @keyframes gpsc-rgb{0%{filter:hue-rotate(0deg) saturate(1)}50%{filter:hue-rotate(180deg) saturate(1.7)}100%{filter:hue-rotate(360deg) saturate(1)}}
        .gpsc-rgb-sync{animation:gpsc-rgb 5s linear infinite}
        @media (prefers-reduced-motion:reduce){.gpsc-rgb-sync{animation:none!important}}
"""

def inject(svg):
    # 1. add keyframes to the existing <style> block
    if '@keyframes gpsc-rgb' in svg:
        return svg
    svg = svg.replace('<style>', '<style>' + RGB_CSS, 1)

    # 2. find the background group (first isolate group, holds only the bg rect)
    m = re.search(r"(<g style='isolation: isolate'>\s*<rect [^>]*fill='#[0-9A-Fa-f]{6}'[^>]*/>\s*</g>)", svg)
    if not m:
        raise SystemExit("FAIL: background group not found")
    end_bg = m.end()

    # 3. locate the final </g> that closes the clip-path wrapper
    last_g = svg.rfind('</g>')
    if last_g == -1 or last_g < end_bg:
        raise SystemExit("FAIL: closing </g> not found")

    # 4. wrap everything between them
    return (svg[:end_bg]
            + "\n<g class='gpsc-rgb-sync'>"
            + svg[end_bg:last_g]
            + "</g>\n"
            + svg[last_g:])

src = open(sys.argv[1]).read()
out = inject(src)
open(sys.argv[2], 'w').write(out)
print("OK ->", sys.argv[2])
