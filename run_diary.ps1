<#
.SYNOPSIS
    開発日記生成・公開自動化スクリプト

.DESCRIPTION
    1. .envファイルから環境変数を読み込み
    2. 開発日記生成ツールを実行
    3. 結果を表示
    
.NOTES
    実行前に .env ファイルを作成し、GEMINI_API_KEYを設定してください。
#>

$ScriptDir = Split-Path $MyInvocation.MyCommand.Path
$EnvFile = Join-Path $ScriptDir ".env"
$ToolScript = "src.tools.diary.main"

# 文字コード設定（文字化け防止）
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "🚀 開発日記生成プロセスを開始します..." -ForegroundColor Cyan

# 1. .envファイルの読み込み
if (Test-Path $EnvFile) {
    Write-Host "📄 .envファイルを読み込んでいます..." -ForegroundColor Gray
    Get-Content $EnvFile | ForEach-Object {
        if ($_ -match "^\s*([^#=]+)\s*=\s*(.*)$") {
            $name = $matches[1].Trim()
            $value = $matches[2].Trim()
            [Environment]::SetEnvironmentVariable($name, $value, "Process")
        }
    }
} else {
    Write-Warning "⚠️ .envファイルが見つかりません。環境変数 GEMINI_API_KEY が設定されていることを確認してください。"
}

# 2. APIキーチェック
if (-not $env:GEMINI_API_KEY) {
    Write-Error "❌ GEMINI_API_KEY が設定されていません。.envファイルを作成するか、環境変数を設定してください。"
    exit 1
}

# 3. ツール実行
Write-Host "🤖 日記生成ツールを実行中..." -ForegroundColor Cyan

# 現在のディレクトリをスクリプトのある場所へ変更（相対パス解決のため）
Push-Location $ScriptDir

try {
    # 対象リポジトリの設定
    $TargetRepos = @(".")
    $FlowRepo = "../Flow"
    
    if (Test-Path $FlowRepo) {
        $TargetRepos += $FlowRepo
        Write-Host "i  Flowリポジトリを検出しました: $FlowRepo" -ForegroundColor Gray
    }
    
    # 2.5. Git Pull（設計担当のコミットを取得）
    Write-Host "Pulling latest changes from remote..." -ForegroundColor Yellow
    foreach ($repo in $TargetRepos) {
        Push-Location $repo
        try {
            $pullResult = git pull --rebase 2>&1
            if ($LASTEXITCODE -eq 0) {
                Write-Host "  [OK] $repo" -ForegroundColor Green
            } else {
                Write-Warning "  [WARN] $repo : $pullResult"
            }
        } finally {
            Pop-Location
        }
    }
    
    # pythonモジュール実行
    python -m $ToolScript --target-repos $TargetRepos
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`n✅ 完了しました！" -ForegroundColor Green
    } else {
        Write-Error "`n❌ ツール実行中にエラーが発生しました。"
    }
} catch {
    Write-Error "❌ 予期せぬエラー: $_"
} finally {
    Pop-Location
}

# 完了後、少し待機（ウィンドウがすぐ消えないようにする場合用）
# Start-Sleep -Seconds 3
