#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head of list
 * @number: value of new node
 * Return: number of nodes
 */
listint_t *insert_node(listint_t **head, int number)
{

	listint_t *new = NULL, *current = NULL;

	if (!head)
		return (NULL);

	if (!*head)
		return (add_nodeint_end(head, number));

	while (*head != NULL)
	{
		if ((*head)->n < number)
		{
			head = &((*head)->next);
			continue;
		}
		else
		{
			current = *head;
			break;
		}
	}

	*head = NULL;
	new = add_nodeint_end(head, number);
	(*head)->next = current;

	return (new);

}
