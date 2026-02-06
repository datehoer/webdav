#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

if docker compose version >/dev/null 2>&1; then
  COMPOSE_CMD=(docker compose)
elif command -v docker-compose >/dev/null 2>&1; then
  COMPOSE_CMD=(docker-compose)
else
  echo "❌ 未找到 docker compose / docker-compose"
  exit 1
fi

echo "Using: ${COMPOSE_CMD[*]}"
"${COMPOSE_CMD[@]}" down --rmi all
"${COMPOSE_CMD[@]}" up -d --build

echo "✅ WebDAV restarted"
