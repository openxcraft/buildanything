# Automation blueprint

Trigger: a new release tag or approved issue.
Action 1: run the reproducible build on CI.
Action 2: upload the release archive to the approved public release host.
Action 3: publish an opt-in release note.
Human gate: a maintainer verifies checksums, rights, accessibility, and locale status before announcement.
