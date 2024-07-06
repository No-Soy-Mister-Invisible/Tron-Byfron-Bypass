# Tron Byfron Bypass Source leak
# Tom's laughable attempt at a infects users (Discord: graxe20 | ID: 1138535226151293028)
# Did you really accuse me of trying to infect you just because you messed up your own grabber? HAHAHAHAH
# Did you even bother searching for my webhook spammer, or did you mistake it for some random GitHub tool? Your Python skills are showing. HAHAHAHAHAH
# Leaked by Mr invisible (Discord mister_invis | ID: 1123835769191153694)

import customtkinter  #Mr Invisible was here
import subprocess  #Mr Invisible was here
import sys  #Mr Invisible was here
import ctypes  #Mr Invisible was here
import os  #Mr Invisible was here
from tkinter import filedialog, messagebox  #Mr Invisible was here
import random  #Mr Invisible was here
import webbrowser  #Mr Invisible was here
import requests  #Mr Invisible was here

SUPPORTED_ROBLOX_VERSION = 'version-1088f3c8e4a44cc7'  #Mr Invisible was here
CURRENT_VERSION_BB = '5.2.1'  #Mr Invisible was here
PASTEBIN_URL = 'https://pastebin.com/raw/V0EJLFcJ'  #Mr Invisible was here

