#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sublime, sublime_plugin

class EscapeCommand(sublime_plugin.TextCommand):
    def html_escape(self, text):
        text = text.replace('&', '&amp;')
        text = text.replace('"', '&quot;')
        text = text.replace("'", '&#39;')
        text = text.replace(">", '&gt;')
        text = text.replace("<", '&lt;')
        text = text.encode('ascii', 'xmlcharrefreplace')
        text = text.replace("\t", " ").replace("  ", " ")
        text = text.replace("\n", "").replace("\r", "")
        return text

    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                line = self.view.substr(region)
                line = self.html_escape(line)
                self.view.replace(edit, region, line)