<#
.SYNOPSIS
    Dev diary auto-generation task scheduler

.DESCRIPTION
    Registers a scheduled task that runs run_diary.ps1 daily at the specified time.

.PARAMETER Time
    Execution time (default: 23:55)
#>

param (
    [string]$Time = "23:55"
)

$TaskName = "DevDiaryAutoGenerate"
$ScriptPath = Join-Path $PSScriptRoot "run_diary.ps1"
$Action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$ScriptPath`""
$Trigger = New-ScheduledTaskTrigger -Daily -At $Time
$Description = "Auto-generate dev diary daily at $Time and push to Git."

try {
    # Remove existing task if present
    if (Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue) {
        Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
        Write-Host "[UPDATE] Updating existing scheduled task..." -ForegroundColor Yellow
    }

    # Register task
    Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Description $Description
    Write-Host "[OK] Scheduled task '$TaskName' registered (daily at $Time)" -ForegroundColor Green
} catch {
    Write-Error "[ERROR] Failed to register task: $_"
}
