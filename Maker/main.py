from UnrealLocres import UnrealLocres;
from StringHelper import StringHelper;
from fontTools.ttLib.ttFont import TTFont
from fontTools import subset
import csv;
import sys;
import os;

reload(sys) 
sys.setdefaultencoding('utf8')

def get_localization():
	loc_en = UnrealLocres("OriginalFile/Game.locres.en");
	loc_zh = UnrealLocres("OriginalFile/Game.locres.zh");
	loc_en.save_to_csv("en.csv");
	loc_zh.save_to_csv("zh.csv");
	
# get_localization();

def gen_fonts():
	sh = StringHelper();
	sh.add_file_text("localization.new.csv");
	sh.add_western();
	strs = sh.get_chars();

	font_export_path = "ExampleGame/Content/UI/Fonts/{0}";
	font_export_path2 = "Engine/Content/EngineFonts/Faces/{0}";
	
	options = subset.Options();
	font = subset.load_font('E:/Python Localization Helper/Font/suxin.ttf', options);
	subsetter = subset.Subsetter(options);
	subsetter.populate(text = strs);
	subsetter.subset(font);
	subset.save_font(font, font_export_path.format("Younger_than_me.ufont"), options);
	subset.save_font(font, font_export_path.format("WC_RoughTrad.ufont"), options);

	font = subset.load_font('E:/Python Localization Helper/Font/chaozishe.ttf', options);
	subsetter.subset(font);
	subset.save_font(font, font_export_path.format("Beast_Impact_2.ufont"), options);
	
	font = subset.load_font('C:/Windows/Fonts/SourceHanSerifSC-Bold.otf', options);
	subsetter.subset(font);
	subset.save_font(font, font_export_path.format("Roboto_Bold.ufont"), options);
	subset.save_font(font, font_export_path2.format("RobotoBold.ufont"), options);

	font = subset.load_font('C:/Windows/Fonts/SourceHanSerifSC-SemiBold.otf', options);
	subsetter.subset(font);
	subset.save_font(font, font_export_path.format("Roboto-Regular_0_Default.ufont"), options);

# Text
loc = UnrealLocres("OriginalFile/Game.locres.zh");

loc.load_from_csv("localization.new.csv");
loc.save_to_locres("ExampleGame/Content/Localization/Game/zh-Hans/Game.locres");

gen_fonts();

tool_path = "\"E:\\Python Localization Helper\\u4pak.py\""
apk_path = "\"..\\Redeemer\\ExampleGame\\Content\\Paks\\ExampleGame-WindowsNoEditor_p.pak\""

# commandstr = "python " + tool_path + " pack " + apk_path + " Redeemer\\ExampleGame\\"
# u4pak can't load sub folder.
commandstr = "python " + tool_path + " pack " + apk_path + " ExampleGame\\" + " Engine\\"
os.system(commandstr.encode('mbcs'));