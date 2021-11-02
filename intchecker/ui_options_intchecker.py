# -*- coding: utf-8 -*-

from PyQt5.QtCore import (
	QCoreApplication,
	QMetaObject
)

from PyQt5.QtWidgets import (
	QGridLayout,
	QGroupBox,
	QVBoxLayout,
	QLabel,
	QLineEdit,
	QAbstractSpinBox,
	QSpinBox,
	QSpacerItem,
	QSizePolicy
)

class Ui_IntCheckerOptionsPage(object):
    def setupUi(self, IntCheckerOptionsPage):
        if not IntCheckerOptionsPage.objectName():
            IntCheckerOptionsPage.setObjectName(u"IntCheckerOptionsPage")
        IntCheckerOptionsPage.resize(677, 563)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(IntCheckerOptionsPage.sizePolicy().hasHeightForWidth())
        IntCheckerOptionsPage.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(IntCheckerOptionsPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.TopGBox = QGroupBox(IntCheckerOptionsPage)
        self.TopGBox.setObjectName(u"TopGBox")
        self.TopGBox.setFlat(True)
        self.verticalLayout = QVBoxLayout(self.TopGBox)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 12, -1, 12)
        self.MP3GBox = QGroupBox(self.TopGBox)
        self.MP3GBox.setObjectName(u"MP3GBox")
        self.MP3GBox.setFlat(True)
        self.MP3GBox.setCheckable(False)
        self.gridLayout_2 = QGridLayout(self.MP3GBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.mp3_min_brate = QSpinBox(self.MP3GBox)
        self.mp3_min_brate.setObjectName(u"mp3_min_brate")
        self.mp3_min_brate.setAccelerated(False)
        self.mp3_min_brate.setMinimum(32)
        self.mp3_min_brate.setMaximum(320)
        self.mp3_min_brate.setSingleStep(8)
        self.mp3_min_brate.setValue(128)

        self.gridLayout_2.addWidget(self.mp3_min_brate, 1, 4, 1, 1)

        self.mpck_path = QLineEdit(self.MP3GBox)
        self.mpck_path.setObjectName(u"mpck_path")
        self.mpck_path.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.mpck_path, 0, 1, 1, 5)

        self.mp3_min_brate_label = QLabel(self.MP3GBox)
        self.mp3_min_brate_label.setObjectName(u"mp3_min_brate_label")

        self.gridLayout_2.addWidget(self.mp3_min_brate_label, 1, 3, 1, 1)

        self.mpck_cmd_label = QLabel(self.MP3GBox)
        self.mpck_cmd_label.setObjectName(u"mpck_cmd_label")

        self.gridLayout_2.addWidget(self.mpck_cmd_label, 0, 0, 1, 1)

        self.mp3_srate_label = QLabel(self.MP3GBox)
        self.mp3_srate_label.setObjectName(u"mp3_srate_label")

        self.gridLayout_2.addWidget(self.mp3_srate_label, 1, 0, 1, 1)

        self.mp3_min_srate = QSpinBox(self.MP3GBox)
        self.mp3_min_srate.setObjectName(u"mp3_min_srate")
        self.mp3_min_srate.setFrame(False)
        self.mp3_min_srate.setReadOnly(False)
        self.mp3_min_srate.setAccelerated(False)
        self.mp3_min_srate.setKeyboardTracking(True)
        self.mp3_min_srate.setProperty("showGroupSeparator", False)
        self.mp3_min_srate.setMinimum(32000)
        self.mp3_min_srate.setMaximum(48000)
        self.mp3_min_srate.setSingleStep(100)
        self.mp3_min_srate.setStepType(QAbstractSpinBox.DefaultStepType)
        self.mp3_min_srate.setValue(44100)

        self.gridLayout_2.addWidget(self.mp3_min_srate, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 5, 1, 1)


        self.verticalLayout.addWidget(self.MP3GBox)

        self.OGGGBox = QGroupBox(self.TopGBox)
        self.OGGGBox.setObjectName(u"OGGGBox")
        self.OGGGBox.setFlat(True)
        self.gridLayout_3 = QGridLayout(self.OGGGBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.ogg_min_brate = QSpinBox(self.OGGGBox)
        self.ogg_min_brate.setObjectName(u"ogg_min_brate")
        self.ogg_min_brate.setAccelerated(False)
        self.ogg_min_brate.setMinimum(32)
        self.ogg_min_brate.setMaximum(500)
        self.ogg_min_brate.setSingleStep(16)
        self.ogg_min_brate.setValue(128)

        self.gridLayout_3.addWidget(self.ogg_min_brate, 1, 4, 1, 1)

        self.ogg_min_brate_label = QLabel(self.OGGGBox)
        self.ogg_min_brate_label.setObjectName(u"ogg_min_brate_label")

        self.gridLayout_3.addWidget(self.ogg_min_brate_label, 1, 3, 1, 1)

        self.ogg_min_srate = QSpinBox(self.OGGGBox)
        self.ogg_min_srate.setObjectName(u"ogg_min_srate")
        self.ogg_min_srate.setMinimum(8000)
        self.ogg_min_srate.setMaximum(192000)
        self.ogg_min_srate.setSingleStep(100)
        self.ogg_min_srate.setValue(44100)

        self.gridLayout_3.addWidget(self.ogg_min_srate, 1, 1, 1, 1)

        self.ogginfo_cmd_label = QLabel(self.OGGGBox)
        self.ogginfo_cmd_label.setObjectName(u"ogginfo_cmd_label")

        self.gridLayout_3.addWidget(self.ogginfo_cmd_label, 0, 0, 1, 1)

        self.ogg_min_srate_label = QLabel(self.OGGGBox)
        self.ogg_min_srate_label.setObjectName(u"ogg_min_srate_label")

        self.gridLayout_3.addWidget(self.ogg_min_srate_label, 1, 0, 1, 1)

        self.ogginfo_path = QLineEdit(self.OGGGBox)
        self.ogginfo_path.setObjectName(u"ogginfo_path")

        self.gridLayout_3.addWidget(self.ogginfo_path, 0, 1, 1, 5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 1, 5, 1, 1)


        self.verticalLayout.addWidget(self.OGGGBox)

        self.FLACGBox = QGroupBox(self.TopGBox)
        self.FLACGBox.setObjectName(u"FLACGBox")
        self.FLACGBox.setFlat(True)
        self.gridLayout_4 = QGridLayout(self.FLACGBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.flac_min_srate_label = QLabel(self.FLACGBox)
        self.flac_min_srate_label.setObjectName(u"flac_min_srate_label")

        self.gridLayout_4.addWidget(self.flac_min_srate_label, 1, 0, 1, 1)

        self.flac_min_srate = QSpinBox(self.FLACGBox)
        self.flac_min_srate.setObjectName(u"flac_min_srate")
        self.flac_min_srate.setMinimum(10)
        self.flac_min_srate.setMaximum(655350)
        self.flac_min_srate.setSingleStep(10)
        self.flac_min_srate.setValue(44100)

        self.gridLayout_4.addWidget(self.flac_min_srate, 1, 1, 1, 1)

        self.flac_spacer2 = QSpacerItem(239, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.flac_spacer2, 1, 3, 1, 1)

        self.flac_cmd_label = QLabel(self.FLACGBox)
        self.flac_cmd_label.setObjectName(u"flac_cmd_label")

        self.gridLayout_4.addWidget(self.flac_cmd_label, 0, 0, 1, 1)

        self.flac_spacer1 = QSpacerItem(115, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.flac_spacer1, 1, 2, 1, 1)

        self.flac_path = QLineEdit(self.FLACGBox)
        self.flac_path.setObjectName(u"flac_path")

        self.gridLayout_4.addWidget(self.flac_path, 0, 1, 1, 3)


        self.verticalLayout.addWidget(self.FLACGBox)

        self.WVGBox = QGroupBox(self.TopGBox)
        self.WVGBox.setObjectName(u"WVGBox")
        self.WVGBox.setFlat(True)
        self.gridLayout_5 = QGridLayout(self.WVGBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.wvunpack_path = QLineEdit(self.WVGBox)
        self.wvunpack_path.setObjectName(u"wvunpack_path")

        self.gridLayout_5.addWidget(self.wvunpack_path, 0, 1, 1, 3)

        self.wavpack_min_srate_label = QLabel(self.WVGBox)
        self.wavpack_min_srate_label.setObjectName(u"wavpack_min_srate_label")

        self.gridLayout_5.addWidget(self.wavpack_min_srate_label, 1, 0, 1, 1)

        self.wavpack_spacer2 = QSpacerItem(145, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.wavpack_spacer2, 1, 3, 1, 1)

        self.wavpack_min_srate = QSpinBox(self.WVGBox)
        self.wavpack_min_srate.setObjectName(u"wavpack_min_srate")
        self.wavpack_min_srate.setMinimum(10)
        self.wavpack_min_srate.setMaximum(655350)
        self.wavpack_min_srate.setSingleStep(10)
        self.wavpack_min_srate.setValue(44100)

        self.gridLayout_5.addWidget(self.wavpack_min_srate, 1, 1, 1, 1)

        self.wavpack_spacer1 = QSpacerItem(145, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.wavpack_spacer1, 1, 2, 1, 1)

        self.wvunpack_cmd_label = QLabel(self.WVGBox)
        self.wvunpack_cmd_label.setObjectName(u"wvunpack_cmd_label")

        self.gridLayout_5.addWidget(self.wvunpack_cmd_label, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.WVGBox)


        self.gridLayout.addWidget(self.TopGBox, 0, 0, 1, 1)


        self.retranslateUi(IntCheckerOptionsPage)

        QMetaObject.connectSlotsByName(IntCheckerOptionsPage)
    # setupUi

    def retranslateUi(self, IntCheckerOptionsPage):
        IntCheckerOptionsPage.setWindowTitle(QCoreApplication.translate("IntCheckerOptionsPage", u"Integrity Checker", None))
        self.TopGBox.setTitle(QCoreApplication.translate("IntCheckerOptionsPage", u"Integrity Checker", None))
        self.MP3GBox.setTitle(QCoreApplication.translate("IntCheckerOptionsPage", u"MP3 Settings", None))
        self.mpck_path.setPlaceholderText(QCoreApplication.translate("IntCheckerOptionsPage", u"mpck", None))
        self.mp3_min_brate_label.setText(QCoreApplication.translate("IntCheckerOptionsPage", u"Minimum Bitrate:", None))
        self.mpck_cmd_label.setText(QCoreApplication.translate("IntCheckerOptionsPage", u"Path to CheckMate (mpck):", None))
        self.mp3_srate_label.setText(QCoreApplication.translate("IntCheckerOptionsPage", u"Minimum Sampling rate:", None))
        self.OGGGBox.setTitle(QCoreApplication.translate("IntCheckerOptionsPage", u"OGG Settings", None))
        self.ogg_min_brate_label.setText(QCoreApplication.translate("IntCheckerOptionsPage", u"Minimum Bitrate:", None))
        self.ogginfo_cmd_label.setText(QCoreApplication.translate("IntCheckerOptionsPage", u"Path to ogginfo:", None))
        self.ogg_min_srate_label.setText(QCoreApplication.translate("IntCheckerOptionsPage", u"Minimum Sampling rate:", None))
        self.ogginfo_path.setPlaceholderText(QCoreApplication.translate("IntCheckerOptionsPage", u"ogginfo", None))
        self.FLACGBox.setTitle(QCoreApplication.translate("IntCheckerOptionsPage", u"FLAC Settings", None))
        self.flac_min_srate_label.setText(QCoreApplication.translate("IntCheckerOptionsPage", u"Minimum Sampling rate:", None))
        self.flac_cmd_label.setText(QCoreApplication.translate("IntCheckerOptionsPage", u"Path to flac (tool):", None))
        self.flac_path.setPlaceholderText(QCoreApplication.translate("IntCheckerOptionsPage", u"flac", None))
        self.WVGBox.setTitle(QCoreApplication.translate("IntCheckerOptionsPage", u"WavPack Settings", None))
        self.wvunpack_path.setPlaceholderText(QCoreApplication.translate("IntCheckerOptionsPage", u"wvunpack", None))
        self.wavpack_min_srate_label.setText(QCoreApplication.translate("IntCheckerOptionsPage", u"Minimum Sampling rate:", None))
        self.wvunpack_cmd_label.setText(QCoreApplication.translate("IntCheckerOptionsPage", u"Path to wvunpack:", None))
    # retranslateUi



