
PREFIX=/usr/local
#PREFIX=/tmp/smplayer

THEMES_PATH=$(DESTDIR)$(PREFIX)/share/smplayer/themes

all:
	cd themes && make

install:
	-install -d $(THEMES_PATH)

	- mkdir $(THEMES_PATH)/Black
	install -m 644 themes/Black/Black.rcc $(THEMES_PATH)/Black/
	install -m 644 themes/Black/main.css $(THEMES_PATH)/Black/

	- mkdir $(THEMES_PATH)/Gonzo
	install -m 644 themes/Gonzo/Gonzo.rcc $(THEMES_PATH)/Gonzo/
	install -m 644 themes/Gonzo/main.css $(THEMES_PATH)/Gonzo/

	- mkdir $(THEMES_PATH)/Mac
	install -m 644 themes/Mac/Mac.rcc $(THEMES_PATH)/Mac/
	install -m 644 themes/Mac/main.css $(THEMES_PATH)/Mac/

	- mkdir $(THEMES_PATH)/Modern
	install -m 644 themes/Modern/Modern.rcc $(THEMES_PATH)/Modern/
	install -m 644 themes/Modern/main.css $(THEMES_PATH)/Modern/

	- mkdir $(THEMES_PATH)/Vista
	install -m 644 themes/Vista/Vista.rcc $(THEMES_PATH)/Vista/
	install -m 644 themes/Vista/main.css $(THEMES_PATH)/Vista/

clean:
	cd themes && make clean

uninstall:
#	-rm -r $(THEMES_PATH)/*
#	-rmdir $(THEMES_PATH)/
