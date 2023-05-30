#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size = PyBytes_Size(p);
    const char *string = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", string);
    printf("  first %zd bytes:", (size < 10) ? size + 1 : 10);

    for (Py_ssize_t i = 0; i < size && i < 10; i++)
    {
        printf(" %02x", bytes->ob_sval[i] & 0xff);
    }

    printf("\n");
}

void print_python_float(PyObject *p)
{
    double val = PyFloat_AsDouble(p);

    printf("[.] float object info\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    printf("  value: %f\n", val);
}

void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size = PyList_Size(p);

    printf("[*] Python list info\n");
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", list->allocated);

    for (Py_ssize_t i = 0; i < size; i++)
    {
        PyObject *obj = PyList_GetItem(p, i);
        const char *typeName = Py_TYPE(obj)->tp_name;

        printf("Element %zd: %s\n", i, typeName);

        if (PyBytes_Check(obj))
            print_python_bytes(obj);
        if (PyFloat_Check(obj))
            print_python_float(obj);
    }
}

