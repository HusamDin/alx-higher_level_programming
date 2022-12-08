#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a node with a specific number into a sorted singly linked list
 * @head: Pointer to the head pointer of a listint_t list
 * @number: Number data of the newly insrted node
 *
 * Return: Address of the newly inserted node
 */

listint_t *insert_node(listint_t **head, int number)
{
  listint_t *current, *new, *nxt;

  if (head == NULL)
    return (NULL);

  current = *head;
  nxt = current->next;

  new = malloc(sizeof(listint_t));
  if (new == NULL)
    return (NULL);

  new->n = number;
  if (current->n >= new->n)
    {
      new->next = current;
      return (new);
    }

  current = current->next;
  nxt = current->next;
  while (current != NULL)
    {
      if (current->n < new->n && nxt->n > new->n)
	break;
      else
	{
	  current = current->next;
	  nxt = current->next;
	}
    }

  if (current == NULL)
    return (NULL);

  new->next = nxt;
  current->next = new;
  
  return (new);
}

