TagoIO Python SDK Documentation
=================================

Welcome to the official Python SDK for TagoIO, the leading IoT platform for connecting, managing, and visualizing your IoT devices and data.

.. image:: https://img.shields.io/pypi/v/tagoio-sdk
   :target: https://pypi.org/project/tagoio-sdk/
   :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/tagoio-sdk
   :target: https://pypi.org/project/tagoio-sdk/
   :alt: Python versions

.. image:: https://img.shields.io/github/license/tago-io/sdk-python
   :target: https://github.com/tago-io/sdk-python/blob/master/LICENSE
   :alt: License

Overview
--------

The TagoIO Python SDK provides a comprehensive interface to interact with the TagoIO IoT platform. Whether you're building IoT applications, creating data analysis scripts, or managing devices at scale, this SDK offers all the tools you need.

**Key Features:**

- 🚀 **Easy Integration** - Simple and intuitive API design
- 📊 **Device Management** - Send, receive, and manage device data
- 🔧 **Resource Control** - Full access to accounts, dashboards, and billing
- 📧 **Communication Services** - Email, SMS, and push notifications
- 🔐 **Secure Authentication** - Token-based authentication with region support
- 📈 **Real-time Data** - WebSocket and Server-Sent Events support
- 🐍 **Modern Python** - Built for Python 3.11+ with comprehensive type hints

Quick Start
-----------

Installation
~~~~~~~~~~~~

Install the SDK using pip:

.. code-block:: bash

    pip install tagoio-sdk

For development with additional tools:

.. code-block:: bash

    pip install tagoio-sdk[dev]

Authentication
~~~~~~~~~~~~~~

Before using the SDK, you'll need a TagoIO account and token. Get started at `TagoIO Console <https://admin.tago.io>`_.

.. code-block:: python

    from tagoio_sdk import Device, Resources

    # Using device token
    device = Device({"token": "your-device-token"})

    # Using account token
    resources = Resources({"token": "your-account-token"})

Basic Examples
--------------

Run External Analysis
~~~~~~~~~~~~~~~~~~~~~

Execute TagoIO Analysis scripts outside the TagoIO platform for testing and development:

.. code-block:: python

    from tagoio_sdk import Analysis

    # Define your analysis function
    def myAnalysis(context, scope):
        # Log messages to TagoIO Analysis console
        context.log("Hello World from external analysis!")

        # Access environment variables
        context.log("Environment:", context.environment)

        # Access scope data passed to the analysis
        context.log("Scope data:", scope)

        # Example: Process device data from scope
        if scope and 'data' in scope:
            for data_point in scope['data']:
                if data_point['variable'] == 'temperature' and data_point['value'] > 30:
                    context.log(f"High temperature alert: {data_point['value']}°C")

        # Example: Send notification or trigger action
        # You can use other SDK modules here like Device, Services, etc.

    # Run the analysis externally with your analysis token
    # Get your analysis token from TagoIO Console > Analysis > Edit > Info tab
    Analysis({"token": "your-analysis-token"}).init(myAnalysis)

.. note::
   The analysis token is only necessary when running analysis scripts outside the TagoIO platform.
   When running inside TagoIO, the token is automatically provided by the environment.

Send Device Data
~~~~~~~~~~~~~~~~~

.. code-block:: python

    from tagoio_sdk import Device

    device = Device({"token": "your-device-token"})

    # Send a single data point
    device.sendData({
        "variable": "temperature",
        "value": 23.5,
        "unit": "°C",
        "time": "2023-12-01 10:30:00",
        "location": {"lat": 40.7128, "lng": -74.0060}
    })

    # Send multiple data points
    device.sendData([
        {"variable": "temperature", "value": 23.5, "unit": "°C"},
        {"variable": "humidity", "value": 65.2, "unit": "%"},
        {"variable": "pressure", "value": 1013.25, "unit": "hPa"}
    ])

Retrieve Device Data
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Get latest 100 temperature readings
    data = device.getData({
        "variable": "temperature",
        "qty": 100,
        "start_date": "2023-12-01",
        "end_date": "2023-12-07"
    })

    for reading in data:
        print(f"Temperature: {reading['value']}°C at {reading['time']}")

Manage Resources
~~~~~~~~~~~~~~~~

.. code-block:: python

    from tagoio_sdk import Resources

    resources = Resources({"token": "your-account-token"})

    # List all devices
    devices = resources.devices.listDevice()

    # Get account information
    account_info = resources.account.info()

    # Create a dashboard
    dashboard = resources.dashboards.createDashboard({
        "name": "My IoT Dashboard",
        "visible": True
    })

