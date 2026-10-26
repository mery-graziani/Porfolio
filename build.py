#!/usr/bin/env python3
"""Generates the static portfolio. Content comes from Mery's Notion."""
import html
import os

OUT = os.path.dirname(os.path.abspath(__file__))
CDN = "https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/"
Q = "/w=1920,quality=90,fit=scale-down"

RESUME = "https://drive.google.com/file/d/1acHskjJDS2ccZEZ6G4T8H_sam3_hk7ib/view?usp=sharing"
LINKEDIN = "https://www.linkedin.com/in/mariagraziani/"
EMAIL = "mailto:megraziani@gmail.com"

HERO = ("Hi! I’m Mery, a Product Designer who turns business goals into thoughtful, "
        "user-centered experiences — with a visual eye, a strategic mind, and a love for AI.")

ABOUT_LEAD = ("Blending 10+ years of visual design with UX expertise to create user-centered, "
              "business-driven solutions. I lead end-to-end design processes, innovate with AI, "
              "and thrive in cross-functional teams to build scalable, impactful experiences.")

PILLARS = [
    ("1. Strategic Thinking", "I design solutions that not only address user needs but also align with business objectives, supporting growth initiatives and laying the foundation for future product evolution."),
    ("2. Leadership & Collaboration", "I lead workshops with stakeholders and cross-functional teams to gather insights, align visions, and co-create solutions, fostering strong collaboration across disciplines."),
    ("3. Data-Driven Decision Making", "I leverage research insights and data analysis to identify opportunities, validate hypotheses, and drive design decisions based on evidence rather than assumptions."),
    ("4. User-Centered Design", "I prioritize user needs by creating intuitive, accessible, and consistent experiences, reusing familiar patterns and components to enhance usability and engagement."),
    ("5. Technical Fluency & Delivery Focus", "I collaborate closely with development teams and design system teams to ensure that design solutions are technically feasible, scalable, and efficiently delivered."),
    ("6. Research & Benchmarking Expertise", "I conduct audits and competitive benchmarking to uncover best practices and innovation opportunities, continually pushing for product and experience improvement."),
]

