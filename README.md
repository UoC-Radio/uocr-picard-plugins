# UoC Radio Picard plugins

These are the plugins we use with Musicbrainz Picard to keep our Music Library consistent and ensure its quality, together with [Library Guardian](https://github.com/UoC-Radio/libguard).

* Integrity checker performs an integrity check (using external tools -see the defaults-) on the files we add to Picard to make sure we don't put corrupted files on our Library (it's ok for ogg/flac/wavpack, it tries its best for mp3s).

* Duplicate checker, prevents our users from saving the same album multiple times, instead it sets an error and the user needs to manualy check out and remove the album from the library to add the new version if needed.

To use them copy them to ~/.config/MusicBrainz/Picard/plugins and enable them on Picard's Options -> Plugins.

Our Picard naming script is this one (paste it in the box on Options -> File Naming):

```
$noop(Set this to 1 for Production music, 2 for Classical music, 0 for default)
$set(_uocr_release_type,0)

$noop(Convert three dots to ellipsis)
$set(title,$replace(%title%,...,…))
$set(album,$replace(%album%,...,…))
$noop(Add \(Live\) at the end of live tracks and \(Compilation\) at the end of compilation albums
-but not from Various Artists since those are always compilations-)
$if($and($inmulti(%releasetype%,live),$not($in(%title%,\(Live\)))),$set(title,%title% \(Live\)))
$if($and($and($eq(%compilation%,1),$ne(%albumartist%,Various Artists)),$not($in(%album%,\(Compilation\)))),$set(album,%album% \(Compilation\)))
$noop(Add original year before the album's name in case of normal releases and after the album's name for Various Artists
-so that compilation series are groupped together-, or Production Music -since we put the artist and album together-)
$if($ne(%_uocr_release_type%,1),
$if($and($ne(%albumartist%,Various Artists),%originalyear%),$set(album,\(%originalyear%\) %album%))
$if($and($eq(%albumartist%,Various Artists),%originalyear%),$set(album,%album% \(%originalyear%\))),
$if(%originalyear%,$set(album,%album% \(%originalyear%\))))

$set(_uocr_album_0,$if2(%albumartist%,%artist%)/$if($ne(%albumartist%,),%album%,Standalone Recordings))
$set(_uocr_album_1,$if(%catalognumber%,%catalognumber% - ,)$if($and(%albumartist%,$ne(%albumartist%,Various Artists)),%albumartist% - ,)%album%)

$set(_uocr_title,$if($gt(%totaldiscs%,1),Disk %discnumber%$if(%discsubtitle%, - %discsubtitle%)/)$if($ne(%albumartist%,),$num(%tracknumber%,2) ,)$if(%_multiartist%,%artist% - ,)%title%)

$if($eq(%_uocr_release_type%,1),
Production Music/%label%/%_uocr_album_1%/%_uocr_title%,
$if($eq(%_uocr_release_type%,2),
Classical Music/%_uocr_album_0%/%_uocr_title%,
%_uocr_album_0%/%_uocr_title%))
```
and we also use the following Plugins as well (from Picard's repository):

* Standardise Performers
* Standardise Feat.
* Compatible TXXX frames

Finaly we want to also move various non-audio files to the Library such as artwork, informational texts, rip logs etc (Libguard will then sort them out in subfolders inside the album folder), so we also tell picard to grab such files as well, using the "Move aditional files" field:
```
*.jpg *.png *.tif *.JPG *.PNG *.txt *.TXT *.log *.accurip *.pdf lock ignore
```
the "lock" and "ignore" files are special, ignore tells Libguard to skip this folder/album, and lock tells picard (through the DuplicateChecker plugin) to not add any albums on the parent folder (e.g. for this artist / release).

Note that [Library Guardian](https://github.com/UoC-Radio/libguard) takes care of ReplayGain tagging, and for moving artwork/media and album infos on subfolders, along with anything else we need that can be performed offline, after the album has been saved. [Library Guardian](https://github.com/UoC-Radio/libguard) also performs integrity checking just in case.
