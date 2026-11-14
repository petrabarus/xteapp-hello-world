# xteapp-hello-world

Hello World app for Xteink InkApps (XTOS Licorice mini-app host).

* `app/` - the app (`manifest.json`, `index.lua`)
* `build.py` - packs the app into `dist/helloworld.xteapp` (needs `pip install -r requirements.txt`)
* `tools/vendor/` - the packer, vendored from
  [touch-licorice-apps](https://github.com/omer-faruq-xteink/touch-licorice-apps) and
  [x4pro-emu](https://github.com/kycube/x4pro-emu) (both MIT, licenses included)

The package format is the upstream `.xtapp` container; it is written with the `.xteapp` extension.
Rename it to `.xtapp` if your device's installer insists on that.

## CI

1. Pull requests: StyLua (default style) for Lua and flake8 (PEP 8) for Python.
2. Push to `main`: builds `helloworld.xteapp` and uploads it as a workflow artifact.
