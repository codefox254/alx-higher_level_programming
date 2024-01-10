#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to a PyObject
 */
void print_python_list_info(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size, alloc, i;
    PyObject *item;

    size = PyList_Size(p);
    alloc = list->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

