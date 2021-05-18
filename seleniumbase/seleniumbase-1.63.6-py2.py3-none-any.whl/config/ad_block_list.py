"""
For use with SeleniumBase ad_block functionality.

Usage:
    On the command line:
    "pytest SOME_TEST.py --ad_block"

    From inside a test:
    self.ad_block()

If using the command line version, the ad_block functionality gets
activated after "self.wait_for_ready_state_complete()" is called,
which is always run after page loads, unless changed in "settings.py".
Using ad_block will slow down test runs a little. (Use only if necessary.)

Format: A CSS Selector that's ready for JavaScript's querySelectorAll()
"""

AD_BLOCK_LIST = [
    '[aria-label="Ads"]',
    '[src*="adservice."]',
    '[src*="adclick"]',
    '[src*="doubleclick"]',
    '[src*="snigelweb.com"]',
    '[src*="tagservices.com"]',
    '[src*="adsby"]',
    '[src*="adroll.com"]',
    '[src*="pagead"]',
    '[src*="3lift"]',
    '[src*="smartads."]',
    '[src*="ad_nexus"]',
    '[src*="/ads/"]',
    '[src*="moatads.com"]',
    '[src*="adsystem"]',
    '[src*="connectad"]',
    '[src*="/adservice."]',
    '[src*="syndication.com"]',
    '[src*="/ads."]',
    '[src*="lijit"]',
    '[src*="pagead"]',
    '[src*="adnxs.com"]',
    '[src*="onetag-sys.com"]',
    '[src*="indexww.com"]',
    '[src*="3lift.com"]',
    '[src*="rubiconproject.com"]',
    '[src*="brealtime.com"]',
    '[src*="33across.com"]',
    '[src*="adsrvr"]',
    '[type="data-doubleclick"]',
    "iframe[data-google-container-id]",
    'iframe[src*="doubleclick"]',
    'iframe[src*="/AdServer/"]',
    'iframe[src*="openx.net"]',
    'iframe[onload*="doWithAds"]',
    'iframe[id*="_ads_frame"]',
    'iframe[style="height:0px;width:0px;display:none;"]',
    '[aria-label="Ad"]',
    '[class*="sponsored-content"]',
    '[class*="adsbygoogle"]',
    '[class^="adroll"]',
    '[data-ad-details*="Advertisement"]',
    '[data-native_ad*="placement"]',
    '[data-provider="dianomi"]',
    '[data-type="ad"]',
    '[data-track-event-label*="-taboola-"]',
    '[data-ad-feedback-beacon*="AD_"]',
    "[data-ad-feedback-beacon]",
    '[data-dcm-click-tracker*="/adclick."]',
    "[data-google-av-adk]",
    "[data-google-query-id]",
    '[data-ylk*="sponsored_cluster"]',
    '[data-google-av-cxn*="pagead"]',
    "[data-ad-client]",
    "[data-ad-slot]",
    '[href*="doubleclick"]',
    '[href*="amazon-adsystem"]',
    '[alt="Advertisement"]',
    '[id*="-ad-"]',
    '[id*="_ads_"]',
    '[id*="AdFrame"]',
    '[id*="carbonads"]',
    '[id^="ad-"]',
    '[id^="my-ads"]',
    '[id^="outbrain_widget"]',
    '[id^="taboola-"]',
    '[id^="google_ads_frame"]',
    '[id^="google_ads_iframe"]',
    '[id="tryitLeaderboard"]',
    '[id="dianomiRightRail"]',
    '[allow*="advertising.com"]',
    "ins.adsby",
    "li.strm-ad-clusters",
    "li.js-stream-ad",
    "div.after_ad",
    "div.ad-container",
    "div.ad_module",
    "div.ad-subnav-container",
    "div.ad-wrapper",
    "div.adroll-block",
    "div.data-ad-container",
    "div.GoogleActiveViewElement",
    "div.l-ad",
    "div.right-ad",
    "div.wx-adWrapper",
    'div.image > a > img[src*="HomepageAd"]',
    'img[src*="HomepageAd"]',
    "img.img_ad",
    'link[href*="/adservice."]',
    "section.dianomi-ad",
]
