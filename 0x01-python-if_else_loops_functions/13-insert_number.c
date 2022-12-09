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
  listint_t *new, *current;

  current = *head;

  new = malloc(sizeof(listint_t));
  if (new == NULL)
    return (NULL);

  new->n = number;

  if (*head == NULL || number < current->n)
    {
      new->next = current;
      current = new;
    }
  

  while (current->next != NULL && current->next->n < number)
    current = current->next;

  new->next = current->next;
  current->next = new;

  return (new);
}
