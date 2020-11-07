all: Black/Black.rcc Gonzo/Gonzo.rcc Mac/Mac.rcc Mint-Y/Mint-Y.rcc Modern/Modern.rcc Vista/Vista.rcc 

Black/Black.rcc: Black.qrc
	rcc -binary Black.qrc -o Black/Black.rcc

Gonzo/Gonzo.rcc: Gonzo.qrc
	rcc -binary Gonzo.qrc -o Gonzo/Gonzo.rcc

Mac/Mac.rcc: Mac.qrc
	rcc -binary Mac.qrc -o Mac/Mac.rcc

Mint-Y/Mint-Y.rcc: Mint-Y.qrc
	rcc -binary Mint-Y.qrc -o Mint-Y/Mint-Y.rcc

Modern/Modern.rcc: Modern.qrc
	rcc -binary Modern.qrc -o Modern/Modern.rcc

Vista/Vista.rcc: Vista.qrc
	rcc -binary Vista.qrc -o Vista/Vista.rcc

clean:
	-rm Black/Black.rcc
	-rm Gonzo/Gonzo.rcc
	-rm Mac/Mac.rcc
	-rm Mint-Y/Mint-Y.rcc
	-rm Modern/Modern.rcc
	-rm Vista/Vista.rcc
