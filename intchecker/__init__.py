PLUGIN_NAME = "File integrity checker"
PLUGIN_AUTHOR = "Nick Kossifidis"
PLUGIN_DESCRIPTION = "Verifies file integrity on load (only works for mp3/ogg/flac/wavpack)"
PLUGIN_VERSION = '0.1'
PLUGIN_API_VERSIONS = ['2.2']
PLUGIN_LICENSE = "GPL-2.0-or-later"
PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-2.0.html"

INTEGRITY_CHECKS = {
    "MPEG-1 Audio": ("intchecker_mpck_path", "-q", "intchecker_mp3_min_srate", "intchecker_mp3_min_brate"),
    "Ogg Vorbis": ("intchecker_ogginfo_path", "-q", "intchecker_ogg_min_srate", "intchecker_mp3_min_brate"),
    "FLAC": ("intchecker_flac_path", "-t", "intchecker_flac_min_srate", -1),
    "WavPack": ("intchecker_wvunpack_path", "-vv", "intchecker_flac_min_srate", -1)
}

from picard import log
from picard.file import (
	File,
	register_file_post_load_processor
)
from picard.util import encode_filename
from os.path import basename
from subprocess import (
	check_call,
	CalledProcessError
)

from picard.config import (
	TextOption,
	IntOption,
	FloatOption,
	BoolOption
)

from picard.ui.options import (
	OptionsPage,
	register_options_page
)

from picard.plugins.intchecker.ui_options_intchecker import Ui_IntCheckerOptionsPage

def integrity_check(infile):
	log.debug("[INTCHECKER] Got file: %s, format: %s", infile.filename, infile.NAME)
	_format = infile.NAME
	if _format in INTEGRITY_CHECKS:

		tagger = infile.tagger
		command = tagger.config.setting[INTEGRITY_CHECKS[_format][0]]
		options = INTEGRITY_CHECKS[_format][1].split(' ')
		filename = infile.filename
		min_srate = int(tagger.config.setting[INTEGRITY_CHECKS[_format][2]])
		if isinstance(INTEGRITY_CHECKS[_format][3], int):
			min_brate = -1.0
		else:
			min_brate = float(tagger.config.setting[INTEGRITY_CHECKS[_format][3]])

		log.debug("[INTCHECKER] min_srate: %s, min_brate: %s", min_srate, min_brate)

		# Check if bitrate  / sampling rate is below minimum
		metadata_keys = set(infile.metadata.keys())

		if "~sample_rate" in metadata_keys:
			sample_rate = int(infile.metadata['~sample_rate'])
			log.debug("[INTCHECKER] got sample rate: %s", sample_rate)
			if sample_rate < min_srate:
				log.error("[INTCHECKER] sample rate too low (%s): %s", sample_rate, filename)
				infile.error = "Sample rate too low"
				infile.state = File.ERROR
				return
		else:
			log.error("[INTCHECKER] could not determine sample rate: %s", filename)
			infile.error = "Integrity checker could not determine sample rate"
			infile.state = File.ERROR
			return

		if "~bitrate" in metadata_keys:
			bitrate = float(infile.metadata['~bitrate'])
			log.debug("[INTCHECKER] got bitrate: %s", bitrate)
			if bitrate < min_brate:
				log.error("[INTCHECKER] bitrate too low (%s): %s", bitrate, filename)
				infile.error = "Bitrate too low"
				infile.state = File.ERROR
				return
		elif min_brate > 0:
			log.error("[INTCHECKER] could not determine bitrate: %s", filename)
			infile.error = "Integrity checker could not determine bitrate"
			infile.state = File.ERROR
			return

		# Verify file integrity
		tagger.window.set_statusbar_message("Verifying integrity of '%(filename)s'",
			{'filename': basename(filename)}, timeout=3000)
		try:
			check_call([command] + options + [encode_filename(filename)])
		except CalledProcessError as error:
			log.error("[INTCHECKER] check failed for: %s", filename)
			infile.error = "Integrity check failed"
			infile.state = File.ERROR
	else:
		log.error("[INTCHECKER] unsupported format: %s", infile.filename)
		infile.error = "Integrity checker doesn't support this format"
		infile.state = File.ERROR
	return


class IntCheckerOptionsPage(OptionsPage):
	NAME = "intchecker"
	TITLE = "File integrity checker"
	PARENT = "plugins"

	options = [
		TextOption("setting", "intchecker_mpck_path", "mpck"),
		IntOption("setting", "intchecker_mp3_min_srate", 44100),
		FloatOption("setting", "intchecker_mp3_min_brate", 128.0),
		TextOption("setting", "intchecker_ogginfo_path", "ogginfo"),
		IntOption("setting", "intchecker_ogg_min_srate", 44100),
		FloatOption("setting", "intchecker_ogg_min_brate", 128.0),
		TextOption("setting", "intchecker_flac_path", "flac"),
		IntOption("setting", "intchecker_flac_min_srate", 44100),
		TextOption("setting", "intchecker_wvunpack_path", "wvunpack"),
		IntOption("setting", "intchecker_wavpack_min_srate", 44100),
	]

	def __init__(self, parent=None):
		super(IntCheckerOptionsPage, self).__init__(parent)
		self.ui = Ui_IntCheckerOptionsPage()
		self.ui.setupUi(self)

	def load(self):
		self.ui.mpck_path.setText(self.config.setting["intchecker_mpck_path"])
		self.ui.mp3_min_srate.setValue(self.config.setting["intchecker_mp3_min_srate"])
		self.ui.mp3_min_brate.setValue(self.config.setting["intchecker_mp3_min_brate"])

		self.ui.ogginfo_path.setText(self.config.setting["intchecker_ogginfo_path"])
		self.ui.ogg_min_srate.setValue(self.config.setting["intchecker_ogg_min_srate"])
		self.ui.ogg_min_brate.setValue(self.config.setting["intchecker_ogg_min_brate"])

		self.ui.flac_path.setText(self.config.setting["intchecker_flac_path"])
		self.ui.flac_min_srate.setValue(self.config.setting["intchecker_flac_min_srate"])

		self.ui.wvunpack_path.setText(self.config.setting["intchecker_wvunpack_path"])
		self.ui.wavpack_min_srate.setValue(self.config.setting["intchecker_wavpack_min_srate"])


	def save(self):
		self.config.setting["intchecker_mpck_path"] = self.ui.mpck_path.text()
		self.config.setting["intchecker_mp3_min_srate"] = self.ui.mp3_min_srate.value()
		self.config.setting["intchecker_mp3_min_brate"] = self.ui.mp3_min_brate.value()

		self.config.setting["intchecker_ogginfo_path"] = self.ui.ogginfo_path.text()
		self.config.setting["intchecker_ogg_min_srate"] = self.ui.ogg_min_srate.value()
		self.config.setting["intchecker_ogg_min_brate"] = self.ui.ogg_min_brate.value()

		self.config.setting["intchecker_flac_path"] = self.ui.flac_path.text()
		self.config.setting["intchecker_flac_min_srate"] = self.ui.flac_min_srate.value()

		self.config.setting["intchecker_wvunpack_path"] = self.ui.wvunpack_path.text()
		self.config.setting["intchecker_wavpack_min_srate"] = self.ui.wavpack_min_srate.value()


register_file_post_load_processor(integrity_check)
register_options_page(IntCheckerOptionsPage)
