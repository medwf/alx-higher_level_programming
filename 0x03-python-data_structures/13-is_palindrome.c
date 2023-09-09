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
    listint_t *check = *head;
    int i = 0, len = 0, first = 0, second = 0;

    if (!*head || !(*head)->next)
        return (1);
    while (check)
        check = check->next, len++;
    check = *head;
    /* printf("*---> %d\n", len); */

    while (check)
    {
        if (len % 2 == 0)
        {
            if (i < (len / 2))
                first += check->n;
            else
                second += check->n;
        }
        else
        {
            if (i <= (len / 2))
                first += check->n;
            if (i >= (len / 2))
                second += check->n;
        }
        check = check->next, i++;
    }
    /* printf("first = %d \nsecond = %d \n", first, second);*/
    if (first == second)
        return (1);
    return (0);
}
