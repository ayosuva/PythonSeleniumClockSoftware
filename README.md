# PythonSeleniumClockSoftware
It is a Selenium Python based test automation framework and the test scripts written for Clock Software site https://www.clock-software.com/demo-clockpms/index.html

It has following features:

-> Page object Model

-> Pytest HTML Report 

-> CI/CD configurable

How to Run:

Load the project in pycharm IDE

you can using Run button that is show at the right hand side top or else you can run the below command

```python -m pytest```

To generate html report install ```pytest-html``` using command ```pip install pytest-html``` and then using this command to run test to generate html report ```python -m pytest --html report.html``` 

To include logs in the html report use command ```python -m pytest --html report.html --capture=tee-sys```