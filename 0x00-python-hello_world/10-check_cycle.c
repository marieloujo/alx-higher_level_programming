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
	while (list != NULL) {
		if (list->isCheck == 1)
			return (1);
 
		list->isCheck = 1;
 
		list = list->next;
	}
 
	return (0);
}
