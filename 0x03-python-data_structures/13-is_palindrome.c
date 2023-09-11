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
	listint_t *helper = *head;
	int array[1024], start, end;

	if (!*head)
		return (1);

	for (end = 0; helper; end++)
		array[end] = helper->n, helper = helper->next;

	array[end] = '\0';
	for (start = 0; start < ((end % 2 == 0) ? (end / 2)
				: (end / 2) + 1); start++)
	{
		if (array[start] != array[end - start - 1])
			return (0);
		/*printf("start = %d - end = %d\n", array[start],array[end- start - 1]);*/
	}
	return (1);
}
