import os
import jinja2
from jinja2.ext import Extension


@jinja2.evalcontextfilter
def getenv(eval_ctx, value, default=None):
    result = os.environ.get(value, default)
    if result is None:
        raise Exception("can't find %s environnement variable" % value)
    return result


class GetenvExtension(Extension):

    def __init__(self, environment):
        super(GetenvExtension, self).__init__(environment)
        environment.filters['getenv'] = getenv
