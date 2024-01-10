#include <Python.h>
#include <bytesobject.h>

/**
 * print_python_list - Prints some basic info about Python lists
 * @p: A pointer to a Python object
 */
void print_python_list(PyObject *p)
{
    PyListObject *list;
    Py_ssize_t size, allocated, i;
    PyObject *item;
    const char *type;

    printf("[*] Python list info\n");
    /* Check if the object is a list */
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }
    /* Cast the object to a list object */
    list = (PyListObject *)p;
    /* Get the size and allocated space of the list */
    size = PyList_Size(p);
    allocated = list->allocated;
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);
    /* Loop over the elements of the list */
    for (i = 0; i < size; i++)
    {
        /* Get the element and its type */
        item = PyList_GetItem(p, i);
        type = (item->ob_type)->tp_name;
        printf("Element %ld: %s\n", i, type);
        /* Call the corresponding function for each type */
        if (PyBytes_Check(item))
            print_python_bytes(item);
        else if (PyFloat_Check(item))
            print_python_float(item);
        else if (PyList_Check(item))
            print_python_list(item);
        /* You can add more types here */
    }
}

/**
 * print_python_bytes - Prints some basic info about Python bytes objects
 * @p: A pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes;
    Py_ssize_t size, i, max;
    char *str;

    printf("[.] bytes object info\n");
    /* Check if the object is a bytes object */
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    /* Cast the object to a bytes object */
    bytes = (PyBytesObject *)p;
    /* Get the size and string representation of the bytes object */
    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);
    /* Print the first bytes of the object */
    max = size + 1 > 10 ? 10 : size + 1;
    printf("  first %ld bytes: ", max);
    for (i = 0; i < max; i++)
    {
        printf("%02hhx", str[i]);
        if (i < max - 1)
            printf(" ");
    }
    printf("\n");
}

