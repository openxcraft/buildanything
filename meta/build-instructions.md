# Build instructions

1. Install Python 3 and the packages used by the local runtime.
2. Set `SOURCE_DATE_EPOCH` to a release timestamp.
3. Run `bash automation/build.sh`.
4. Run Markdown, link, axe, EPUBCheck/Ace, veraPDF, and manual accessibility checks.
5. Review `release-readiness/` and replace all release-blocking `[ASSUMPTION]` entries.
6. Run `python3 automation/update_manifest.py`, then create the ZIP with `zip -X -r universal-build-workflow-v1.0.0.zip universal-build-workflow-v1.0.0`.
