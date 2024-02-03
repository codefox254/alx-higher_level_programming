#ifndef PYTHON_H
#define PYTHON_H

/* Define necessary structures and types */

typedef struct _object PyObject;
typedef struct {
    PyObject ob_base;
    Py_ssize_t length;
} PyVarObject;

typedef struct {
    PyVarObject ob_base;
} PyASCIIObject;

/* Define necessary functions */

int PyUnicode_Check(PyObject *p);
Py_ssize_t PyUnicode_GET_LENGTH(PyObject *p);
int PyUnicode_IS_COMPACT_ASCII(PyObject *p);
wchar_t *PyUnicode_AsWideCharString(PyObject *unicode, Py_ssize_t *length);

/* Define macros */

#define METH_O 1

/* Define PyMODINIT_FUNC macro */
#ifdef __cplusplus
#define PyMODINIT_FUNC extern "C" PyObject*
#else
#define PyMODINIT_FUNC PyObject*
#endif

/* Define PyModuleDef_HEAD_INIT macro */
#define PyModuleDef_HEAD_INIT PyObject_HEAD_INIT(NULL) 0, NULL, 0, NULL

/* Define PyModuleDef struct */
typedef struct PyModuleDef_Base {
    PyObject_HEAD
    PyObject *m_name;
    PyObject *m_doc;
    Py_ssize_t m_size;
    PyObject *m_methods;
    PyObject *m_reload;
    PyObject *m_traverse;
    PyObject *m_clear;
    PyObject *m_free;
} PyModuleDef_Base;

typedef struct PyModuleDef {
    PyModuleDef_Base m_base;
    PyObject *m_dict;
    PyObject *m_weaklist;
} PyModuleDef;

/* Define PyModule_Create function */
PyObject* PyModule_Create(PyModuleDef *def);

#endif /* PYTHON_H */

