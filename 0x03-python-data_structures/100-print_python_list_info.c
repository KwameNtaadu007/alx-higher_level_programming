#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python list
 * @p: Python object
 **/
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = list->ob_item[i];
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

