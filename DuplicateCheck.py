PLUGIN_NAME = "Prevent duplicates"
PLUGIN_AUTHOR = "Nick Kossifidis"
PLUGIN_DESCRIPTION = "Marks files added to the track processor, that would overlap with existing files after renaming/moving"
PLUGIN_VERSION = '0.2'
PLUGIN_API_VERSIONS = ['2.2']
PLUGIN_LICENSE = "GPL-2.0-or-later"
PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-2.0.html"

from os import path
from pathlib import Path
import glob
from picard import (
	log,
	config
)
from picard.file import (
	File,
	register_file_post_addition_to_track_processor
)
from picard.util import encode_filename
from picard.track import Track

# This plugin assumes that user maintains the same filenaming rules/script
# since it checks for existing filenames. If the same file is saved in
# a different way this won't work.

def prevent_from_saving(intrack, infile, error_msg):
	intrack.album.errors.append(error_msg)
	log.debug(type(infile.item))
#	Since the fis for this: https://tickets.metabrainz.org/browse/PICARD-1914
#	we can't move the matching file from the track to the album's
#	umnatched_files cluster to prevent it from being saved when the
#	user saves the album. The next best thing is to mark the file
#	as File.REMOVED which acomblishes the same thing (but now the
#	user needs to remove and re-add the files to try again).
#
#	infile.move(intrack.album.unmatched_files)
	infile.remove(from_parent=False)

def duplicate_check(intrack, infile):
	log.debug("[DUPCHECKER] Got file: %s, format: %s", infile.filename, infile.NAME)

	# No need to do anything if the file is not to be renamed/moved
	if (not (config.setting["rename_files"] or config.setting["move_files"])):
		log.debug("[DUPCHECKER] renaming/moving disabled, moving on")
		return

	# Get the old/new filename, split the extensions and compare them
	old_filename, old_ext = path.splitext(infile.filename)
	new_filename, new_ext = path.splitext(infile.make_filename(infile.filename, infile.metadata))
	log.debug("[DUPCHECKER] Old filename: %s, new filename: %s", old_filename, new_filename)

	# Is it the same ? Are we overwriting / re-tagging the file ?
	if infile.filename == new_filename + new_ext:
		log.debug("[DUPCHECKER] it's the same file, moving on")
		return

	# Check if a file with the same path/filename already exists
	if path.exists(new_filename + new_ext):
		log.debug("[DUPCHECKER] %s already exists on destination", new_filename + new_ext)
		error_msg = "[DUPCHECKER] '" + path.basename(new_filename + new_ext) + "' already exists on destination"
		prevent_from_saving(intrack, infile, error_msg)
		return

	# Check if a file with the same path/filename but with different extension exists
	# Also cover the case of "title (1).ext" where picard has placed the "(x)" part
	# before. Finaly make sure we do a case insensitive search, since sometimes the
	# initials of album/titles may change due to different plugins used (e.g. title case).
	search_pattern = glob.escape(new_filename) + "*"
	log.debug("[DUPCHECKER] searching for files matching %s", search_pattern)

	def either(c):
	        return '[%s%s]' % (c.lower(), c.upper()) if c.isalpha() else c

	if glob.glob(''.join(either(char) for char in search_pattern)):
		log.debug("[DUPCHECKER] %s already exists on destination", new_filename)
		error_msg = "[DUPCHECKER] '" + path.basename(new_filename) + "' already exists on destination"
		prevent_from_saving(intrack, infile, error_msg)
		return


	# UoC-Radio specific: Check if a file named "lock" exists on the parent directory
	# of the destination directory (where the album will be saved)
	target_directory = Path(path.dirname(new_filename))
	parent_directory = target_directory.parent
	log.debug("[DUPCHECKER] parent directory: %s", parent_directory)
	if path.exists(str(parent_directory) + path.sep + "lock"):
		log.debug("[DUPCHECKER] parent directory is locked")
		error_msg = "[DUPCHECKER] parent directory of " + path.basename(new_filename)+ " is locked"
		prevent_from_saving(intrack, infile, error_msg)

register_file_post_addition_to_track_processor(duplicate_check)
