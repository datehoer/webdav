# webdav

轻量 WebDAV 服务（Python + WsgiDAV + Docker Compose）。

## 功能

- 通过 Docker Compose 一键启动
- 数据目录持久化到宿主机
- 支持账号密码认证
- 提供 `restart.sh` 一键重建并重启

## 目录结构

- `webdav_server.py`：WebDAV 服务入口
- `Dockerfile`：镜像构建文件
- `docker-compose.yml`：容器编排
- `restart.sh`：重建并重启脚本
- `.env.example`：环境变量示例

## 使用方法

```bash
cp .env.example .env
# 修改 .env 中的 WEBDAV_PASSWORD

./restart.sh
```

## 访问

容器内部端口：`8080`

当前 compose 映射：`127.0.0.1:5736 -> 8080`

如果配合 Nginx 反代，可通过域名访问（例如 `webdav.example.com`）。

## 注意事项

- 请务必修改默认密码
- `.env` 与 `data/` 已在 `.gitignore` 中排除，不会提交到仓库
