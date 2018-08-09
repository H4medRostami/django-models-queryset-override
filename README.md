# django-models-queryset-override
example that explain models.Manager queryset method override


    >> person.women.all()
    >> person.men.all()

remember:
Call a parent class's method from child class

    class Foo(Bar):
        def baz(self, arg):
            return super(Foo, self).baz(arg)

