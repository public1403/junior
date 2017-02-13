#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import listdir
from os.path import isfile, join


head = """
<div class="mdui-col-md-4">
<div class="mdui-panel" mdui-panel>
  <div class="mdui-panel-item mdui-panel-item-open">

      <div class="mdui-panel-item-header">
            <div>数字图像处理</div>
      <i class="mdui-panel-item-arrow mdui-icon material-icons">&#xe313;</i>
  </div>
      <div class="mdui-panel-item-body">
          <div style=" position: relative;">
"""

tail = """
    </div>
    </div>
  </div>
</div>
</div>
"""

def getmiddle():
    left = '<button id="zz" class="mdui-btn mdui-btn-raised mdui-ripple mdui-color-theme-accent" style="width:100%"><a style="color:#E0F7FA; text-decoration:none" href="./'
    right = '</a></button>'
    center = ''
    for filename in listdir("."):
        if filename.endswith(".zip") or filename.endswith(".ppt") or filename.endswith(".pptx"):
            center += left + filename + '">' + filename + right + '\n'
    return center


final = head + getmiddle() + tail

with open("dip.html", 'w') as f:
    f.write(final)
    f.close

    











