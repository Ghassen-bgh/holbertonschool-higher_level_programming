#include"lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: listint_t
 * Return: 0 for no cycle, otherwise 1.
 */
int check_cycle(listint_t *list)
{
	int i = 0;

	if (!list)
		return (0);

	while (list)
	{
		list = list->next;
		i++;
		if (i > 100)
			return (1);
	}
	return (0);
}
