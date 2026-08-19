# **HTML Audio, Video \& Poster**

**HTML provides built-in tags to add audio and video content directly to a webpage without requiring external plugins.**



**The main elements are:**



**<audio> → adds audio**

**<video> → adds video**

**poster → displays an image before a video starts**



**1. HTML Audio**



**The <audio> element is used to embed an audio file in a webpage.**



**Basic syntax**

**<audio controls>**

&#x20;   **<source src="song.mp3" type="audio/mpeg">**

**</audio>**



**The controls attribute displays the browser's audio controls such as:**



**Play**

**Pause**

**Volume**

**Progress bar**



**Important Audio Attributes**

**controls**



**Displays audio controls.**



**<audio controls>**

&#x20;   **<source src="music.mp3" type="audio/mpeg">**

**</audio>**

**autoplay**



**Automatically starts playing the audio.**



**<audio autoplay>**

&#x20;   **<source src="music.mp3" type="audio/mpeg">**

**</audio>**



**⚠️ Modern browsers may block autoplay, especially when the audio has sound.**



**loop**



**Repeats the audio continuously.**



**<audio controls loop>**

&#x20;   **<source src="music.mp3" type="audio/mpeg">**

**</audio>**

**muted**



**Starts the audio in muted mode.**



**<audio controls muted>**

&#x20;   **<source src="music.mp3" type="audio/mpeg">**

**</audio>**

**preload**



**Specifies how the browser should load the audio.**



**Possible values:**



**none**

**metadata**

**auto**



**Example:**



**<audio controls preload="metadata">**

&#x20;   **<source src="music.mp3" type="audio/mpeg">**

**</audio>**

**2. <source> Element**



**<source> specifies the actual media file.**



**<source src="music.mp3" type="audio/mpeg">**

**Important attributes**



**src → location of the media file.**



**type → MIME type of the media.**



**Examples:**



**type="audio/mpeg"**

**type="audio/ogg"**

**type="audio/wav"**



**Using <source> is useful because you can provide multiple formats.**



**<audio controls>**





&#x20;   **<source src="music.mp3" type="audio/mpeg">**

&#x20;   **<source src="music.ogg" type="audio/ogg">**





&#x20;   **Your browser does not support audio.**





**</audio>**



**The browser chooses a supported format.**



**3. HTML Video**



**The <video> element is used to embed a video file into a webpage.**



**Basic syntax**

**<video controls width="500">**

&#x20;   **<source src="video.mp4" type="video/mp4">**

**</video>**

**Important Video Attributes**

**controls**



**Displays video controls.**



**<video controls>**



**Controls include:**



**Play/Pause**

**Volume**

**Progress bar**

**Full screen**

**Playback options, depending on browser**

**width**



**Sets the width of the video.**



**<video width="600">**

**height**



**Sets the height.**



**<video width="600" height="400">**

**autoplay**



**Automatically starts the video.**



**<video autoplay>**



**Autoplay is commonly used together with muted because browsers often restrict autoplay with sound.**



**<video autoplay muted>**

**loop**



**Repeats the video continuously.**



**<video controls loop>**

**muted**



**Starts the video without sound.**



**<video controls muted>**

**preload**



**Specifies how the browser should load the video.**



**<video controls preload="metadata">**



**Values:**



**none**

**metadata**

**auto**

**4. Poster Attribute ⭐**



**This is an important one.**



**The poster attribute specifies an image that is displayed before the video starts playing.**



**Syntax**

**<video controls poster="thumbnail.jpg">**

&#x20;   **<source src="video.mp4" type="video/mp4">**

**</video>**



**Think of poster as the thumbnail/cover image of a video.**



**For example:**



**Before video starts:**





**┌─────────────────────────────┐**

**│                             │**

**│       VIDEO THUMBNAIL       │**

**│                             │**

**│             ▶               │**

**│                             │**

**└─────────────────────────────┘**



**Once the video starts, the poster is replaced by the video.**



**Important**



**poster is an attribute of <video>, not a separate HTML tag.**



**<video poster="image.jpg">**

**5. Audio vs Video**

**Feature	Audio	Video**

**Tag	<audio>	<video>**

**Used for	Sound	Video**

**controls	Yes	Yes**

**autoplay	Yes	Yes**

**loop	Yes	Yes**

**muted	Yes	Yes**

**poster	❌ No	✅ Yes**

**width	Usually not needed	Yes**

**height	Usually not needed	Yes**



**6. Common Audio Formats**

**Format	MIME Type**

**MP3	audio/mpeg**

**WAV	audio/wav**

**OGG	audio/ogg**



**Example:**



**<audio controls>**

&#x20;   **<source src="song.mp3" type="audio/mpeg">**

**</audio>**



**7. Common Video Formats**

**Format	MIME Type**

**MP4	video/mp4**

**WebM	video/webm**

**OGG	video/ogg**



**The most commonly used format is MP4.**

