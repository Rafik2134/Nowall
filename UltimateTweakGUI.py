import tkinter as tk
from tkinter import messagebox
import subprocess
import os

# تحديد المسار إلى السكربتات
script_folder = os.path.dirname(os.path.abspath(__file__))

# قائمة السكربتات
scripts = [
    "Disable_Unnecessary_Services.bat",
    "Optimize_RAM_Usage.bat",
    "Gaming_Tweak_Settings.bat",
    "Network_Optimization.bat",
    "System_Cleanup.bat",
    "SSD_Optimization.bat",
    "Power_Optimization.bat",
    "Clear_DNS_and_Network_Reset.bat",
    "Visual_Effects_Optimization.bat",
    "Windows_Update_Disable.bat",
    "Disable_Background_Apps.bat",
    "Low_Latency_Registry_Tweak.bat",
    "Disable_Telemetry.bat",
    "Remove_OneDrive.bat",
    "Speed_Up_Shutdown.bat"
]

# تنفيذ سكربت معين
def run_script(script):
    path = os.path.join(script_folder, script)
    try:
        subprocess.run(["cmd", "/c", path], check=True)
        messagebox.showinfo("نجاح", f"تم تنفيذ {script} بنجاح")
    except Exception as e:
        messagebox.showerror("خطأ", f"فشل تنفيذ {script}\n{str(e)}")

# إنشاء الواجهة
root = tk.Tk()
root.title("أداة تعديل أداء الكمبيوتر")
root.geometry("400x600")
root.configure(bg="#1e1e1e")

title = tk.Label(root, text="🔧 أداة Ultimate Tweak", bg="#1e1e1e", fg="white", font=("Arial", 16))
title.pack(pady=10)

for script in scripts:
    btn = tk.Button(root, text=script.replace(".bat", ""), width=40, bg="#2d89ef", fg="white",
                    command=lambda s=script: run_script(s))
    btn.pack(pady=5)

root.mainloop()