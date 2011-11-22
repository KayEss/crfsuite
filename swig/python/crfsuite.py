# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_crfsuite', [dirname(__file__)])
        except ImportError:
            import _crfsuite
            return _crfsuite
        if fp is not None:
            try:
                _mod = imp.load_module('_crfsuite', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _crfsuite = swig_import_helper()
    del swig_import_helper
else:
    import _crfsuite
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _crfsuite.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _crfsuite.SwigPyIterator_value(self)
    def incr(self, n = 1): return _crfsuite.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _crfsuite.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _crfsuite.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _crfsuite.SwigPyIterator_equal(self, *args)
    def copy(self): return _crfsuite.SwigPyIterator_copy(self)
    def next(self): return _crfsuite.SwigPyIterator_next(self)
    def __next__(self): return _crfsuite.SwigPyIterator___next__(self)
    def previous(self): return _crfsuite.SwigPyIterator_previous(self)
    def advance(self, *args): return _crfsuite.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _crfsuite.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _crfsuite.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _crfsuite.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _crfsuite.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _crfsuite.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _crfsuite.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _crfsuite.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class Item(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Item, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Item, name)
    __repr__ = _swig_repr
    def iterator(self): return _crfsuite.Item_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _crfsuite.Item___nonzero__(self)
    def __bool__(self): return _crfsuite.Item___bool__(self)
    def __len__(self): return _crfsuite.Item___len__(self)
    def pop(self): return _crfsuite.Item_pop(self)
    def __getslice__(self, *args): return _crfsuite.Item___getslice__(self, *args)
    def __setslice__(self, *args): return _crfsuite.Item___setslice__(self, *args)
    def __delslice__(self, *args): return _crfsuite.Item___delslice__(self, *args)
    def __delitem__(self, *args): return _crfsuite.Item___delitem__(self, *args)
    def __getitem__(self, *args): return _crfsuite.Item___getitem__(self, *args)
    def __setitem__(self, *args): return _crfsuite.Item___setitem__(self, *args)
    def append(self, *args): return _crfsuite.Item_append(self, *args)
    def empty(self): return _crfsuite.Item_empty(self)
    def size(self): return _crfsuite.Item_size(self)
    def clear(self): return _crfsuite.Item_clear(self)
    def swap(self, *args): return _crfsuite.Item_swap(self, *args)
    def get_allocator(self): return _crfsuite.Item_get_allocator(self)
    def begin(self): return _crfsuite.Item_begin(self)
    def end(self): return _crfsuite.Item_end(self)
    def rbegin(self): return _crfsuite.Item_rbegin(self)
    def rend(self): return _crfsuite.Item_rend(self)
    def pop_back(self): return _crfsuite.Item_pop_back(self)
    def erase(self, *args): return _crfsuite.Item_erase(self, *args)
    def __init__(self, *args): 
        this = _crfsuite.new_Item(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _crfsuite.Item_push_back(self, *args)
    def front(self): return _crfsuite.Item_front(self)
    def back(self): return _crfsuite.Item_back(self)
    def assign(self, *args): return _crfsuite.Item_assign(self, *args)
    def resize(self, *args): return _crfsuite.Item_resize(self, *args)
    def insert(self, *args): return _crfsuite.Item_insert(self, *args)
    def reserve(self, *args): return _crfsuite.Item_reserve(self, *args)
    def capacity(self): return _crfsuite.Item_capacity(self)
    __swig_destroy__ = _crfsuite.delete_Item
    __del__ = lambda self : None;
Item_swigregister = _crfsuite.Item_swigregister
Item_swigregister(Item)

class ItemSequence(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ItemSequence, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ItemSequence, name)
    __repr__ = _swig_repr
    def iterator(self): return _crfsuite.ItemSequence_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _crfsuite.ItemSequence___nonzero__(self)
    def __bool__(self): return _crfsuite.ItemSequence___bool__(self)
    def __len__(self): return _crfsuite.ItemSequence___len__(self)
    def pop(self): return _crfsuite.ItemSequence_pop(self)
    def __getslice__(self, *args): return _crfsuite.ItemSequence___getslice__(self, *args)
    def __setslice__(self, *args): return _crfsuite.ItemSequence___setslice__(self, *args)
    def __delslice__(self, *args): return _crfsuite.ItemSequence___delslice__(self, *args)
    def __delitem__(self, *args): return _crfsuite.ItemSequence___delitem__(self, *args)
    def __getitem__(self, *args): return _crfsuite.ItemSequence___getitem__(self, *args)
    def __setitem__(self, *args): return _crfsuite.ItemSequence___setitem__(self, *args)
    def append(self, *args): return _crfsuite.ItemSequence_append(self, *args)
    def empty(self): return _crfsuite.ItemSequence_empty(self)
    def size(self): return _crfsuite.ItemSequence_size(self)
    def clear(self): return _crfsuite.ItemSequence_clear(self)
    def swap(self, *args): return _crfsuite.ItemSequence_swap(self, *args)
    def get_allocator(self): return _crfsuite.ItemSequence_get_allocator(self)
    def begin(self): return _crfsuite.ItemSequence_begin(self)
    def end(self): return _crfsuite.ItemSequence_end(self)
    def rbegin(self): return _crfsuite.ItemSequence_rbegin(self)
    def rend(self): return _crfsuite.ItemSequence_rend(self)
    def pop_back(self): return _crfsuite.ItemSequence_pop_back(self)
    def erase(self, *args): return _crfsuite.ItemSequence_erase(self, *args)
    def __init__(self, *args): 
        this = _crfsuite.new_ItemSequence(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _crfsuite.ItemSequence_push_back(self, *args)
    def front(self): return _crfsuite.ItemSequence_front(self)
    def back(self): return _crfsuite.ItemSequence_back(self)
    def assign(self, *args): return _crfsuite.ItemSequence_assign(self, *args)
    def resize(self, *args): return _crfsuite.ItemSequence_resize(self, *args)
    def insert(self, *args): return _crfsuite.ItemSequence_insert(self, *args)
    def reserve(self, *args): return _crfsuite.ItemSequence_reserve(self, *args)
    def capacity(self): return _crfsuite.ItemSequence_capacity(self)
    __swig_destroy__ = _crfsuite.delete_ItemSequence
    __del__ = lambda self : None;
ItemSequence_swigregister = _crfsuite.ItemSequence_swigregister
ItemSequence_swigregister(ItemSequence)

class StringList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringList, name)
    __repr__ = _swig_repr
    def iterator(self): return _crfsuite.StringList_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _crfsuite.StringList___nonzero__(self)
    def __bool__(self): return _crfsuite.StringList___bool__(self)
    def __len__(self): return _crfsuite.StringList___len__(self)
    def pop(self): return _crfsuite.StringList_pop(self)
    def __getslice__(self, *args): return _crfsuite.StringList___getslice__(self, *args)
    def __setslice__(self, *args): return _crfsuite.StringList___setslice__(self, *args)
    def __delslice__(self, *args): return _crfsuite.StringList___delslice__(self, *args)
    def __delitem__(self, *args): return _crfsuite.StringList___delitem__(self, *args)
    def __getitem__(self, *args): return _crfsuite.StringList___getitem__(self, *args)
    def __setitem__(self, *args): return _crfsuite.StringList___setitem__(self, *args)
    def append(self, *args): return _crfsuite.StringList_append(self, *args)
    def empty(self): return _crfsuite.StringList_empty(self)
    def size(self): return _crfsuite.StringList_size(self)
    def clear(self): return _crfsuite.StringList_clear(self)
    def swap(self, *args): return _crfsuite.StringList_swap(self, *args)
    def get_allocator(self): return _crfsuite.StringList_get_allocator(self)
    def begin(self): return _crfsuite.StringList_begin(self)
    def end(self): return _crfsuite.StringList_end(self)
    def rbegin(self): return _crfsuite.StringList_rbegin(self)
    def rend(self): return _crfsuite.StringList_rend(self)
    def pop_back(self): return _crfsuite.StringList_pop_back(self)
    def erase(self, *args): return _crfsuite.StringList_erase(self, *args)
    def __init__(self, *args): 
        this = _crfsuite.new_StringList(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _crfsuite.StringList_push_back(self, *args)
    def front(self): return _crfsuite.StringList_front(self)
    def back(self): return _crfsuite.StringList_back(self)
    def assign(self, *args): return _crfsuite.StringList_assign(self, *args)
    def resize(self, *args): return _crfsuite.StringList_resize(self, *args)
    def insert(self, *args): return _crfsuite.StringList_insert(self, *args)
    def reserve(self, *args): return _crfsuite.StringList_reserve(self, *args)
    def capacity(self): return _crfsuite.StringList_capacity(self)
    __swig_destroy__ = _crfsuite.delete_StringList
    __del__ = lambda self : None;
StringList_swigregister = _crfsuite.StringList_swigregister
StringList_swigregister(StringList)

class Attribute(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Attribute, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Attribute, name)
    __repr__ = _swig_repr
    __swig_setmethods__["attr"] = _crfsuite.Attribute_attr_set
    __swig_getmethods__["attr"] = _crfsuite.Attribute_attr_get
    if _newclass:attr = _swig_property(_crfsuite.Attribute_attr_get, _crfsuite.Attribute_attr_set)
    __swig_setmethods__["value"] = _crfsuite.Attribute_value_set
    __swig_getmethods__["value"] = _crfsuite.Attribute_value_get
    if _newclass:value = _swig_property(_crfsuite.Attribute_value_get, _crfsuite.Attribute_value_set)
    def __init__(self, *args): 
        this = _crfsuite.new_Attribute(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _crfsuite.delete_Attribute
    __del__ = lambda self : None;
Attribute_swigregister = _crfsuite.Attribute_swigregister
Attribute_swigregister(Attribute)

class Trainer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Trainer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Trainer, name)
    __repr__ = _swig_repr
    def __init__(self): 
        if self.__class__ == Trainer:
            _self = None
        else:
            _self = self
        this = _crfsuite.new_Trainer(_self, )
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _crfsuite.delete_Trainer
    __del__ = lambda self : None;
    def clear(self): return _crfsuite.Trainer_clear(self)
    def append(self, *args): return _crfsuite.Trainer_append(self, *args)
    def select(self, *args): return _crfsuite.Trainer_select(self, *args)
    def train(self, *args): return _crfsuite.Trainer_train(self, *args)
    def params(self): return _crfsuite.Trainer_params(self)
    def set(self, *args): return _crfsuite.Trainer_set(self, *args)
    def get(self, *args): return _crfsuite.Trainer_get(self, *args)
    def help(self, *args): return _crfsuite.Trainer_help(self, *args)
    def message(self, *args): return _crfsuite.Trainer_message(self, *args)
    def __disown__(self):
        self.this.disown()
        _crfsuite.disown_Trainer(self)
        return weakref_proxy(self)
Trainer_swigregister = _crfsuite.Trainer_swigregister
Trainer_swigregister(Trainer)

class Tagger(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Tagger, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Tagger, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _crfsuite.new_Tagger()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _crfsuite.delete_Tagger
    __del__ = lambda self : None;
    def open(self, *args): return _crfsuite.Tagger_open(self, *args)
    def close(self): return _crfsuite.Tagger_close(self)
    def labels(self): return _crfsuite.Tagger_labels(self)
    def tag(self, *args): return _crfsuite.Tagger_tag(self, *args)
    def set(self, *args): return _crfsuite.Tagger_set(self, *args)
    def viterbi(self): return _crfsuite.Tagger_viterbi(self)
    def probability(self, *args): return _crfsuite.Tagger_probability(self, *args)
    def marginal(self, *args): return _crfsuite.Tagger_marginal(self, *args)
Tagger_swigregister = _crfsuite.Tagger_swigregister
Tagger_swigregister(Tagger)


def version():
  return _crfsuite.version()
version = _crfsuite.version


