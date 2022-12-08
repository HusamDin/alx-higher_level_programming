#include <stdlib.h>

#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - Singly linked list
 * @n: An integer Data
 * @next: A pointer to the next node
 *
 * Description: Singly linked list node structure
 *
 */
typedef struct listint_s
{
  int n;
  struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *);
listint_t *add_nodeint_end(listint_t **, const int);
void free_listint(listint_t *);
listint_t *insert_node(listint_t **, int);

#endif /* LISTS_H */

