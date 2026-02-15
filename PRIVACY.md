# Privacy Policy / 隐私政策

[English](#english) | [中文](#中文)

---

## English

### Data Collection

This plugin collects and processes the following data when used:

| Data Type | Purpose | Required |
|-----------|---------|----------|
| API Key | Authentication with Amap Open Platform | Yes |
| IP Address | Geolocation queries (China only) | Optional |
| Geographic Coordinates | Walking route planning | Yes (for route tools) |

### Data Usage

#### API Key
- Used solely for authenticating requests to Amap APIs
- Stored securely by the Dify platform
- Never logged or transmitted to third parties

#### IP Address
- Sent to Amap servers for geolocation services
- Used to determine province and city information
- Not stored locally by this plugin

#### Geographic Coordinates
- Sent to Amap servers for route planning
- Used to calculate walking routes and directions
- Not stored locally by this plugin

### Data Storage

- **This plugin does not store any user data locally**
- All data processing is performed in real-time through Amap API calls
- API keys are securely stored by the Dify platform using encryption
- No data is retained after the API request is completed

### Third-Party Services

This plugin interacts with the following third-party service:

**Amap Open Platform (高德开放平台)**
- **Provider:** AutoNavi Software Co., Ltd. (高德软件有限公司)
- **Purpose:** Map services, geolocation, and route planning
- **Website:** https://lbs.amap.com/
- **Privacy Policy:** https://lbs.amap.com/pages/privacy/
- **Data Transferred:** API Key, IP addresses, geographic coordinates

### Data Security

- All API requests are made over HTTPS (TLS 1.2+)
- API keys are transmitted securely and never exposed in logs
- No sensitive data is cached or stored locally

### User Rights

Users have the following rights regarding their data:

- **Access:** Users can view their API key configuration in Dify settings
- **Deletion:** Users can remove their API key at any time through Dify settings
- **Opt-out:** Users can choose not to provide optional parameters (e.g., IP address)

### Children's Privacy

This plugin is not intended for use by children under the age of 13. We do not knowingly collect personal information from children under 13.

### Changes to This Policy

We may update this privacy policy from time to time. Any changes will be posted on this page with an updated revision date.

**Last Updated:** 2026-02-15

### Contact

For privacy-related inquiries, please contact:

- **GitHub Issues:** https://github.com/piconasha/dify-plugin-amap/issues
- **Repository:** https://github.com/piconasha/dify-plugin-amap

---

## 中文

### 数据收集

本插件在使用过程中会收集和处理以下数据：

| 数据类型 | 用途 | 是否必需 |
|----------|------|----------|
| API Key | 高德开放平台身份验证 | 是 |
| IP 地址 | IP 归属地查询（仅限中国境内） | 可选 |
| 地理坐标 | 步行路线规划 | 是（路线工具必需） |

### 数据使用

#### API Key
- 仅用于向高德 API 发起认证请求
- 由 Dify 平台安全存储
- 不会被记录或传输给第三方

#### IP 地址
- 发送至高德服务器用于定位服务
- 用于确定省份和城市信息
- 本插件不会在本地存储

#### 地理坐标
- 发送至高德服务器用于路线规划
- 用于计算步行路线和导航指引
- 本插件不会在本地存储

### 数据存储

- **本插件不会在本地存储任何用户数据**
- 所有数据处理均通过高德 API 实时完成
- API Key 由 Dify 平台加密安全存储
- API 请求完成后不保留任何数据

### 第三方服务

本插件与以下第三方服务交互：

**高德开放平台**
- **提供商：** 高德软件有限公司
- **用途：** 地图服务、定位、路线规划
- **网站：** https://lbs.amap.com/
- **隐私政策：** https://lbs.amap.com/pages/privacy/
- **传输数据：** API Key、IP 地址、地理坐标

### 数据安全

- 所有 API 请求均通过 HTTPS（TLS 1.2+）加密传输
- API Key 安全传输，不会在日志中暴露
- 不缓存或本地存储任何敏感数据

### 用户权利

用户对其数据拥有以下权利：

- **访问权：** 用户可在 Dify 设置中查看其 API Key 配置
- **删除权：** 用户可随时通过 Dify 设置删除其 API Key
- **选择权：** 用户可选择不提供可选参数（如 IP 地址）

### 儿童隐私

本插件不面向 13 岁以下儿童使用。我们不会故意收集 13 岁以下儿童的个人信息。

### 政策变更

我们可能会不时更新本隐私政策。任何变更将在此页面上发布，并更新修订日期。

**最后更新：** 2026-02-15

### 联系方式

如有隐私相关问题，请通过以下方式联系：

- **GitHub Issues：** https://github.com/piconasha/dify-plugin-amap/issues
- **代码仓库：** https://github.com/piconasha/dify-plugin-amap

---

## Open Source License / 开源许可

This is an open-source plugin. You can fork and modify it without permission. Have fun! :)

本插件为开源项目，您可以自由 fork 和修改。祝您使用愉快！:)