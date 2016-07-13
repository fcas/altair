# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T
from ..baseobject import BaseObject
from .aggregateop import AggregateOp
from .bin import Bin
from .sortorder import SortOrder
from .timeunit import TimeUnit
from .type import Type


class OrderChannelDef(BaseObject):
    """Wrapper for Vega-Lite OrderChannelDef definition.
    
    Attributes
    ----------
    aggregate: AggregateOp
        Aggregation function for the field .
    bin: Union(Bool, Bin)
        Flag for binning a `quantitative` field, or a bin property object for binning parameters.
    field: Unicode
        Name of the field from which to pull a data value.
    sort: SortOrder
        
    timeUnit: TimeUnit
        Time unit for a `temporal` field .
    title: Unicode
        Title for axis or legend.
    type: Type
        The encoded field's type of measurement.
    value: Union(CFloat, Unicode, Bool)
        A constant value in visual domain.
    """
    aggregate = AggregateOp(allow_none=True, default_value=None, help="""Aggregation function for the field .""")
    bin = T.Union([T.Bool(allow_none=True, default_value=None), T.Instance(Bin, allow_none=True, default_value=None, help="""Binning properties or boolean flag for determining whether to bin data or not.""")])
    field = T.Unicode(allow_none=True, default_value=None, help="""Name of the field from which to pull a data value.""")
    sort = SortOrder(allow_none=True, default_value=None)
    timeUnit = TimeUnit(allow_none=True, default_value=None, help="""Time unit for a `temporal` field .""")
    title = T.Unicode(allow_none=True, default_value=None, help="""Title for axis or legend.""")
    type = Type(allow_none=True, default_value=None, help="""The encoded field's type of measurement.""")
    value = T.Union([T.CFloat(allow_none=True, default_value=None), T.Unicode(allow_none=True, default_value=None), T.Bool(allow_none=True, default_value=None)])
    
    def __init__(self, aggregate=None, bin=None, field=None, sort=None, timeUnit=None, title=None, type=None, value=None, **kwargs):
        kwds = dict(aggregate=aggregate, bin=bin, field=field, sort=sort, timeUnit=timeUnit, title=title, type=type, value=value)
        kwargs.update({k:v for k, v in kwds.items() if v is not None})
        super(OrderChannelDef, self).__init__(**kwargs)