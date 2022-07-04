#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * listint_len - Function that prints returns the number of
 * elements in a linked listint_t list
 *
 * @h: list of elements
 *
 * Return: number of nodes
 */
size_t listint_len(const listint_t *h)
{
	size_t i = 0;

	while (h != NULL)
	{
		h = h->next;
		i++;
	}

	return (i);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: 0 if it is not a palindrome, 1 if it is a palindrome
 * Return: number of nodes
 */
int is_palindrome(listint_t **head)
{
	unsigned int size = listint_len(*head),
					middle = (int) size / 2, isPalindrome = 1;
	size_t i, j;

	if (!*head)
		return (1);

	for (i = 0, j = size - 1; i < middle && j > middle; i++, j--)
	{
		if ((*head + i)[i].n == (*head + j)[j].n)
			isPalindrome = 1;
		else
		{
			isPalindrome = 0;
			break;
		}
	}

	if (size % 2 == 0)
	{
		i = middle - 1;

		if ((*head + i)[i].n == (*head + middle)[middle].n)
			isPalindrome = 1;
		else
			isPalindrome = 0;
	}

	return (isPalindrome);

}
