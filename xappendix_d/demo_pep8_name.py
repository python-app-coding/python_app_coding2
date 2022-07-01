# coding = utf8


def demo_name_var():
    # 尽量使用英文单词和数字混合的命名变量，多个单词之间以下划线连接，不使用数字开始。
    # 以单下划线结束的变量，主要用于区别于Python的关键字或标准库使用的名称。
    # 以单下划线开始的变量视为内部变量，如使用“import *”，不会导入这些变量。
    student_count = 100
    math_ = True
    _module_sign = '01021330'


def demo_name_class_var():
    # 在类内部使用双下划线开始命名属性或方法，作为内部使用对象。
    # 在外部调用时受到保护，不能直接使用本名调用，会加入“_类名”作为前缀。

    class Student:
        __name = 'name'

    st = Student()
    print([p for p in dir(st) if '__name' in p])
    # ['_Student__name']


def demo_name_constant():
    # 常数通常在模块级定义，以下划线连接的大写字母方式表示，放在模块的顶部，导入语句之后。
    import pkgutil
    from importlib import import_module

    DEFAULT_DB_ALIAS = 'default'
    DJANGO_VERSION_PICKLE_KEY = '_django_version'


def demo_class_name():
    # 类命名使用CapWords方式，即多个单词直接连接，每个单词首字母大写。

    class InterfaceError(Exception):
        pass


def demo_name_function():
    # 函数命名与变量命名的约定基本相同，使用小写形式，多个单词之间使用下划线连接。

    def pretty_name(name):
        """Convert 'first_name' to 'First name'."""
        if not name:
            return ''
        return name.replace('_', ' ').capitalize()


def demo_name_parameter():
    # 对象方法中的第一个参数使用self，表示所创建的对象。类方法中的第一个参数使用cls，表示类本身。

    class Student:
        """学生信息模型"""
        school_name = "Ming Hu"

        def __init__(self):
            self.name = ''

        @classmethod
        def get_school_name(cls):
            return cls.school_name


if __name__ == '__main__':
    pass
