# CLAUDE.md - TagoIO Python SDK

This document provides comprehensive information about the TagoIO Python SDK project for Claude AI assistant interactions.

## Project Overview

**Project Name:** TagoIO Python SDK
**Version:** 4.3.0
**Description:** Official Python SDK for TagoIO IoT platform
**Language:** Python
**Minimum Python Version:** 3.11
**License:** Apache-2.0

## Project Structure

```
src/tagoio_sdk/
├── __init__.py                 # Main package exports
├── config.py                   # SDK configuration
├── params.py                   # Parameter utilities
├── regions.py                  # Regional endpoint handling
├── types.py                    # Type definitions
├── common/
│   ├── Common_Type.py          # Shared type definitions
│   └── tagoio_module.py        # Base module class
├── infrastructure/
│   ├── api_request.py          # HTTP request handling
│   ├── api_socket.py           # WebSocket connections
│   └── api_sse.py              # Server-Sent Events
├── modules/
│   ├── Analysis/               # Analysis module
│   ├── Device/                 # Device management
│   ├── Resources/              # Account resources
│   ├── Services/               # TagoIO services
│   └── Utils/                  # Utility functions
tests/                          # Test suite
docs/                          # Documentation
```

## Key Components

### Core Modules
- **Analysis:** Execute and manage TagoIO Analysis scripts
- **Device:** Device data management and operations
- **Resources:** Account, billing, dashboards, profiles management
- **Services:** Email, SMS, MQTT, PDF, notifications
- **Utils:** Helper utilities for common operations

### Infrastructure
- **API Request:** Centralized HTTP client with proper error handling
- **WebSocket/SSE:** Real-time communication support
- **Authentication:** Token-based authentication system

## Dependencies

### Production Dependencies
```toml
dependencies = [
    "requests>=2.32.0,<3.0.0",    # HTTP client
    "python-dateutil>=2.9.0",     # Date parsing utilities
    "sseclient-py>=1.8.0",        # Server-Sent Events client
]
```

### Development Dependencies
```toml
dev = [
    "pytest>=8.4.1",              # Testing framework
    "ruff>=0.12.5",                # Linting and formatting
    "sphinx>=8.2.3",               # Documentation generation
    "requests-mock>=1.12.1",       # HTTP mocking for tests
]
```

## Development Setup

### Installation
```bash
# Sync dependencies
uv sync --dev

# Run tests
uv run pytest tests/

# Run linting
uv run ruff check src
uv run ruff format src
```

## Code Quality Tools

The project uses **Ruff** as a modern, fast alternative to flake8, black, and isort:

### Linting
```bash
ruff check src          # Check for issues
ruff check --fix src    # Auto-fix issues
```

### Formatting
```bash
ruff format src         # Format code
```

### Configuration
See `pyproject.toml` for complete Ruff configuration including:
- Import sorting (replaces isort)
- Code formatting (replaces black)
- Linting rules (replaces flake8)

## Testing

### Test Structure
```
tests/
├── Device/                    # Device module tests
├── Resources/                 # Resources module tests
├── Utils/                     # Utility tests
├── commom/                    # Common functionality tests
└── conftest.py               # Pytest configuration
```

### Running Tests
```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run specific test file
pytest tests/Device/test_device.py
```

### Test Coverage
- 33 test cases covering core functionality
- Mocked HTTP requests using `requests-mock`
- Tests for all major modules and utilities

## Common Development Tasks

### Adding New Features
1. Create feature branch
2. Implement functionality in appropriate module
3. Add comprehensive tests
4. Update type definitions if needed
5. Run linting and formatting
6. Ensure all tests pass

### Code Style Guidelines
- Follow PEP 8 conventions
- Use type hints for all public APIs
- Maintain consistent import organization
- Document public methods and classes
- Use descriptive variable and function names

### Type Hints
The project uses comprehensive type hints:
```python
from typing import Optional, Union, List, Dict
from tagoio_sdk.common.Common_Type import Data, GenericID

def sendData(self, data: Union[Data, List[Data]]) -> str:
    """Send data to TagoIO device."""
    pass
```

