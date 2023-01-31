#include "lists.h"

/**
 * check_cycle - a function to check if a linked list has a cycle
 * @list: the head node
 * Description: the function will return 1 if cycle else 0
 * Return: 0 or 1 
*/

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (fast == slow)
		{
			return (1);
		}
	}
	return (0);
}
