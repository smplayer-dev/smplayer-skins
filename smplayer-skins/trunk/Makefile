
PREFIX=/usr/local
#PREFIX=/tmp/smplayer

THEMES_PATH=$(DESTDIR)$(PREFIX)/share/smplayer/themes

install:
	-install -d $(THEMES_PATH)
#	cp -r themes/* $(THEMES_PATH)
	tar -C themes/ --exclude=.svn -c -f - . | tar -C $(THEMES_PATH) -x -f -

uninstall:
#	-rm -r $(THEMES_PATH)/*
#	-rmdir $(THEMES_PATH)/
