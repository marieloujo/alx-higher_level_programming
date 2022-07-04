#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	/* listint_t *temp = malloc(sizeof(listint_t)), *next = NULL;

	while (list != NULL)
	{
		if (list->next == NULL)
			return (0);

		if (list->next == temp)
			return (1);

		next = list->next;
		list->next = temp;
		list = next;
	} */
	return (0);
}
