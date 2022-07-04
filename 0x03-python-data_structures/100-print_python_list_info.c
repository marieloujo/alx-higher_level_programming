#include "Python.h"

/**
 * print_python_list_info - prints python list info
 * @p: python object
 * Return nothing
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size, i;

	if (strcmp(p->ob_type->tp_name, "list") == 0)
	{
		list = (PyListObject *)p;
		size = list->ob_base.ob_size;
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", list->allocated);
		for (i = 0; i < size; i++)
		{
			printf("Element %ld: %s\n", i, (list->ob_item[i])->ob_type->tp_name);
		}
	}
}
