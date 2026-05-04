# 🌗 Instant Theme Switcher (Dark/Light Mode)

A lightweight, automated background utility that interacts directly with the Windows Registry to toggle your system and application themes instantly. This bypasses the need to navigate through the Windows Settings GUI every time you want to switch between light and dark mode.

## ⚙️ Technologies Used
* **PowerShell:** Handles the registry modifications and API calls.
* **Windows Batch (.bat):** Acts as a secure, clickable wrapper to bypass execution policies cleanly.

## 🚀 How It Works
The script modifies the `AppsUseLightTheme` and `SystemUsesLightTheme` values within the `HKCU:\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize` registry key. 

Crucially, it utilizes the `SendMessageTimeout` API to broadcast the "ImmersiveColorSet" and "WindowsTheme" changes to the operating system. This forces the UI to refresh immediately without requiring a Windows Explorer restart!

## 📦 Installation & Usage

1. Download or clone this repository to your local machine.
2. Navigate to the `DarkModeToggle` folder.
3. Do **not** run the `.ps1` script directly unless your execution policies are completely open. 
4. Instead, double-click the `Toggle.bat` file. It will run silently in the background and flip your theme.

### 💡 Pro-Tip: Create a Global Keyboard Shortcut
For maximum efficiency, bind this script to a hotkey so you don't even have to click it:
1. Right-click on your desktop and select **New > Shortcut**.
2. Set the target to: `cmd.exe /c "C:\Path\To\Your\Toggle.bat"` *(Make sure to use your actual file path).*
3. Right-click the newly created shortcut, go to **Properties**, and click the **Shortcut key** field.
4. Press your desired combination (e.g., `Ctrl + Alt + D`), click **Apply**, and you are done!