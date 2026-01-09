<#
.SYNOPSIS
    開発日記自動生成タスク登録スクリプト

.DESCRIPTION
    開発日記生成スクリプト（run_diary.ps1）を毎日指定時刻に実行するスケジュールタスクを登録します。

.PARAMETER Time
    実行時刻（デフォルト: 23:55）
#>

param (
    [string]$Time = "23:55"
)

$TaskName = "DevDiaryAutoGenerate"
$ScriptPath = Join-Path $PSScriptRoot "run_diary.ps1"
$Action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$ScriptPath`""
$Trigger = New-ScheduledTaskTrigger -Daily -At $Time
$Description = "毎日 $Time に開発日記を自動生成し、Gitにプッシュします。"

try {
    # 既存タスクがあれば削除
    if (Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue) {
        Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
        Write-Host "🔄 既存のスケジュールタスクを更新します..." -ForegroundColor Yellow
    }

    # タスク登録
    Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Description $Description
    Write-Host "✅ スケジュールタスク '$TaskName' を登録しました（毎日 $Time 実行）" -ForegroundColor Green
} catch {
    Write-Error "❌ タスク登録に失敗しました: $_"
}
