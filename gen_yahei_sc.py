import utils
import shutil as fs


def gen_yahei_regular_sc():
    fs.copy(utils.DOWNLOAD_DIR + '/SarasaMonoSC-Regular.ttf', utils.DOWNLOAD_DIR + '/SarasaMonoSC-Regular-ui.ttf')

    font = utils.open_font(utils.DOWNLOAD_DIR + '/SarasaMonoSC-Regular.ttf')
    utils.remove_gasp(font)
    utils.set_cleartype(font)
    utils.set_yahei_regular_names(font)

    font_ui = utils.open_font(utils.DOWNLOAD_DIR + '/SarasaMonoSC-Regular-ui.ttf')
    utils.remove_gasp(font_ui)
    utils.set_cleartype(font_ui)
    utils.set_yahei_regular_ui_names(font_ui)

    font.generateTtc(utils.OUTPUT_DIR_SC + '/msyh.ttc', font_ui, ttcflags = ('merge'), layer = 1)

def gen_yahei_light_sc():
    fs.copy(utils.DOWNLOAD_DIR + '/SarasaMonoSC-Light.ttf', utils.DOWNLOAD_DIR + '/SarasaMonoSC-Light-ui.ttf')

    font = utils.open_font(utils.DOWNLOAD_DIR + '/SarasaMonoSC-Light.ttf')
    utils.remove_gasp(font)
    utils.set_cleartype(font)
    utils.set_yahei_light_names(font)

    font_ui = utils.open_font(utils.DOWNLOAD_DIR + '/SarasaMonoSC-Light-ui.ttf')
    utils.remove_gasp(font_ui)
    utils.set_cleartype(font_ui)
    utils.set_yahei_light_ui_names(font_ui)

    font.generateTtc(utils.OUTPUT_DIR_SC + '/msyhl.ttc', font_ui, ttcflags = ('merge'), layer = 1)

def gen_yahei_bold_sc():
    fs.copy(utils.DOWNLOAD_DIR + '/SarasaMonoSC-Bold.ttf', utils.DOWNLOAD_DIR + '/SarasaMonoSC-Bold-ui.ttf')

    font = utils.open_font(utils.DOWNLOAD_DIR + '/SarasaMonoSC-Bold.ttf')
    utils.remove_gasp(font)
    utils.set_cleartype(font)
    utils.set_yahei_bold_names(font)

    font_ui = utils.open_font(utils.DOWNLOAD_DIR + '/SarasaMonoSC-Bold-ui.ttf')
    utils.remove_gasp(font_ui)
    utils.set_cleartype(font_ui)
    utils.set_yahei_bold_ui_names(font_ui)

    font.generateTtc(utils.OUTPUT_DIR_SC + '/msyhbd.ttc', font_ui, ttcflags = ('merge'), layer = 1)
