trakt.tv scrobbler and library sync
==============================================

###What is trakt?

Automatically scrobble all TV episodes and movies you are watching to trakt.tv! Keep a comprehensive history of everything you've watched and be part of a global community of TV and movie enthusiasts. Sign up for a free account at [trakt.tv](http://trakt.tv) and get a ton of features:

* Automatically scrobble what you're watching
* [Mobile apps](http://trakt.tv/downloads) for iPhone, iPad, Android, and Windows Phone
* Share what you're watching (in real time) and rating to facebook and twitter
* Personalized calendar so you never miss a TV show
* Follow your friends and people you're interesed in
* Use watchlists so you don't forget to what to watch
* Track your media collections and impress your friends
* Create custom [lists](http://trakt.tv/lists) around any topics you choose
* Easily track your TV show progress across all seasons and episodes
* Track your progress against industry lists such as the [IMDb Top 250](http://trakt.tv/lists/imdb/top-250)
* Discover new shows and movies based on your viewing habits
* Widgets for your forum signature

###What can this addon do?

* Automatically scrobble all TV episodes and movies you are watching 
* Sync your TV episode and movie collections to trakt (triggered after a library update)
* Auto clean your trakt collection so that it matches up with XBMC
* Keep watched statuses synced between XBMC and trakt
* Rate movies and episodes after watching them
* Custom skin/keymap actions for toggling watched status, rating, tagging, and listing

###What can be scrobbled?

This plugin will scrobble local media and most remote streaming content. Local content should be played in XBMC library mode and you should use [TVDb](http://thetvdb.com/) (for tv shows) and [TMDb](http://themoviedb.org) (for movies) as your scrapers. TV shows are identified using their TVDb ID. Movies are identified using the IMDb ID. This helps trakt match up the correct show or movie regardless of the title and improves accuracy a lot.

Remote streaming content will scrobble assuming the metadata is correctly set in XBMC. The various streaming plugins need to correctly identify TV episodes and movies with as much metadata as they can for trakt to know what you're watching.

###Tested and scrobbling correctly

* XBMC library mode
* PleXBMC
* Amazon (bluecop repo)
* CBS (bluecop repo)
* South Park

###Installation

1. Clone this repository (or [download it here](https://github.com/rectifyer/script.trakt/zipball/master)) into a folder called **script.trakt** inside your XBMC **addons** folder
2. Start up XMBC (or restart if its already running)
3. Navigate to *Settings* > *Add-ons* > *Enabled add-ons* > *Services* > **trakt**
4. Select *trakt* and go to **Configure**
5. Enter your **username**, **password**, and change any other settings as needed
6. Select **OK** to save your settings
7. Watch something and see it show up on trakt.tv!

###Thanks

Special thanks to all who contribute to this plugin! Check the commit history and changelog to see these talented developers.
