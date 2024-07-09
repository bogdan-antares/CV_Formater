import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView
import subprocess
import os

class CVFormaterApp(App):
    def build(self):
        self.cv_text_input = TextInput(hint_text='Collez le texte du CV ici', size_hint=(1, 0.7))
        self.format_button = Button(text='Formater le CV', size_hint=(1, 0.15))
        self.format_button.bind(on_press=self.open_file_chooser)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.cv_text_input)
        layout.add_widget(self.format_button)

        return layout

    def open_file_chooser(self, instance):
        self.file_chooser = FileChooserIconView()
        self.save_button = Button(text='Sélectionner le répertoire', size_hint=(1, 0.1))
        self.save_button.bind(on_press=self.open_filename_dialog)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.file_chooser)
        layout.add_widget(self.save_button)

        self.popup = Popup(title='Choisir le répertoire de sauvegarde', content=layout, size_hint=(0.9, 0.9))
        self.popup.open()

    def open_filename_dialog(self, instance):
        self.selected_path = self.file_chooser.path
        self.popup.dismiss()

        if not self.selected_path:
            popup = Popup(title='Erreur', content=Label(text='Veuillez choisir un répertoire.'), size_hint=(0.6, 0.3))
            popup.open()
            return

        self.filename_input = TextInput(hint_text='Entrez le nom du fichier (sans extension)', size_hint=(1, 0.2))
        self.save_filename_button = Button(text='Sauvegarder', size_hint=(1, 0.2))
        self.save_filename_button.bind(on_press=self.save_cv_text)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.filename_input)
        layout.add_widget(self.save_filename_button)

        self.filename_popup = Popup(title='Nom du fichier', content=layout, size_hint=(0.8, 0.4))
        self.filename_popup.open()

    def save_cv_text(self, instance):
        cv_text = self.cv_text_input.text
        filename = self.filename_input.text

        if not cv_text:
            popup = Popup(title='Erreur', content=Label(text='Veuillez entrer du texte.'), size_hint=(0.6, 0.3))
            popup.open()
            return

        if not filename:
            popup = Popup(title='Erreur', content=Label(text='Veuillez entrer un nom de fichier.'), size_hint=(0.6, 0.3))
            popup.open()
            return

        # Sauvegarder le texte du CV dans un fichier
        try:
            with open('cv_text.txt', 'w', encoding='utf-8') as f:
                f.write(cv_text)
            # Réinitialiser la zone de texte après sauvegarde
            self.cv_text_input.text = ''
            # Construire le chemin complet du fichier
            save_path = os.path.join(self.selected_path, f"{filename}.docx")
            # Exécuter le script web.py
            self.run_web_script(save_path)
            self.filename_popup.dismiss()
        except Exception as e:
            popup = Popup(title='Erreur', content=Label(text=f'Erreur de sauvegarde: {e}'), size_hint=(0.6, 0.3))
            popup.open()

    def run_web_script(self, save_path):
        try:
            result = subprocess.run(['python', 'web.py', 'cv_text.txt', save_path], check=True, capture_output=True, text=True)
            print(f"STDOUT: {result.stdout}")
            print(f"STDERR: {result.stderr}")
            popup = Popup(title='Succès', content=Label(text=f'Document sauvegardé à {save_path}'), size_hint=(0.6, 0.3))
            popup.open()
        except subprocess.CalledProcessError as e:
            popup = Popup(title='Erreur', content=Label(text=f'Erreur d\'exécution: {e.stderr}'), size_hint=(0.6, 0.3))
            popup.open()

if __name__ == "__main__":
    CVFormaterApp().run()