## Architecture Patterns

### Base Module Pattern
All modules inherit from `TagoIOModule`:
```python
from tagoio_sdk.common.tagoio_module import TagoIOModule

class MyModule(TagoIOModule):
    def __init__(self, params):
        super().__init__(params)
```

### Request Handling
Centralized request handling through `api_request.py`:
```python
def doRequest(self, params: RequestParams) -> ResultHandlerResponse:
    # Centralized error handling, authentication, etc.
```

### Type Safety
Extensive use of TypedDict for API contracts:
```python
class DeviceInfo(TypedDict):
    id: str
    name: Optional[str]
    description: Optional[str]
```

## API Usage Examples

### Device Data Management
```python
from tagoio_sdk import Device

device = Device({"token": "your-token"})

# Send data
device.sendData({
    "variable": "temperature",
    "value": 25.5,
    "unit": "°C"
})

# Get data
data = device.getData({"variable": "temperature"})
```

### Resource Management
```python
from tagoio_sdk import Resources

resources = Resources({"token": "your-token"})

# List devices
devices = resources.devices.listDevice()

# Get account info
info = resources.account.info()
```

## Regional Support

The SDK supports multiple TagoIO regions:
```python
from tagoio_sdk.regions import Regions

# Supported regions: USA, EUR
params = {
    "token": "your-token",
    "region": Regions.USA  # or Regions.EUR
}
```

## Error Handling

Centralized error handling with custom exceptions:
```python
from tagoio_sdk.infrastructure.api_request import TagoIORequestError

try:
    result = device.sendData(data)
except TagoIORequestError as e:
    print(f"API Error: {e}")
```

## Environment Variables

Analysis context automatically reads from environment:
- `T_ANALYSIS_TOKEN` - Analysis token
- `T_ANALYSIS_ID` - Analysis ID
- `T_ANALYSIS_ENV` - Environment variables (JSON)
- `T_ANALYSIS_DATA` - Input data (JSON)

## Contributing Guidelines

1. **Code Quality:** Use Ruff for linting and formatting
2. **Testing:** Maintain test coverage for new features
3. **Documentation:** Update docstrings and type hints
4. **Compatibility:** Support Python 3.11+
5. **Dependencies:** Minimize external dependencies

## Build and Release

### Building
```bash
# Build wheel and source distribution
python -m build
```

### Package Structure
- Uses Hatchling as build backend
- Proper package discovery from `src/tagoio_sdk/`
- Comprehensive metadata in `pyproject.toml`

## Recent Fixes and Improvements

### Analysis Logging Fix (January 2025)
Fixed a critical bug in Analysis module logging where complex data structures were being truncated in the TagoIO console:

**Issue:** The `context.log()` function was using `str(args)[1:][:-2]` which incorrectly truncated log messages, especially for complex data like lists and dictionaries.

**Solution:** Replaced with `" ".join(str(arg) for arg in args)` which properly formats all arguments without truncation.

**Impact:** Analysis logs now display complete data structures in the TagoIO console without being cut off.

### Signal Handling Improvements
Enhanced Analysis module with proper signal handling for graceful shutdowns:
- Added `SIGINT` and `SIGTERM` handlers
- Clean "Analysis stopped by user. Goodbye!" message instead of ugly Python tracebacks
- Proper cleanup of SSE connections

## Known Issues and Limitations

1. **Python Version:** Requires Python 3.11+ due to modern type annotations
2. **Rate Limiting:** API rate limits handled by TagoIO backend
3. **Regional Endpoints:** Some features may vary by region

## Future Improvements

- Async/await support for better performance
- Enhanced type safety with Pydantic models
- More comprehensive documentation examples
- Additional utility functions for common patterns

## Support and Resources

- **Documentation:** https://py.sdk.tago.io/
- **Repository:** https://github.com/tago-io/sdk-python/
- **Issues:** https://github.com/tago-io/sdk-python/issues
- **TagoIO Platform:** https://tago.io/

---

This document should be updated as the project evolves. Last updated: January 2025