# Order = order on the live homepage
PROJECTS = [
    dict(slug="n26-case-study", name="N26 KYC", cover="cc430961-fffe-4070-ac95-636eb72e9f45/bottom_module_snap_fullsize_desktop_es",
         title="N26 KYC", summary=None, role="Lead Designer", employer=("N26", "https://n26.com/es-es"),
         platforms="App", areas="Research, Strategy, Design", phases=[], impact=None, stats=[], pending=True),
    dict(slug="n26-acquisition", name="N26 Acquire", cover="9382e1e2-3221-401f-8380-3ac814781bd2/crst19874_go-lp_7_mobile_754x533_es_es",
         title="N26 Account Opening optimization",
         summary="Streamlining the digital onboarding experience through continuous product discovery to eliminate conversion friction, accelerating user activation and driving Monthly Active User (MAU) growth.",
         role="Lead Designer", employer=("N26", "https://n26.com/es-es"), platforms="App", areas="Research, Strategy, Design",
         phases=[
             ("Understand", "In this phase, I established a continuous discovery framework to systematically uncover drop-off points within the account opening flow. By pairing quantitative funnel analysis with routine qualitative user testing, I mapped the friction gaps slowing down onboarding. This ongoing feedback loop allowed us to rapidly isolate usability issues and prioritize high-impact experience optimizations that aligned user needs with activation goals."),
             ("Explore", "In this phase, we moved rapidly from discovery to execution, prioritizing and exploring immediate fixes for critical onboarding blockers we uncovered."),
             ("Materialize", "In this phase, we moved into rapid implementation, working side-by-side with engineers to ensure all fixes met strict security and compliance standards without compromising the user experience. To validate the changes, we launched them via A/B testing while conducting live shadowing sessions to observe real-world user behavior."),
         ],
         impact=["All the initiatives implemented contributed to an increase in monthly active users."],
         stats=[("+4.0%", "MAUs (Monthly active users)"), ("+0.23 pp", "E2E global impact")]),
    dict(slug="mango-case-study", name="MANGO", cover="08758ee2-261c-438c-bb22-ec7ab88856b6/Mango",
         title="Elevating Mango PDP experience",
         summary="Redesigning Mango’s fashion e-commerce Product Detail Page (PDP) to enhance the shopping experience, address both user and business needs, and modernize the UI—while establishing a scalable foundation for long-term innovation across both web and app.",
         role="Lead Designer", employer=("Mango", "http://shop.mango.com"), platforms="iOS, AND, WEB", areas="Research, Strategy, Design",
         phases=[
             ("Understand", "In this phase, I focused on understanding the problem by gathering business requirements, analyzing user needs, identifying opportunities through a PDP audit, and collecting best practices via benchmarking. This process allowed us to define the key challenges and develop a strategic approach to address them."),
             ("Explore", "In this phase, I began addressing the identified problems by creating wireframes for potential solutions, iterating through multiple rounds with stakeholder validations. This process culminated in a final design proposal, outlining a long-term vision for the PDP across both web and app."),
             ("Materialize", "In this phase, we initially validated the final design through a usability test. After implementing user’s feedback, the project was then broken down into smaller initiatives, starting with an MVP. Each phase was progressively rolled out using continuous delivery, with A/B testing conducted along the way to gather valuable user insights. We are still in the process of developing many of these smaller initiatives."),
         ],
         impact=["Our analytics team has been closely monitoring the impact of the new design on our core metrics. With only two initiatives launched to date, the results indicate a positive shift, significantly enhancing the overall PDP experience."],
         stats=[("+42%", "Add to cart"), ("€ 4,899,927", "gross over 12 months")]),
    dict(slug="mango-outlet-case-study", name="MANGO OUTLET", cover="760f2df8-61cd-4279-9bb0-8ff4400f3715/Mango_outlet",
         title="Mango Outlet CRO micro-optimizations",
         summary="Redefining Mango Outlet’s digital strategy by designing tailored UX improvements to drive sales and address business-specific challenges—while maintaining technical and brand synergy with the main Mango e-commerce platform.",
         role="Lead Designer", employer=("Mango Outlet", "https://www.mangooutlet.com"), platforms="WEB", areas="Research, Strategy, Design",
         phases=[
             ("Understand", "In this phase, I focused on gaining a deep understanding of the business challenges and key differences between Mango and Mango Outlet. I analyzed user behavior through data and explored user needs and motivations via targeted surveys, which helped me define Mango Outlet’s user archetypes. I also conducted benchmarking to gather best practices."),
             ("Explore", "In this phase, we began crafting and prioritizing ideas in collaboration with the team and stakeholders to develop a strategic roadmap. Additionally, I laid the foundations for the design system to support the implementation of the initiatives."),
             ("Materialize", "In this phase, we validated our hypotheses by conducting A/B tests on the small CRO initiatives we crafted. This allowed us to gather valuable insights and iterate on the designs to further optimize the user experience."),
         ],
         impact=["All the initiatives implemented contributed to a net sales revenue of €5.5M, surpassing the initial target of €3.9M.",
                 "Several initiatives developed for the Outlet were successfully implemented on the main shop during sales and promotional periods.",
                 "By creating user archetypes, we gained valuable insights to guide the implementation of new initiatives to enhance their online experience.",
                 "As a team, we evolved and established efficient work dynamics, enabling smooth progress and ensuring continuous, high-quality delivery."],
         stats=[("€3.9 M", "Net sales target"), ("€5.5 M", "Net sales Revenue")]),
    dict(slug="vidal-case-study", name="VIDAL & VIDAL", cover="738d2fbd-0577-40f5-94e7-2d4a76df7eb0/Vidal",
         title="Vidal & Vidal e-commerce redesign",
         summary="Redesigning Vidal & Vidal’s e-commerce— a Spanish jewelry brand— within a limited budget to elevate the brand with a refreshed UI and enhance the user experience through a thorough audit and usability improvements.",
         role="Lead Designer", employer=("Vidal & Vidal", None), platforms="WEB", areas="Design",
         phases=[
             ("Understand", "In this phase, I applied my expertise in heuristic evaluation to identify usability issues and uncover opportunities for improvement, while gathering key stakeholder requirements to align the redesign with business and user needs."),
             ("Explore", "Afterwards, I tackled the identified challenges by redefining the information architecture, validating user flows, and developing wireframes for potential solutions. I iterated through several rounds of stakeholder feedback to refine the design. The process culminated in a final design proposal, ensuring alignment with both user needs and business objectives."),
             ("Materialize", "The implementation was executed in a single rollout, successfully achieving the goal of migrating their e-commerce platform from Magento to PrestaShop to reduce operational costs."),
         ],
         impact=["I don’t have data on the impact of the redesign on business performance and user experience, as I transitioned to a new role shortly after the e-commerce launch. However, I believe the results were positive, as we significantly improved usability with minimal resources while also equipping the business with new tools to enhance sales."],
         stats=[]),
    dict(slug="kibuc-case-study", name="KIBUC", cover="024a9d75-fc87-487b-a517-58f0dd82a37b/Kibuc",
         title="Kibuc e-commerce redesign",
         summary="Redesigning Kibuc’s e-commerce— a furniture design brand with over 40 stores in Spain— to enhance the user experience and drive higher conversion rates through strategic improvements.",
         role="Lead Designer", employer=("Kibuc", None), platforms="WEB", areas="Research, Design",
         phases=[
             ("Understand", "In this phase, I focused on gaining a deep understanding of both business and user challenges. I conducted an e-commerce audit and competitive analysis to identify market gaps while uncovering usability issues and user needs through guerrilla testing and card sorting. This research-driven approach informed the creation of a new design that effectively addressed these challenges."),
             ("Explore", "In this phase, I addressed the identified challenges by defining a new information architecture and creating wireframes for potential solutions across various sections of the website. I also developed a design system to ensure consistency and scalability. I iterated through multiple rounds of stakeholder feedback, refining the design, which ultimately led to a final proposal ready for testing and eventual implementation."),
             ("Materialize", "In this phase, we validated the information architecture through a tree test and the final e-commerce design with usability testing. Using the insights gathered from user feedback, we iterated on the designs to refine and prepare them for implementation, ensuring a simultaneous launch across the platform."),
         ],
         impact=["I don’t have data on the impact of the redesign on business performance and user experience, as I transitioned to a new role shortly after the e-commerce launch. However, usability testing confirmed that we enhanced user engagement and elevated the brand image, which we believe likely contributed to increased conversions."],
         stats=[]),
]

