# Where to look

The `find-roles` skill checks every **enabled** source on each run, then does a broad web search. Enable,
disable or add rows freely.

**How** tells Claude how to read each site:
- `fetch`: public listing pages it can read directly.
- `search`: it uses web search restricted to the site (e.g. `site:linkedin.com/jobs …`), because the site
  blocks direct reading or needs a login.
- `browser`: needs your login. Only used in live sessions when you're there to sign in, and skipped in
  scheduled runs.

## Job boards (UK defaults)
| On | Source | URL | Good for | How |
|---|---|---|---|---|
| ✅ | Bright Network | https://www.brightnetwork.co.uk/graduate-jobs/ | Grad schemes, internships | search |
| ✅ | Prospects | https://www.prospects.ac.uk/graduate-jobs | Grad jobs, all sectors | fetch |
| ✅ | TARGETjobs | https://targetjobs.co.uk/ | Grad schemes, internships | fetch |
| ✅ | Gradcracker | https://www.gradcracker.com/ | STEM grad jobs, internships, placements | search |
| ✅ | RateMyPlacement | https://www.ratemyplacement.co.uk/ | Placements, internships | fetch |
| ✅ | Milkround | https://www.milkround.com/ | Grad jobs, internships | fetch |
| ✅ | Indeed UK | https://uk.indeed.com/ | Broad coverage, smaller employers | search |
| ✅ | LinkedIn Jobs | https://www.linkedin.com/jobs/ | Broad coverage, startups | search |
| ⬜ | Welcome to the Jungle (Otta) | https://www.welcometothejungle.com/ | Startups and scale-ups | search |
| ⬜ | Civil Service Jobs | https://www.civilservicejobs.service.gov.uk/ | Public sector, Fast Stream | fetch |
| ⬜ | Your university careers portal | <URL> | Uni-exclusive roles, local employers | browser |

## Target employer careers pages
Checked directly on every run. Add the companies from your brief.
| On | Employer | Careers / early-careers URL |
|---|---|---|
| ⬜ | <Company> | <URL> |

## Broad search
Always on. On each run Claude also searches the open web using the job titles and sectors in `BRIEF.md`
(e.g. "graduate machine learning engineer 2027 UK"), to catch roles on sites not listed here.
