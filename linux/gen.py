#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import listdir
from os.path import isfile, join
import os


head = """
<div class="mdui-col-md-4">
<div class="mdui-panel" mdui-panel>
  <div class="mdui-panel-item mdui-panel-item-open">

      <div class="mdui-panel-item-header">
            <div>嵌入式linux(选修)</div>
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

def trans_size(filename):
    byts = os.path.getsize(filename)
    if byts <= 1024:
        return str(byts) + "B"
    elif byts <= 1024*1024:
        return str("%.1f" % (byts/1024.) ) + "KB"
    else:
        return str("%.1f" % (byts/1024./1024.) ) + "MB"
 

def getmiddle():
    left = '<button id="zz" class="mdui-btn mdui-btn-raised mdui-ripple mdui-color-theme-accent" style="width:100%"><a style="color:#E0F7FA; text-decoration:none" href="./linux/'
    right = '</a></button>'
    center = ''
    for filename in listdir("."):
        if filename.endswith(".zip") or filename.endswith(".pdf") or filename.endswith(".doc") or filename.endswith(".docx"):
            center += left + filename + '">' + filename +' '+ trans_size(filename) + right + '\n'
    return center


final = head + getmiddle() + tail

with open("linux.html", 'w') as f:
    f.write(final)
    f.close

    











