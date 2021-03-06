
#####################################################################################
#                   How to use this module in implmentation                         #
#####################################################################################
#                                                                                   #
# from common_apk_module import * # Used for easily finding app ID's                #
#                                                                                   #
# app_name_input = input("App Name: ")                                              #
# app_id_output = return_app_id(app_name_input)                                     #
# print("App Name input: " + app_name_input + " | App ID Output: " + app_id_output) #
#                                                                                   #
##################################################################################### 
#                             Helpful Links                                         #
#####################################################################################
# - https://apkpure.com/                                                            #
# - https://learn.apptentive.com/knowledge-base/finding-your-app-store-id/          #
# - https://play.google.com/store/apps                                              #
##################################################################################### 

def return_app_id(app_name_query_search_term):
    common_apk_app_id_dictionary = {"App Name": "App ID", 
                                    "Adobe Acrobat Reader":"com.adobe.reader",
                                    "Airbnb":"com.airbnb.android",
                                    "Akinator":"com.digidust.elokence.akinator.freemium",
                                    "Akinator VIP":"com.digidust.elokence.akinator.paid",
                                    "Amazon":"com.amazon.mShop.android.shopping",
                                    "Amazon Music":"com.amazon.mp3",
                                    "Amazon Prime Video":"com.amazon.avod.thirdpartyclient",
                                    "American Airlines":"com.aa.android",
                                    "Among Us":"com.innersloth.spacemafia",
                                    "Android Accessibility Suite":"com.google.android.marvin.talkback",
                                    "Android System WebView":"com.google.android.webview",
                                    "Angry Birds 2":"com.rovio.baba",
                                    "ANT Radio Service":"com.dsi.ant.service.socket",
                                    "ANT+ Plugins Service":"com.dsi.ant.plugins.antplus",
                                    "Bank of America":"com.infonow.bofa",
                                    "Beautiful Widgets Pro":"com.levelup.beautifulwidgets",
                                    "BitLife":"com.candywriter.bitlife",
                                    "Bloons TD 6":"com.ninjakiwi.bloonstd6",
                                    "Bridge Constructor":"com.headupgames.bridgeconstructor",
                                    "Buff Knight Advanced - Retro RPG Runner":"com.buffstudio.bka",
                                    "Bumble":"com.bumble.app",
                                    "Camera ZOOM FX Premium":"slide.cameraZoom",
                                    "CampusGroups":"com.novalsys.CampusGroups",
                                    "Candy Crush Saga":"com.king.candycrushsaga",
                                    "Canvas Student":"com.instructure.candroid",
                                    "Canvas Teacher":"com.instructure.teacher",
                                    "Cash App":"com.squareup.cash",
                                    "Chase":"com.chase.sig.android",
                                    "Clash of Clans":"com.supercell.clashofclans",
                                    "Clubhouse":"io.clubhouse.clubhouse",
                                    "Coin Princess VIP: Retro RPG Quest":"com.norizabob.coinprincessvip",
                                    "Coinbase":"com.coinbase.pro",
                                    "Construction Simulator 3":"com.astragon.cs3",
                                    "Craigslist":"org.craigslist.CraigslistMobile",
                                    "Crunchyroll":"com.crunchyroll.crunchyroid",
                                    "Crypto.com":"co.mona.android",
                                    "Cut the Rope GOLD":"com.zeptolab.ctr.paid",
                                    "DailyArt":"com.moiseum.dailyart2",
                                    "Device Care":"com.samsung.android.lool",
                                    "Discord":"com.discord",
                                    "Discovery+":"com.discovery.discoveryplus.mobile",
                                    "Disney+":"com.disney.disneyplus",
                                    "DoorDash":"com.dd.doordash",
                                    "DraStic DS Emulator":"com.dsemu.drastic",
                                    "Draw Something":"com.omgpop.dstpaid",
                                    "Dropbox":"com.dropbox.android",
                                    "Dungeon Defense":"com.GameCoaster.ProtectDungeon",
                                    "Duo Mobile":"com.duosecurity.duomobile",
                                    "Duolingo":"com.duolingo",
                                    "Dutch Bros":"com.dutchbros.loyalty",
                                    "Earn to Die":"com.notdoppler.earntodie",
                                    "Ebay":"com.ebay.mobile",
                                    "Empire Warriors Premium: Tactical TD Game":"com.zitga.empire.warriors.td.tower.defense",
                                    "EoSFitness":"com.netpulse.mobile.eosfitness",
                                    "Evil Apples":"com.evilapples.app",
                                    "Facebook":"com.facebook.katana",
                                    "Facebook Lite":"com.facebook.lite",
                                    "Firefox":"org.mozilla.firefox",
                                    "Fitbit":"com.fitbit.FitbitMobile",
                                    "FitNotes":"com.github.jamesgay.fitnotes",
                                    "Five Nights at Freddy's":"com.scottgames.fivenightsatfreddys",
                                    "Flappy Bird":"com.ShivanshTiwari.FlappyBird",
                                    "Flipboard":"flipboard.app",
                                    "Flipboard Briefing":"flipboard.boxer.app",
                                    "Fruit Ninja Classic":"com.halfbrick.fruitninja",
                                    "Gboard":"com.google.android.inputmethod.latin",
                                    "Geometry Dash":"com.robtopx.geometryjump",
                                    "Gmail":"com.google.android.gm",
                                    "Goat Simulator":"com.coffeestainstudios.goatsimulator",
                                    "Google":"com.google.android.googlequicksearchbox",
                                    "Google Calendar":"com.google.android.calendar",
                                    "Google Chrome":"com.android.chrome",
                                    "Google Classroom":"com.google.android.apps.classroom",
                                    "Google Docs":"com.google.android.apps.docs.editors.docs",
                                    "Google Drive":"com.google.android.apps.docs",
                                    "Google Duo":"com.google.android.apps.tachyon",
                                    "Google Hangouts":"com.google.android.talk",
                                    "Google Home":"com.google.android.apps.chromecast.app",
                                    "Google Maps":"com.google.android.apps.maps",
                                    "Google Meet":"com.google.android.apps.meetings",
                                    "Google News":"com.google.android.apps.magazines",
                                    "Google Pay":"com.google.android.apps.nbu.paisa.user",
                                    "Google Photos":"com.google.android.apps.photos",
                                    "Google Play Books":"com.google.android.apps.books",
                                    "Google Play Games":"com.google.android.play.games",
                                    "Google Play Music":"com.google.android.music",
                                    "Google Sheets":"com.google.android.apps.docs.editors.sheets",
                                    "Google Slides":"com.google.android.apps.docs.editors.slides",
                                    "Google Street View":"com.google.android.street",
                                    "Google Text-to-Speech":"com.google.android.tts",
                                    "Google Translate":"com.google.android.apps.translate",
                                    "Google TV":"com.google.android.videos",
                                    "GoPro":"com.gopro.smarty",
                                    "Grand Theft Auto III":"com.rockstargames.gta3",
                                    "Grand Theft Auto: San Andreas":"com.rockstargames.gtasa",
                                    "Grand Theft Auto: Vice City":"com.rockstargames.gtavc",
                                    "Grindr":"com.grindrapp.android",
                                    "GroupMe":"com.linkedin.android",
                                    "GrubHub":"com.grubhub.android",
                                    "Happy Wheels":"com.fancyforce.happywheels",
                                    "HBO Max":"com.hbo.hbonow",
                                    "Her":"com.weareher.her",
                                    "Hill Climb Racing 2":"com.fingersoft.hcr2",
                                    "Hinge":"co.hinge.app",
                                    "Hitman: Sniper":"com.squareenixmontreal.hitmansniperandroid",
                                    "HP Print Service Plugin":"com.hp.android.printservice",
                                    "Hulu":"com.hulu.plus",
                                    "iHeartRadio":"com.clearchannel.iheartradio.tv",
                                    "IMLeagues":"com.linkedin.android",
                                    "Imo free video calls and chat":"com.imo.android.imous",
                                    "Infinity Dungeon VIP: RPG Adventure":"com.sosc.firstfantasy1super",
                                    "Instagram":"com.instagram.android",
                                    "IRS2Go":"gov.irs",
                                    "Jitsi Meet":"org.jitsi.meet",
                                    "Like":"video.like",
                                    "LINE":"jp.naver.line.android",
                                    "LinkedIn":"com.linkedin.android",
                                    "Lyft":"me.lyft.android",
                                    "Match":"com.match.android.matchmobile",
                                    "Mathway":"com.bagatrix.mathway.android",
                                    "MATLAB":"com.mathworks.matlabmobile",
                                    "Mercari":"com.mercariapp.mercari",
                                    "Messages":"com.google.android.apps.messaging",
                                    "Messenger":"com.facebook.orca",
                                    "Microsoft Authenticator":"com.azure.authenticator",
                                    "Microsoft Excel":"com.microsoft.office.excel",
                                    "Microsoft OneDrive":"com.microsoft.skydrive",
                                    "Microsoft OneNote":"com.microsoft.office.onenote",
                                    "Microsoft PowerPoint":"com.microsoft.office.powerpoint",
                                    "Microsoft Teams":"com.microsoft.teams",
                                    "Microsoft Word":"com.microsoft.office.word",
                                    "Minecraft":"com.mojang.minecraftpe",
                                    "Modern Combat 4: Zero Hour":"com.gameloft.android.ANMP.GloftM4HM",
                                    "Monument Valley":"com.ustwo.monumentvalley2",
                                    "MX Player":"com.mxtech.videoplayer.ad",
                                    "My Boy! - GBA Emulator":"com.fastemulator.gba",
                                    "My Talking Tom":"com.outfit7.mytalkingtomfree",
                                    "MyPlate":"com.livestrong.tracker",
                                    "Mystic Guardian VIP??: Old School Action RPG":"com.buffstudio.mysticguardian.paid",
                                    "MySubaru":"com.subaru.telematics.app.remote",
                                    "Need for Speed Most Wanted":"com.ea.games.nfs13_na",
                                    "Nest":"com.nest.android",
                                    "Netflix":"com.netflix.mediaclient",
                                    "Nord VPN":"com.nordvpn.android",
                                    "Nova Launcher Prime":"com.teslacoilsw.launcher.prime",
                                    "OfficeSuite Pro + PDF":"com.mobisystems.editor.office_registered",
                                    "OkCupid":"com.okcupid.okcupid",
                                    "OkOk-International":"com.chipsea.btcontrol.en",
                                    "Opera News":"com.opera.app.news",
                                    "PayPal Mobile":"com.paypal.android.p2pmobile",
                                    "Peacock TV":"com.peacocktv.peacockandroid",
                                    "Personal Cap":"com.personalcapital.pcapandroid",
                                    "Photomath":"com.microblink.photomath",
                                    "PicsArt Photo Studio":"com.picsart.studio",
                                    "Pinterest":"com.pinterest",
                                    "PlanetFitness":"com.planetfitness",
                                    "Pocket Casts":"au.com.shiftyjelly.pocketcasts",
                                    "Pokemon Go":"com.nianticlabs.pokemongo",
                                    "Pok??mon Go":"com.nianticlabs.pokemongo",
                                    "Postmates":"com.postmates.android",
                                    "Pou":"me.pou.app",
                                    "Poweramp Full Version Unlocker":"com.maxmpz.audioplayer.unlock",
                                    "PowerAudio Pro Music Player":"xsoftstudio.musicplayer.pro",
                                    "PrivacySimplified":"com.eteu.privacysimplified",                       ######################
                                    "PUBG Mobile":"com.tencent.ig",                                         # !!! UPDATE NOW !!! #
                                    "Quizlet":"com.quizlet.quizletandroid",                                 ######################
                                    "Rayman Jungle Run":"com.pastagames.ro1mobile",
                                    "Reddit":"com.reddit.frontpage",
                                    "ReFace":"video.reface.app",
                                    "Ring":"com.ringapp",
                                    "Robinhood":"com.robinhood.android",
                                    "Roblox":"com.roblox.client",
                                    "Roku":"com.roku.trc",
                                    "Samsung Calculator":"com.sec.android.app.popupcalculator",
                                    "Samsung Email":"com.samsung.android.email.provider",
                                    "Samsung Experience Service":"com.samsung.android.mobileservice",
                                    "Samsung Gallery":"com.sec.android.gallery3d",
                                    "Samsung Health":"com.sec.android.app.shealth",
                                    "Samsung Internet Browser":"com.sec.android.app.sbrowser",
                                    "Samsung Keyboard":"com.samsung.keyboard.themes",
                                    "Samsung My Files":"com.sec.android.app.myfiles",
                                    "Samsung Print Service Plugin":"com.sec.app.samsungprintservice",
                                    "Samsung Push Service":"com.sec.spp.push",
                                    "Samsung Voice Recorder":"com.sec.android.app.voicenote",
                                    "Scribblenauts Unlimited":"com.wb.goog.scribblenauts3",
                                    "Scruff":"com.appspot.scruffapp",
                                    "SHAREit":"com.lenovo.anyshare.gps",
                                    "Sharkee Browser":"com.sharkeeapp.browser",
                                    "Shazam":"com.shazam.android",
                                    "Shop":"com.shopify.arrive",
                                    "Signal":"org.thoughtcrime.securesms",
                                    "SiriusXM":"com.sirius",
                                    "Skype":"com.skype.raider",
                                    "Sleep as Android Unlock":"com.urbandroid.sleep.full.key",
                                    "Smart Tools":"kr.aboy.tools",
                                    "Snapchat":"com.snapchat.android",
                                    "Solitare":"com.lemongame.klondike.solitaire",
                                    "SoundCloud":"com.soundcloud.android",
                                    "Southwest Airlines":"com.southwestairlines.mobile",
                                    "Spotify":"com.spotify.music",
                                    "Star Wars Pinball 7":"com.zenstudios.StarWarsPinball",
                                    "Starbucks":"com.starbucks.mobilecard",
                                    "Steps":"com.stepsappgmbh.stepsapp",
                                    "Subway Surfers":"com.kiloo.subwaysurf",
                                    "Survival Island: EVO PRO ??? Survivor building home":"com.dbSoftware.siepro",
                                    "Tasker":"net.dinglisch.android.taskerm",
                                    "TeamSpeak 3 - Voice Chat Software":"com.teamspeak.ts3client",
                                    "Telegram":"org.telegram.messenger",
                                    "Temple Run":"com.imangi.templerun",
                                    "Temple Run 2":"com.imangi.templerun2",
                                    "Terraria":"com.and.games505.TerrariaPaid",
                                    "TextNow":"com.enflick.android.TextNow",
                                    "The Room":"com.FireproofStudios.TheRoom",
                                    "The Room Three":"com.FireproofStudios.TheRoom3",
                                    "The Room Two":"com.FireproofStudios.TheRoom2",
                                    "Threema":"ch.threema.app",
                                    "TikTok":"com.ss.android.ugc.trill",
                                    "Timing Hero VIP??: Retro Fighting Action RPG":"com.buffstudio.timingheropaid",
                                    "Tinder":"com.tinder",
                                    "Titanium Backup PRO Key":"com.keramidas.TitaniumBackupPro",
                                    "Torque Pro (OBD 2 & Car)":"org.prowl.torque",
                                    "True Skate":"com.trueaxis.trueskate",
                                    "Tubi":"com.tubitv",
                                    "Tumblr":"com.tumblr",
                                    "TuneIn Pro: Live Sports, News, Music & Podcast":"tunein.player",
                                    "TurboTax":"com.intuit.turbotax.mobile",
                                    "Twitch":"tv.twitch.android.app",
                                    "Twitter":"com.twitter.android",
                                    "Uber":"com.ubercab",
                                    "Uber Eats":"com.ubercab.eats",
                                    "UC Browser":"com.UCMobile.intl",
                                    "United Airlines":"com.united.mobile.android",
                                    "Venmo":"com.venmo",
                                    "Viber Messenger":"com.viber.voip",
                                    "vojaGO":"com.eggsnbaconapps.vojago",
                                    "Vrbo":"com.vrbo.android",
                                    "Waze":"com.waze",
                                    "WebEx":"com.cisco.webex.meetings",
                                    "WeHeartIt":"com.weheartit",
                                    "Wells Fargo Mobile":"com.wf.wellsfargomobile",
                                    "WhatsApp Messenger":"com.whatsapp",
                                    "Where's My Water":"com.disney.WMW",
                                    "Whisper":"sh.whisper",
                                    "WolframAlpha":"com.wolfram.android.alpha",
                                    "Word Search":"com.easybrain.word.search",
                                    "World Series of Poker":"com.playtika.wsop.gp",
                                    "Worms 3":"com.worms3.app",
                                    "YouTube":"com.google.android.youtube",
                                    "Zillow":"com.zillow.android.zillowmap",
                                    "Zombie Avengers:(Dreamsky)Stickman War Z":"me.dreamsky.leagueofstickmanzombie",
                                    "Zoom":"us.zoom.videomeetings"
                                   }

    app_name_query_search_term_list = [app_name_query_search_term]

    if app_name_query_search_term in common_apk_app_id_dictionary:
        app_id_value = common_apk_app_id_dictionary[app_name_query_search_term]

    return app_id_value

