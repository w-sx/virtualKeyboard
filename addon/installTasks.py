import addonHandler

def onInstall():
	for addon in addonHandler.getAvailableAddons():
		if addon.name == "DdummyKeyboard":
			addon.requestRemove()
			break