# Footer order from the live site
FOOTER_ORDER = ["mango-case-study", "mango-outlet-case-study", "vidal-case-study",
                "kibuc-case-study", "n26-acquisition", "n26-case-study"]
BY_SLUG = {p["slug"]: p for p in PROJECTS}
NAMES = {"mango-case-study": "Mango", "mango-outlet-case-study": "Mango Outlet",
         "vidal-case-study": "Vidal & Vidal", "kibuc-case-study": "Kibuc",
         "n26-acquisition": "N26 Acquire", "n26-case-study": "N26 KYC"}

e = html.escape


def cover_url(p):
    return CDN + p["cover"] + Q


def page(title, body, depth, current="", desc="Featured projects"):
    root = "../" * depth
    nav = lambda key, href, label: (
        f'<a href="{href}"' + (' aria-current="page"' if current == key else "") + f">{label}</a>")
    footer_projects = "".join(
        f'<li><a href="{root}{s}/">{e(NAMES[s])}</a></li>' for s in FOOTER_ORDER)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}styles.css">
</head>
<body>
<header class="site-header"><div class="wrap">
  <a class="brand" href="{root or './'}">Mery Graziani</a>
  <nav class="nav">
    {nav("projects", root or "./", "Projects")}
    <a href="{RESUME}" target="_blank" rel="noopener">Resume</a>
    {nav("about", root + "about/", "About")}
  </nav>
