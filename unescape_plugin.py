#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sublime, sublime_plugin

class UnescapeCommand(sublime_plugin.TextCommand):

    def html_unescape(self, text):
        text = text.replace("&lt;", "<")
        text = text.replace("&gt;", ">")
        text = text.replace("&quot;", "\"")
        text = text.replace("&#39;", "'")
        text = text.replace("&amp;", "&")
        text = re.sub("&#(\d+);", lambda m: "%s" % unichr(int(m.group(1))), text)
        return text

    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                line = self.view.substr(region)
                line = self.html_unescape(line)
                self.view.replace(edit, region, line)