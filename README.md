# Starlink API Collector Agent

## Overview

`starlink-api-collector-agent` is a project aimed at creating an agent that can be duplicated across multiple sites. This agent will collect status information from a Starlink dish and relay it back to a defined central server by the means of HTTP requests.

## Features

- Collects status information from Starlink dishes.
- Sends collected data to a central server.
- Designed for easy deployment across multiple sites.

## Getting Started

### Prerequisites

- Python v3.12.3

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ashton-southall/starlink-api-collector-agent.git
    cd starlink-grpc-agent
    ```

### Configuration

Create a configuration file `config.yaml` with the following structure:

```yaml
server:
  host: "central.server.com"
  port: 8080

starlink:
  dish_id: "your_dish_id"
  location: "your_location"
  dish_ip: "192.168.100.1"
  dish_port: 9200
```

## Contributing
Contributions are welcome! Please fork the repository and create a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Special thanks to the Starlink community for their support and contributions.