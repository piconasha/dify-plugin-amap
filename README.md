# Amap Plugin for Dify

[![Dify Plugin](https://img.shields.io/badge/Dify-Plugin-155EEF)](https://dify.ai)
[![Version](https://img.shields.io/badge/version-0.0.1-green)](https://github.com/piconasha/dify-plugin-amap)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

**Author:** Piconasha  
**Type:** Tool Plugin  
**Version:** 0.0.1

---

## Overview

This plugin connects Dify to the [Amap Open Platform](https://lbs.amap.com/), enabling AI applications to perform IP geolocation queries and walking route planning within China.

## Features

### 1. IP Location Query

Query the geographical location of an IPv4 address (China only).

- **Input:** IPv4 address (optional - returns requester's location if empty)
- **Output:** Province and city information

**Use Cases:**
- User location detection
- Regional content personalization
- Security and fraud prevention

### 2. Walking Route Planning

Plan walking routes between two coordinate points.

- **Input:** Starting point and destination coordinates (longitude, latitude)
- **Output:** Walking distance, duration, and step-by-step directions

**Use Cases:**
- Navigation assistance
- Travel planning
- Distance calculation

---

## Installation

### From Dify Marketplace

1. Go to **Plugins** in your Dify workspace
2. Search for "Amap" or "高德"
3. Click **Install**

### Manual Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/piconasha/dify-plugin-amap.git
   cd dify-plugin-amap
   ```

2. Package the plugin:
   ```bash
   dify plugin package
   ```

3. Upload the `.difypkg` file to your Dify instance

---

## Configuration

### Step 1: Get Amap API Key

1. Visit [Amap Open Platform](https://lbs.amap.com/)
2. Register/Login to your account
3. Go to **Console** → **Application Management** → **My Applications**
4. Create a new application and get your **Key**

### Step 2: Configure in Dify

1. After installing the plugin, go to **Plugin Settings**
2. Enter your Amap API Key in the credentials field
3. Click **Save**

---

## Usage

### IP Location Query

**Tool Name:** `ip-query`

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ipv4_address | string | No | IPv4 address (e.g., `114.114.114.114`). Leave empty to query requester's IP. |

**Example:**
```
Query: "Where is IP 114.114.114.114 located?"
Result: "IP 114.114.114.114 location: Jiangsu Nanjing"
```

### Walking Route Planning

**Tool Name:** `direction_v2-walking`

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| starting_point | string | Yes | Starting coordinates (longitude,latitude), e.g., `116.397428,39.90923` |
| ending_point | string | Yes | Destination coordinates (longitude,latitude), e.g., `116.481028,39.989643` |

**Example:**
```
Query: "Plan a walking route from Beijing Tiananmen (116.397428,39.90923) to Beijing Railway Station (116.427093,39.903738)"
Result:
Walking Route Planning Result
━━━━━━━━━━━━━━━━━━━━
Total Distance: 2.85 km (2850 m)
Estimated Time: 38 minutes
━━━━━━━━━━━━━━━━━━━━

Detailed Directions:
1. Walk 200m north along East Chang'an Avenue...
2. Turn right and walk 150m east...
...
```

---

## API Reference

This plugin uses the following Amap APIs:

| API | Endpoint | Documentation |
|-----|----------|---------------|
| IP Location | `/v3/ip` | [API Docs](https://lbs.amap.com/api/webservice/guide/api/ipconfig) |
| Walking Route | `/v5/direction/walking` | [API Docs](https://lbs.amap.com/api/webservice/guide/direction/walk) |

---

## Limitations

- **IP Location:** Only works for IP addresses within China
- **Coordinates:** Must use GCJ-02 coordinate system (China standard)
- **Rate Limits:** Subject to Amap API rate limits based on your account tier

---

## Privacy

This plugin sends the following data to Amap servers:
- API Key (for authentication)
- IP addresses (for geolocation queries)
- Geographic coordinates (for route planning)

For details, see [PRIVACY.md](PRIVACY.md).

---

## Development

### Prerequisites

- Python 3.12+
- Dify Plugin SDK

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
dify plugin dev
```

### Project Structure

```
dify-plugin-amap/
├── manifest.yaml          # Plugin manifest
├── provider/
│   ├── amap.py           # Provider implementation
│   └── amap.yaml         # Provider configuration
├── tools/
│   ├── ip/
│   │   ├── query.py      # IP query tool
│   │   └── query.yaml    # IP query configuration
│   └── direction_v2/
│       ├── walking.py    # Walking route tool
│       └── walking.yaml  # Walking route configuration
├── _assets/
│   ├── icon.svg          # Light mode icon
│   └── icon-dark.svg     # Dark mode icon
├── README.md             # English documentation
├── readme/
│   └── README_zh_Hans.md # Chinese documentation
└── PRIVACY.md            # Privacy policy
```

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## Support

- **Issues:** [GitHub Issues](https://github.com/piconasha/dify-plugin-amap/issues)
- **Amap API Support:** [Amap Developer Community](https://lbs.amap.com/dev/)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Dify](https://dify.ai/) - The AI application development platform
- [Amap Open Platform](https://lbs.amap.com/) - Location and map services