Send Notifications
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from tagoio_sdk import Services

    services = Services({"token": "your-account-token"})

    # Send email
    services.email.send({
        "to": "user@example.com",
        "subject": "Alert: High Temperature",
        "message": "Temperature exceeded 30°C",
        "template": "alert_template"
    })

    # Send SMS
    services.sms.send({
        "to": "+1234567890",
        "message": "Alert: Device offline"
    })

Analysis Scripts
~~~~~~~~~~~~~~~~

Perfect for TagoIO Analysis environment:

.. code-block:: python

    from tagoio_sdk import Analysis, Device, Services
    import json

    # Initialize analysis context
    context = Analysis()

    # Get environment variables and input data
    env_vars = context.getEnvironment()
    input_data = json.loads(env_vars.get("input_data", "[]"))

    # Process device data
    device = Device({"token": env_vars["device_token"]})

    for data_point in input_data:
        if data_point["variable"] == "temperature" and data_point["value"] > 30:
            # Send alert
            services = Services()
            services.email.send({
                "to": env_vars["alert_email"],
                "subject": "High Temperature Alert",
                "message": f"Temperature is {data_point['value']}°C"
            })

            # Log to analysis console
            context.log("Alert sent for high temperature")

Regional Support
----------------

TagoIO operates in multiple regions. Specify your region when initializing:

.. code-block:: python

    from tagoio_sdk import Resources, Regions

    # US region (default)
    resources = Resources({
        "token": "your-token",
        "region": Regions.USA
    })

    # European region
    resources = Resources({
        "token": "your-token",
        "region": Regions.EUR
    })

Error Handling
--------------

The SDK provides comprehensive error handling:

.. code-block:: python

    from tagoio_sdk import Device
    from tagoio_sdk.infrastructure.api_request import TagoIORequestError

    device = Device({"token": "your-token"})

    try:
        result = device.sendData({
            "variable": "temperature",
            "value": 25.0
        })
        print("Data sent successfully")
    except TagoIORequestError as e:
        print(f"API Error: {e}")
        print(f"Status Code: {e.status_code}")
        print(f"Response: {e.response}")
    except Exception as e:
        print(f"Unexpected error: {e}")

API Reference
-------------

.. toctree::
   :maxdepth: 2
   :caption: Core Modules

   Resources/index
   Device/index
   Services/index
   Utils/index

.. toctree::
   :maxdepth: 1
   :caption: Type Definitions

   common/Common_Type

Development
-----------

Contributing
~~~~~~~~~~~~

We welcome contributions! Here's how to set up the development environment:

.. code-block:: bash

    # Clone the repository
    git clone https://github.com/tago-io/sdk-python.git
    cd sdk-python

    # Install with development dependencies
    pip install -e ".[dev]"

    # Run tests
    pytest tests/

    # Run linting and formatting
    ruff check src
    ruff format src

Project Commands
~~~~~~~~~~~~~~~~

.. code-block:: bash

    # Install dependencies
    uv sync --dev

    # Run tests with coverage
    uv run pytest tests/ --cov=src

    # Build documentation
    cd docs && make html

    # Build package
    python -m build

Requirements
~~~~~~~~~~~~

- **Python:** 3.11 or higher
- **Dependencies:** requests, python-dateutil, sseclient-py
- **Optional:** pytest, ruff (for development)

Support & Resources
-------------------

📚 **Documentation:** You're reading it!

🐛 **Issues & Bugs:** `GitHub Issues <https://github.com/tago-io/sdk-python/issues>`_

💬 **Help Center:** `TagoIO Support <https://help.tago.io/portal/en/home>`_

🌐 **Platform:** `TagoIO Console <https://admin.tago.io>`_

📦 **PyPI Package:** `tagoio-sdk <https://pypi.org/project/tagoio-sdk/>`_

📖 **Source Code:** `GitHub Repository <https://github.com/tago-io/sdk-python>`_

📧 **Contact:** For enterprise support, contact our team through the TagoIO Console.

License
-------

TagoIO SDK for Python is released under the `Apache-2.0 License <https://github.com/tago-io/sdk-python/blob/master/LICENSE>`_.

Copyright © 2024 TagoIO. All rights reserved.

----

*Built with ❤️ by the TagoIO team for the Python community.*
