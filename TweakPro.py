import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os

# موقع السكربتات
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# الدوال لتشغيل السكربتات
def run_script(script_name):
    try:
        path = os.path.join(SCRIPT_DIR, script_name)
        subprocess.run(["cmd", "/c", path], check=True)
        messagebox.showinfo("نجاح", f"تم تنفيذ {script_name} بنجاح!")
    except Exception as e:
        messagebox.showerror("خطأ", str(e))

# النافذة الأساسية
root = tk.Tk()
root.title("Ultimate Tweak Pro")
root.geometry("600x500")
style = ttk.Style()
style.theme_use("clam")

# إنشاء التبويبات
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True, fill="both")

# تبويب تحسين الأداء
frame_perf = ttk.Frame(notebook)
notebook.add(frame_perf, text="🎮 تحسين الأداء")

# تبويب الإنترنت
frame_net = ttk.Frame(notebook)
notebook.add(frame_net, text="🌐 تسريع الإنترنت")

# تبويب النظام
frame_sys = ttk.Frame(notebook)
notebook.add(frame_sys, text="🖥️ تنظيف النظام")

# تبويب شامل
frame_auto = ttk.Frame(notebook)
notebook.add(frame_auto, text="⚙️ تعديل تلقائي")

# ========== أزرار التبويب الأول ==========
ttk.Label(frame_perf, text="تحسين الفريمات وتقليل الديلاي:", font=("Arial", 12)).pack(pady=5)
ttk.Button(frame_perf, text="تعطيل المؤثرات البصرية", command=lambda: run_script("Visual_Effects_Optimization.bat")).pack(pady=3)
ttk.Button(frame_perf, text="تعطيل خدمات الخلفية", command=lambda: run_script("Disable_Unnecessary_Services.bat")).pack(pady=3)
ttk.Button(frame_perf, text="تفعيل خطة طاقة عالية الأداء", command=lambda: run_script("Power_Optimization.bat")).pack(pady=3)

# ========== أزرار التبويب الثاني ==========
ttk.Label(frame_net, text="تسريع الاتصال وتقليل البينغ:", font=("Arial", 12)).pack(pady=5)
ttk.Button(frame_net, text="تعديل إعدادات TCP/IP", command=lambda: run_script("Low_Latency_Registry_Tweak.bat")).pack(pady=3)
ttk.Button(frame_net, text="تنظيف DNS وإعادة الشبكة", command=lambda: run_script("Clear_DNS_and_Network_Reset.bat")).pack(pady=3)

# ========== أزرار التبويب الثالث ==========
ttk.Label(frame_sys, text="تحسين واستقرار النظام:", font=("Arial", 12)).pack(pady=5)
ttk.Button(frame_sys, text="تنظيف الملفات المؤقتة", command=lambda: run_script("System_Cleanup.bat")).pack(pady=3)
ttk.Button(frame_sys, text="تعطيل تحديثات ويندوز", command=lambda: run_script("Windows_Update_Disable.bat")).pack(pady=3)
ttk.Button(frame_sys, text="تعطيل التطبيقات في الخلفية", command=lambda: run_script("Disable_Background_Apps.bat")).pack(pady=3)

# ========== تبويب التعديل التلقائي ==========
ttk.Label(frame_auto, text="تعديل شامل تلقائي:", font=("Arial", 12)).pack(pady=5)
ttk.Button(frame_auto, text="تشغيل جميع التعديلات", command=lambda: [
    run_script("Visual_Effects_Optimization.bat"),
    run_script("Disable_Unnecessary_Services.bat"),
    run_script("Power_Optimization.bat"),
    run_script("Low_Latency_Registry_Tweak.bat"),
    run_script("Clear_DNS_and_Network_Reset.bat"),
    run_script("System_Cleanup.bat"),
    run_script("Windows_Update_Disable.bat"),
    run_script("Disable_Background_Apps.bat")
]).pack(pady=20)

root.mainloop()