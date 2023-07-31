# Python API Automation Framework
## Integration Test case for the Restfull Booker 

### URL - https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking-CreateBooking
1. Verify GET, POST, PATCH, DELETE, PUT
2. Response Body, Headers, Status Code.
3. Auth - BAsic Auth, Cookie Based Auth.
4. JSON Schema Validation 

### tech stack ( python packages used)
1. python, Request Module
2. PyTest, PyTest-html
3. Allure Report 
4. Faker, CSV, JSON, YAML.
5. Run via Commandline - Jenkins
6. 
### P.s -DB Connection

# Install packages
- ` pip install pytest requests pytest-html faker allure-pytest jsonschema`
- ` pip install requirements.txt`

## how to run locally and see the report 
- `pytest -s -v --alluredir=./reports --html=report.html`

### how to Run via junkins 