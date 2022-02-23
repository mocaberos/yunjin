#!/usr/bin/env bash
#
# CIテストを実行する
#
set -eu;

# 共通ライブラリを読み込む
source "$(dirname "${0}")/../vendor/shell-scripts/common-functions.sh"

# YunJinを起動する
#"$(dirname "${0}")/../bin/start.sh"


health_check "https://ifconfig.io/ip" 3
