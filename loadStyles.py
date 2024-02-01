from PyQt6.QtCore import QFile, QIODevice, QTextStream


def parse_css_styles(tag: str, css_file: str) -> str:
    """tag - your tag in style sheet, css_file - the way to your style file.
     The function return a string with styles for your tag"""
    style_sheet = ''
    style_sheet_file = QFile(css_file)
    if style_sheet_file.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text):
        style_sheet = QTextStream(style_sheet_file).readAll()
    tag_index = style_sheet.find(tag)
    style = ''
    if tag_index >= 0:
        start = style_sheet.find('{', tag_index)
        end = style_sheet.find('}', tag_index)
        style = style_sheet[start + 1:end].strip()
    return style
