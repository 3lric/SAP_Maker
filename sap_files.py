def get_sap_files(category):
    if category == "Core":
        return [
            "core00.sap", "core01.sap", "core11.sap", "core12.sap", "core13.sap", "core14.sap", "core15.sap",
            "core16.sap", "core17.sap", "core18.sap", "core19.sap", "core20.sap", "core21.sap", "core22.sap",
            "core32.sap", "core33.sap", "core34.sap", "core35.sap", "core36.sap", "core37.sap", "core38.sap"
        ]
    elif category == "Door":
        return [
            "door00.sap", "door01.sap", "door06.sap", "door10.sap", "door12.sap", "door14.sap", "door15.sap",
            "door16.sap", "door18.sap", "door19.sap", "door20.sap", "door21.sap", "door22.sap", "door23.sap",
            "door25.sap", "door27.sap", "door28.sap", "door29.sap", "door30.sap", "door31.sap", "door32.sap",
            "door33.sap", "door36.sap", "door37.sap", "door38.sap", "door39.sap", "door40.sap", "door42.sap",
            "door43.sap", "door44.sap", "door45.sap", "door46.sap", "door50.sap", "door51.sap", "door52.sap",
            "door53.sap", "door54.sap", "door98.sap", "door99.sap"
        ]
    elif category == "Enemy":
        return [
            "enemy00.sap", "enemy01.sap", "enemy02.sap", "enemy03.sap", "enemy04.sap", "enemy05.sap", "enemy06.sap",
            "enemy07.sap", "enemy08.sap", "enemy09.sap", "enemy10.sap", "enemy11.sap", "enemy12.sap", "enemy13.sap",
            "enemy14.sap", "enemy15.sap", "enemy16.sap", "enemy17.sap", "enemy18.sap", "enemy19.sap", "enemy20.sap",
            "enemy21.sap", "enemy22.sap", "enemy23.sap", "enemy24.sap", "enemy25.sap", "enemy26.sap", "enemy27.sap",
            "enemy28.sap", "enemy29.sap", "enemy30.sap", "enemy31.sap", "enemy32.sap", "enemy33.sap", "enemy34.sap",
            "enemy35.sap", "enemy36.sap", "enemy37.sap", "enemy38.sap", "enemy39.sap", "enemy40.sap", "enemy41.sap",
            "enemy42.sap", "enemy43.sap", "enemy44.sap", "enemy45.sap", "enemy48.sap", "enemy49.sap", "enemy50.sap",
            "enemy51.sap", "enemy52.sap", "enemy53.sap", "enemy54.sap", "enemy55.sap", "enemy56.sap", "enemy59.sap",
            "enemy60.sap", "enemy61.sap", "enemy62.sap", "enemy63.sap", "enemy64.sap", "enemy65.sap", "enemy66.sap",
            "enemy67.sap", "enemy68.sap", "enemy69.sap", "enemy70.sap", "enemy71.sap", "enemy72.sap", "enemy98.sap",
            "enemy99.sap"
        ]
    elif category == "Room":
        return [
            "room000.sap", "room100.sap", "room101.sap", "room102.sap", "room103.sap", "room104.sap", "room105.sap",
            "room106.sap", "room107.sap", "room108.sap", "room109.sap", "room10a.sap", "room10b.sap", "room10c.sap",
            "room10d.sap", "room10e.sap", "room10f.sap", "room110.sap", "room111.sap", "room112.sap", "room113.sap",
            "room114.sap", "room115.sap", "room116.sap", "room117.sap", "room118.sap", "room119.sap", "room11a.sap",
            "room11b.sap", "room11c.sap", "room200.sap", "room201.sap", "room202.sap", "room203.sap", "room204.sap",
            "room205.sap", "room206.sap", "room207.sap", "room208.sap", "room209.sap", "room20a.sap", "room20b.sap",
            "room20c.sap", "room20d.sap", "room20e.sap", "room20f.sap", "room210.sap", "room211.sap", "room212.sap",
            "room213.sap", "room214.sap", "room215.sap", "room216.sap", "room219.sap", "room21a.sap", "room21b.sap",
            "room300.sap", "room301.sap", "room302.sap", "room303.sap", "room304.sap", "room305.sap", "room306.sap",
            "room307.sap", "room308.sap", "room309.sap", "room30a.sap", "room30b.sap", "room30c.sap", "room30d.sap"
        ]
    elif category == "Weapon":
        return [
            "weapon01.sap", "weapon02.sap", "weapon03.sap", "weapon04.sap", "weapon05.sap", "weapon06.sap", "weapon07.sap",
            "weapon08.sap", "weapon09.sap", "weapon10.sap", "weapon11.sap", "weapon12.sap", "weapon13.sap", "weapon14.sap",
            "weapon15.sap", "weapon16.sap", "weapon17.sap", "weapon18.sap", "weapon19.sap"
        ]
    return []
