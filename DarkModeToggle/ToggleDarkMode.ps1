$path = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"

$current = (Get-ItemProperty -Path $path -Name AppsUseLightTheme -ErrorAction SilentlyContinue).AppsUseLightTheme
if ($null -eq $current) { $current = 1 }

$new = if ($current -eq 1) { 0 } else { 1 }

New-ItemProperty -Path $path -Name AppsUseLightTheme -Value $new -PropertyType DWord -Force | Out-Null
New-ItemProperty -Path $path -Name SystemUsesLightTheme -Value $new -PropertyType DWord -Force | Out-Null

if (-not ("Native" -as [type])) {
Add-Type @"
using System;
using System.Runtime.InteropServices;
public class Native {
  [DllImport("user32.dll", SetLastError=true)]
  public static extern IntPtr SendMessageTimeout(
    IntPtr hWnd, int Msg, IntPtr wParam, string lParam,
    SendMessageTimeoutFlags flags, uint timeout, out IntPtr lpdwResult);

  public enum SendMessageTimeoutFlags : uint {
    SMTO_ABORTIFHUNG = 0x2
  }
}
"@
}

$res = [IntPtr]::Zero
[void][Native]::SendMessageTimeout([IntPtr]0xffff, 0x001A, [IntPtr]0, "ImmersiveColorSet",
  [Native+SendMessageTimeoutFlags]::SMTO_ABORTIFHUNG, 100, [ref]$res)

[void][Native]::SendMessageTimeout([IntPtr]0xffff, 0x001A, [IntPtr]0, "WindowsTheme",
  [Native+SendMessageTimeoutFlags]::SMTO_ABORTIFHUNG, 100, [ref]$res)