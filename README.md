### Project Description: AWS IoT Locust Test

#### Overview

The AWS IoT Locust Test project is designed to evaluate the performance and scalability of an IoT (Internet of Things) system using Locust, an open-source load testing tool. This project focuses on simulating a large number of MQTT (Message Queuing Telemetry Transport) clients to assess the system's ability to handle high-throughput data transmission and multiple simultaneous connections.

#### Objectives

- **Performance Testing:** Simulate a high number of concurrent MQTT clients to test the IoT system's performance.
- **Scalability Assessment:** Determine how well the system scales with increasing load and identify any potential bottlenecks.
- **Reliability Analysis:** Ensure the IoT system can maintain stable operation under heavy traffic conditions.

#### Key Components

1. **Locust:** An open-source load testing tool that allows you to define user behavior with Python code and generate load on the system.
2. **MQTT Protocol:** A lightweight messaging protocol for small sensors and mobile devices, optimized for high-latency or unreliable networks.
3. **AWS IoT Core:** A managed cloud platform that lets connected devices easily and securely interact with cloud applications and other devices.

#### Features

- **User Simulation:** The project simulates `N` number of clients connecting to the AWS IoT Core endpoint.
- **Dynamic Data Generation:** Each simulated client sends random data payloads of a specified size to an MQTT topic.
- **Configurable Throughput:** The project allows configuration of constant throughput, ensuring a steady flow of messages per client connection.
- **Scalable Load Testing:** The test runs in headless mode, enabling automation and execution in various environments, with configurable user spawn rates and durations.

#### Environment Setup

The project uses a Python virtual environment to manage dependencies and ensure consistency across different development and testing environments. The tested Python version is 3.12, and all dependencies are specified in the `requirements.txt` file.

#### Configuration

The project relies on several environment variables to configure the MQTT connection and test parameters:

- **MQTT Certificate Files:** Paths to the CA file, client certificate, and private key for secure communication.
- **MQTT Connection Details:** Host, port, and topic for the MQTT broker.
- **Test Parameters:** Quality of Service (QoS) level, payload size, and throughput settings.

#### Execution

The Locust test is executed with the following parameters:

- **Headless Mode:** Runs without a graphical interface, suitable for automated testing environments.
- **Users and Spawn Rate:** Configurable with the `--users` and `--spawn-rate` paramers
- **Run Time:** Confgurable using the `--run-time` parameter
- **Processes:** Can be confiured to use multiple CPUs using the `--processes` parameter

By following the provided setup and execution instructions, users can effectively simulate and evaluate the performance of their AWS IoT system under various load conditions. This project helps identify performance bottlenecks, ensuring the system can handle real-world scenarios with high reliability and scalability.

### Step-by-Step Instructions

These steps will guide you through updating your package list, installing necessary packages, setting up a virtual environment, installing project dependencies, configuring environment variables, and running a Locust performance test.

> :warning: The following commands were tested using Ubuntu, 24.04 LTS. Adjust commands according to your Operating System.

**Update Package List:**
Update the package list to ensure you have the latest information on the newest versions of packages and their dependencies.

```bash
sudo apt update -y
```

**Install Python 3.12 Virtual Environment Package:**
Install the `python3.12-venv` package, which allows you to create virtual environments for Python projects.

```bash
sudo apt install python3.12-venv -y
```

**Clone Project:**
Clone the `aws-iot-locust-test` project fromt the `aws-samples` repository into your home directory.

```bash
cd ~/
git clone https://github.com/aws-samples/aws-iot-locust-test
```

**Navigate to Project Directory:**
Change your current directory to the directory of your project

```bash
cd ~/aws-iot-locust-test
```

**Create a Python Virtual Environment:**
Create a new virtual environment using Python 3 within your project directory.

```bash
python3 -m venv .venv
```

**Activate the Virtual Environment:**
Activate the virtual environment to ensure that any packages you install will be contained within this environment.

```bash
source .venv/bin/activate
```

**Install Project Dependencies:**
Install the required dependencies for your project from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

**Set Environment Variables:**
Export the necessary environment variables required for the Locust test. These variables include paths to your MQTT certificate files, MQTT host information, and test-specific configurations.

```bash
export LOCUST_MQTT_CAFILE="pki/root_ca.pem"
export LOCUST_MQTT_CERT="pki/certificate.pem.crt"
export LOCUST_MQTT_KEY="pki/private.pem.key"
export LOCUST_MQTT_HOST="EXAMPLEdjbt-ats.iot.eu-west-1.amazonaws.com"
export LOCUST_MQTT_PORT=8883

export LOCUST_MQTT_TOPIC="locust/test/topic"
export LOCUST_MQTT_QOS=0
export LOCUST_MQTT_RANDOM_DATA_KB_SIZE=5
export LOCUST_MQTT_CONSTANT_THROUGHPUT=100
```

**Set Run ID:**
Use a unique identifier for this run.

```bash
export LOCUST_MQTT_RUN_ID="EXAMPLE-AC28-45D0-9EC8-7A4B57A9C04B"
```

**Run Locust Test:**
Execute the Locust test with the specified configuration. The test will run in headless mode, simulating 10 users with a spawn rate of 1 user per second, for a duration of 10 minutes, using 2 processes. You can adjust these settings based on your load testing requirements.

```bash
locust -f locustfile.py  \
    --headless \
    --users 10 \
    --spawn-rate 1 \
    --run-time 10m \
    --processes 2
```

> :warning: Be aware of potential costs from device messages sent to AWS IoT Core, as message volumes can accumulate rapidly. In this example, each simulated client attempts to send 100 messages every second, resulting in aproximately 600,000 messages for a 10-minute test with 10 clients, costing approximately $0.60 based on AWS IoT Core's pricing of $1.00 per million messages. Costs can increase significantly with longer tests, higher client counts, or frequent testing, potentially escalating quickly without careful monitoring. To manage costs, regularly check your usage, set budgets and alerts, optimize test parameters, and stay informed about [AWS IoT Core pricing](https://aws.amazon.com/iot-core/pricing/).
