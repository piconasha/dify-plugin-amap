# 高德开放平台 Dify 插件

[![Dify Plugin](https://img.shields.io/badge/Dify-插件-155EEF)](https://dify.ai)
[![Version](https://img.shields.io/badge/版本-0.0.1-green)](https://github.com/piconasha/dify-plugin-amap)
[![License](https://img.shields.io/badge/许可证-MIT-blue)](LICENSE)

**作者:** Piconasha  
**类型:** 工具插件  
**版本:** 0.0.1

---

## 简介

本插件将 Dify 连接到[高德开放平台](https://lbs.amap.com/)，使 AI 应用能够进行 IP 归属地查询和步行路线规划。

## 功能特性

### 1. IP 归属地查询

查询 IPv4 地址的地理位置（仅限中国境内）。

- **输入：** IPv4 地址（可选，为空时返回请求者 IP 的位置）
- **输出：** 省份和城市信息

**应用场景：**
- 用户位置检测
- 区域化内容推荐
- 安全与反欺诈

### 2. 步行路线规划

在两个坐标点之间规划步行路线。

- **输入：** 起点和终点坐标（经度,纬度）
- **输出：** 步行距离、预计时间和详细路线指引

**应用场景：**
- 导航辅助
- 出行规划
- 距离计算

---

## 安装

### 从 Dify 插件市场安装

1. 在 Dify 工作空间中进入 **插件** 页面
2. 搜索 "Amap" 或 "高德"
3. 点击 **安装**

### 手动安装

1. 克隆本仓库：
   ```bash
   git clone https://github.com/piconasha/dify-plugin-amap.git
   cd dify-plugin-amap
   ```

2. 打包插件：
   ```bash
   dify plugin package
   ```

3. 将 `.difypkg` 文件上传到你的 Dify 实例

---

## 配置

### 第一步：获取高德 API Key

1. 访问[高德开放平台](https://lbs.amap.com/)
2. 注册/登录账号
3. 进入 **控制台** → **应用管理** → **我的应用**
4. 创建新应用并获取 **Key**

### 第二步：在 Dify 中配置

1. 安装插件后，进入 **插件设置**
2. 在凭证字段中输入高德 API Key
3. 点击 **保存**

---

## 使用方法

### IP 归属地查询

**工具名称：** `ip-query`

**参数：**
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| ipv4_address | string | 否 | IPv4 地址（如 `114.114.114.114`），为空时查询请求者 IP |

**示例：**
```
查询："IP 114.114.114.114 在哪里？"
结果："IP 114.114.114.114 归属地：江苏省 南京市"
```

### 步行路线规划

**工具名称：** `direction_v2-walking`

**参数：**
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| starting_point | string | 是 | 起点坐标（经度,纬度），如 `116.397428,39.90923` |
| ending_point | string | 是 | 终点坐标（经度,纬度），如 `116.481028,39.989643` |

**示例：**
```
查询："规划从北京天安门(116.397428,39.90923)到北京站(116.427093,39.903738)的步行路线"
结果：
步行路线规划结果
━━━━━━━━━━━━━━━━━━━━
总距离：2.85 公里 (2850 米)
预计时间：38 分钟
━━━━━━━━━━━━━━━━━━━━

详细路线指引：
1. 沿东长安街向北步行200米...
2. 右转向东步行150米...
...
```

---

## API 参考

本插件使用以下高德 API：

| API | 接口 | 文档 |
|-----|------|------|
| IP 定位 | `/v3/ip` | [API 文档](https://lbs.amap.com/api/webservice/guide/api/ipconfig) |
| 步行路线 | `/v5/direction/walking` | [API 文档](https://lbs.amap.com/api/webservice/guide/direction/walk) |

---

## 限制说明

- **IP 定位：** 仅支持中国境内的 IP 地址
- **坐标系：** 必须使用 GCJ-02 坐标系（中国标准）
- **调用限制：** 受高德 API 调用频率限制，具体取决于您的账户等级

---

## 隐私声明

本插件会向高德服务器发送以下数据：
- API Key（用于身份验证）
- IP 地址（用于定位查询）
- 地理坐标（用于路线规划）

详细信息请参阅 [PRIVACY.md](PRIVACY.md)。

---

## 开发

### 环境要求

- Python 3.12+
- Dify 插件 SDK

### 本地开发

```bash
# 安装依赖
pip install -r requirements.txt

# 本地运行
dify plugin dev
```

### 项目结构

```
dify-plugin-amap/
├── manifest.yaml          # 插件清单
├── provider/
│   ├── amap.py           # Provider 实现
│   └── amap.yaml         # Provider 配置
├── tools/
│   ├── ip/
│   │   ├── query.py      # IP 查询工具
│   │   └── query.yaml    # IP 查询配置
│   └── direction_v2/
│       ├── walking.py    # 步行路线工具
│       └── walking.yaml  # 步行路线配置
├── _assets/
│   ├── icon.svg          # 浅色模式图标
│   └── icon-dark.svg     # 深色模式图标
├── README.md             # 英文文档
├── readme/
│   └── README_zh_Hans.md # 中文文档
└── PRIVACY.md            # 隐私政策
```

---

## 贡献

欢迎贡献代码！请随时提交 Pull Request。

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request

---

## 支持

- **问题反馈：** [GitHub Issues](https://github.com/piconasha/dify-plugin-amap/issues)
- **高德 API 支持：** [高德开发者社区](https://lbs.amap.com/dev/)

---

## 许可证

本项目采用 MIT 许可证 - 详情请参阅 [LICENSE](LICENSE) 文件。

---

## 致谢

- [Dify](https://dify.ai/) - AI 应用开发平台
- [高德开放平台](https://lbs.amap.com/) - 位置与地图服务