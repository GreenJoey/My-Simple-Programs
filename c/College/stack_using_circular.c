#include <stdio.h>
#include <malloc.h>


typedef struct _node {
    int data;
    struct _node *next;
    struct _node *prev;
} node;


node *newNode(int data, node *next, node *prev) {
    node *new = (node *)malloc(sizeof(node));
    new->data = data;
    new->next = next;
    new->prev = prev;

    return new;
}


node *push(node *list, int data) {
    if (list == NULL) {
        node *curr = newNode(data, NULL, NULL);
        curr->next = curr;
        curr->prev = curr;

        return curr;
    }

    node *new = newNode(data, list, list->prev);
    list->prev->next = new;
    list->prev = new;

    return new;
}


node *pop(node *list) {
    if (list == NULL)
        return NULL;

    int data = list->data;
    node *next = list->next;
    next->prev = list->prev;
    list->prev->next = next;
    free(list);
    
    printf("%d\n", data);

    return next;
}


int main() {
    node *list = NULL;

    list = push(list, 14);
    list = push(list, 15);
    list = push(list, 16);

    list = pop(list);
    list = pop(list);
    list = pop(list);
    pop(list);

    return 0;
}
