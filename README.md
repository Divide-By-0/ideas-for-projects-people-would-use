# Ideas for Software that People Would Actually Use

Inspired by https://github.com/joereynolds/what-to-code.

These ideas, as far as I know, don't exist yet (or have done a poor job with SEO on Google). These are also ideas I desperately wish I could have tried at least once, meaning many others probably have as well. It's difficult to stay motivated coding or on a side project when you don't know if people will use it, or if your end goal is solving a solved problem. This list aims to fix that.

This list is around 100 curated ideas, and I hope to hit 150 by the end of 2023. Stay tuned, as I have several hundred on my list (the majority of them are patently ridiculous and not a good use of anyone's time to read).

Feel free to use these for a hackathon, side project, or hacklodge project -- I'd love to see them get built! If you're curious about an idea but don't know where to start, just reach out to me at aayushg@mit.edu; I'd be happy to give pointers on the frameworks I'd use, the high-level design, and/or the best way to learn how to build them. Ideas include apps, web apps, and chrome extensions. All I ask for is they are open source, credit is given to Aayush or [yush_g](https://twitter.com/yush_g) or [Divide-By-0](https://github.com/Divide-By-0/), and your repo + site link back to this list (the shortlink is https://aayushg.com/ideas) :)

## Funding

If you fully deploy the project publicly, I award free hosting and small cash prizes at $200 per idea ($400 per crypto idea). I personally put in $200 (crypto ideas additionally 2x matched by [@smsunarto](https://twitter.com/smsunarto)). This is at my discretion so people don't game the system or feel cheated; the point is to build the project for learning and self-satisfaction, not the grant -- the money is mostly just so it can continue to exist :). I will likely fund any good-faith implementation. Reach out to [me](https://twitter.com/yush_g) if you're interested in helping sponsor bounties as well!

**Total projects built: 16.**

**<details><summary>Finished + Paid out Bounties</summary>**
<p>

### Mixmello: Remix Spotify Playlists

**Bounty Prompt**: A program that takes your spotify playlist and converts it to another one of remixes of the same songs, to get some variety. Create remixed versions of your favourite playlists. Free and open source! </br>
**Website Link:** [mixmello.com](https://www.mixmello.com) </br>
**GitHub Repo:** [alexgurr/mixmello](https://github.com/alexgurr/mixmello)

### Damn Daniel Button

**Bounty Prompt**: The bruh button, but for damn daniel </br>
**Completed by**: Daniel Bessonov, Patrick Li </br>
**Press:** [Saratoga Falcon: Top 25 App on App Store Taken Down](https://www.saratogafalcon.org/content/students%E2%80%99-top-25-app-taken-down-after-%E2%80%98damn-daniel%E2%80%99-lawyers-threaten-legal-action)

### Phone Scroll Distance Leaderboard

**Bounty Prompt:** An app that tracks the distance you've scrolled on your phone and puts it on a leaderboard </br>
**Completed by**: Bryan Chiang </br>
**Demo Video**: [Demo](https://i.imgur.com/9VCWd7l.mp4)

### Auto-LaTeX Equations

**Bounty Prompt:** A way to use LaTeX equations in Google Docs </br>
**Completed by**: Aayush Gupta (me) </br>
**Website:** https://autolatex.com </br>
**Press:** [Nature](https://www.nature.com/articles/d41586-019-01796-1)

### Spotify Playlist Cleanify

**Bounty Prompt:** A program that takes your spotify playlist and converts it to a clean version with the same songs and removes it if it can't find any. Used to be able to listen to my playlists in the car with my parents </br>
**Completed by**: Arman Rafati</br>
**Website:** https://www.cleanify.app/ </br>
**Github Link:** https://github.com/code-arman/Cleanify

### Windows Automatic Unzipper

**Bounty Prompt:** When something is downloaded, unzip it to its own folder then delete the original zip file </br>
**Completed by**: Aiden Magrath</br>
**Github Repo:** https://github.com/aidenmagrath/Windows-Auto-Unzipper
**Website Link:** https://autounzipper.com/

### Trippy Videos

**Bounty Prompt:** Upsample each frame in a video independently with a GAN, creating an entirely style-transfered universe that moves from frame to frame in a slightly jarring and hypnotic way. </br>
**Completed by**: Milo Cress, David Wu, Alice Chen, Vincent Huang </br>
**Demo Video:** [30 second Video](https://streamable.com/e/dow82b) </br>
**Github Repo:** [Github](https://github.com/zephyrys/stylish-flask-backend)

### Colorize Video

**Bounty Prompt:** An API endpoint for temporally consistent video colorization</br>
**Completed by**: Syed Mustafa</br>
**Deployed Demo:** [Replicate API Demo](https://replicate.com/cudanexus/debvc)</br>

### Get Off Those Sites

**Bounty Prompt:** A good Chrome extension to keep you off Facebook etc. Tracks how long you spend on degenerate sites, then when you go to Facebook etc, it says "On average, you think you'll spend 16 minutes, but you end up spending 31 minutes on this tab. How many minutes do you think you'll spend this time?" And at the end of that # of minutes, it makes the page black and white so you can continue to browse but it'll be slightly uncomfortable. </br>
**Completed by** [GrimSteel](github.com/grimsteel) </br>
**Github Repo:** [get-off-those-sites](https://github.com/grimsteel/get-off-those-sites/) </br>

### Spotify Match

**Bounty Prompt**: A website that, when given a certain song or artist on Spotify, it finds friends who have listened to that artist/song (by # of occurrences in their public playlists). Useful to find concert buddies/people with similar music tastes. </br>
**Completed By**: Colin Flueck </br>
**Website Link**: [spotifymatch.com](https://spotifymatch.com)

### Safe Tornado Cash

**Bounty Prompt**: Safe tornado cash, where users can use it but hackers/North Korea can't. To be able to use tornado.cash, you have to wait a significant number of blocks between deposits and withdraws. You know the leaves being added to the Merkle tree, and can trace which are linked to stolen deposits. You can create a second blocklist of "banned leaves", which allows you to block withdraws of nullifier leaves, meaning hackers can deposit but not withdraw. </br>
**Github Repo**: [tornado-core-blacklist](https://github.com/hananbeer/tornado-core-blacklist)

### Open-source Keybr Clone with More Statistics

**Bounty Prompt**: Make an open source keybr clone with more statistics, like seperating lowercase/capital letters, and showing most missed keys and most missed pairs of keys. </br>
**Completed by**: Aayush Gupta (me) </br>
**Github Repo**: [keybr-with-stats](https://github.com/Divide-By-0/keybr-with-stats/)
**Deployed Website**: https://keybr.onrender.com

### Tuneder

**Bounty Prompt**: A tinder for songs -- plays the most commented 10 seconds of a song on Apple Music and adds it to a playlist if you like it. Inspired by Soundsieve (https://github.com/wilzh40/SoundSieve) which is unfortunately dead, and fab.fm which has a different song discovery method. Released as an iOS app. </br>
**Completed by**: Aditya Saravana </br>
**Github Repo**: [github.com/adityasaravana/Tuneder](https://github.com/adityasaravana/Tuneder)

### SoundSwipe

**Bounty Prompt**: A tinder for songs -- plays the most commented 10 seconds of a song on SoundCloud and adds it to a playlist if you like it. Inspired by Soundsieve (https://github.com/wilzh40/SoundSieve) which is unfortunately dead, and fab.fm which has a different song discovery method. Released as a web app. </br>
**Completed by**: Kevin Grosso ([k0dev](https://github.com/k0dev))</br>
**Github Repo**: https://github.com/k0dev/sc-explorer</br>
**Website Link**: [SoundSwipe](http://soundswipe.org)

### AI Video Colorization APIs

**Bounty Prompt**: Make it really easy (replicate.com deployed, with a nice interface and API) to run the latest colorization and OCR AI models, at near-cost.</br>
**Completed by**: [Cudanexus](https://github.com/cudanexus) </br>
**Demo**: [debvc](https://replicate.com/cudanexus/debvc) and [tcvc](https://replicate.com/cudanexus/tcvc) were state-of-the-art, but perform poorly in practice. Facebook Nougat (academic OCR AI where [huggingface demo](https://huggingface.co/facebook/nougat-base) doesn't work) and BiSTNet (which won NTIRE2023's video colorization challenge) are in progress.

### Pitchpin

**Bounty Prompt**: An audio recorder where you can tap to add a flag at any time -- you can attach a note if you want, but the purpose is that later you can quickly skip to that time and know something important is there. </br>
**Completed by**: Aditya Saravana </br>
**Github Repo**: [github.com/adityasaravana/Pitchpin](https://github.com/adityasaravana/Pitchpin)
**Website Link**: <a href="https://adityasaravana.github.io/pitchpin-site/">Pitchpin</a>

</p>
</details>
</br>

## Contribution & pull requests

If you make any of these, please make them open source!

If you want to be added to the list of people that have completed a project, request a PR adding the project idea, your project's URL, and your repo's URL to [CONTRIBUTORS.md](./CONTRIBUTORS.md) and above, and edit the README to mark them done. I can help brainstorm relevant communities, and recommend marketing ideas to help get your first few hundred users.

**<details><summary>Why make them open source and ad-free?</summary>**

<p>
I think open source is very, very powerful. I'd also love to add features to apps that I use if I want them, and I'm sure I'm not alone. Your app can be maintained and improved by the community that most cares about it (with minimal effort on your part!). If you're worried about someone else making money off of your work, you can just put a note in the README that anyone is free to share it not for profit, but anyone who monetizes, needs to check in with you first (and hopefully partner with them!).

Open source companies with canonical deployments are still often successful, and it makes little difference to the end user -- 99.99 percent of end users are not technical enough to even deploy a Github app. Gitlab, Android, Linux, Firefox, Flutter, React, Python, Rust, Docker, AWS, Box, Darabricks, Kubernetes, etc -- there's a massive list of open source projects that are wildly successful, and many of them have some "canonical deployment" which is monetized. People will pay a lot just for a hosted service of existing open source software. 

I wasn't always pro-open source. I thought, aren't you giving up your technical moat by open sourcing? But the financial upside to closed source compared to open source is very little, and the developer friendliness of open source is high enough that if there's any shot for the app to get big, that's the best shot. If someone publishes a competing app without your consent, expose them on Twitter (you can partner with them which is win-win, or report them to the app store which in a sense is lose-lose but an option). Companies recruit through open source too, so if you're a student, it's a great way to show off your skills.

I promise none of these will be a billion dollar app (or frankly even a thousand dollar app), and is just an early step in a long list of many future great things you will do. I highly recommend you invest in maximum social capital right now, and convert it to technical capital later. If you have a desire for monetizable projects, I'm happy to send over more ideas for those! Open source is also a great way to make sure you structure your repository well, especially secret management.

Ads bring in surprisingly low revenue -- I hope that the bounty makes it worth your time; for most of these apps, the amount you expect to make off of ads will probably be less than the bounty amount I pay you upfront. Overall, I strongly advise against closed source and ads -- not just because of me, but for the success of the app, and for you to have the satisfaction of creating software used by the maximum number of people :)

</p>
</details>
</br>

## Index

[All Software](#all-software)

- [Music](#Music)
- [Health](#Health)
- [Programming Tools](#Coding)
- [Family/Roommates](#Family-Roommates)
- [Politics](#Politics)
- [Image Processing](#Image-Processing)
- [Video Processing](#Video-Processing)
- [Audio Processing](#audio)
- [Edtech/Research](#Edtech)
- [Text Processing/NLP](#Text-Processing)
- [Fun](#Fun)
- [Crypto](#Crypto)
  <a name="all-software"></a>

## All Software

<a name="Music"></a>

### Music

- A Chrome extension that tracks if you're on a certain song or artist on Spotify, and it finds friends who have listened to that artist/song (by # of occurrences in their public playlists). Useful to find concert buddies/people with similar music tastes.
  - This is surprisingly highly requested, see [thread 1](https://community.spotify.com/t5/Closed-Ideas/Social-See-Friends-who-also-listen-to-an-Artist/idi-p/4397516), [2](https://community.spotify.com/t5/Closed-Ideas/Sort-By-Friends-Who-Listen-To-the-Same-Artists/idi-p/72047), and [3](https://community.spotify.com/t5/Closed-Ideas/Social-Listenalike-but-for-friends/idi-p/5041383).
  - DONE: This is done by [Colin Flueck](https://github.com/colin4554/spotify-match), project at [spotifymatch.com](https://www.spotifymatch.com)!
  - Note that the above isn't exhasutive; as [@alexgurr](https://twitter.com/alexgurr) points out, for thoroughness you may need a Chrome extension to hit the friends API endpoint on Spotify web, or Facebook login to use Facebook friends.
- **Spotify Playlist Remixer**: A program that takes your Spotify playlist and converts it to another one of remixes of the same songs, to get some variety.
  - DONE: By [Alex Gurr](https://github.com/alexgurr/mixmello), project at [mixmello.com](https://www.mixmello.com/)!
- **Spotify Parent-Friendly-ifier**: A program that takes your Spotify playlist and converts it to a clean version with the same songs, and removes it if it can't find any. Used to be able to listen to my playlists in the car with my parents.
  - DONE: By [Arman Rafati](https://github.com/code-arman/Cleanify), project at [cleanify.app](https://www.cleanify.app)!
- **Tinder for Songs**. Plays the most commented 10 seconds of a song on SoundCloud and adds it to a playlist if you like it. Inspired by Soundsieve (https://github.com/wilzh40/SoundSieve) which is unfortunately dead, and fab.fm which has a different song discovery method.
  - Note: This already exists for Spotify, namely [Tuneful](https://www.tuneful.app/) for a webapp, [Discz](https://www.reddit.com/r/spotify/comments/ojogbt/i_built_a_tinder_for_spotify_so_you_can_make/) which has an iOS app, and [Swipify](https://www.reddit.com/r/spotify/comments/mov9rq/swipify_a_tinderstyle_android_music_discovery_app/) on the Play Store!
  - DONE: By [Aditya Saravana](https://github.com/adityasaravana/Tuneder) for Apple Music on iOS
  - DONE: By [Kevin Grosso](https://github.com/k0dev/sc-explorer) for Soundcloud as a Webapp
- **Responsive AI DJ**: Uses a camera to monitor the movement of the people in the crowd and run sentiment analysis on their faces. Notices how that changes as it changes the music, with higher weights for more people. Can then "gradient descent" towards the optimal AI generated music for that crowd, keeping in mind things like repetitiveness and how the audience composition changes over time. Want to add variety over just beats, so give it some samples and voices to throw in as well.
- **Automatic Music Video Creator**: Upload any collection of videos, pictures, or a topic, that you want to auto-align to an uploaded mp3. The app detects drumbeats or other features and staggers the videos to transition at those times. Note that this kind of exists with Adobe Firefly now, I think.
  - Could potentially also upload a 3d scene somehow, and randomly move around and show the field of view, but at a speed proportional to music energy and rotating only when beats hit. Perhaps to import the 3d scene, could be autogenerated from an image/set of images, or just a spot on google earth or something?
- **Nightcore Song Compiler:** Automatically nightcore songs and post them as YouTube compilations
- **Flagging Audio Recorder:** An audio recorder where you can tap to add a flag at any time -- you can attach a note if you want, but the purpose is that later you can quickly skip to that time and know something important is there.
  - Can do this for a timer app/song player also, not just an audio recorder.
  - DONE: By <a href="https://github.com/adityasaravana/Pitchpin">Aditya Saravana</a>
- **Kaggle for Music Production**: The site provides samples and teaches the general structure to layer them, then has a periodic competition to layer them to create the best beat [Note: Kenny Beats runs a similar competition but without the lessons].
- **Spotify Data Visualizer**: Connect your Spotify and visualize Spotify data insights as pretty plots. Existing apps show tables or lists, but it's a small jump to display eye-candy plots instead, and will help with virality. There are some versions that already exist, but I want to go deeper into the data.
- **Music Plugin**: A plugin that just takes a piano melody and adds corresponding drums and reverb and a beat and a chorus and everything just off those notes (like the [harmony7](https://mitadmissions.org/blogs/entry/we-made-a-website/) MIT web.lab app).
- **Karaoke Training Tool:** Scrape a karaoke or music video from YouTube, match the pitch to notes (FFT?), then make bars at those pitches for you to hit, and overlay your current singing on top of it. Allows you to quickly train pitch like Yousician or Riyaz, but for any song. Can be used for live singing, singing covers at home, or singing lessons.
- **Movie to Playlist Converter**: Website that takes a video or movie, Shazam's all the songs or looks up soundtracks if they're public, and converts it to a Spotify playlist automatically. This might already be commonplace for mainstream movies, but doesn't exist for uncommon ones.
- **Little Dancer:** Use echo nest labs and FFT to sync a bunch of clips to a specific BPM or sequence of beats. Using some beat detector (likely also FFT), have a mini cheerleader or dancing figure synced to the beat in the bottom corner of your laptop. Can be based off of [stable diffusion dancing](https://metaphysic.ai/creating-authentic-human-motion-synthesis-via-diffusion/) to enable custom dancing.
- An app that chooses songs of a specific BPM from all your Spotify liked and playlisted songs, for workouts
- An app that plays hype beats or just a simple beat behind a podcast, so when you run you can listen and stay on pace
- A better rap lyrics generator than basic [MCMC/RNN methods](https://www.reddit.com/r/hiphopheads/comments/acwky9/original_python_program_that_writes/); use GPT-Neo/Llama/Mistral (any good OSS LLM) to generate reasonable distributions over the next words, then reweight the distribution of probabilities over next words by hard-coded poetic heuristics, such as the amount of internal rhyming to same syllable count on the previous line, alliteration, etc.

<a name="Health"></a>

### Health

- **8 Hours of Sleep App**: Sleep tracker app that detects when you fall asleep. It then turns off your sleep podcast/asmr and makes sure you get as close to 8 hours as possible and wakes you up in a light sleep state. Note that existing sleep cycle apps force a wake-up time, but time-to-sleep is often so inconsistent that chances are you won't be getting 8 hours.
- **Lucid dreaming app**: Pairs with Oura ring or Sleep Cycle-type apps, to play a lucid symbol sound when you are in REM sleep to try to induce lucid dreaming, inspired by Lucid Experiment. It will also have you practice snapping to awareness when the sound is played for 5 minutes as you fall asleep every day.
  - Edit: Turns out Sleep by Android sort of does this; I actually lucid dreamt the first time I tried it. Oura doesn't have a real-time API that can be called during sleep unfortunately. This is good enough for me, so going to deactivate this idea's bounty.
- **Patient radiology in your own hands**: An app that lets you take your physician's radiology image (or auto-align a sneaky picture of it), generate the hotspots of bilaterally asymmetric places or ML-determined anomalies, then the patient can ask the radiologist to double check those spots and comment on what it is. Inspired since radiologists' eyes often pause at the place where people have tumors, according to some studies -- noticably AI is significantly better than humans yet not widely deployed.
- A collection of all large-scale health studies for foods, ranked on a single number line of toxicity with error bars. Can scrape correlation/p values and error bars directly from papers.
  - Resulting graphic should look like this: https://cdn.vox-cdn.com/uploads/chorus_asset/file/3523382/Medical_studies-05.0.png
  - DONE (close enough): This is basically what [examine.com](https://examine.com) does, and I'm satisfied with their holistic large-scale study rating system.
- **Dishes likely to have Allergens**: Search portal where you put in a dish and it says what percent of online recipes of that dish have nuts, maybe by country too. Done by scraping recipes by the country of origin to determine what to avoid when allergic people eat that cuisine and create an intuition about what allergens and what restaurant dishes to avoid for a certain culture.
- **Instacart/Amazon Notifier for Food Allergies**: A chrome extension that goes through an Instacart/Amazon Fresh cart and finds them on an ingredient website and scrapes the ingredients, and flags foods with user-specified bad ingredients: whether it's nut allergies, seed oil aversion, or high fructose corn syrup. Various nutrition authors would certainly help market this, especially on Twitter.

<a name="Coding"></a>

### Programming Tools

- Automatically track all the keyboard shortcuts/clicks you do within an editor, and suggest/generate keybindings and commands for your most inefficient workflows (an interactive way to practice forgotten yet useful vim shortcuts, for instance)
- **Auto-Archiver**: A greasemonkey/tampermonkey script to automatically in the background, backup all visited pages and their hyperlinks to Internet Archive. 
  - Edit: [ATRescue + Flare0n's script from 2014](https://gist.github.com/ATRescue/e40efa579e4461561697934c1c3be229) still works well. I [forked it](https://gist.github.com/Divide-By-0/313bf6ab375e4f3112adf41ef8c15d5f) to add a small delay after each link to avoid being ratelimited. The [version deployed to the Chrome store](https://chrome.google.com/webstore/detail/autosave-to-wayback-machi/defmcmdgnplidnoilmeleeglnmjkalnk) doesn't have enough customizability (i.e. if you want to, say, avoid all Google drive links or avoid ratelimits), so I recommend the Tampermonkey script instead. My 'User Excludes' list includes \*google.com\* and \*gmail.com\* but for some reason Google Chrome keeps thinking I'm getting hacked (on my calendar I think?) so evidently better filtering needs to be done here. Maybe instead of just blocking the original host, also block all links out from safe hosts? Anyways if anyone can correctly diagnose and fork this code to fix this Google banning issue, I'll still award a half bounty.
- A lightweight create-react app for ML apps. This starter app would compile on first clone and run React and Python. Should have a 'yarn deploy' or something that does a one-click deploy to an API endpoint as well.
  - Edit: I now think this should use React and [Modal](http://modal.com) or [Replicate](https://replicate.com) instead.
- **404 to Archive Redirecter**: A greasemonkey/tampermonkey script to, when detecting a page that says "404" or "Not Found" on it, automatically redirect to that page in the Internet Archive.
- OSS Keybr Clone: Make an open source keybr clone with more statistics, like seperating lowercase/capital letters, and showing most missed keys and most missed pairs of keys.
  - DONE: This is done at [https://keybr.onrender.com](https://keybr.onrender.com).

<a name="Family-Roommates"></a>

### Family/Roommates

- Remotely control your grandparents' computer/phone with one link click that you can send them. It should be one-time and only work for a few minutes, so hackers can't exploit it in the future. Chrome Remote Desktop requires Google sign-in from the same account in both places, which is harder to pull off for 2 different people.
- Make an algorithm for a mounted camera that sends SMS notifications if your roommate leaves dirty dishes, based on this [similar one](https://medium.com/@ageitgey/snagging-parking-spaces-with-mask-r-cnn-and-python-955f2231c400) for parking spaces.

<a name="Politics"></a>

### Politics

- Rate your affinity towards topics and get a ranked list of candidates that are most aligned based on the wiki grid, like a BuzzFeed quiz for local candidates.
  - Prefer to make this automated by building a scraping service for all candidates on Ballotpedia comparing state senators etc. and scraping their beliefs from their speeches on youtube transcripts or personal links or Twitter etc. Can also train on the Wikipedia grid of candidate beliefs/policy votes.
  - Existing solutions are lacking: isidewith (only for presidential race), voteredge (ugly), ballotpedia (no side by side or issues grid).
  - This project may or may not have been done by a team from [AIM Labs](https://aimlabs.mit.edu/).
- Given a county, it automatically scrapes candidates running for local office and analyzes their social media/public statements to infer possible political stances. If this is not enough info on local leaders, it might require an embedding/LDA type approach to analyze their public profile. Will likely be pretty easy with ChatGPT prompting.

<a name="Image-Processing"></a>

### Image Processing

- Make app/Chrome extension/background integration to auto tag Google Photos images with ongoing calendar events, so I can search for the event and see the photos from that. Useful for class notes (if all your classes are on your calendar) and generally increasing the searchability + tagging of photos.
- A way to share event photos to specific people. It should be possible to upload an album to i.e. Google Photos or Flickr of thousands of pics of the event, and attendees can input a picture of themselves and/or their friends, and it automatically runs facial recognition on every pic in the album and only returns pics that include people from the inputted picture. Alternatively, since Google Photos already does this, a script that scrapes through the album and sees which ones are tagged with you, and saves those to your library.

<a name="Video-Processing"></a>

### Video Processing

- **Blink Tracker for iOS/Android**: Count blinks and display on screen. Here is a [full spec for an iOS app](https://docs.google.com/document/d/1w6dA5UAvva4zIa9e-msC-8sv5pUHpkX-7uuwCeT-C3Q/edit?usp=sharing).
  - DONE (Android): This is done by [Sergey V.](https://github.com/djkovrik/BlinkTracker), download from [Google Play](https://play.google.com/store/apps/details?id=com.sedsoftware.blinktracker)
- **Combine Lecture Videos**: Given a set of videos (that may be slightly offset) from different angles, combine them into one video that cuts between the frames. This already exists for ai podcast processing software so shouldn't be too hard to adapt? Full [spec for CLI tool here](https://docs.google.com/document/d/1oInpmyf3xikM6TOMaz6Uqz5ZStdFyP7YqKX39RR9nMQ/edit).
  - In Progress: There is a 2x match bounty amount matched by [MIT Soul](https://mitsoul.org).
- Convert any youtube video to the trapezoid holographic projection (like [this](https://www.instructables.com/3D-Holograms-Using-Phone/)) by running depth perception AI on the video, and changing the depths that different pixels are at on different screens, so you see a depth modulated image on top of your screen, holographically, for any video!
- Animation Generator: AI labels each frame in a video with the contents in a text (representation learning), then based on given labels, generates missing labels/coherent story, then generates an animation based on all those labels. Can deepfake style transfer all images to be the same style (like Gen-1).
- A dashcam that alerts you if someone is giving you a parking ticket when you're away. Bonus points if it tells the cop that you'll be back in just a minute.
- **Auto Analyze Game Footage**: A drone above a sports game keeps track of all the footage and then you infer the plays the opponent is making based on similarity of movement, so you can get the strategies of an arbitrary team. Can also do with phone cameras possibly.
- A hidden camera on a lapel that lets you record all poker hands at a casino and then analyses them for you.
- **Trippy Video Generator**: A superresolution/style transfer model runs on each frame of a video independently, leading to a very raw flipbook-style animation. Perhaps generate a trippy video from a regular video. For instance, upresolutioning every frame, or recoloring each frame (or any other transformation) independently with an imperfect generative adversarial network to have disconnected images but a connected idea.
  - DONE: This got built! See [aimlabs.mit.edu/](https://web.archive.org/web/20230402001627/https://aimlabs.mit.edu/) > Stylish Videos! These days, stable diffusion basically does this pretty well.
- **Automatic Emoji Videocaller**: Fill in people's videos when their cameras are off. By using the speech-to-face paper in a browser extension, fill in other's inactive google hangouts/zoom logos with low bitrate moving bitmojis, and send yours as that when your camera is off. Cool research done at 5.3 (https://arxiv.org/pdf/1905.09773.pdf).
- **Lecture Video Autopacer**: Given a (lecture) video, edit it so that automatically speeds up during times where no actual lecture content is delivered (ex. an instructor talking about their dog), and slow down when content is dense (ex. slide full of equations that the lecturer is going through). Use both visual info (slides) and audio (what the lecturer is saying). Example use case: a student wants to watch a recorded lecture video in an optimal manner that maximizes learning in a shorter amount of time.
- **Deployed AI Models**: Make it really easy (replicate.com deployed, with a nice interface and API) to run the latest colorization and OCR AI models, at near-cost.
  - DONE: Cudanexus put up [debvc](https://replicate.com/cudanexus/debvc) and [tcvc](https://replicate.com/cudanexus/tcvc), which are both pretty bad in practice. Facebook Nougat ([T4](https://replicate.com/cudanexus/nougat), [A40](https://replicate.com/alaradirik/nougat), [PDF url version](https://replicate.com/awilliamson10/meta-nougat/examples)) is now up as well (academic OCR AI whose [huggingface demo](https://huggingface.co/facebook/nougat-base) doesn't work). BiSTNet (which won NTIRE2023's video colorization challenge) is in progress, but has no working demos online yet.
- **Anime Undimmer**: During action scenes, animes will often dim scenes. Given a set of timestamps, create an automatic website or ffmpeg script that can take a video and undim those specific sections. Note that it's just a semiopaque black filter, so in practice, it seems just adjusting brightness, gamma, contrast, and saturation should be sufficient to undo it. The dimming parameters are different for each scene depending on the amount of motion, so it would have to somehow dynamically adapt.
  - DONE: This is done by [projectdate](https://github.com/projectdate/anime-undimmer) as a local bash script. I will still pay a half-bounty to convert it into a simple webtool.

<a name="audio"></a>
### Audio Processing

- **Chrome Transcriber**: Live transcribe any Chrome tabs audio by pushing it into OpenAI Whisper-type model, enabling transcriptions for all meetings including gather.town out of the box. Can have a start/stop button that auto-saves it to a Google Doc.
  - This works for Google Meet well with tactiq, but I have not found anything else.
- **Mac Transcriber**: Create a new audio output device on the Mac that I can change to, that detects the previously selected audio device. Then, it automatically reroutes all outgoing audio to the previously selected Mac output auto device. However, it also logs this data and runs it through Whisper with multi-speaker diarization in real time and constructs a transcript. Blocks of text are stored for say 1 month before getting deleted, and anyone can copy any "block" of text. A bonus is if it also runs a second input device that transcribes inputs in parallel and allows you to select only-inputs, only-outputs, or both interleaved.

<a name="Edtech"></a>

### Edtech/Research/School

- ***Timed comments for YouTube**: Like the [existing beta which doesn't seem likely to rollout soon](https://www.engadget.com/youtube-testing-timed-comments-114419554.html) but shown in a Soundcloud style. That is, a scraper gets all the comments, extracts timestamps, and like Soundcloud, displays previews that expand on hover in tiny popups at the timestamp the bottom of the video as you watch. If not fullscreeen, each comment thread at the timestamp can scroll by on the side in place of the next video suggestion, like an auto-scrolling Khan Academy comments board. Would likely be a Chrome extension. Ideally, could also show such comments automatically on any embedded YouTube video as well. If someone using the extension likes or responds, should just respond from their logged in YouTube account.
  - DONE: This already exists! [Tempus](https://chrome.google.com/webstore/detail/tempus/bpdhbpeecmmglmkjfmigehaebpndmceh) is a Chrome Extension that does exactly this.
- **Combine Lecture Videos**: (copied from video processing section) -- given a set of videos (that may be slightly offset) from different angles, combine them into one video that cuts between the frames. This already exists for ai podcast processing software so shouldn't be too hard to adapt? Full [spec for CLI tool here](https://docs.google.com/document/d/1oInpmyf3xikM6TOMaz6Uqz5ZStdFyP7YqKX39RR9nMQ/edit).
  - In Progress: There is a 2x match bounty amount matched by [MIT Soul](https://mitsoul.org).
- An extension where you could double click a citation # in a paper and it would automatically open the pdf from jstor or other 👀 sources.
- A bounty program to make top papers on paperswithcode.com into interactive APIs on [Replicate](https://replicate.com) that anyone can play with.
- **Tunemeet for cohort-based classes**: It's known that cohort-based learning is powerful. An extension students can get that drops a chat box in their window if they're watching the same video (class zoom recordings or OCW content to start) as another student at the same time. Can perhaps comment on specific timestamps in the video, or have a Khan Academy-style board for any video.
  - There are several proponents of cohort-based learning, including [Wes Kao](https://www.weskao.com/cohort-based-courses-articles) or [Forte Labs](https://fortelabs.co/blog/the-rise-of-cohort-based-courses/) that I'm sure would love to see this!
  - This feels similar to what spencerc99/jackyzha0 built with cozy internets.
- A script to apply to all companies on Glassdoor with just your LinkedIn, and doublechecking its autogenerated answers to all questions with the user, before it batches autosubmits all of it. It will likely require some Selenium in Python. <a name="OCW"></a>
- **Open Source Collaborative Class Materials Page**: Make the [the Missing Semester website](https://missing.csail.mit.edu/) into a general template for any class. In addition, try adding new features. One example possible new feature is sign-in, where every user can sign in to get some perk (say pset answers) -- in exchange, we can get data on which courses people study, and if the materials for a course are sufficient or need improvement. Experiment with things like forums like Khan Academy for questions on any video, easy course feedback, and PRs on GitHub for each class. Also, it should be easy to find others to self-study a class with. Users could have permissions like course admin, course teacher, TA, and contributor. For example, a contributor can upload a document they worked on, and a TA can edit the class page to include it. This can streamline contributions, so class webpages can just be approved OCW staff, and instead updated by contributors.
  - In Progress: There is a 2x match on this bounty by [MIT Soul](https://mitsoul.org).
- **Piazza to Stack Overflow:** Piazza, a question-answer forum, does not allow downloading or archiving posts on the site. But many times, an instructor wants to make the Q/A from a previous class accessible as another learning resource, either to the next offering of the class or to self-study learners, especially if the class materials are made free and openly accessible on a site such as MIT OpenCourseWare. It would be awesome to automatically cross-post Piazza questions to a new Stack Overflow account, and repost all questions to Stack Overflow with self-answer. The questions would all be anonymous, and we can flag all questions that have a name or proper noun in them to manually review. We can also tag each question to a certain class, so class-specific questions can have appropriate context provided or be skipped entirely. Note that a consent question for this should be asked upon class signup.
- **“Suggestion mode” for OverLeaf/[Slate](slate.rs)**: Imagine if there was a way to collaboratively have LaTeX notes and have anyone provide feedback or questions on the notes themselves. Ideally, we would just share an overleaf page and people can leave such comments themselves. However, it is too difficult to add this functionality to a closed source codebase. Luckily, it should be possible to add this to https://slate.rs, a faster open-source overleaf. We think adding a suggestion mode to this would be super high impact and an interesting experiment for open education, to foster a collaborative environment to improve the notes.

<a name="###Text-Processing"></a>

### Text Processing/NLP

- **Goodreads Book Recommender via OpenSyllabus**: A site that takes in your Goodreads profile and uses the OpenSyllabus Galaxy book embeddings to build a recommender system for what you might like next.
    - DONE: This is [done](https://goodreads-recommender.vercel.app/) with a nice to use GPT-4 wrapper!
- A creative startup name finder powered by baby names. Find meanings for baby babes, and make a site where you can input keywords your startup is about, and it will print resulting baby names with meanings with the highest keyword overlap (or min distance in the word embedding space). You can also have a keyword masher, where you input 2+ keywords, then try all reasonable pairwise ship names till you reach an untaken name .com/.ai/.io/other top TLD.
  - Inspired by https://www.joinleelo.com/blog/how-we-came-up-with-the-name-leelo
  - DONE: This is [done](https://baby-names-generator.vercel.app)
- Convert all text in messenger apps to lowercase automatically (ideally on mobile for speech to text or bad autocorrect).
- **Chat to Journal**: Go through all my messenger history via my Facebook download or WhatsApp backup, and use an LLM to go through and see which texts were about my day that day (and not responses to the other person), use the timestamps the message was sent, and bootstrap a journal for me.
- **Unit Prices on Instacart**: A Chrome Extension that adds the per ounce/unit price to Instacart the same way Amazon does.
- **Fix Forgot to Reply To Message**: App that finds old messenger chats or emails you left on read or unread, or unfinished threads, so you can respond to them. Requires probably mapping the last few texts to a score of how likely it was to be the end of a conversation.
- Talk to a 'painting' and have it talk back, like Harry Potter paintings. Speech-to-text on your voice, gpt-3-type-model for conversation, tokkingheads/other deepfakes to have a face emulate the response. This has been [attempted](https://github.com/Halcyox/XRAgents) and there are [some open source demos](https://replicate.com/cudanexus/makeittalk), but it's not yet real-time end to end on arbitrary humans, and nowhere close on quality with animation on cartoons (anime is close).
- Create a simple scraper that searches Google for [specific bot websites](https://twitter.com/gregegansf/status/1363978958841155585) and reports/blocks them. This is more a way to get to talk to/help Greg Egan, than it is a real problem.

<a name="Fun"></a>

### Fun

- Create a nice frontend for DeepSaber, a way to AI generate beatsaber maps for any youtube video. Currently, it's just a [colab notebook](https://colab.research.google.com/drive/11v-ztHOUXLXFHmH4QIuXGXtTvD-3r7oP#scrollTo=mocWjd1-oatL), but it's [a few short steps away](https://gist.github.com/Divide-By-0/0fd38b7b8b0102b21b4f11bf8dd7d707) from having a nice frontend. BeatSage is a similar AI mapper that's generally regarded as having an inferior algorithm, and they hit 100K uses in a few months.
  - Edit: Done at [bsmapper.com](https://bsmapper.com) and [beatsaberai.com](https://beatsaberai.com). A new one is coming out soon as well that should blow these two out of the water.
- A better smart time-based phone password lock. For instance, if the current time is AB:CD, the user can set their password as say, (A+B), (|C-D|), (A \* B % 10), (D), or a general user-coded function, so it changes every minute. Existing solutions only allow rudimentary functions.
- Automatic haircut chooser -- input a picture, and based on aligning your face to a celebrity with similar facial features (via keypoint matching or AI facial recognition %), then overlay celebrity hair on top of yours to preview the style or directly show that celebrity's hair to your barber.
- Automatically take a picture of your face and take cross ratios and edge detection/curve detection to determine the best sunglasses based on face shape. Training data can be celebrities with similar face shapes, and you can even have a whole startup ship and send you completely custom-sized sunglasses.
- **The [Wiki game](https://www.thewikigame.com/) for Subreddits**: Instead of Wikipedia pages, you have to navigate to a target subreddit only via clicking other subreddits in sidebars, wikis, and pinned posts.
- Nerve (like the movie) but to avoid the horror scenarios, all submitted new dares must be moderated for safety. Alternatively, mix and match a reasonable list of locations and actions.
- ~~A good Chrome extension to keep you off Facebook etc. Tracks how long you spend on degenerate sites, then when you go to Facebook etc, it says "On average, you think you'll spend 16 minutes, but you end up spending 31 minutes on this tab. How many minutes do you think you'll spend this time?" And at the end of that # of minutes, it makes the page black and white so you can continue to browse but it'll be slightly uncomfortable.~~
  - DONE: Built at [get-off-those-sites](https://github.com/grimsteel/get-off-those-sites/).
  - Can also do for apps on phone.
- ~~Windows automatic unzipper. When something is downloaded, unzip it to its folder then delete the original zip file (Macs do this already, but not Windows).~~
  - DONE: See contributors.md, site at https://autounzipper.com/
- Intersite with a live count of how many people are watching. OG Silicon Valley watchers will know what this means.
- A bidding platform for radio ads, where corporations/clubs/people put their ads, and radio hosts play the highest paying ones and post the time and station, and location. Once the site auto-verifies it with audio matching from tune-in + shazam type system, it automatically transfers revenue from radio station to radio hosts (can be done easily via crypto).
  - I think college radio stations (like MIT WMBR) would really like this and probably use it!
- A Twitter bot that tweets the opposite of what a Twitter thought leader influencer says and is therefore just as insightful.
- Run analysis on which dance teams placed in what rank, to see the correlation between show order and rankings to measure bias, at shows like the Desi Dance Network.
- An Amazon price per ounce/count calculation that works all the time, and the equivalent for Instacart, Walmart, etc.
- Draw a [bad luck circle](https://twitter.com/marsreviewer/status/1646608776747798565?t=UjK5wKUiA29kWEkDm99jSg&s=19) and sell t-shirts nearby that say you flip all bad luck for good luck, [inspired by this](https://twitter.com/Noahpinion/status/1648052997241577472). Pretty performance art-y.

<a name="Crypto"></a>

### Crypto ($400 each)

- **Quantum Proof Keypairs on Ethereum with AA**: Implement ECDSA in a STARK and integrate into EIP 4337 like this [ethresearch post suggests](https://ethresear.ch/t/quantum-proof-keypairs-with-ecdsa-zk/14901), allowing anyone to move their money to a quantum-safe wallet with ECDSA, without having to switch keypair algorithms.
- **Truly random NFT drops** The problem is that you can predict randomness and mint the best NFTs by simulating the chain. Some solutions [exist](https://www.paradigm.xyz/2021/10/a-guide-to-designing-effective-nft-launches#phase-4-metadata-reveal). However, a better way to do this is, on mint, you generate a 24+ second (2+ block) VRF seeded by the previous blockhash. Minters pay gas upfront for anyone to send a second reveal transaction. MEV searchers calculate the VDF and send the result to the chain for that gas money + a small bonus, in return for updating the NFT values on chain first. More description at this hackmd: https://hackmd.io/xgR6mtWyQYC_SZYtZTdoDA .
- **Futarchy On-Chain**: Build the first prediction markets for governance, like [MerkleDao](http://www.ralphmerkle.com/papers/DAOdemocracyDraft.pdf)'s plan. Add features like also betting reputation points proportional to money, where higher reputation leads to higher investment limits, which will help institutional players to be long-term aligned with the project instead of financial manipulators. This will also help elect legislators who consistently have high reputation, meaning they accurately predict long term impact of legislation on people.
- **EVM Bytecode Splitter**: There is a 24kb contract limit on the EVM, and it's a huge pain to cut down contract size. However, taking bytecode or Yul directly, determining memory access patterns, and automatically splitting contracts so that they are deployable on chain would be extremely valuable. Specifically, halo2 cannot be verified on chain right now because the Yul verifier without aggregation is too big.
  - Note: There is an additional 2x match on this bounty from zk-email.
- **Artist Royalties for Using Their AI Voice**: Prove via zk-email on Spotify confirmation emails and EZKL proof of voi e via ML, that you used an artists voice and split profit with them. Details at https://hackmd.io/Nf8mSSKwRIu3GYyhGq5f9A
- **Private Generative NFTs with ZK/NFC** (Joint idea with Vivek): Via NFC cards that generate unique BLS signatures, each tap on the artist’s NFC card provides a signature on a unique edition number and seed. This can be used to generate a private piece of art based on the seed, only visible to the owner of the signature. We found a few algorithms that make this possible, dm us for a bigger project doc.
  - This idea is 2x matched by Provenant.
- **Bitcoin on Chain**: [Not my ideas, but still excellent] The four ideas at the bottom of https://bitcoinmirror.org/ have not been created yet and are technically feasible as an intermediate-level project, and could be the first trustless applications of Bitcoin on Ethereum! They haven't been built yet because this was only possible a few months ago and isn't marketed very widely. Would likely quality for Gitcoin/Eth Uni grant for much more funding. WBTC uses a centralized minting system with a 10B$ market cap and can be replaced by this. Can do as well with [ZK proof of BTC headers](https://devfolio.co/projects/bls-pil-865f), which will be substantially cheaper. Can even do [optimistic ZK verification via Naysayer proofs] to make it even cheaper.
- Run automated static analysis and formal verification tools on all existing and new smart contracts: I have a more [fleshed-out proposal here](https://docs.google.com/document/d/1D9extlCKq0qbroTjv6FD-JHstpAulRylVM0hpOuZsyM/edit). Can add bespoke checks like seeing if code calls unsafe oracles like [keep3rV2Feed.current](https://kyrianalex.substack.com/p/the-inverse-finance-hack?s=r). Can also use more recent powerful tools like [Veridise](https://veridise.com/), which likely haven't been run very widely.
- **RISC0 verifier in Solidity** Due to gas costs, the team building verifiable RISC execution has only verifiers for non-EVM chains. It should be easy to convert this verifier generator to use solidity syntax instead and run on an L2, letting you do stuff like verifiable Pytorch execution on chain. Code is even OSS as of Q2 2022. Idk if it exists yet, it might already.
- **Bountied Whistleblowing**: A bounty platform for leaks where people can bit on leaks with specific sources (i.e. from @___) and specific text (i.e. includes the phrase "___"), and it creates an escrow system on chain where others can upload those anonymized leaks along with [zk-email proofs](https://github.com/zkemail) that they satisfy the regexes, and reveal only the parts that they want to reveal.
- **Donate to Any Arxiv Paper and Its References**: Put in an arxiv link, and a bot scrapes all the emails out of the PDF/Arxiv itself. Then it scrapes all of the emails off of all of the dependencies and allows the donor to reweight them based on where they appeared in the text (i.e. it defaults to something like, cited in previous work or methods splits 40% of the donation, authors cited in intro split 10% of the funds or whatever). Then it deploys [zk-email wallets](https://github.com/zkemail/email-wallet)  for all of them and sends them the money.
- **AA L2**: An L2 whose only feature is account abstraction on top of the Ethereum L1.
- A Vitalik-style blog post on accumulators. Explaining the difference between RSA accumulator, merkle trees, hashed prefix tries, etc along with time and space complexity for set inclusion and set exclusion, with and without ZK. Might also inspire a new idea for a ZK friendly accumulator (although Merkle trees are already quite efficient).
  - Edit: Vitalik has now put up a similar one, [this post](https://ethresear.ch/t/arithmetic-hash-based-alternatives-to-kzg-for-proto-danksharding-eip-4844/13863) would be a great model for it.
- **ZK Mao On Chain**: Put the [Mao card game](<https://en.wikipedia.org/wiki/Mao_(card_game)>) on chain, with a rule like any new rule must be < 20 characters of code. This game would be perfect to demo both programmability of blockchains and provide a fun twist to one of my favorite card games. You can use ZK-SNARKed execution of commited-to code in order to prove consistent execution of your code, with something like Risc0 or a zkEVM, and use a zk verifier as a "commitment" to the code. Can also be off-chain, since is only a fun SNARK demo.
- **Pay for L1 Txs With Any Coin**: Gas station network v2 mainnet frontend, even for simple ERC20 sends. Would allow people to send transactions to the chain without any eth in their wallet; there are no live mainnet frontends right now. This is being vaguely pushed for with account abstraction, but you can also run MEV-incentivized relayers to do this (see [stealthdrop](https://github.com/stealthdrop/stealthdrop) or [surrogeth](https://github.com/lsankar4033/surrogeth) without centralized relayers).
- **Higher Degree Gates in Circom**: Allow circom to do higher-degree gates via automatically decomposing it (i.e. z = x _ x _ x is automatically parsed as y = x _ x and z = y _ x in the backend, where \_ can be + or \*)
- **Onboard to Crypto via Your Brain**: Imagine a private data marketplace over moves in on-chain games (imagine https://words3.xyz/ or any other MUD game, but with faster payouts and less bottability). If a new user to the chain has no funds, they can prove that they know some move costs x and gains y points, and make a zk proof of knowledge of that transaction (can be via an axiom proof or any zkevm proof). They need to continue to prove that the move is still available, which can be a smaller recursive proof on top of this base proof (i.e. a refreshing salted Merkle proof to constantly updating Merkle roots). Then, they can sell that word in a marketplace where people can bid for it. Without any money in my wallet, they can still play this game and get $. Other players can just buy moves off the marketplace if the point per dollar they can buy there is higher than what they were planning on playing, and that difference is what they'd likely bid for that knowledge. If the game is constantly adapting rulesets as so to thwart bots, it can be a compelling way to onboard without KYC or bridging.
- **Is this website actually clientside ZK?**: A very simple browser extension that detects if a website that claims to be ZK is sending any information to a server, or is clientside only. One version would spoof all outgoing requests to be from an empty server, so that you can still do things like download zkeys, but you can't send personal data.
  - Partially DONE. First half done by Monia, not open source yet.
- Create a GitHub org for non-censored DeFi frontends, as suggested [here](https://twitter.com/smsunarto/status/1560897907405901824). Host them under an uncensorable domain as well.
- A stablecoin for basket-of-goods price index, which adjusts the interest rates of its vaults to create this peg i.e. (us dollar / inflation). It maintains surplus in the Treasury by issuing gas options and flash loans on the treasury. The gas options will allow a simple on chain derivates framework to generate actual income in other cryptocurrencies, allowing it to deviate from the dollar. You should peg to a basket of arbitrary real world currencies or assets, not crypto assets.
- **Dev NFTs on Goerli**: A developer-friendly ERC721 on testnets i.e. Goerli, that lets you send Eth to the contract and will auto-mint you back 100 dev NFTs to experiment with, so super easy to test with during hackathons
- **ZK Email Applications**: Using our SDK linked to from https://prove.email, build any one of the applications listed on [our organization readme](https://github.com/zkemail/.github/blob/main/profile/README.md#help-out)! Most useful for getting off-chain data on chain, or sending assets to people off-chain in a trustless manner via email.
- **Optimal NFT Auctions**: Build a full NFT marketplace that uses optimal auction theory instead of first price auctions, like Opensea etc do right now. You should use our [on chain blind Vickrey auction contracts](https://github.com/Philogy/create2-vickrey-contracts), which you can understand via our [blog post](https://blog.aayushg.com/posts/vickrey).
- **Safe Tornado Cash**: Where users can use it, and prove non-membership in blocked lists of addresses. Such a list could be i.e. money linked to hacks/North Korea or something. Currently, to be able to use tornado.cash, you have to wait a significant number of blocks between deposits and withdraws. You know the leaves being added to the Merkle tree, and can trace which are linked to stolen deposits. You can create a second blocklist of "banned leaves", which allows you to block withdraws of nullifier leaves, meaning hackers can deposit but not withdraw.
  - Partially DONE: This was [built](https://github.com/hananbeer/tornado-core-blacklist) and a bounty was awarded! Ameen built a similar centralized version of such a list, but he controls who is on that list. A version with any number of permissionless lists that users can choose to prove or not prove inclusion in, and anyone can make a new list, is a better way to do this. Note that this bounty is **still open with the same reward** for the more general construction.
  - Note that this can be made more general. Any entity (the government, rektfinance.eth, or you) can create a curated list of "bad addresses". Any withdrawer can prove non-inclusion in any set of lists they think others would care about when they withdraw (via proof of inclusions in the complement).
- **Better Gitcoin Comments**: Make a PR to [Gitcoin](https://github.com/gitcoinco) to order comment section by comments first, then all contributions. Also recalculate the matching amount shown on the frontend to be adjusted to project future donations based on the average distribution, so that the matching amount is more accurate.
- Patch ethers.js to add a function that calculates the transaction hash, without having to send the transaction. keccak256 on the signed transaction doesn't work, and there is no built in function to do so even though it is possible and one can write their own helper function (see the [description here](https://github.com/Divide-By-0/ideas-for-projects-people-would-use/issues/12)).
- **XOR Optimizer**: Rewrite general arithmetic circuits or computational programs to maximize the number of XORs used, compared to other gates. This would allow us to create garbled circuits with maximal efficiency because [XORs are free](http://www.cs.toronto.edu/~vlad/papers/XOR_ICALP08.pdf). See a beginners [intro to garbled circuits](https://crypto.stanford.edu/cs355/18sp/lec6.pdf) here.
- **ZK Soft KYC**: A circuit on the simpler end, with a proof-of-membership to Gitcoin Alpha Passport. When you send a donation on Gitcoin, you prove you own an account (i.e. via a signature match into a merkle tree heyanon style) to prove a matching % (or soft KYC-ability), without revealing who you are. You can use an Axiom state root of the on chain Gitcoin passport to ensure up-to-dateness with the chain. Note that this trusts Gitcoin to verify your matching in a centralized manner.
- **Witness Encypted Tinder**: Implement Protocol Labs’ [new construction](https://drive.google.com/file/d/1GEfm77BfKRz1Xzby89era8KOgalqn00L/view) or [this non-succinct one](https://eprint.iacr.org/2021/1423.pdf), and then build a proof of concept Tinder where everyone selects 5 people they want to match with, and are only matched if people select each other. First, everyone commits to, say, 5 people they are most interested in. Those 5 people should get only notified if they also commit to that person as one of their chosen 5 as well. So, after everyone commits, those commitments are used in the FC-WE scheme that everyone then runs, to publish a message only to their 5 folks only if they also had valid commitments (i.e. with them in it, while keeping it anonymous, which may not be possible with groth16). Finally, in the reveal stage, everyone attempts to read every message and can only end up reading the ones that work for them. You can do this with a pairwise Socialist Millionaire or Yao’s Garbled Circuits, but this requires more back and forth stages.
- **On Chain Proof Aggregator**: To get L1-level censorship resistance and data availability of ZK circuits is expensive, but there is a way to make this cheaper at the cost of a delay. Imagine building a contract called DelayedBatchGroth16Verify. Let's say, for instance, that I am withdrawing from Torando Cash. Then, I have two phases. One, I send my proof + public parameters to the DelayedBatchGroth16Verify contract along with a small amount of eth (say, calldata cost of that many parameters + a tip). That contract, say ~12 hours, collects all the proofs sent to it. It then uses Snarkpack or analogous (via additivity of KZG commitments) to verify all of the proofs at once. Note that calculations are in Gt so it will not be gas efficient.  However, anyone can batch verify and send as soon as the size of the tips in the contract exceeds the cost of a single KZG verification. Once such a verify passes, it stores say hash(proof, public) in a "passed proofs" mapping. Thus, once someone has verified for me cheaper than a single verify, I can send a second transaction to tornado cash that just checks that the proof + public parameters have been part of a past batch verification (for instance, by hashing all of them and checking that it is a valid mapping key mapping to a 1), and then continues with the rest of the logic. While long-term we expect to not need this due to exceedingly cheapening L2 costs, it will be useful for the next 2 years while we do not have robust ZK L2-to-L2 bridges or audited ZK rollups.
- ~~ed25519 encryption in a ZK SNARK (using circom). Metamask's [encrypt](https://github.com/MetaMask/eth-sig-util/blob/main/src/encryption.ts#L94) function on chain would be new, and save people from having to use MIMC as an encryption function.~~
  - Edit: This is [done](https://ethresear.ch/t/verify-ed25519-signatures-cheaply-on-eth-using-zk-snarks/13139).
- ~~DNS record cert proving in SNARK. Prove the consecutive signatures for root signatures, CA signatures, etc, to be able to verify that some specific string in a name record was signed by a valid chain of authorities. Would likely use sig-verify circuits in circom.~~
  - Edit: Realized ENS's DNS oracle already has this, but only like 35 websites in the Alexa 100K use DNSSEC, so it is fairly irrelevant. We are too early: another idea is to offer an airdrop or some other incentive to everyone who does do this in the Alexa Top 100K.
- ~~Integrate Nova as a proving backend in circom, with Solidity verifiers~~
  - Edit: [Circom-nova](https://github.com/nalinbhardwaj/Nova-Scotia) is done.
- ~~Create an OSS, easy frontend for the [weth contract](https://etherscan.io/address/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2#code) with just three buttons: connect to web3, wrap, and withdraw.~~
  - Edit: Just discovered https://wrapeth.com/, existed for 2+ years, and is open source. This bounty is no longer offered!
- ~~Add a nice frontend to https://github.com/nulven/zk-message-board, and build a proof-of-concept anonymous group posting app powered by zero-knowledge proofs.~~
  - Edit: Done by https://heyanon.xyz.
