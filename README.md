# Kijiji Bot

<!-- [START badges] -->
[![pypi](https://img.shields.io/pypi/v/kijiji-bot)](https://pypi.org/project/kijiji-bot)
[![pyversions](https://img.shields.io/pypi/pyversions/kijiji-bot)](#)
[![license](https://img.shields.io/github/license/george-lim/kijiji-bot)](https://github.com/george-lim/kijiji-bot/blob/master/LICENSE)
<!-- [END badges] -->

> Kijiji Bot is a Python library that allows Kijiji ads to be reposted programmatically. It mirrors [Kijiji-Repost-Headless](https://github.com/ArthurG/Kijiji-Repost-Headless) as a PyPI package, so ads can be reposted from other Python libraries.

<!-- [START features] -->
## Features

### API Session Cookie Persistence

Logging into Kijiji Bot will return cookies encoded as a Base64 string. When reposting ads, these cookies are used to authenticate the user in a new API session. You may choose to persist these cookies for reuse in subsequent `repost_ads` calls.

### Ad Scanning + Reposting Multiple Ads

This package allows users to specify a folder to look for ads, and automatically repost all ads in the folder at once. The following is a valid folder structure for ads:

```
ads
├── test_ad_1
│   ├── item.yaml
│   └── 1.JPG
└── test_ad_2
    ├── item.yaml
    └── 1.JPG
```

### Duplicate Ad Detection

Kijiji has a system to automatically delete newly posted ads if they appear to be duplicate ads. This package will wait for thirty seconds after posting an ad to detect duplicate ad removal.

### Alternate Ad Support

To combat duplicate ad removal, this package allows users to specify alternate details for each ad, and use the `is_using_alternate_ad` flag to repost ads using alternate details. You may use this flag as a fallback when duplicate ad removal is detected, or just cycle between using primary / alternate ad details when reposting.

Add the following four fields to your `item.yaml` file (created by `Kijiji-Repost-Headless`) to specify alternate ad details:

```yaml
postAdForm.alternateTitle: Alternate ad title
postAdForm.alternateCity: North York
postAdForm.alternateAddressCity: North York
postAdForm.alternateDescription: Alternate ad description
```
<!-- [END features] -->

<!-- [START getstarted] -->
## Getting Started

### Installation

To use Kijiji Bot in your project, add `kijiji-bot` to your project's `requirements.txt`.

### Usage

An [example project](https://github.com/george-lim/kijiji-bot/blob/master/examples/repost_ads) is provided to demonstrate how Kijiji Bot can be used to repost all ads in a specific folder.

Execute script on the command line:
```bash
cd examples/repost_ads
pip install -r requirements.txt
python3 .
```
<!-- [END getstarted] -->
