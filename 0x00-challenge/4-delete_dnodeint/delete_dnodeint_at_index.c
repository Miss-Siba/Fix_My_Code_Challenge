#include "lists.h"
#include <stdlib.h>

/**
 * delete_dnodeint_at_index - Delete a node at a specific index from a list
 *
 * @head: A pointer to the first element of a list
 * @index: The index of the node to delete
 *
 * Return: 1 on success, -1 on failure
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *saved_head;
	dlistint_t *tmp;
	unsigned int p;

	saved_head = *head;

	if (saved_head != NULL)
		while (saved_head->prev != NULL)
			saved_head = saved_head->prev;
	p = 0;

	while (saved_head != NULL)
	{
		if (p == index)
		{
			if (p == index)
			{
				*head = saved_head->next;
				if (*head != NULL)
					(*head)->prev = NULL;
			}
			else
			{
				tmp->next = saved_head->next;
				if (saved_head->next != NULL)
					saved_head->next->prev = tmp;
			}
			free(saved_head);
			return (1);
		}
		tmp = saved_head;
		saved_head = saved_head->next;
		p++;
	}
	return (-1);
}
