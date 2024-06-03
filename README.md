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

Ensure your machine has the folling Evironment Variables:
## App required Starlink Environment Variables
ENV STARLINK_DISH_IP = https://192.168.100.1:9200

ENV STARLINK_DISH_ID = TEST-DISH-STL-001

ENV STARLINK_DISH_LOCATION = Location

## App required server Environment Variables
SERVER_HOST=central.server.com

SERVER_PORT=8080


## Contributing
Contributions are welcome! Please fork the repository and create a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Special thanks to the Starlink community for their support and contributions.