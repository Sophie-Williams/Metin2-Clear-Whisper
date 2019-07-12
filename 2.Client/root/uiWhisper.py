## 1.) Find this:
import chr

## 2.) Add after this:
if app.ENABLE_WHISPER_CLEAR:
	WHISPER_CLEAR_BUTTON_PATH = [
		"d:/ymir work/ui/public/close_button_01.sub",
		"d:/ymir work/ui/public/close_button_02.sub",
		"d:/ymir work/ui/public/close_button_03.sub"]

## 1.) Find this:
		self.textRenderer.Show()

## 2.) Add after this:
		if app.ENABLE_WHISPER_CLEAR:
			self.btnClearWhisper = ui.Button()
			self.btnClearWhisper.SetParent(self)
			self.btnClearWhisper.SetPosition(200, 15)
			self.btnClearWhisper.SetUpVisual(WHISPER_CLEAR_BUTTON_PATH[0])
			self.btnClearWhisper.SetOverVisual(WHISPER_CLEAR_BUTTON_PATH[1])
			self.btnClearWhisper.SetDownVisual(WHISPER_CLEAR_BUTTON_PATH[2])
			self.btnClearWhisper.SetToolTipText("Clear Whisper")
			self.btnClearWhisper.SetEvent(ui.__mem_func__(self.CheckClearWhisper))
			self.btnClearWhisper.Hide()

## 1.) Find this: (Destroy())
		self.resizeButton = None

## 2.) Add after this:
		if app.ENABLE_WHISPER_CLEAR:
			self.btnClearWhisper = None

## 1.) Find this: (OpenWithTarget())
		self.minimizeButton.Show()

## 2.) Add after this:
		if app.ENABLE_WHISPER_CLEAR:
			self.btnClearWhisper.Show()

## 1.) Find this: (OpenWithoutTarget())
		self.gamemasterMark.Hide()

## 2.) Add after this:
		if app.ENABLE_WHISPER_CLEAR:
			self.btnClearWhisper.Hide()

## 1.) Find this:
	def SetGameMasterLook(self):
		self.gamemasterMark.Show()

## 2.) Add after this:
	if app.ENABLE_WHISPER_CLEAR:
		def CheckClearWhisper(self):
			chat.ClearWhisper(self.targetName)
