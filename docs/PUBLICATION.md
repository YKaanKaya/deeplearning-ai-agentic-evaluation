# Publication and validation record

Date: 14 November 2026. This record covers documentation publication and portfolio implementation, not fresh execution of the hosted labs.

- Course repository: [YKaanKaya/deeplearning-ai-agentic-evaluation](https://github.com/YKaanKaya/deeplearning-ai-agentic-evaluation), initialized in the intended Windows course folder. The folder had no previous Git repository or history.
- Portfolio repository: [YKaanKaya/yasarkaankaya](https://github.com/YKaanKaya/yasarkaankaya), showcase commit `8436b2350ad0963459cf2fe4bdde9d18d04d13f1`. Work used an isolated checkout under `.publication/portfolio-source`; the original `C:\Users\kaank\portfolio-check` and its unrelated untracked files were preserved.
- Showcase: [Evaluating and Improving Agentic Applications](https://yasarkaankaya.com/showcase/agentic-evaluation/).
- Deployment: existing GitHub `main` to Netlify site `5a59387a-2915-4e31-b9a5-2732b273a285`; no site migration or manual production upload.

## Checks performed

| Check | Result |
| --- | --- |
| Original artifact preservation | All 34 source hashes match; 6 notebooks, 22 standalone GIFs, 5 PDFs, 1 ZIP |
| Publication scan | No detected secret patterns, restricted raw files or broken relative Markdown links; all 140 relative links resolve within public Git |
| Synthetic comparison example | Python 3.11.9; identity, reordered-case, duplicate-case and missing-case checks pass |
| Portfolio TypeScript | `tsc --noEmit` passes |
| Changed-file ESLint | Passes |
| Full-site lint | Fails on existing unrelated JSX apostrophe, `any` and `prefer-const` errors; those files were preserved |
| Production build | Passes; Next.js 15.5.21, 23 static pages; new route about 2.96 kB / 111 kB first-load JS |
| Desktop and mobile | Visually inspected at 1440 px and 390 px; no article overflow; anchors, module disclosure, source links and homepage integration checked |
| Gallery | No GIF requests before explicit play; one active animation; switching/stopping restores stills |
| Reduced motion and keyboard access | Reduced-motion mode disables smooth scrolling/transitions; native buttons/details and visible focus states; dark-panel focus contrast corrected |
| Certificate | Public browser page confirms Kaan KAYA, the course title and completion on November 14, 2026 |

Local portfolio build used Node 24.13.1 and the existing dependency installation through an ignored junction. Netlify is configured for Node 20, so local and hosted runtime versions differ. Existing build configuration skips lint. The push also reported existing Dependabot alerts; dependencies were not changed by this content publication.

Assignment scores 30/30 and 10/10 remain learner-reported. No grade screen was inspected. Course helper trees and dependency/data snapshots remain missing; this repository does not claim the hosted labs run locally.

## Live deployment verified

Netlify deploy `6af8169c5a50ee2762f8b36d` reached `ready`, publishing portfolio commit `8436b2350ad0963459cf2fe4bdde9d18d04d13f1` on 14 November 2026 at 09:08 Luxembourg time. The deploy reports no error.

The production showcase returned HTTP 200 with the intended title, headline and canonical URL. Live checks at 1440 px and 390 px found no content overflow or missing in-page anchors. All four poster images have alt text; zero GIF requests occurred before explicit play, switching kept one animation active and Stop restored the stills. Reduced-motion mode used `scroll-behavior: auto` and displayed no GIFs. No failed resource response was observed during these checks.

The production homepage includes the showcase link, the new certificate in both learning lists, nine public projects and nine credentials. Sitemap and robots return HTTP 200; the sitemap includes the new route. The public GitHub results page and independent notebook links both return HTTP 200. The certificate's recipient/course/date were verified separately in the browser.
