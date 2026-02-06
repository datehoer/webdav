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

## Nginx 参考配置（HTTPS 反代）

以下示例与当前部署方式一致：Nginx 监听 443，反代到本机 `127.0.0.1:5736`。

```nginx
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name webdav.example.com;

    ssl_certificate     /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.key;

    add_header Strict-Transport-Security "max-age=63072000" always;
    add_header X-Content-Type-Options nosniff;
    add_header X-Frame-Options DENY;
    add_header X-XSS-Protection "1; mode=block";

    client_max_body_size 100m;

    location / {
        proxy_pass http://127.0.0.1:5736;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 40960s;
        proxy_send_timeout 40960s;
    }
}
```

可选：增加 80 到 443 的跳转。

```nginx
server {
    listen 80;
    listen [::]:80;
    server_name webdav.example.com;
    return 301 https://$host$request_uri;
}
```

## 注意事项

- 请务必修改默认密码
- `.env` 与 `data/` 已在 `.gitignore` 中排除，不会提交到仓库
