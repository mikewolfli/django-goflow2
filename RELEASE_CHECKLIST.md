# Release Checklist

## Pre-flight
- [ ] Confirm working tree clean or changes accounted for
- [ ] Verify Python and Django versions in README/INSTALL
- [ ] Update version number in setup.py (if releasing)

## Quality
- [x] Run system checks:
  - sampleproject: python sampleproject/manage.py check
  - leavedemo: python leavedemo/manage.py check
- [x] Run tests:
  - sampleproject: python sampleproject/manage.py test sampleapp
  - leavedemo: python leavedemo/manage.py test leavedemo.leave
- [x] Re-run tests after API ownership hardening
- [x] Verify migrations are up to date
- [x] Apply migrations:
  - sampleproject: python sampleproject/manage.py migrate
  - leavedemo: python leavedemo/manage.py migrate

## Docs
- [x] Build Sphinx docs: python -m sphinx -b html -d docs/build/doctrees docs/source docs/build/html
- [x] Verify REST API docs and schema tables
- [ ] Confirm install steps still match current settings

## Release
- [ ] Tag release in git
- [ ] Build package: python -m build
- [ ] Publish package (if applicable)
- [ ] Draft release notes and include key changes
