EPG = "EPG/tvtv.us.guide.xml"
EPG1 = "EPG/CZ.xml"
Out = "EPG/EPG.xml"

merge = "tv_merge -d -i " + EPG + " -m " + EPG1 + " -o " + Out
