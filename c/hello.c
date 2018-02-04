#include <Python.h>

static PyObject *
hello_echo(PyObject *self, PyObject *args, PyObject *keywds)
{
char *something;

if (!PyArg_ParseTuple(args, "s", &something))
return NULL;

printf("%s\n", something);
Py_INCREF(Py_None);
return Py_None;
}

static PyMethodDef hello_methods[] = {
{"echo", (PyCFunction)hello_echo, METH_VARARGS | METH_KEYWORDS, "print string"},
{NULL, NULL, 0, NULL}
};

void
inithello(void)
{
Py_InitModule("hello", hello_methods);
}