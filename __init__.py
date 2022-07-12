# -*- coding: utf-8 -*-
# inspired by Henrik Giesel: https://forums.ankiweb.net/t/access-to-dom-element-in-editorfield/8782/8
# published for https://forums.ankiweb.net/t/change-default-html-css-template-in-editing-mode/9902
# 2021 - Matthias Metelka @kleinerpirat

from aqt import mw
from aqt.gui_hooks import (
    webview_will_set_content,
    editor_will_load_note
)
from aqt.editor import Editor

mw.addonManager.setWebExports(__name__, r"(user_files)/.*\.(css|js)|(web)/.*\.(js)")

def append_webcontent(webcontent, context):
    global base_path
    if isinstance(context, Editor):
        addon_package = context.mw.addonManager.addonFromModule(__name__)
        base_path = f"/_addons/{addon_package}"

        webcontent.css.append(f"{base_path}/user_files/editor.css")
        webcontent.js.append(f"{base_path}/web/injector.js")


def inject_field_CSS(js, note, editor):
    global base_path
    path = f"{base_path}/user_files/field.css"

    return js + f"StyleInjector.inject('{path}', {note.mid});"


webview_will_set_content.append(append_webcontent)
editor_will_load_note.append(inject_field_CSS)
