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
	listint_t *helper = *head, *first_node = *head, *last_node = *head;
	int len = 0, last;

	if (!*head)
		return (1);
	while (helper)
		helper = helper->next, len++;

	/* printf("len = %d\n", len);*/
	while (first_node)
	{
		for (last = 1; last < len; last++)
			last_node = last_node->next;
		/*printf("fist = %d -- second = %d\n", first_node->n, last_node->n);*/
		if (first_node->n != last_node->n)
			return (0);
		first_node = first_node->next, len--, last_node = *head;
	}
	return (1);
}
