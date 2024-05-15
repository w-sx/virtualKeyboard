import addonHandler
import globalPluginHandler
from scriptHandler import script
import winInputHook
import ui
import tones
from keyboardHandler import KeyboardInputGesture
import ctypes

addonHandler.initTranslation()

def key(name):
	if not name: return None
	kig = KeyboardInputGesture.fromName(name)
	return (kig.vkCode,kig.isExtended)

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	_seizedKeys = None
	_isHooked = False
	_index = 1
	_oriNumKey = False
	_keyDict = [
		{
			key('7'): key('numLockNumpad7'),
			key('8'): key('numLockNumpad8'),
			key('9'): key('numLockNumpad9'),
			key('y'): key('numpadDivide'),
			key('u'): key('numLockNumpad4'),
			key('i'): key('numLockNumpad5'),
			key('o'): key('numLockNumpad6'),
			key('p'): key('numpadMultiply'),
			key('h'): key('numpadPlus'),
			key('j'): key('numLockNumpad1'),
			key('k'): key('numLockNumpad2'),
			key('l'): key('numLockNumpad3'),
			key(';'): key('numpadMinus'),
			key('m'): key('numLockNumpad0'),
			key(','): key('numpadDecimal'),
			key('.'): key('numpadEnter'),
			key('/'): key('numLock'),
			key('\''): key('applications'),
		} , {
			'description' : _('numpad'),
			key('7'): key('numpad7'),
			key('8'): key('numpad8'),
			key('9'): key('numpad9'),
			key('y'): key('numpadDivide'),
			key('u'): key('numpad4'),
			key('i'): key('numpad5'),
			key('o'): key('numpad6'),
			key('p'): key('numpadMultiply'),
			key('h'): key('numpadPlus'),
			key('j'): key('numpad1'),
			key('k'): key('numpad2'),
			key('l'): key('numpad3'),
			key(';'): key('numpadMinus'),
			key('m'): key('numpadInsert'),
			key(','): key('numpadDecimal'),
			key('.'): key('numpadEnter'),
			key('/'): key('numLock'),
			key('\''): key('applications'),
		} , {
			"description" : _('function extension'),
			key('7'): key('f22'),
			key('8'): key('f23'),
			key('9'): key('f24'),
			#key('y'): key(''),
			key('u'): key('f19'),
			key('i'): key('f20'),
			key('o'): key('f21'),
			#key('p'): key(''),
			#key('h'): key(''),
			key('j'): key('f16'),
			key('k'): key('f17'),
			key('l'): key('f18'),
			#key(';'): key(''),
			key('m'): key('f13'),
			key(','): key('f14'),
			key('.'): key('f15'),
			#key('/'): key(''),
			key('\''): key('applications'),
		} , {
			"description" : _("multimedia"),
			key('7'): key('browserSearch'),
			key('8'): key('browserHome'),
			key('9'): key('browserFavorites'),
			key('y'): key('launchMediaPlayer'),
			key('u'): key('volumeDown'),
			key('i'): key('mediaStop'), #key('volumeMute'),
			key('o'): key('volumeUp'),
			key('p'): key('launchApp1'),
			key('h'): key('launchMail'),
			key('j'): key('mediaPrevTrack'),
			key('k'): key('mediaPlayPause'),
			key('l'): key('mediaNextTrack'),
			key(';'): key('launchApp2'),
			key('m'): key('browserBack'),
			key(','): key('browserRefresh'),
			key('.'): key('browserForward'),
			#key('/'): key(''),
			key('\''): key('applications'),
		}
	]

	@script(
		description=_('turn on/off virtual keyboard'),
		category=_('virtual keyboard'),
		gesture='kb:NVDA+-'
	)
	def script_hookSwitch(self,gesture):
		if self._isHooked:
			self.disable()
			msg = _('turn off')
		else:
			if not self.enable(): return
			msg = _('turn on') + ' , ' + self._getMode()
		self._msg(_('virtual keyboard') + msg)

	def enable(self):
		if self._isHooked: return
		if self._seizedKeys!=None:
			tones.beep(110,500,100,100)
			self._msg(_('Please release all keys and try again'))
			return False
		self._seizedKeys = {}
		self._oriKeyDown = winInputHook.keyDownCallback
		winInputHook.keyDownCallback = self._keyDown
		self._oriKeyUp = winInputHook.keyUpCallback
		winInputHook.keyUpCallback = self._keyUp
		self._isHooked = True
		self._isSleeping = False
		return True

	def disable(self):
		if not self._isHooked: return
		self._isHooked = False

	def _keyDown(self, vkCode, scanCode, extended, injected):
		self._token = 0
		if vkCode==163: self._token = 1
		if not self._isSleeping:
			if self._downKeepKeys(vkCode) == -1: return False
			#if vkCode==46 and self._index==1:
			#	self._oriNumKey = not self._oriNumKey
			#	return False
			index = self._index if self._index>1 else self._index-ctypes.windll.user32.GetKeyState(0X90)
			vk = (vkCode,extended)
			if vk in self._keyDict[index]:
				vkNew = self._keyDict[index][vk]
				if self._oriKeyDown(vkNew[0], scanCode, vkNew[1], injected): self._send(vkNew)
				self._seizedKeys[vk] = vkNew
				return False
		return self._oriKeyDown(vkCode, scanCode, extended, injected)

	def _keyUp(self, vkCode, scanCode, extended, injected):
		if vkCode==163 and self._token==1: self._sleep()
		self._token = 0
		vk = (vkCode,extended)
		if vk in self._seizedKeys:
			vkNew = self._seizedKeys[vk]
			del(self._seizedKeys[vk])
			bool = self._oriKeyUp(vkNew[0], scanCode, vkNew[1], injected)
		else: bool = self._oriKeyUp(vkCode, scanCode, extended, injected)
		if not self._isHooked and len(self._seizedKeys) == 0:
			winInputHook.keyDownCallback = self._oriKeyDown
			winInputHook.keyUpCallback = self._oriKeyUp
			self._seizedKeys = None
		return bool

	def _downKeepKeys(self,vkCode):
		if vkCode==219:
			self._index = self._index-1
			self._msg(self._getMode())
			return -1
		if vkCode==221:
			self._index = self._index+1
			self._msg(self._getMode())
			return -1
		return vkCode

	def _getMode(self):
		self._checkIndex()
		return self._keyDict[self._index]['description'] + _('mode') + ' , '+str(self._index)+' / '+str(len(self._keyDict)-1)+_('items')

	def _checkIndex(self):
		if len(self._keyDict)-1 < self._index:
			self._index = len(self._keyDict)-1
		if self._index < 1:
			self._index = 1

	def _sleep(self):
		if self._isSleeping:
			tones.beep(3520,80)
			self._isSleeping = False
		else:
			tones.beep(220,160)
			self._isSleeping = True

	def _msg(self,msg):
		ui.speech.cancelSpeech()
		ui.message(msg)

	def _send(self,vk):
		return KeyboardInputGesture([],vk[0],0,vk[1]).send()
