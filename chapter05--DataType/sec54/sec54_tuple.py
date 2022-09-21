# coding: utf8

"""
class tuple(object)
    tuple(iterable=(), /)
    元组可以接受可迭代对象作为初始数据，生成元组对象
    
    Built-in immutable sequence.
    元组为内置不可修改序列
    
    If no argument is given, the constructor returns an empty tuple.
    If iterable is specified the tuple is initialized from iterable's items.
    如果没有设置参数，元组构建方法生成一个空元组
    如果接受可迭代对象，由可迭代对象的数据项，创建一个元组
    
    If the argument is a tuple, the return value is the same object.
    如果参数为一个元组，返回值为相同的对象（原对象的视图, 指向同一个对象）

    >>> a = (1, 2)
    >>> b = tuple(a)
    >>> id(a) == id(b)
    True

    Built-in subclasses: 内置子类
        asyncgen_hooks
        UnraisableHookArgs

    具有的方法
    Methods defined here:
    __add__(self, value, /)
        Return self+value.
    
    __contains__(self, key, /)
        Return key in self.
    
    __eq__(self, value, /)
        Return self==value.
    
    __ge__(self, value, /)
        Return self>=value.
    
    __getattribute__(self, name, /)
        Return getattr(self, name).
    
    __getitem__(self, key, /)
        Return self[key].
    
    __getnewargs__(self, /)
    
    __gt__(self, value, /)
        Return self>value.
    
    __hash__(self, /)
        Return hash(self).
    
    __iter__(self, /)
        Implement iter(self).
    
    __le__(self, value, /)
        Return self<=value.
    
    __len__(self, /)
        Return len(self).
    
    __lt__(self, value, /)
        Return self<value.
    
    __mul__(self, value, /)
        Return self*value.
    
    __ne__(self, value, /)
        Return self!=value.
    
    __repr__(self, /)
        Return repr(self).
    
    __rmul__(self, value, /)
        Return value*self.
    
    count(self, value, /)
        Return number of occurrences of value.
    
    index(self, value, start=0, stop=9223372036854775807, /)
        Return first index of value.
        
        Raises ValueError if the value is not present.
    
    ----------------------------------------------------------------------
    类方法
    Class methods defined here:
    __class_getitem__(...) from builtins.type
        See PEP 585
    
    ----------------------------------------------------------------------
    静态方法
    Static methods defined here:
    __new__(*args, **kwargs) from builtins.type
        Create and return a new object.  See help(type) for accurate signature.

"""