class App(customtkinter.CTk):  #Mr Invisible was here
    def __init__(self):  #Mr Invisible was here
        super().__init__()  #Mr Invisible was here

        self.title('Byfron Bypasser v5.2.1 (BETA)')  #Mr Invisible was here
        self.geometry('600x250')  #Mr Invisible was here

        self.grid_columnconfigure((0, 1), weight=1)  #Mr Invisible was here

        if not self.check_current_version():  #Mr Invisible was here
            ctypes.windll.user32.MessageBoxW(0, 'Outdated Version, we are redirecting you to our discord to install the new version.', 'Version Update Required', 16)  #Mr Invisible was here
            webbrowser.open_new('https://discord.gg/yHhUW9RQyE')  #Mr Invisible was here
            sys.exit()  #Mr Invisible was here

        self.roblox_process = None  #Mr Invisible was here
        self.roblox_process_name = 'RobloxPlayerLauncher.exe'  #Mr Invisible was here

        self.detectbutton = customtkinter.CTkButton(  #Mr Invisible was here
            master=self,  #Mr Invisible was here
            text='Detect Roblox Path',  #Mr Invisible was here
            command=self.detect_roblox_path  #Mr Invisible was here
        )  #Mr Invisible was here
        self.detectbutton.grid(row=1, column=0, padx=20, pady=10, sticky='ew', columnspan=2)  #Mr Invisible was here

        self.path_entry = customtkinter.CTkEntry(master=self, width=400)  #Mr Invisible was here
        self.path_entry.grid(row=2, column=0, padx=20, pady=10, sticky='ew', columnspan=2)  #Mr Invisible was here

        self.bypassbutton = customtkinter.CTkButton(  #Mr Invisible was here
            master=self,  #Mr Invisible was here
            text='Bypass Byfron',  #Mr Invisible was here
            command=self.bypassbutton_callback  #Mr Invisible was here
        )  #Mr Invisible was here
        self.bypassbutton.grid(row=3, column=0, padx=20, pady=20, sticky='ew', columnspan=2)  #Mr Invisible was here

        self.hwidcheckbox = customtkinter.CTkCheckBox(master=self, text='Coming Soon')  #Mr Invisible was here
        self.hwidcheckbox.grid(row=4, column=0, padx=20, pady=(0, 20), sticky='w')  #Mr Invisible was here

        self.emulatorcheckbox = customtkinter.CTkCheckBox(master=self, text='Coming Soon')  #Mr Invisible was here
        self.emulatorcheckbox.grid(row=4, column=1, padx=20, pady=(0, 20), sticky='w')  #Mr Invisible was here

        self.statustext = customtkinter.CTkLabel(master=self, text='Status: Byfron Enabled', fg_color='transparent')  #Mr Invisible was here
        self.statustext.grid(row=5, column=0, padx=20, pady=(0, 20), sticky='w')  #Mr Invisible was here

        self.disablebutton = customtkinter.CTkButton(  #Mr Invisible was here
            master=self,  #Mr Invisible was here
            text='Enable Byfron',  #Mr Invisible was here
            command=self.disablebyfrondisable_callback  #Mr Invisible was here
        )  #Mr Invisible was here
        self.disablebutton.grid(row=5, column=1, padx=20, pady=(0, 20), sticky='w')  #Mr Invisible was here

        self.check_roblox_version()  #Mr Invisible was here

    def check_roblox_version(self):  #Mr Invisible was here
        live_version = self.get_roblox_version()  #Mr Invisible was here
        if live_version and live_version != SUPPORTED_ROBLOX_VERSION:  #Mr Invisible was here
            message = f'Roblox has updated to {live_version} and this Byfron Bypasser version supports {SUPPORTED_ROBLOX_VERSION}. Please join our Discord server to get the latest version.'  #Mr Invisible was here
            ctypes.windll.user32.MessageBoxW(0, message, 'Version Mismatch', 64)  #Mr Invisible was here
            webbrowser.open_new('https://discord.gg/yHhUW9RQyE')  #Mr Invisible was here
            sys.exit()  #Mr Invisible was here

    def check_current_version(self):  #Mr Invisible was here
        try:  #Mr Invisible was here
            response = requests.get(PASTEBIN_URL)  #Mr Invisible was here
            response.raise_for_status()  #Mr Invisible was here
            latest_version = response.text.strip()  #Mr Invisible was here
            return latest_version == CURRENT_VERSION_BB  #Mr Invisible was here
        except requests.exceptions.RequestException as e:  #Mr Invisible was here
            print(f'Error checking version: {e}')  #Mr Invisible was here
            return True  #Mr Invisible was here

    def detect_roblox_path(self):  #Mr Invisible was here
        roblox_path = self.find_roblox_launcher()  #Mr Invisible was here
        if roblox_path:  #Mr Invisible was here
            self.path_entry.delete(0, 'end')  #Mr Invisible was here
            self.path_entry.insert(0, roblox_path)  #Mr Invisible was here
            self.show_message_box('Roblox Path', 'Roblox Launcher found and set.')  #Mr Invisible was here
        else:  #Mr Invisible was here
            self.show_message_box('Error', "Couldn't find Roblox Launcher, please select yourself.")  #Mr Invisible was here
            self.detectbutton.configure(text='Browse', command=self.browse_roblox_path)  #Mr Invisible was here

    def find_roblox_launcher(self):  #Mr Invisible was here
        possible_paths = ['C:\\Program Files (x86)\\Roblox\\Versions', 'C:\\Program Files\\Roblox\\Versions']  #Mr Invisible was here
        for path in possible_paths:  #Mr Invisible was here
            if os.path.exists(path):  #Mr Invisible was here
                for root, dirs, files in os.walk(path):  #Mr Invisible was here
                    if 'RobloxPlayerLauncher.exe' in files:  #Mr Invisible was here
                        return os.path.join(root, 'RobloxPlayerLauncher.exe')  #Mr Invisible was here
        return None  #Mr Invisible was here

    def browse_roblox_path(self):  #Mr Invisible was here
        roblox_path = filedialog.askopenfilename(filetypes=[('Executable files', '*.exe')])  #Mr Invisible was here
        if roblox_path:  #Mr Invisible was here
            if os.path.exists(roblox_path):  #Mr Invisible was here
                if self.validate_roblox_path(roblox_path):  #Mr Invisible was here
                    self.path_entry.delete(0, 'end')  #Mr Invisible was here
                    self.path_entry.insert(0, roblox_path)  #Mr Invisible was here
                    self.show_message_box('Roblox Path', 'Valid Path')  #Mr Invisible was here
                else:  #Mr Invisible was here
                    self.show_message_box('Error', 'Selected file must be RobloxPlayerLauncher.exe or Bloxstrap.exe')  #Mr Invisible was here
        else:  #Mr Invisible was here
            return  #Mr Invisible was here

    def validate_roblox_path(self, path):  #Mr Invisible was here
        valid_executables = ['RobloxPlayerLauncher.exe', 'Bloxstrap.exe']  #Mr Invisible was here
        return os.path.basename(path) in valid_executables  #Mr Invisible was here

    def disablebyfrondisable_callback(self):  #Mr Invisible was here
        if self.statustext.cget('text') == 'Status: Byfron Disabled':  #Mr Invisible was here
            self.statustext.configure(text='Status: Byfron Enabled')  #Mr Invisible was here
            self.show_message_box('Byfron Disabled', 'Byfron has been enabled. Please close the roblox process.')  #Mr Invisible was here
            self.terminate_roblox_process()  #Mr Invisible was here
        else:  #Mr Invisible was here
            self.show_message_box('Error', 'Byfron is not currently disabled.')  #Mr Invisible was here

    def terminate_roblox_process(self):  #Mr Invisible was here
        if self.roblox_process:  #Mr Invisible was here
            try:  #Mr Invisible was here
                subprocess.call(['taskkill', '/F', '/PID', str(self.roblox_process.pid)])  #Mr Invisible was here
                self.roblox_process = None  #Mr Invisible was here
            except Exception as e:  #Mr Invisible was here
                self.show_message_box('Error', f'Failed to terminate process: {e}')  #Mr Invisible was here

    def bypassbutton_callback(self):  #Mr Invisible was here
        roblox_path = self.path_entry.get()  #Mr Invisible was here
        if not roblox_path:  #Mr Invisible was here
            self.show_message_box('Error', 'Please set Roblox launcher file path.')  #Mr Invisible was here
            return  #Mr Invisible was here
        if not self.validate_roblox_path(roblox_path):  #Mr Invisible was here
            self.show_message_box('Error', 'Selected file must be RobloxPlayerLauncher.exe or Bootstrapper.exe')  #Mr Invisible was here
            return  #Mr Invisible was here

        self.statustext.configure(text='Status: Detecting Byfron Files')  #Mr Invisible was here
        delay = random.randint(3000, 7000)  #Mr Invisible was here
        self.after(delay, self.update_status)  #Mr Invisible was here

    def get_roblox_version(self):  #Mr Invisible was here
        try:  #Mr Invisible was here
            response = requests.get('https://clientsettings.roblox.com/v2/client-version/WindowsPlayer')  #Mr Invisible was here
            response.raise_for_status()  #Mr Invisible was here
            data = response.json()  #Mr Invisible was here
            return data['clientVersionUpload']  #Mr Invisible was here
        except requests.exceptions.RequestException as e:  #Mr Invisible was here
            print(f'An error occurred: {e}')  #Mr Invisible was here
            return None  #Mr Invisible was here

    def show_message_box(self, title, message, style=0):  #Mr Invisible was here
        ctypes.windll.user32.MessageBoxW(0, message, title, style)  #Mr Invisible was here

    def update_status(self):  #Mr Invisible was here
        self.statustext.configure(text='Status: Byfron Disabled')  #Mr Invisible was here
        self.launch_roblox()  #Mr Invisible was here

    def launch_roblox(self):  #Mr Invisible was here
        roblox_path = self.path_entry.get()  #Mr Invisible was here
        if roblox_path and os.path.exists(roblox_path):  #Mr Invisible was here
            self.roblox_process = subprocess.Popen([roblox_path])  #Mr Invisible was here

def detect_debugger():  #Mr Invisible was here
    if hasattr(sys, 'gettrace') and sys.gettrace():  #Mr Invisible was here
        print('Tron AntiFucker | Debugger Detected')  #Mr Invisible was here
        sys.exit()  #Mr Invisible was here

detect_debugger()  #Mr Invisible was here

customtkinter.set_appearance_mode('dark')  #Mr Invisible was here
customtkinter.set_default_color_theme('dark-blue')  #Mr Invisible was here

app = App()  #Mr Invisible was here
app.mainloop()  #Mr Invisible was here
