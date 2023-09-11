#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - a function that checks if a singly
 *                         linked list is a palindrome.
 * @head: a pointer to linked list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *first_node = *head, *last_node = *head;
	int len = 0, first = 0, last = 0;

	if (!*head)
		return (1);

	while (first_node)
		first_node = first_node->next, len++;

	first_node = *head;
	for (first = 1; first <= ((len % 2 == 0) ? (len / 2)
				: (len / 2) + 1);
			first++)
	{
		for (last = first; last <= len - first; last++)
			last_node = last_node->next;
		/*printf("fist = %d -- second = %d\n", first_node->n, last_node->n);*/
		if (first_node->n != last_node->n)
			return (0);
		first_node = first_node->next, last_node = first_node;
	}
	return (1);
}
