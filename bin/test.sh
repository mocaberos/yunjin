#!/usr/bin/env bash
#
# アプリケーションテストを実行する
# @important アプリケーションが既に同じホストで実行している必要がある
#
set -e;

# テストを実行する
pytest "$(dirname "${0}")/../tests"
