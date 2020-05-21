# jinja2_getenv_extension

[//]: # (automatically generated from https://github.com/metwork-framework/resources/blob/master/cookiecutter/_%7B%7Bcookiecutter.repo%7D%7D/README.md)

**Status (master branch)**




[![GitHub CI](https://github.com/metwork-framework/jinja2_getenv_extension/workflows/CI/badge.svg?branch=master)](https://github.com/metwork-framework/jinja2_getenv_extension/actions?query=workflow%3ACI&branch=master)
[![Maintenance](https://github.com/metwork-framework/resources/blob/master/badges/maintained.svg)]()


[//]: # (TABLE_OF_CONTENTS_PLACEHOLDER)

Traceback (most recent call last):
  File "/opt/metwork-mfext-master/opt/python3/bin/envtpl", line 11, in <module>
    sys.exit(main())
  File "/opt/metwork-mfext-master/opt/python3/lib/python3.7/site-packages/envtpl.py", line 79, in main
    not args.reduce_multi_blank_lines)
  File "/opt/metwork-mfext-master/opt/python3/lib/python3.7/site-packages/envtpl.py", line 114, in process_file
    keep_multi_blank_lines=keep_multi_blank_lines)
  File "/opt/metwork-mfext-master/opt/python3/lib/python3.7/site-packages/envtpl.py", line 166, in _render_string
    undefined, keep_multi_blank_lines=keep_multi_blank_lines)
  File "/opt/metwork-mfext-master/opt/python3/lib/python3.7/site-packages/envtpl.py", line 212, in _render
    output = template.render(**variables)
  File "/opt/metwork-mfext-master/opt/python3/lib/python3.7/site-packages/jinja2/asyncsupport.py", line 76, in render
    return original_render(self, *args, **kwargs)
  File "/opt/metwork-mfext-master/opt/python3/lib/python3.7/site-packages/jinja2/environment.py", line 1008, in render
    return self.environment.handle_exception(exc_info, True)
  File "/opt/metwork-mfext-master/opt/python3/lib/python3.7/site-packages/jinja2/environment.py", line 780, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/opt/metwork-mfext-master/opt/python3/lib/python3.7/site-packages/jinja2/_compat.py", line 37, in reraise
    raise value.with_traceback(tb)
  File "<template>", line 9, in top-level template code
  File "/opt/metwork-mfext-master/opt/python3/lib/python3.7/site-packages/envtpl.py", line 256, in getenv
    raise Exception("can't find %s environnement variable" % value)
Exception: can't find ENV_VAR environnement variable











## Contributing guide

See [CONTRIBUTING.md](CONTRIBUTING.md) file.



## Code of Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) file.



## Sponsors

*(If you are officially paid to work on MetWork Framework, please contact us to add your company logo here!)*

[![logo](https://raw.githubusercontent.com/metwork-framework/resources/master/sponsors/meteofrance-small.jpeg)](http://www.meteofrance.com)
