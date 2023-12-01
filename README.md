# jinja2_getenv_extension

[//]: # (automatically generated from https://github.com/metwork-framework/github_organization_management/blob/master/common_files/README.md)

**Status (master branch)**

[![GitHub CI](https://github.com/metwork-framework/jinja2_getenv_extension/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/metwork-framework/jinja2_getenv_extension/actions?query=workflow%3ACI+branch%3Amaster)
[![Maintenance](https://raw.githubusercontent.com/metwork-framework/resources/master/badges/maintained.svg)](https://github.com/metwork-framework/resources/blob/master/badges/maintained.svg)




## What is it ?

This is a [jinja2](http://jinja.pocoo.org/) extension to access to system
environment variables. It is usefull if you have dynamically generated
variable names.

## Syntax

The syntax is `{{ 'ENV_VAR'|getenv }}` to access to the `ENV_VAR` environment
variable. Don't forget the quotes around `ENV_VAR` !

If you want to provide a default value to avoid an exception if the corresponding
environment variable does not exist, you can use the following syntax:
`{{ 'ENV_VAR'|getenv('default_value') }}`.

## Examples

```python

from jinja2 import Template, Environment

# We load the extension in a jinja2 Environment
env = Environment(extensions=["jinja2_getenv_extension.GetenvExtension"])

# For the example, we use a template from a simple string
template = env.from_string("the value of HOME environment variable is: "
                           "{{ 'HOME'|getenv }}")
result = template.render()

# [...]
```






## Contributing guide

See [CONTRIBUTING.md](CONTRIBUTING.md) file.



## Code of Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) file.



## Sponsors

*(If you are officially paid to work on MetWork Framework, please contact us to add your company logo here!)*

[![logo](https://raw.githubusercontent.com/metwork-framework/resources/master/sponsors/meteofrance-small.jpeg)](http://www.meteofrance.com)
