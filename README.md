# Universal Build Workflow — v1.0.0

This release contains the complete English workflow, copy-paste master prompt, guarantees table, templates, machine-readable data, accessibility material, automation, and generated distribution formats.

## Canonical identity

- Title: Universal Build Workflow: From Idea to Full Execution Readiness
- Slug: `universal-build-workflow`
- Version: `1.0.0`
- Source language: English (`en`)
- Initial locales: `en`, `ar`, `es`, `fr`
- Canonical URL: `https://example.org/universal-build-workflow`
- URL status: **[ASSUMPTION] placeholder supplied by the release prompt; replace before public launch.**
- Text license: CC BY 4.0
- Code/templates license: MIT
- Data/schemas license: CC0 1.0
- Reader cost: FREE; no paywall, registration wall, email gate, or telemetry.

## Contents

`docs/` contains the workflow. `master-prompt/` contains the publishing prompt. `templates/` contains reusable forms. `formats/` contains generated reading formats. `data/` contains machine-readable representations. `i18n/` contains locale files. `automation/` contains reproducible build definitions. `release-readiness/` contains publication gates and records.

## Build

Run `bash automation/build.sh` from the package root. The script rebuilds the generated HTML, PDF, EPUB, office derivatives, poster, image assets, checksums, and manifest. Run `bash automation/make-slides.sh` to rebuild the editable six-slide PPTX. It uses `SOURCE_DATE_EPOCH` when supplied and records tool versions.

## License and attribution

Documentation is CC BY 4.0. Code and scripts are MIT. Data and schemas are CC0 1.0. Third-party tools remain under their own licenses. See `NOTICE`, `LICENSE`, `LICENSE-CODE`, and `LICENSE-DATA`.

## Accessibility

The package targets WCAG 2.2 AA for HTML and provides plain text, offline, large-print, dyslexia-friendly, RTL-ready, and braille-ready text alternatives. See `accessibility/accessibility-statement.md`. Automated checks are not a substitute for human testing.

## Immediate release condition

Before publication, replace the placeholder canonical URL, complete rights review, assign two maintainers, test the four locale files with fluent reviewers, and record the binary gates in `release-readiness/`. The local package is complete; public release still requires those external approvals and identifiers.
