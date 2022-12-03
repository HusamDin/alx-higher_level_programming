 #include "lists.h"
/**
 * check_cycle - Checks for a singly linked list cycle
 *
 * Return: 1. On a cycle
 * 0. On no cycle.
 */
int check_cycle(listint_t *list)
{
  listint_t *slow = list;
  listint_t *fast = list;

   for (; slow != NULL && fast->next != NULL && fast != NULL;)
    {
      slow = slow->next;
      fast = fast->next->next;
      if (slow == fast)
	return (1);
    }
  return (0);
}