</div></header>
<main>
{body}
</main>
<footer class="site-footer"><div class="wrap">
  <div class="cols">
    <div><h4>Projects</h4><ul>{footer_projects}</ul></div>
    <div><h4>Experience</h4><ul>
      <li><a href="{root}about/">About</a></li>
      <li><a href="{RESUME}" target="_blank" rel="noopener">Resume</a></li></ul></div>
    <div><h4>Contact</h4><ul>
      <li><a href="{LINKEDIN}" target="_blank" rel="noopener">Linkedin</a></li>
      <li><a href="{EMAIL}">Email</a></li></ul></div>
  </div>
  <p class="copy">© 2026 Mery Graziani</p>
</div></footer>
</body>
</html>
"""


def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


# Home
cards = "".join(
    f'<a class="card" href="{p["slug"]}/"><div class="thumb"><img src="{cover_url(p)}" alt="{e(p["name"])}" loading="lazy"></div><h3>{e(p["name"])}</h3></a>'
    for p in PROJECTS)
home = f"""<section class="wrap hero"><h1>{e(HERO)}</h1></section>
<section class="wrap"><p class="section-label">Featured projects</p><div class="grid">{cards}</div></section>"""
write("index.html", page("Mery Graziani", home, 0, "projects"))

# About
pillars = "".join(f"<div><h3>{e(t)}</h3><p>{e(d)}</p></div>" for t, d in PILLARS)
about = f"""<section class="wrap about"><h1>About me</h1><p class="lead">{e(ABOUT_LEAD)}</p></section>
<section class="wrap"><div class="pillars">{pillars}</div></section>"""
write("about/index.html", page("About — Mery Graziani", about, 1, "about", "About Mery Graziani"))

# Case studies (prev/next follow the live-site footer order)
for i, p in enumerate(PROJECTS):
    emp_name, emp_url = p["employer"]
    emp = f'<a href="{emp_url}" target="_blank" rel="noopener">{e(emp_name)}</a>' if emp_url else e(emp_name)
    meta = (f'<dl class="meta"><div><dt>Role</dt><dd>{e(p["role"])}</dd></div>'
            f'<div><dt>Employer</dt><dd>{emp}</dd></div>'
            f'<div><dt>Platforms</dt><dd>{e(p["platforms"])}</dd></div>'
            f'<div><dt>Areas</dt><dd>{e(p["areas"])}</dd></div></dl>')
    body = f'<section class="wrap case-head"><h1>{e(p["title"])}</h1>'
    if p["summary"]:
        body += f'<p class="summary">{e(p["summary"])}</p>'
    body += meta + f'<div class="cover"><img src="{cover_url(p)}" alt="{e(p["name"])}"></div></section>'
    if p.get("pending"):
        body += '<section class="wrap"><p class="note">Case study coming soon.</p></section>'
    else:
        body += '<section class="wrap">'
        for n, (name, text) in enumerate(p["phases"], 1):
            body += f'<div class="phase"><div class="num">0{n}</div><div><h2>{name}</h2><p>{e(text)}</p></div></div>'
        paras = "".join(f"<li>{e(t)}</li>" for t in p["impact"]) if len(p["impact"]) > 1 \
            else f'<p>{e(p["impact"][0])}</p>'
        if len(p["impact"]) > 1:
            paras = f"<ul>{paras}</ul>"
        stats = "".join(f'<div class="stat"><b>{e(v)}</b><span>{e(l)}</span></div>' for v, l in p["stats"])
        body += f'<div class="impact"><h2>Impact</h2>{paras}<div class="stats">{stats}</div></div></section>'
    order = FOOTER_ORDER  # navigate in the same sequence as the footer
    idx = order.index(p["slug"])
    prev_s = order[idx - 1] if idx > 0 else None
    next_s = order[idx + 1] if idx < len(order) - 1 else None
    prev_a = f'<a href="../{prev_s}/">← {e(NAMES[prev_s])}</a>' if prev_s else "<span></span>"
    next_a = f'<a href="../{next_s}/">{e(NAMES[next_s])} →</a>' if next_s else "<span></span>"
    body += f'<div class="wrap pager">{prev_a}{next_a}</div>'
    write(f'{p["slug"]}/index.html',
          page(f'{p["name"]} — Mery Graziani', body, 1, "projects", p["summary"] or "Case study"))

print("built", len(PROJECTS) + 2, "pages")
